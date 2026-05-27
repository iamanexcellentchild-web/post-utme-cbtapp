from app import db
from datetime import datetime

class Topic(db.Model):
    __tablename__ = 'topics'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)  # e.g., "Algebra", "Comprehension"
    subject = db.Column(db.String(100), nullable=False)  # e.g., "Mathematics", "English", "General"
    description = db.Column(db.Text)
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    questions = db.relationship('Question', backref='topic', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Topic {self.name}>'

class Exam(db.Model):
    __tablename__ = 'exams'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    duration_minutes = db.Column(db.Integer, default=60)
    total_questions = db.Column(db.Integer)
    passing_score = db.Column(db.Integer, default=50)
    
    # Metadata
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    questions = db.relationship('Question', backref='exam', lazy=True, cascade='all, delete-orphan')
    results = db.relationship('Result', backref='exam', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Exam {self.title}>'

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=True)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(20), default='multiple_choice')  # multiple_choice, true_false, fill_blank
    subject = db.Column(db.String(100), nullable=False)  # Mathematics, English, General
    
    # For multiple choice
    option_a = db.Column(db.String(500))
    option_b = db.Column(db.String(500))
    option_c = db.Column(db.String(500))
    option_d = db.Column(db.String(500))
    
    correct_answer = db.Column(db.String(1), nullable=False)  # A, B, C, D, True, False
    explanation = db.Column(db.Text)
    
    # Metadata
    marks = db.Column(db.Integer, default=1)
    question_order = db.Column(db.Integer)
    difficulty = db.Column(db.String(20), default='medium')  # easy, medium, hard
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    answers = db.relationship('Answer', backref='question', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Question {self.id}>'

class Result(db.Model):
    __tablename__ = 'results'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), nullable=False)
    
    # Exam Mode: 'practice_topic', 'full_exam', 'subject_practice', 'custom_timed'
    exam_mode = db.Column(db.String(50), default='practice_topic')
    
    # Mode Settings
    selected_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=True)
    selected_subjects = db.Column(db.String(200))  # Comma-separated: 'Mathematics,English,General'
    num_questions_allowed = db.Column(db.Integer, default=40)  # For full exam and custom
    time_limit_minutes = db.Column(db.Integer, default=30)  # For full exam and custom
    
    # Score
    total_score = db.Column(db.Float, default=0)
    percentage = db.Column(db.Float, default=0)
    passing_score = db.Column(db.Integer, default=30)  # 30 marks out of 40
    is_passed = db.Column(db.Boolean, default=False)
    is_graded = db.Column(db.Boolean, default=False)  # False for practice mode
    
    # Timing
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    time_taken_seconds = db.Column(db.Integer)
    
    # Relationships
    answers = db.relationship('Answer', backref='result', lazy=True, cascade='all, delete-orphan')
    selected_topic = db.relationship('Topic', foreign_keys=[selected_topic_id])
    
    def __repr__(self):
        return f'<Result User:{self.user_id} Mode:{self.exam_mode}>'

class Answer(db.Model):
    __tablename__ = 'answers'
    
    id = db.Column(db.Integer, primary_key=True)
    result_id = db.Column(db.Integer, db.ForeignKey('results.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    
    # User's answer
    user_answer = db.Column(db.String(500))
    is_correct = db.Column(db.Boolean, default=False)
    score_obtained = db.Column(db.Float, default=0)
    
    # Timing
    answered_at = db.Column(db.DateTime, default=datetime.utcnow)
    time_spent_seconds = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Answer Question:{self.question_id}>'
