# UNILAG CBT Practice Web Application

A comprehensive Computer-Based Testing (CBT) practice platform for UNILAG Post-UTME examinations.

## Features

- ✅ **User Authentication** - Secure registration and login
- 📚 **Multiple Practice Exams** - Organized by subject and difficulty
- ⏱️ **Timed Exams** - Practice under real exam conditions
- 📊 **Detailed Analytics** - Track performance and progress
- 💡 **Instant Feedback** - Get explanations for answers
- 📱 **Responsive Design** - Works on desktop and mobile
- 🔐 **Secure Database** - SQLite with encrypted passwords

## Project Structure

```
MeritPostUtme/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── exam.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── auth.py
│   │   └── exam.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── profile.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── exam/
│   │       ├── view_exam.html
│   │       ├── take_exam.html
│   │       └── result.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── exam.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   └── __init__.py
├── run.py
├── requirements.txt
├── seed_db.py
├── .env.example
└── README.md
```

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy with SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF

## Installation & Setup

### 1. Clone/Download the Project

```bash
cd MeritPostUtme
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and set your variables (optional for development)
```

### 5. Initialize Database

```bash
python seed_db.py
```

This will create the database and populate it with sample exams and questions.

### 6. Run the Application

```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Default Test Accounts

The seeding script populates the database with sample exams. Create your own account by registering on the application.

## Features Walkthrough

### 1. **Authentication**
   - Register with email, username, and password
   - Secure login system
   - Profile management

### 2. **Dashboard**
   - View all available exams
   - See statistics (tests taken, passed, average score)
   - Quick access to previous results
   - Start new exam attempts

### 3. **Taking Exams**
   - Multiple choice questions
   - Real-time timer
   - Question navigator
   - Auto-save answers
   - Comprehensive feedback after submission

### 4. **Results & Analytics**
   - Detailed score breakdown
   - Correct/incorrect answer analysis
   - Explanations for each question
   - Performance history

## API Endpoints

### Authentication Routes
- `GET /` - Homepage
- `GET/POST /login` - User login
- `GET/POST /register` - User registration
- `GET /logout` - User logout
- `GET /profile` - View user profile
- `POST /profile/update` - Update profile

### Dashboard Routes
- `GET /dashboard` - Main dashboard

### Exam Routes
- `GET /exam/<exam_id>` - View exam details
- `GET /exam/<exam_id>/start` - Start exam
- `GET /exam/<exam_id>/take/<result_id>` - Take exam
- `POST /exam/<exam_id>/submit/<result_id>` - Submit exam
- `GET /exam/<exam_id>/result/<result_id>` - View results
- `POST /api/exam/<exam_id>/submit-answer` - Auto-save answer

## Database Models

### User
- id
- username
- email
- password_hash
- full_name
- department
- admission_year
- created_at
- updated_at

### Exam
- id
- title
- subject
- description
- duration_minutes
- total_questions
- passing_score
- is_active
- created_at
- updated_at

### Question
- id
- exam_id
- question_text
- question_type
- option_a, option_b, option_c, option_d
- correct_answer
- explanation
- marks
- question_order

### Result
- id
- user_id
- exam_id
- total_score
- percentage
- is_passed
- started_at
- completed_at
- time_taken_seconds

### Answer
- id
- result_id
- question_id
- user_answer
- is_correct
- score_obtained
- answered_at
- time_spent_seconds

## Customization

### Adding New Exams

1. Edit `seed_db.py` to add more exams and questions
2. Run: `python seed_db.py`

### Changing Styling

- Edit `app/static/css/style.css` for global styles
- Edit `app/static/css/exam.css` for exam-specific styles

### Adding New Features

1. Create new route in `app/routes/`
2. Create corresponding template in `app/templates/`
3. Register blueprint in `app/__init__.py`

## Troubleshooting

### Port 5000 Already in Use
```bash
# Use different port
python -c "from run import app; app.run(port=5001)"
```

### Database Issues
```bash
# Remove existing database and reseed
rm cbt_app.db
python seed_db.py
```

### Module Not Found
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## Security Notes

- Change `SECRET_KEY` in `.env` for production
- Use environment variables for sensitive data
- Implement HTTPS for production
- Add CSRF protection for forms
- Rate limiting for login attempts
- Input validation and sanitization

## Future Enhancements

- [ ] Admin panel for exam management
- [ ] Question bank management
- [ ] Certificate generation
- [ ] Email notifications
- [ ] Mobile app
- [ ] Advanced analytics dashboard
- [ ] Question revision notes
- [ ] Study materials integration
- [ ] Leaderboards
- [ ] Social features

## Support & Contributing

For issues, bugs, or feature requests, please open an issue on the project repository.

## License

This project is open source and available under the MIT License.

## Author

Developed for UNILAG students

---

**Last Updated**: May 2024
**Version**: 1.0.0
