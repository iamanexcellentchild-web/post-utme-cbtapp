# Getting Started with UNILAG CBT Practice

## Quick Start Guide

### Step 1: Prerequisites
Ensure you have Python 3.8+ installed on your system.
```bash
python --version
```

### Step 2: Project Setup

1. **Navigate to project directory:**
   ```bash
   cd c:\Users\HP\OneDrive\Desktop\MeritPostUtme
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create .env file:**
   ```bash
   copy .env.example .env
   ```

6. **Initialize database:**
   ```bash
   python seed_db.py
   ```

7. **Run the application:**
   ```bash
   python run.py
   ```

The application is now running at: **http://localhost:5000**

---

## How to Use the Application

### 1. **Create Account**
   - Click "Register" on the homepage
   - Fill in your details
   - Submit to create account

### 2. **Login**
   - Click "Login"
   - Enter your credentials
   - Access your dashboard

### 3. **Take Practice Exams**
   - View available exams on dashboard
   - Click "Start Exam"
   - Answer questions within time limit
   - Submit when done

### 4. **Review Results**
   - See detailed score breakdown
   - Review answer explanations
   - Track progress over time

---

## Adding Your Own Questions

Edit `seed_db.py` and add questions in the format:

```python
{
    'question_text': 'Your question here?',
    'option_a': 'Option A',
    'option_b': 'Option B',
    'option_c': 'Option C',
    'option_d': 'Option D',
    'correct_answer': 'A',  # Single letter
    'explanation': 'Why this is correct...'
}
```

Then run: `python seed_db.py`

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Port 5000 in use | Change port in `run.py` or kill the process |
| Database errors | Delete `cbt_app.db` and run `python seed_db.py` |
| Module not found | Run `pip install -r requirements.txt` again |
| Template not found | Check `app/templates/` folder structure |

---

## File Structure Explanation

```
app/
├── __init__.py          - App factory and configuration
├── models/              - Database models
├── routes/              - Application routes/endpoints
├── templates/           - HTML files
└── static/              - CSS, JS, images

run.py                   - Application entry point
seed_db.py               - Database seeding script
requirements.txt         - Python dependencies
.env.example             - Environment variables template
```

---

## Next Steps

1. ✅ Setup and run the application
2. 📝 Register a test account
3. 🧪 Take a sample exam
4. ➕ Add your own questions
5. 🎨 Customize styling if needed
6. 📤 Deploy to production (update security settings)

---

For more detailed documentation, see **README.md**
