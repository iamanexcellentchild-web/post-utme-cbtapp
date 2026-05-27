from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from datetime import datetime, timedelta
from app import db
from app.models import Exam, Question, Result, Answer, Topic, User
from sqlalchemy import desc, func
import random

exam_bp = Blueprint('exam', __name__)

@exam_bp.route('/exam/<int:exam_id>')
@login_required
def view_exam(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    user_results = Result.query.filter_by(user_id=current_user.id, exam_id=exam_id).all()
    
    return render_template('exam/view_exam.html', exam=exam, user_results=user_results)

@exam_bp.route('/exam/<int:exam_id>/start')
@login_required
def start_exam(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    
    # Create a new result entry
    result = Result(user_id=current_user.id, exam_id=exam_id, started_at=datetime.utcnow())
    db.session.add(result)
    db.session.commit()
    
    return redirect(url_for('exam.take_exam', exam_id=exam_id, result_id=result.id))

@exam_bp.route('/exam/<int:exam_id>/take/<int:result_id>')
@login_required
def take_exam(exam_id, result_id):
    exam = Exam.query.get_or_404(exam_id)
    result = Result.query.get_or_404(result_id)
    
    # Security check
    if result.user_id != current_user.id:
        flash('You do not have permission to take this exam.', 'error')
        return redirect(url_for('main.dashboard'))
    
    # Check if exam time has expired
    if result.completed_at:
        flash('This exam has already been completed.', 'info')
        return redirect(url_for('exam.view_exam', exam_id=exam_id))
    
    questions = Question.query.filter_by(exam_id=exam_id).order_by(Question.question_order).all()
    
    return render_template('exam/take_exam.html', exam=exam, result=result, questions=questions)

@exam_bp.route('/api/exam/<int:exam_id>/submit-answer', methods=['POST'])
@login_required
def submit_answer(exam_id):
    data = request.get_json()
    result_id = data.get('result_id')
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    
    result = Result.query.get_or_404(result_id)
    question = Question.query.get_or_404(question_id)
    
    # Security check
    if result.user_id != current_user.id or question.exam_id != exam_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    # Check if already answered
    existing_answer = Answer.query.filter_by(result_id=result_id, question_id=question_id).first()
    
    is_correct = user_answer == question.correct_answer
    score = question.marks if is_correct else 0
    
    if existing_answer:
        existing_answer.user_answer = user_answer
        existing_answer.is_correct = is_correct
        existing_answer.score_obtained = score
    else:
        answer = Answer(
            result_id=result_id,
            question_id=question_id,
            user_answer=user_answer,
            is_correct=is_correct,
            score_obtained=score
        )
        db.session.add(answer)
    
    db.session.commit()
    
    return jsonify({'success': True, 'is_correct': is_correct})

@exam_bp.route('/exam/<int:exam_id>/submit/<int:result_id>', methods=['POST'])
@login_required
def submit_exam(exam_id, result_id):
    exam = Exam.query.get_or_404(exam_id)
    result = Result.query.get_or_404(result_id)
    
    # Security check
    if result.user_id != current_user.id:
        flash('You do not have permission to submit this exam.', 'error')
        return redirect(url_for('main.dashboard'))
    
    # Calculate score
    answers = Answer.query.filter_by(result_id=result_id).all()
    total_score = sum(a.score_obtained for a in answers)
    
    # Get total possible marks
    questions = Question.query.filter_by(exam_id=exam_id).all()
    total_marks = sum(q.marks for q in questions)
    
    percentage = (total_score / total_marks * 100) if total_marks > 0 else 0
    is_passed = percentage >= exam.passing_score
    
    # Update result
    result.completed_at = datetime.utcnow()
    result.total_score = total_score
    result.percentage = percentage
    result.is_passed = is_passed
    result.time_taken_seconds = int((result.completed_at - result.started_at).total_seconds())
    
    db.session.commit()
    
    return redirect(url_for('exam.view_result', exam_id=exam_id, result_id=result_id))

@exam_bp.route('/exam/<int:exam_id>/result/<int:result_id>')
@login_required
def view_result(exam_id, result_id):
    exam = Exam.query.get_or_404(exam_id)
    result = Result.query.get_or_404(result_id)
    
    # Security check
    if result.user_id != current_user.id:
        flash('You do not have permission to view this result.', 'error')
        return redirect(url_for('main.dashboard'))
    
    answers = Answer.query.filter_by(result_id=result_id).all()
    
    # Calculate total marks for display
    total_marks = sum(q.marks for q in exam.questions)
    
    return render_template('exam/result.html', exam=exam, result=result, answers=answers, total_marks=total_marks)


# ============ FEATURE 1: EXAM MODE (40 questions, 30 minutes, graded) ============

@exam_bp.route('/exam-mode')
@login_required
def exam_mode_home():
    """Display exam mode overview"""
    return render_template('exam/exam_mode.html')


@exam_bp.route('/exam-mode/start', methods=['POST'])
@login_required
def exam_mode_start():
    """Start a new exam mode (40 questions, 30 min, mixed subjects)"""
    # Get random questions from Maths, English, General Paper (if exists)
    subjects = ['Mathematics', 'English', 'General Paper']
    
    # Get approximately 20 from Maths, 15 from English, 5 from General (or available)
    all_questions = []
    
    for subject in subjects:
        questions = Question.query.filter_by(subject=subject).all()
        if subject == 'Mathematics':
            all_questions.extend(random.sample(questions, min(20, len(questions))))
        elif subject == 'English':
            all_questions.extend(random.sample(questions, min(15, len(questions))))
        else:
            all_questions.extend(random.sample(questions, min(5, len(questions))))
    
    # If we don't have enough questions, take what we can get
    if len(all_questions) < 40:
        all_questions = random.sample(all_questions, len(all_questions))
    else:
        all_questions = random.sample(all_questions, 40)
    
    # Create a result entry for exam mode
    exam = Exam.query.filter_by(title='Full Exam').first()
    if not exam:
        # Use first exam as base
        exam = Exam.query.first()
    
    result = Result(
        user_id=current_user.id,
        exam_id=exam.id if exam else 1,
        exam_mode='full_exam',
        selected_subjects='Mathematics,English,General Paper',
        num_questions_allowed=40,
        time_limit_minutes=30,
        passing_score=30,
        started_at=datetime.utcnow()
    )
    db.session.add(result)
    db.session.commit()
    
    return jsonify({'success': True, 'result_id': result.id, 'redirect': url_for('exam.exam_mode_take', result_id=result.id)})


@exam_bp.route('/exam-mode/take/<int:result_id>')
@login_required
def exam_mode_take(result_id):
    """Take the full exam"""
    result = Result.query.get_or_404(result_id)
    
    if result.user_id != current_user.id:
        flash('Unauthorized access.', 'error')
        return redirect(url_for('main.dashboard'))
    
    if result.completed_at:
        flash('This exam has already been completed.', 'info')
        return redirect(url_for('exam.exam_mode_result', result_id=result_id))
    
    # Get all questions for this result
    answers = Answer.query.filter_by(result_id=result_id).all()
    answered_question_ids = [a.question_id for a in answers]
    
    # Get all questions from selected subjects
    subjects = result.selected_subjects.split(',')
    questions = Question.query.filter(Question.subject.in_(subjects)).order_by(func.random()).limit(40).all()
    
    return render_template('exam/exam_mode_take.html', result=result, questions=questions, answered_ids=answered_question_ids)


@exam_bp.route('/exam-mode/result/<int:result_id>')
@login_required
def exam_mode_result(result_id):
    """View exam mode result"""
    result = Result.query.get_or_404(result_id)
    
    if result.user_id != current_user.id:
        flash('Unauthorized access.', 'error')
        return redirect(url_for('main.dashboard'))
    
    answers = Answer.query.filter_by(result_id=result_id).all()
    total_marks = 40  # 40 questions × 1 mark
    
    return render_template('exam/exam_mode_result.html', result=result, answers=answers, total_marks=total_marks)


@exam_bp.route('/api/exam-mode/<int:result_id>/submit-answer', methods=['POST'])
@login_required
def exam_mode_submit_answer(result_id):
    """Submit answer for exam mode"""
    data = request.get_json()
    result = Result.query.get_or_404(result_id)
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    
    if result.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    question = Question.query.get_or_404(question_id)
    
    existing_answer = Answer.query.filter_by(result_id=result_id, question_id=question_id).first()
    is_correct = user_answer == question.correct_answer
    score = question.marks if is_correct else 0
    
    if existing_answer:
        existing_answer.user_answer = user_answer
        existing_answer.is_correct = is_correct
        existing_answer.score_obtained = score
    else:
        answer = Answer(
            result_id=result_id,
            question_id=question_id,
            user_answer=user_answer,
            is_correct=is_correct,
            score_obtained=score
        )
        db.session.add(answer)
    
    db.session.commit()
    return jsonify({'success': True, 'is_correct': is_correct})


@exam_bp.route('/api/exam-mode/<int:result_id>/finish', methods=['POST'])
@login_required
def exam_mode_finish(result_id):
    """Finish and grade exam mode"""
    result = Result.query.get_or_404(result_id)
    
    if result.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    answers = Answer.query.filter_by(result_id=result_id).all()
    total_score = sum(a.score_obtained for a in answers)
    
    result.completed_at = datetime.utcnow()
    result.total_score = total_score
    result.percentage = (total_score / 40 * 100)  # 40 marks total
    result.is_passed = result.total_score >= result.passing_score
    result.is_graded = True
    result.time_taken_seconds = int((result.completed_at - result.started_at).total_seconds())
    
    db.session.commit()
    
    return jsonify({'success': True, 'redirect': url_for('exam.exam_mode_result', result_id=result_id)})


# ============ FEATURE 2: PRACTICE MODE (Topic-based practice) ============

@exam_bp.route('/practice-mode')
@login_required
def practice_mode_home():
    """Select subject and topic for practice"""
    topics = Topic.query.all()
    subjects = db.session.query(Topic.subject).distinct().all()
    subjects = [s[0] for s in subjects]
    
    return render_template('exam/practice_mode.html', subjects=subjects, topics=topics)


@exam_bp.route('/practice-mode/subjects')
@login_required
def practice_mode_subjects():
    """Get topics for a subject"""
    subject = request.args.get('subject')
    topics = Topic.query.filter_by(subject=subject).all()
    
    return jsonify({
        'topics': [{'id': t.id, 'name': t.name, 'description': t.description} for t in topics]
    })


@exam_bp.route('/practice-mode/start/<int:topic_id>', methods=['POST'])
@login_required
def practice_mode_start(topic_id):
    """Start practice for a specific topic"""
    topic = Topic.query.get_or_404(topic_id)
    
    # Get questions for this topic
    questions = Question.query.filter_by(topic_id=topic_id).all()
    
    if not questions:
        return jsonify({'error': 'No questions available for this topic'}), 404
    
    # Create result entry
    exam = Exam.query.first()
    result = Result(
        user_id=current_user.id,
        exam_id=exam.id if exam else 1,
        exam_mode='practice_topic',
        selected_topic_id=topic_id,
        num_questions_allowed=len(questions),
        time_limit_minutes=None,  # No time limit for practice
        passing_score=0,  # Not graded
        is_graded=False,
        started_at=datetime.utcnow()
    )
    db.session.add(result)
    db.session.commit()
    
    return jsonify({'success': True, 'result_id': result.id, 'redirect': url_for('exam.practice_mode_take', result_id=result.id)})


@exam_bp.route('/practice-mode/take/<int:result_id>')
@login_required
def practice_mode_take(result_id):
    """Take practice questions for topic"""
    result = Result.query.get_or_404(result_id)
    
    if result.user_id != current_user.id:
        flash('Unauthorized access.', 'error')
        return redirect(url_for('main.dashboard'))
    
    # Get questions for this topic
    questions = Question.query.filter_by(topic_id=result.selected_topic_id).all()
    answered_ids = [a.question_id for a in result.answers]
    
    return render_template('exam/practice_mode_take.html', result=result, questions=questions, answered_ids=answered_ids)


@exam_bp.route('/practice-mode/result/<int:result_id>')
@login_required
def practice_mode_result(result_id):
    """View practice mode result"""
    result = Result.query.get_or_404(result_id)
    
    if result.user_id != current_user.id:
        flash('Unauthorized access.', 'error')
        return redirect(url_for('main.dashboard'))
    
    if not result.completed_at:
        # Calculate score
        answers = Answer.query.filter_by(result_id=result_id).all()
        total_score = sum(a.score_obtained for a in answers)
        total_questions = len(answers)
        
        result.completed_at = datetime.utcnow()
        result.total_score = total_score
        result.percentage = (total_score / total_questions * 100) if total_questions > 0 else 0
        result.time_taken_seconds = int((result.completed_at - result.started_at).total_seconds())
        
        db.session.commit()
    
    answers = Answer.query.filter_by(result_id=result_id).all()
    
    return render_template('exam/practice_mode_result.html', result=result, answers=answers)


@exam_bp.route('/api/practice-mode/<int:result_id>/submit-answer', methods=['POST'])
@login_required
def practice_mode_submit_answer(result_id):
    """Submit answer for practice mode"""
    data = request.get_json()
    result = Result.query.get_or_404(result_id)
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    
    if result.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    question = Question.query.get_or_404(question_id)
    
    existing_answer = Answer.query.filter_by(result_id=result_id, question_id=question_id).first()
    is_correct = user_answer == question.correct_answer
    score = question.marks if is_correct else 0
    
    if existing_answer:
        existing_answer.user_answer = user_answer
        existing_answer.is_correct = is_correct
        existing_answer.score_obtained = score
    else:
        answer = Answer(
            result_id=result_id,
            question_id=question_id,
            user_answer=user_answer,
            is_correct=is_correct,
            score_obtained=score
        )
        db.session.add(answer)
    
    db.session.commit()
    return jsonify({'success': True, 'is_correct': is_correct, 'explanation': question.explanation})


# ============ FEATURE 3: LEADERBOARD ============

@exam_bp.route('/leaderboard')
@login_required
def leaderboard():
    """Display top scores from exam mode"""
    # Get top 50 exam mode results, ordered by score
    top_results = Result.query.filter_by(exam_mode='full_exam', is_graded=True)\
        .order_by(desc(Result.total_score))\
        .limit(50).all()
    
    # Get current user's rank
    user_rank = db.session.query(func.count(Result.id)).filter(
        Result.exam_mode == 'full_exam',
        Result.is_graded == True,
        Result.total_score > current_user.results[0].total_score if current_user.results else 0
    ).scalar() + 1
    
    return render_template('exam/leaderboard.html', top_results=top_results, user_rank=user_rank)
