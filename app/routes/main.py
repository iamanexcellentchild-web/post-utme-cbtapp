from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Exam, Result

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    exams = Exam.query.filter_by(is_active=True).all()
    user_results = Result.query.filter_by(user_id=current_user.id).all()
    
    # Calculate statistics
    total_tests = len(user_results)
    passed_tests = sum(1 for r in user_results if r.is_passed)
    avg_score = sum(r.percentage for r in user_results) / len(user_results) if user_results else 0
    
    # Calculate total marks for each result for display
    for result in user_results:
        result.total_marks = sum(q.marks for q in result.exam.questions)
    
    return render_template('dashboard.html', 
                         exams=exams, 
                         user_results=user_results,
                         total_tests=total_tests,
                         passed_tests=passed_tests,
                         avg_score=avg_score)

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')
