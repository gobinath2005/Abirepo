from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# MongoDB Connection
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = os.getenv('DB_NAME', 'portfolio_db')
COLLECTION_NAME = 'contact_submissions'

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    print("✓ Connected to MongoDB successfully")
except Exception as e:
    print(f"✗ MongoDB connection error: {e}")

# Admin password (change this to something secure)
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

@app.route('/')
def home():
    """Redirect to portfolio"""
    return render_template('index.html')

@app.route('/api/submit-contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('name') or not data.get('email') or not data.get('message'):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
        # Create submission document
        submission = {
            'name': data.get('name').strip(),
            'email': data.get('email').strip(),
            'message': data.get('message').strip(),
            'submitted_at': datetime.utcnow(),
            'ip_address': request.remote_addr,
            'user_agent': request.headers.get('User-Agent', 'Unknown')
        }
        
        # Insert into MongoDB
        result = collection.insert_one(submission)
        
        return jsonify({
            'success': True,
            'message': 'Thank you! Your message has been received.',
            'submission_id': str(result.inserted_id)
        }), 201
    
    except Exception as e:
        print(f"Error submitting contact: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/admin')
def admin_login():
    """Admin login page"""
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    """Admin dashboard - view all submissions"""
    password = request.args.get('password')
    
    if password != ADMIN_PASSWORD:
        return render_template('admin_login.html', error='Invalid password'), 401
    
    return render_template('admin_dashboard.html')

@app.route('/api/admin/submissions', methods=['GET'])
def get_submissions():
    """Get all contact submissions (protected)"""
    password = request.args.get('password')
    
    if password != ADMIN_PASSWORD:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        submissions = list(collection.find({}).sort('submitted_at', -1))
        
        # Convert ObjectId and datetime to strings for JSON serialization
        for submission in submissions:
            submission['_id'] = str(submission['_id'])
            submission['submitted_at'] = submission['submitted_at'].isoformat()
        
        return jsonify({
            'success': True,
            'count': len(submissions),
            'submissions': submissions
        }), 200
    
    except Exception as e:
        print(f"Error retrieving submissions: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/admin/delete/<submission_id>', methods=['DELETE'])
def delete_submission(submission_id):
    """Delete a submission"""
    password = request.args.get('password')
    
    if password != ADMIN_PASSWORD:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        from bson.objectid import ObjectId
        collection.delete_one({'_id': ObjectId(submission_id)})
        return jsonify({'success': True, 'message': 'Submission deleted'}), 200
    
    except Exception as e:
        print(f"Error deleting submission: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({'success': False, 'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return jsonify({'success': False, 'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
