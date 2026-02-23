# Portfolio with Contact Database

A professional portfolio website with a backend database to store contact form submissions.

## Features

✅ Beautiful, responsive portfolio website
✅ Contact form that saves submissions to MongoDB
✅ Admin dashboard to view all contact messages
✅ Admin login with password protection
✅ Real-time submission tracking with stats
✅ Delete submissions functionality
✅ Professional animations and styling

## Project Structure

```
portfolio/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── .env                   # Configuration file
├── templates/
│   ├── index.html        # Portfolio website
│   ├── admin_login.html  # Admin login page
│   └── admin_dashboard.html # Admin dashboard
└── README.md             # This file
```

## Setup Instructions

### Prerequisites

You need:
- Python 3.8 or higher
- MongoDB installed locally or a MongoDB Atlas connection string
- pip (Python package manager)

### Step 1: Install MongoDB

**Option A: Local MongoDB**
- Download and install from [mongodb.com](https://www.mongodb.com/try/download/community)
- Make sure MongoDB is running

**Option B: MongoDB Atlas (Cloud)**
- Create free account at [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
- Create a cluster and get your connection string
- Update `MONGO_URI` in `.env` with your connection string

### Step 2: Install Dependencies

1. Open Windows PowerShell in the portfolio folder
2. Run:
```powershell
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

The `.env` file is already created with defaults:
- `MONGO_URI=mongodb://localhost:27017/` (local MongoDB)
- `DB_NAME=portfolio_db`
- `ADMIN_PASSWORD=admin123` ⚠️ **Change this to a secure password!**

Edit `.env` to change the admin password:
```
ADMIN_PASSWORD=your_secure_password_here
```

### Step 4: Run the Application

1. In PowerShell, run:
```powershell
python app.py
```

2. You should see:
```
✓ Connected to MongoDB successfully
 * Running on http://127.0.0.1:5000
```

3. Open your browser and go to:
- **Portfolio**: http://localhost:5000
- **Admin Panel**: http://localhost:5000/admin

### Step 5: Access Admin Dashboard

1. Click "Admin" link in the top-right corner of the portfolio
2. Enter your admin password (default: `admin123`)
3. View all contact form submissions with:
   - Visitor name and email
   - Message content
   - Submission date and time
   - IP address
   - Delete button for each submission

## How It Works

### User Flow

1. Visitor fills out the contact form on the portfolio
2. Clicks "Send Message"
3. Data is sent to the backend API
4. Flask validates and stores in MongoDB
5. Visitor sees success message
6. Admin can view submission in dashboard

### Admin Flow

1. Click "Admin" link
2. Enter admin password
3. See all submissions in real-time
4. View submission details
5. Delete submissions as needed
6. Stats update automatically

## API Endpoints

### Public Endpoints

- `POST /api/submit-contact` - Submit contact form
  - Body: `{ "name": "...", "email": "...", "message": "..." }`
  - Response: `{ "success": true, "submission_id": "..." }`

### Admin Endpoints

- `GET /api/admin/submissions?password=YOUR_PASSWORD`
  - Returns all submissions with count

- `DELETE /api/admin/delete/<submission_id>?password=YOUR_PASSWORD`
  - Deletes a specific submission

## MongoDB Database Schema

```javascript
// submissions collection
{
  _id: ObjectId,
  name: String,
  email: String,
  message: String,
  submitted_at: DateTime,
  ip_address: String,
  user_agent: String
}
```

## Security Notes

⚠️ **Important Security Considerations:**

1. Change `ADMIN_PASSWORD` in `.env` to a strong password
2. In production, use environment variables instead of `.env` file
3. Never commit `.env` to version control
4. Use HTTPS in production
5. Add rate limiting to prevent spam
6. Implement email verification for submissions
7. Use database backups regularly

## Troubleshooting

### MongoDB Connection Error
- Check if MongoDB is running
- Verify connection string in `.env`
- For local MongoDB: `mongod` should be running

### Port Already in Use
- The app runs on port 5000 by default
- To change: `app.run(port=5001)`

### Import Errors
- Make sure all packages are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

### Admin Password Not Working
- Check `.env` file has correct `ADMIN_PASSWORD`
- Password is case-sensitive
- Make sure there are no extra spaces

## Customization

### Change Admin Password

Edit `.env`:
```
ADMIN_PASSWORD=your_new_secure_password
```

### Change Database Name

Edit `.env`:
```
DB_NAME=my_portfolio_db
```

### Add More Form Fields

1. Edit `templates/index.html` - Add form fields
2. Edit `app.py` - Update `submit_contact()` function
3. Update MongoDB schema in documentation

### Deploy to Production

For deployment, consider:
- Heroku (with Atlas MongoDB)
- AWS Elastic Beanstalk
- DigitalOcean
- Railway
- Render

## File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Flask backend server with API endpoints |
| `requirements.txt` | Python package dependencies |
| `.env` | Configuration (passwords, DB connection) |
| `templates/index.html` | Portfolio website frontend |
| `templates/admin_login.html` | Admin authentication page |
| `templates/admin_dashboard.html` | Admin submission viewer |

## Features Overview

### Portfolio Page
- Responsive design
- Hero section with profile
- Navigation menu
- About section
- Skills showcase
- Projects gallery
- Experience timeline
- Contact form
- Footer with social links
- Smooth animations

### Admin Panel
- Secure login with password
- Real-time submission list
- Submission stats (#total, #today, last submission)
- View full message details
- Delete submissions
- Auto-refresh every 30 seconds
- Professional dark theme UI

## Future Enhancements

- Email notifications on new submissions
- CSV export of submissions
- Advanced filtering/search
- Submission status tracking
- File upload support
- reCAPTCHA integration
- Multi-language support
- Mobile app for admin

## License

This project is free to use and modify.

## Support

For issues or questions:
1. Check Troubleshooting section
2. Review error messages in console
3. Verify environment configuration
4. Check MongoDB connection

---

**Created**: 2026
**Last Updated**: February 18, 2026
