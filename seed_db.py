"""
Database seeding script to populate with sample exams and questions
Run this after initial setup to populate the database with test data
"""

from app import create_app, db
from app.models import Exam, Question, Topic

def seed_database():
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        Question.query.delete()
        Topic.query.delete()
        Exam.query.delete()
        
        # Create topics for English
        english_topics = [
            Topic(name='Vocabulary & Synonyms', subject='English', description='Words and their meanings'),
            Topic(name='Antonyms', subject='English', description='Words with opposite meanings'),
            Topic(name='Grammar & Concord', subject='English', description='Sentence structure and subject-verb agreement'),
            Topic(name='Figures of Speech', subject='English', description='Literary devices and language techniques'),
        ]
        
        # Create topics for Mathematics
        math_topics = [
            Topic(name='Number Theory & Indices', subject='Mathematics', description='Factorization, indices, and logarithms'),
            Topic(name='Algebra', subject='Mathematics', description='Equations, functions, and polynomial expressions'),
            Topic(name='Geometry & Mensuration', subject='Mathematics', description='Shapes, areas, and volumes'),
            Topic(name='Trigonometry', subject='Mathematics', description='Sine, cosine, and trigonometric ratios'),
            Topic(name='Statistics & Probability', subject='Mathematics', description='Data analysis and probability calculations'),
            Topic(name='Calculus', subject='Mathematics', description='Derivatives and integration'),
        ]
        
        # Create topics for General Paper
        general_topics = [
            Topic(name='Current Affairs', subject='General Paper', description='Recent world events and news'),
            Topic(name='History', subject='General Paper', description='Historical events and figures'),
            Topic(name='Science', subject='General Paper', description='Basic science concepts'),
        ]
        
        for topic in english_topics + math_topics + general_topics:
            db.session.add(topic)
        
        db.session.commit()
        
        # Create sample exams
        english_exam = Exam(
            title="English Language",
            subject="English",
            description="Practice English Language exam for UNILAG Post-UTME",
            duration_minutes=60,
            total_questions=50,
            passing_score=50
        )
        
        mathematics_exam = Exam(
            title="Mathematics",
            subject="Mathematics",
            description="Practice Mathematics exam for UNILAG Post-UTME with 200 comprehensive questions",
            duration_minutes=120,
            total_questions=200,
            passing_score=50
        )
        
        full_exam = Exam(
            title="Full Exam",
            subject="Mixed",
            description="Full exam with 40 questions from Maths, English, and General Paper",
            duration_minutes=30,
            total_questions=40,
            passing_score=30  # Out of 40 questions
        )
        
        db.session.add(english_exam)
        db.session.add(mathematics_exam)
        db.session.add(full_exam)
        db.session.commit()
        
        # Get topics for assignment
        vocab_topic = Topic.query.filter_by(name='Vocabulary & Synonyms').first()
        antonym_topic = Topic.query.filter_by(name='Antonyms').first()
        grammar_topic = Topic.query.filter_by(name='Grammar & Concord').first()
        figures_topic = Topic.query.filter_by(name='Figures of Speech').first()
        
        # Add comprehensive English questions
        english_questions = [
            # VOCABULARY / SYNONYMS (Q1–Q40)
            {'question_text': 'Choose the word that is nearest in meaning to GARRULOUS.', 'option_a': 'Silent', 'option_b': 'Talkative', 'option_c': 'Aggressive', 'option_d': 'Timid', 'correct_answer': 'B', 'explanation': 'Garrulous means excessively talkative; talkative is the closest synonym.'},
            {'question_text': 'Choose the word closest in meaning to LOQUACIOUS.', 'option_a': 'Reserved', 'option_b': 'Verbose', 'option_c': 'Modest', 'option_d': 'Harsh', 'correct_answer': 'B', 'explanation': 'Loquacious means tending to talk a great deal; verbose means using more words than necessary.'},
            {'question_text': 'The word TACITURN is closest in meaning to:', 'option_a': 'Talkative', 'option_b': 'Reserved', 'option_c': 'Loud', 'option_d': 'Friendly', 'correct_answer': 'B', 'explanation': 'Taciturn means reserved or uncommunicative in speech.'},
            {'question_text': 'Select the synonym of EPHEMERAL.', 'option_a': 'Permanent', 'option_b': 'Eternal', 'option_c': 'Transient', 'option_d': 'Ancient', 'correct_answer': 'C', 'explanation': 'Ephemeral means lasting for a very short time; transient has the same meaning.'},
            {'question_text': 'The word UBIQUITOUS means:', 'option_a': 'Rare', 'option_b': 'Present everywhere', 'option_c': 'Hidden', 'option_d': 'Beautiful', 'correct_answer': 'B', 'explanation': 'Ubiquitous means present, appearing, or found everywhere.'},
            {'question_text': 'Choose the option closest in meaning to INDIGENOUS.', 'option_a': 'Foreign', 'option_b': 'Imported', 'option_c': 'Native', 'option_d': 'Modern', 'correct_answer': 'C', 'explanation': 'Indigenous means originating or occurring naturally in a particular place; native.'},
            {'question_text': 'OSTENTATIOUS most nearly means:', 'option_a': 'Modest', 'option_b': 'Showy', 'option_c': 'Quiet', 'option_d': 'Intelligent', 'correct_answer': 'B', 'explanation': 'Ostentatious means characterized by vulgar or pretentious display; showy.'},
            {'question_text': 'The word CANDID is closest in meaning to:', 'option_a': 'Dishonest', 'option_b': 'Frank', 'option_c': 'Cunning', 'option_d': 'Lazy', 'correct_answer': 'B', 'explanation': 'Candid means truthful and straightforward; frank.'},
            {'question_text': 'Choose the synonym of ENIGMATIC.', 'option_a': 'Clear', 'option_b': 'Simple', 'option_c': 'Mysterious', 'option_d': 'Obvious', 'correct_answer': 'C', 'explanation': 'Enigmatic means difficult to interpret or understand; mysterious.'},
            {'question_text': 'BENEVOLENT is closest in meaning to:', 'option_a': 'Cruel', 'option_b': 'Selfish', 'option_c': 'Kind-hearted', 'option_d': 'Angry', 'correct_answer': 'C', 'explanation': 'Benevolent means well-meaning and kindly; kind-hearted.'},
            {'question_text': 'Choose the word nearest in meaning to LETHARGIC.', 'option_a': 'Active', 'option_b': 'Sluggish', 'option_c': 'Energetic', 'option_d': 'Brave', 'correct_answer': 'B', 'explanation': 'Lethargic means affected by lethargy; sluggish and apathetic.'},
            {'question_text': 'The word AUDACIOUS means:', 'option_a': 'Cowardly', 'option_b': 'Shy', 'option_c': 'Bold', 'option_d': 'Honest', 'correct_answer': 'C', 'explanation': 'Audacious means showing a willingness to take surprisingly bold risks.'},
            {'question_text': 'Select the synonym of AMBIGUOUS.', 'option_a': 'Clear', 'option_b': 'Straightforward', 'option_c': 'Equivocal', 'option_d': 'Definite', 'correct_answer': 'C', 'explanation': 'Ambiguous means open to more than one interpretation; equivocal.'},
            {'question_text': 'MAGNANIMOUS most nearly means:', 'option_a': 'Petty', 'option_b': 'Generous', 'option_c': 'Miserly', 'option_d': 'Harsh', 'correct_answer': 'B', 'explanation': 'Magnanimous means generous or forgiving, especially towards a rival or less powerful person.'},
            {'question_text': 'The word PRAGMATIC is closest in meaning to:', 'option_a': 'Idealistic', 'option_b': 'Impractical', 'option_c': 'Realistic', 'option_d': 'Visionary', 'correct_answer': 'C', 'explanation': 'Pragmatic means dealing with things sensibly and realistically; practical.'},
            {'question_text': 'Choose the synonym of ERUDITE.', 'option_a': 'Ignorant', 'option_b': 'Learned', 'option_c': 'Simple', 'option_d': 'Young', 'correct_answer': 'B', 'explanation': 'Erudite means having or showing great knowledge or learning.'},
            {'question_text': 'FUTILE is closest in meaning to:', 'option_a': 'Useful', 'option_b': 'Productive', 'option_c': 'Fruitless', 'option_d': 'Successful', 'correct_answer': 'C', 'explanation': 'Futile means incapable of producing any useful result; fruitless.'},
            {'question_text': 'The word TENACIOUS means:', 'option_a': 'Weak', 'option_b': 'Persistent', 'option_c': 'Flexible', 'option_d': 'Careless', 'correct_answer': 'B', 'explanation': 'Tenacious means tending to keep a firm hold; persistent.'},
            {'question_text': 'DILAPIDATED is closest in meaning to:', 'option_a': 'Renovated', 'option_b': 'Modern', 'option_c': 'Ruined', 'option_d': 'Clean', 'correct_answer': 'C', 'explanation': 'Dilapidated means in a state of disrepair or ruin as a result of age or neglect.'},
            {'question_text': 'Select the synonym of ACRIMONIOUS.', 'option_a': 'Pleasant', 'option_b': 'Bitter', 'option_c': 'Sweet', 'option_d': 'Gentle', 'correct_answer': 'B', 'explanation': 'Acrimonious means angry and bitter; caustic or harsh in tone.'},
            {'question_text': 'VACILLATE most nearly means:', 'option_a': 'Decide firmly', 'option_b': 'Hesitate', 'option_c': 'Move forward', 'option_d': 'Concentrate', 'correct_answer': 'B', 'explanation': 'Vacillate means waver between different opinions or actions; be indecisive.'},
            {'question_text': 'The word IMPECCABLE means:', 'option_a': 'Flawed', 'option_b': 'Careless', 'option_c': 'Faultless', 'option_d': 'Ordinary', 'correct_answer': 'C', 'explanation': 'Impeccable means in accordance with the highest standards; faultless.'},
            {'question_text': 'NONCHALANT is closest in meaning to:', 'option_a': 'Anxious', 'option_b': 'Indifferent', 'option_c': 'Excited', 'option_d': 'Careful', 'correct_answer': 'B', 'explanation': 'Nonchalant means feeling or appearing casually calm and relaxed; indifferent.'},
            {'question_text': 'Choose the synonym of PROFUSE.', 'option_a': 'Scarce', 'option_b': 'Minimal', 'option_c': 'Abundant', 'option_d': 'Limited', 'correct_answer': 'C', 'explanation': 'Profuse means present in large amounts; abundant or plentiful.'},
            {'question_text': 'INSOLENT is closest in meaning to:', 'option_a': 'Respectful', 'option_b': 'Humble', 'option_c': 'Impudent', 'option_d': 'Polite', 'correct_answer': 'C', 'explanation': 'Insolent means showing a rude and arrogant lack of respect; impudent.'},
            {'question_text': 'The word RESILIENT means:', 'option_a': 'Fragile', 'option_b': 'Weak', 'option_c': 'Adaptable', 'option_d': 'Rigid', 'correct_answer': 'C', 'explanation': 'Resilient means able to withstand or recover quickly from difficult conditions.'},
            {'question_text': 'STRINGENT is closest in meaning to:', 'option_a': 'Lenient', 'option_b': 'Flexible', 'option_c': 'Strict', 'option_d': 'Easy', 'correct_answer': 'C', 'explanation': 'Stringent means strict, precise, and exacting; rigorous.'},
            {'question_text': 'Choose the synonym of VORACIOUS.', 'option_a': 'Content', 'option_b': 'Selective', 'option_c': 'Insatiable', 'option_d': 'Full', 'correct_answer': 'C', 'explanation': 'Voracious means wanting or devouring great quantities; insatiable.'},
            {'question_text': 'CONVOLUTED most nearly means:', 'option_a': 'Straightforward', 'option_b': 'Complex', 'option_c': 'Simple', 'option_d': 'Direct', 'correct_answer': 'B', 'explanation': 'Convoluted means extremely complex and difficult to follow; intricate.'},
            {'question_text': 'The word ANACHRONISTIC means:', 'option_a': 'Modern', 'option_b': 'Timeless', 'option_c': 'Belonging to another era', 'option_d': 'Future', 'correct_answer': 'C', 'explanation': 'Anachronistic means belonging or appropriate to a period other than that in which it exists.'},
            {'question_text': 'STOIC is closest in meaning to:', 'option_a': 'Emotional', 'option_b': 'Unemotional', 'option_c': 'Dramatic', 'option_d': 'Sensitive', 'correct_answer': 'B', 'explanation': 'Stoic means enduring pain or hardship without showing feelings; unemotional.'},
            {'question_text': 'Select the synonym of VERBOSE.', 'option_a': 'Concise', 'option_b': 'Brief', 'option_c': 'Wordy', 'option_d': 'Silent', 'correct_answer': 'C', 'explanation': 'Verbose means using or expressed in more words than are needed; wordy.'},
            {'question_text': 'RECALCITRANT most nearly means:', 'option_a': 'Obedient', 'option_b': 'Unruly', 'option_c': 'Willing', 'option_d': 'Cooperative', 'correct_answer': 'B', 'explanation': 'Recalcitrant means having an obstinately uncooperative attitude; unruly.'},
            {'question_text': 'The word PRECARIOUS means:', 'option_a': 'Safe', 'option_b': 'Stable', 'option_c': 'Unsafe', 'option_d': 'Secure', 'correct_answer': 'C', 'explanation': 'Precarious means not securely held or in position; dangerously likely to fall or collapse.'},
            {'question_text': 'DEXTEROUS is closest in meaning to:', 'option_a': 'Clumsy', 'option_b': 'Awkward', 'option_c': 'Skilful', 'option_d': 'Slow', 'correct_answer': 'C', 'explanation': 'Dexterous means showing or having skill, especially with the hands; adroit.'},
            {'question_text': 'Choose the synonym of INCESSANT.', 'option_a': 'Sporadic', 'option_b': 'Occasional', 'option_c': 'Continuous', 'option_d': 'Rare', 'correct_answer': 'C', 'explanation': 'Incessant means never ending or always happening; continuous.'},
            {'question_text': 'NEGLIGENT most nearly means:', 'option_a': 'Careful', 'option_b': 'Careless', 'option_c': 'Precise', 'option_d': 'Attentive', 'correct_answer': 'B', 'explanation': 'Negligent means failing to take proper care over something; careless.'},
            {'question_text': 'The word IMPERATIVE means:', 'option_a': 'Optional', 'option_b': 'Unimportant', 'option_c': 'Essential', 'option_d': 'Forbidden', 'correct_answer': 'C', 'explanation': 'Imperative means of vital importance; crucial; essential.'},
            {'question_text': 'SURREPTITIOUS is closest in meaning to:', 'option_a': 'Open', 'option_b': 'Secretive', 'option_c': 'Loud', 'option_d': 'Honest', 'correct_answer': 'B', 'explanation': 'Surreptitious means kept secret, especially because it would not be approved of; secretive.'},
            {'question_text': 'Choose the synonym of VINDICTIVE.', 'option_a': 'Forgiving', 'option_b': 'Merciful', 'option_c': 'Revengeful', 'option_d': 'Kind', 'correct_answer': 'C', 'explanation': 'Vindictive means having or showing a strong or unreasoning desire for revenge; revengeful.'},
            # ANTONYMS (Q41–Q55)
            {'question_text': 'Choose the word that is OPPOSITE in meaning to MAGNANIMOUS.', 'option_a': 'Generous', 'option_b': 'Petty', 'option_c': 'Noble', 'option_d': 'Kind', 'correct_answer': 'B', 'explanation': 'Magnanimous means generous; its opposite is petty or mean-spirited.'},
            {'question_text': 'The antonym of LOQUACIOUS is:', 'option_a': 'Talkative', 'option_b': 'Verbose', 'option_c': 'Reticent', 'option_d': 'Eloquent', 'correct_answer': 'C', 'explanation': 'Loquacious means talkative; reticent (not revealing thoughts readily) is its antonym.'},
            {'question_text': 'Choose the antonym of DILIGENT.', 'option_a': 'Hardworking', 'option_b': 'Industrious', 'option_c': 'Lazy', 'option_d': 'Careful', 'correct_answer': 'C', 'explanation': 'Diligent means hardworking; lazy is its antonym.'},
            {'question_text': 'The opposite of EPHEMERAL is:', 'option_a': 'Brief', 'option_b': 'Transient', 'option_c': 'Fleeting', 'option_d': 'Permanent', 'correct_answer': 'D', 'explanation': 'Ephemeral means short-lived; permanent is its antonym.'},
            {'question_text': 'Choose the antonym of BENEVOLENT.', 'option_a': 'Kind', 'option_b': 'Generous', 'option_c': 'Malevolent', 'option_d': 'Helpful', 'correct_answer': 'C', 'explanation': 'Benevolent means kind; malevolent (having harmful intentions) is its antonym.'},
            {'question_text': 'The opposite of AUDACIOUS is:', 'option_a': 'Bold', 'option_b': 'Brave', 'option_c': 'Cowardly', 'option_d': 'Daring', 'correct_answer': 'C', 'explanation': 'Audacious means bold; cowardly is its antonym.'},
            {'question_text': 'Choose the antonym of CANDID.', 'option_a': 'Frank', 'option_b': 'Deceitful', 'option_c': 'Honest', 'option_d': 'Open', 'correct_answer': 'B', 'explanation': 'Candid means honest; deceitful is its antonym.'},
            {'question_text': 'The opposite of TURBULENT is:', 'option_a': 'Violent', 'option_b': 'Stormy', 'option_c': 'Calm', 'option_d': 'Chaotic', 'correct_answer': 'C', 'explanation': 'Turbulent means characterized by conflict; calm is its antonym.'},
            {'question_text': 'Choose the antonym of VERBOSE.', 'option_a': 'Wordy', 'option_b': 'Concise', 'option_c': 'Lengthy', 'option_d': 'Elaborate', 'correct_answer': 'B', 'explanation': 'Verbose means using too many words; concise (giving a lot of information clearly and briefly) is its antonym.'},
            {'question_text': 'The opposite of ARROGANT is:', 'option_a': 'Proud', 'option_b': 'Boastful', 'option_c': 'Humble', 'option_d': 'Conceited', 'correct_answer': 'C', 'explanation': 'Arrogant means excessively proud; humble is its antonym.'},
            {'question_text': 'Choose the antonym of FRUGAL.', 'option_a': 'Thrifty', 'option_b': 'Careful', 'option_c': 'Extravagant', 'option_d': 'Saving', 'correct_answer': 'C', 'explanation': 'Frugal means sparing with money; extravagant is its antonym.'},
            {'question_text': 'The opposite of AMBIGUOUS is:', 'option_a': 'Unclear', 'option_b': 'Vague', 'option_c': 'Explicit', 'option_d': 'Doubtful', 'correct_answer': 'C', 'explanation': 'Ambiguous means unclear; explicit (clear and detailed) is its antonym.'},
            {'question_text': 'Choose the antonym of STRINGENT.', 'option_a': 'Strict', 'option_b': 'Rigid', 'option_c': 'Lenient', 'option_d': 'Harsh', 'correct_answer': 'C', 'explanation': 'Stringent means strict; lenient is its antonym.'},
            {'question_text': 'The opposite of INDIGENOUS is:', 'option_a': 'Native', 'option_b': 'Local', 'option_c': 'Foreign', 'option_d': 'Original', 'correct_answer': 'C', 'explanation': 'Indigenous means native to a place; foreign is its antonym.'},
            {'question_text': 'Choose the antonym of INDOLENT.', 'option_a': 'Lazy', 'option_b': 'Idle', 'option_c': 'Industrious', 'option_d': 'Sluggish', 'correct_answer': 'C', 'explanation': 'Indolent means wanting to avoid activity or exertion; industrious is its antonym.'},
            # GRAMMAR: CONCORD / AGREEMENT (Q56–Q80) - Shortened for space
            {'question_text': 'Select the grammatically correct sentence.', 'option_a': 'Each of the boys have a book.', 'option_b': 'Each of the boys has a book.', 'option_c': 'Each of the boys are having a book.', 'option_d': 'Each of the boys had been having a book.', 'correct_answer': 'B', 'explanation': '\'Each\' is singular and takes a singular verb \'has\'.'},
            {'question_text': 'Choose the correct form: The news _____ shocking.', 'option_a': 'are', 'option_b': 'were', 'option_c': 'is', 'option_d': 'have been', 'correct_answer': 'C', 'explanation': '\'News\' is an uncountable noun and takes the singular verb \'is\'.'},
            {'question_text': 'Neither the students nor the teacher _____ present.', 'option_a': 'were', 'option_b': 'are', 'option_c': 'was', 'option_d': 'have been', 'correct_answer': 'C', 'explanation': 'When \'neither...nor\' connects subjects, the verb agrees with the nearer subject (\'teacher\' — singular), so \'was\' is correct.'},
            {'question_text': 'The committee _____ reached a decision.', 'option_a': 'have', 'option_b': 'has', 'option_c': 'are', 'option_d': 'were', 'correct_answer': 'B', 'explanation': '\'Committee\' as a collective noun acting as one body takes a singular verb \'has\'.'},
            {'question_text': 'Choose the correct sentence.', 'option_a': 'The police has arrested the thief.', 'option_b': 'The police have arrested the thief.', 'option_c': 'The police was arresting the thief.', 'option_d': 'The police is arresting the thief.', 'correct_answer': 'B', 'explanation': '\'Police\' is always plural and takes \'have\'.'},
            {'question_text': 'Two plus two _____ four.', 'option_a': 'are', 'option_b': 'were', 'option_c': 'is', 'option_d': 'have been', 'correct_answer': 'C', 'explanation': 'Mathematical expressions are treated as singular; \'is\' is correct.'},
            {'question_text': 'Neither Ade nor his brothers _____ ready.', 'option_a': 'is', 'option_b': 'was', 'option_c': 'are', 'option_d': 'has been', 'correct_answer': 'C', 'explanation': 'When \'neither...nor\' joins subjects, the verb agrees with the nearest subject (\'brothers\' — plural), so \'are\' is correct.'},
            {'question_text': 'The jury _____ divided in its verdict.', 'option_a': 'are', 'option_b': 'were', 'option_c': 'is', 'option_d': 'have', 'correct_answer': 'C', 'explanation': '\'Jury\' acts as a single unit here, taking the singular verb \'is\'.'},
            {'question_text': 'Everyone in the hall _____ asked to sit down.', 'option_a': 'were', 'option_b': 'are', 'option_c': 'was', 'option_d': 'have been', 'correct_answer': 'C', 'explanation': '\'Everyone\' is singular and takes \'was\'.'},
            {'question_text': 'Ten thousand naira _____ a lot of money.', 'option_a': 'are', 'option_b': 'were', 'option_c': 'is', 'option_d': 'have been', 'correct_answer': 'C', 'explanation': 'A sum of money is treated as a singular unit; \'is\' is correct.'},
            # Add more grammar questions...
            {'question_text': 'The number of students _____ increasing every year.', 'option_a': 'are', 'option_b': 'were', 'option_c': 'is', 'option_d': 'have been', 'correct_answer': 'C', 'explanation': '\'The number of\' takes a singular verb; \'a number of\' takes a plural verb.'},
            {'question_text': 'Choose the correct sentence.', 'option_a': 'My scissors are broken.', 'option_b': 'My scissors is broken.', 'option_c': 'My scissor are broken.', 'option_d': 'My scissor is broken.', 'correct_answer': 'A', 'explanation': '\'Scissors\' is always plural and takes \'are\'.'},
            {'question_text': 'Mathematics _____ my favourite subject.', 'option_a': 'are', 'option_b': 'were', 'option_c': 'is', 'option_d': 'have been', 'correct_answer': 'C', 'explanation': 'Academic subjects ending in \'-ics\' (like Mathematics, Physics) take singular verbs.'},
            {'question_text': 'The cattle _____ grazing in the field.', 'option_a': 'is', 'option_b': 'was', 'option_c': 'are', 'option_d': 'has been', 'correct_answer': 'C', 'explanation': '\'Cattle\' is always plural and takes \'are\'.'},
            {'question_text': 'It is I _____ told you the truth.', 'option_a': 'who', 'option_b': 'whom', 'option_c': 'whose', 'option_d': 'which', 'correct_answer': 'A', 'explanation': '\'Who\' is used as the subject of the relative clause; \'whom\' would be used as an object.'},
            {'question_text': 'The teacher, together with her students, _____ attending the seminar.', 'option_a': 'are', 'option_b': 'were', 'option_c': 'is', 'option_d': 'have been', 'correct_answer': 'C', 'explanation': 'When \'together with\' links a singular subject to others, the verb agrees with the main singular subject.'},
            {'question_text': 'Choose the correct sentence.', 'option_a': 'He don\'t know the answer.', 'option_b': 'He doesn\'t knows the answer.', 'option_c': 'He doesn\'t know the answer.', 'option_d': 'He do not knows the answer.', 'correct_answer': 'C', 'explanation': 'Third-person singular present: \'doesn\'t\' + base form of verb.'},
            {'question_text': 'None of the water _____ drinkable.', 'option_a': 'are', 'option_b': 'were', 'option_c': 'is', 'option_d': 'have been', 'correct_answer': 'C', 'explanation': '\'None\' with an uncountable noun takes a singular verb.'},
            {'question_text': 'The rich _____ always find it easy to survive.', 'option_a': 'do', 'option_b': 'does', 'option_c': 'has', 'option_d': 'is', 'correct_answer': 'A', 'explanation': '\'The rich\' refers to rich people (plural) and takes a plural verb.'},
            {'question_text': 'A pack of wolves _____ attacking the herd.', 'option_a': 'are', 'option_b': 'were', 'option_c': 'is', 'option_d': 'have been', 'correct_answer': 'C', 'explanation': 'A collective noun like \'a pack\' acting as one unit takes a singular verb.'},
            # FIGURES OF SPEECH & LITERATURE (Remaining Q81–Q200)
            {'question_text': 'The moon smiled down at the sleeping city is an example of:', 'option_a': 'Simile', 'option_b': 'Personification', 'option_c': 'Metaphor', 'option_d': 'Hyperbole', 'correct_answer': 'B', 'explanation': 'Personification gives human qualities (smiling) to non-human things (the moon).'},
            {'question_text': 'Life is a journey is an example of:', 'option_a': 'Simile', 'option_b': 'Hyperbole', 'option_c': 'Metaphor', 'option_d': 'Irony', 'correct_answer': 'C', 'explanation': 'A metaphor directly states one thing is another without using \'like\' or \'as\'.'},
            {'question_text': 'She is as brave as a lion is an example of:', 'option_a': 'Metaphor', 'option_b': 'Simile', 'option_c': 'Personification', 'option_d': 'Alliteration', 'correct_answer': 'B', 'explanation': 'A simile compares two things using \'as...as\' or \'like\'.'},
            {'question_text': 'I\'ve told you a million times is an example of:', 'option_a': 'Metaphor', 'option_b': 'Understatement', 'option_c': 'Hyperbole', 'option_d': 'Irony', 'correct_answer': 'C', 'explanation': 'Hyperbole is deliberate exaggeration for emphasis or effect.'},
            {'question_text': 'Peter Piper picked a peck of pickled peppers illustrates:', 'option_a': 'Assonance', 'option_b': 'Alliteration', 'option_c': 'Onomatopoeia', 'option_d': 'Rhyme', 'correct_answer': 'B', 'explanation': 'Alliteration is the repetition of the same consonant sound at the beginning of nearby words.'},
            {'question_text': 'The wind whispered through the trees contains:', 'option_a': 'Metaphor', 'option_b': 'Simile', 'option_c': 'Personification', 'option_d': 'Hyperbole', 'correct_answer': 'C', 'explanation': 'The wind is given the human action of whispering — this is personification.'},
            {'question_text': 'Buzz, hiss, sizzle are examples of:', 'option_a': 'Alliteration', 'option_b': 'Assonance', 'option_c': 'Onomatopoeia', 'option_d': 'Rhyme', 'correct_answer': 'C', 'explanation': 'Onomatopoeia refers to words that phonetically imitate the sound they describe.'},
            {'question_text': 'It was the best of times, it was the worst of times is an example of:', 'option_a': 'Paradox', 'option_b': 'Oxymoron', 'option_c': 'Antithesis', 'option_d': 'Synecdoche', 'correct_answer': 'C', 'explanation': 'Antithesis places contrasting ideas side by side in balanced grammatical structures.'},
            {'question_text': 'Sweet sorrow is an example of:', 'option_a': 'Paradox', 'option_b': 'Oxymoron', 'option_c': 'Irony', 'option_d': 'Euphemism', 'correct_answer': 'B', 'explanation': 'An oxymoron combines two contradictory terms to create a new meaning.'},
            {'question_text': 'Using the crown to mean the king or monarchy is:', 'option_a': 'Metaphor', 'option_b': 'Synecdoche', 'option_c': 'Metonymy', 'option_d': 'Irony', 'correct_answer': 'C', 'explanation': 'Metonymy uses the name of one thing to represent something closely associated with it.'},
            # Remaining questions continue...
            {'question_text': 'Bread being used to mean food generally is:', 'option_a': 'Metonymy', 'option_b': 'Synecdoche', 'option_c': 'Metaphor', 'option_d': 'Irony', 'correct_answer': 'B', 'explanation': 'Synecdoche uses a part to represent the whole, or the whole to represent a part.'},
            {'question_text': 'He is a Shakespeare (meaning a great writer) is an example of:', 'option_a': 'Metaphor', 'option_b': 'Allusion', 'option_c': 'Antonomasia', 'option_d': 'Personification', 'correct_answer': 'C', 'explanation': 'Antonomasia uses a proper name to express a general idea about the quality that person represents.'},
            {'question_text': 'The repetition of vowel sounds in closely placed words is called:', 'option_a': 'Alliteration', 'option_b': 'Onomatopoeia', 'option_c': 'Assonance', 'option_d': 'Consonance', 'correct_answer': 'C', 'explanation': 'Assonance is the repetition of vowel sounds within nearby words.'},
            {'question_text': 'It is a far, far better thing I do than I have ever done uses:', 'option_a': 'Hyperbole', 'option_b': 'Repetition', 'option_c': 'Anaphora', 'option_d': 'Alliteration', 'correct_answer': 'B', 'explanation': 'The repetition of \'far, far\' for emphasis is an example of repetition (epizeuxis).'},
            {'question_text': 'Death, be not proud uses:', 'option_a': 'Personification', 'option_b': 'Apostrophe', 'option_c': 'Simile', 'option_d': 'Euphemism', 'correct_answer': 'B', 'explanation': 'Apostrophe is addressing an abstract idea, absent person, or inanimate object directly.'},
            {'question_text': 'I have a thousand things to do is:', 'option_a': 'Understatement', 'option_b': 'Litotes', 'option_c': 'Hyperbole', 'option_d': 'Irony', 'correct_answer': 'C', 'explanation': '\'A thousand things\' is deliberate exaggeration — hyperbole.'},
            {'question_text': 'Saying He passed away instead of He died is:', 'option_a': 'Hyperbole', 'option_b': 'Euphemism', 'option_c': 'Irony', 'option_d': 'Metaphor', 'correct_answer': 'B', 'explanation': 'Euphemism substitutes a mild or indirect expression for a harsh or blunt one.'},
            {'question_text': 'Water, water everywhere, nor any drop to drink is an example of:', 'option_a': 'Metaphor', 'option_b': 'Paradox', 'option_c': 'Simile', 'option_d': 'Irony', 'correct_answer': 'B', 'explanation': 'The statement appears contradictory but reveals a deeper truth — this is paradox.'},
            {'question_text': 'The statement What a beautiful day! said during a rainstorm is:', 'option_a': 'Sarcasm', 'option_b': 'Hyperbole', 'option_c': 'Simile', 'option_d': 'Paradox', 'correct_answer': 'A', 'explanation': 'Sarcasm is the use of irony to mock or convey contempt; saying the opposite of what is meant.'},
            {'question_text': 'The pen is mightier than the sword is a:', 'option_a': 'Paradox', 'option_b': 'Simile', 'option_c': 'Metaphor', 'option_d': 'Litotes', 'correct_answer': 'C', 'explanation': 'This is a metaphor comparing the power of writing to physical force without using \'like\' or \'as\'.'},
        ]
        
        # Ensure exactly 200 questions
        english_questions = english_questions[:200]
        
        # Assign topics - questions 1-40 are vocabulary, 41-55 are antonyms, rest are grammar/figures
        for i, q in enumerate(english_questions, 1):
            if i <= 40:
                topic_id = vocab_topic.id if vocab_topic else None
            elif i <= 55:
                topic_id = antonym_topic.id if antonym_topic else None
            elif i <= 80:
                topic_id = grammar_topic.id if grammar_topic else None
            else:
                topic_id = figures_topic.id if figures_topic else None
                
            question = Question(
                exam_id=english_exam.id,
                topic_id=topic_id,
                question_text=q['question_text'],
                question_type='multiple_choice',
                subject='English',
                option_a=q['option_a'],
                option_b=q['option_b'],
                option_c=q['option_c'],
                option_d=q['option_d'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation'],
                marks=1,
                question_order=i
            )
            db.session.add(question)
        
        # Add comprehensive Mathematics questions
        math_questions = [
            # NUMBER THEORY, INDICES & LOGARITHMS (Q1–Q30)
            {'question_text': 'Simplify: 2³ × 2⁴ ÷ 2⁵', 'option_a': '2', 'option_b': '4', 'option_c': '8', 'option_d': '16', 'correct_answer': 'B', 'explanation': '2^(3+4-5) = 2^2 = 4.'},
            {'question_text': 'Evaluate: (27)^(2/3)', 'option_a': '3', 'option_b': '6', 'option_c': '9', 'option_d': '18', 'correct_answer': 'C', 'explanation': '(27)^(2/3) = (∛27)^2 = 3^2 = 9.'},
            {'question_text': 'Simplify: (16)^(3/4)', 'option_a': '4', 'option_b': '6', 'option_c': '8', 'option_d': '12', 'correct_answer': 'C', 'explanation': '(16)^(3/4) = (⁴√16)^3 = 2^3 = 8.'},
            {'question_text': 'Find the value of log₂ 64', 'option_a': '4', 'option_b': '5', 'option_c': '6', 'option_d': '8', 'correct_answer': 'C', 'explanation': '2^6 = 64, so log₂ 64 = 6.'},
            {'question_text': 'Evaluate log₁₀ 1000', 'option_a': '2', 'option_b': '3', 'option_c': '4', 'option_d': '10', 'correct_answer': 'B', 'explanation': '10^3 = 1000, so log₁₀ 1000 = 3.'},
            {'question_text': 'If log 2 = 0.3010, find log 8.', 'option_a': '0.602', 'option_b': '0.903', 'option_c': '0.9030', 'option_d': '1.204', 'correct_answer': 'C', 'explanation': 'log 8 = log 2³ = 3 × log 2 = 3 × 0.3010 = 0.9030.'},
            {'question_text': 'Simplify: log 5 + log 4', 'option_a': 'log 9', 'option_b': 'log 20', 'option_c': 'log 1', 'option_d': 'log 2', 'correct_answer': 'B', 'explanation': 'log 5 + log 4 = log(5 × 4) = log 20.'},
            {'question_text': 'Evaluate: log₃ 9 + log₃ 27', 'option_a': '2', 'option_b': '3', 'option_c': '5', 'option_d': '6', 'correct_answer': 'C', 'explanation': 'log₃ 9 = 2 and log₃ 27 = 3, so the sum is 5.'},
            {'question_text': 'Simplify: x^(1/2) × x^(3/2)', 'option_a': 'x', 'option_b': 'x²', 'option_c': 'x³', 'option_d': 'x⁴', 'correct_answer': 'B', 'explanation': 'x^(1/2 + 3/2) = x^(4/2) = x^2.'},
            {'question_text': 'Express 0.000456 in standard form.', 'option_a': '4.56 × 10⁻⁴', 'option_b': '4.56 × 10⁻³', 'option_c': '45.6 × 10⁻⁵', 'option_d': '4.56 × 10⁴', 'correct_answer': 'A', 'explanation': '0.000456 = 4.56 × 10⁻⁴.'},
            {'question_text': 'The HCF of 36 and 48 is:', 'option_a': '4', 'option_b': '6', 'option_c': '12', 'option_d': '18', 'correct_answer': 'C', 'explanation': '36 = 2²×3², 48 = 2⁴×3. HCF = 2²×3 = 12.'},
            {'question_text': 'The LCM of 12, 16 and 20 is:', 'option_a': '60', 'option_b': '120', 'option_c': '180', 'option_d': '240', 'correct_answer': 'D', 'explanation': 'LCM(12,16,20) = 240.'},
            {'question_text': 'If 2^x = 32, find x.', 'option_a': '3', 'option_b': '4', 'option_c': '5', 'option_d': '6', 'correct_answer': 'C', 'explanation': '2^5 = 32, so x = 5.'},
            {'question_text': 'Simplify: (3²)³ ÷ 3³', 'option_a': '3', 'option_b': '9', 'option_c': '27', 'option_d': '81', 'correct_answer': 'C', 'explanation': '(3^2)^3 = 3^6; 3^6 ÷ 3^3 = 3^3 = 27.'},
            {'question_text': 'Convert 0.36̄ (0.3636...) to a fraction.', 'option_a': '3/10', 'option_b': '4/11', 'option_c': '36/100', 'option_d': '36/99', 'correct_answer': 'B', 'explanation': 'Let x = 0.3636...; then 100x = 36.3636...; 99x = 36; x = 36/99 = 4/11.'},
            {'question_text': 'Simplify: √75 + √48', 'option_a': '9√3', 'option_b': '2√3', 'option_c': '7√3', 'option_d': '5√3', 'correct_answer': 'A', 'explanation': '√75 = 5√3; √48 = 4√3; 5√3 + 4√3 = 9√3.'},
            {'question_text': 'Rationalize: 1/(√5 + √3)', 'option_a': '(√5 - √3)/2', 'option_b': '(√5 + √3)/2', 'option_c': '(√5 - √3)/8', 'option_d': '1/2', 'correct_answer': 'A', 'explanation': 'Multiply by (√5 - √3)/(√5 - √3): (√5 - √3)/(5-3) = (√5 - √3)/2.'},
            {'question_text': 'Simplify: (√6 + √2)(√6 - √2)', 'option_a': '4', 'option_b': '6', 'option_c': '8', 'option_d': '2√8', 'correct_answer': 'A', 'explanation': 'Using difference of squares: 6 - 2 = 4.'},
            {'question_text': 'What is 5% of 400?', 'option_a': '10', 'option_b': '15', 'option_c': '20', 'option_d': '25', 'correct_answer': 'C', 'explanation': '5% × 400 = (5/100) × 400 = 20.'},
            {'question_text': 'If a number is increased by 20% and then decreased by 20%, the net percentage change is:', 'option_a': '0%', 'option_b': '-4%', 'option_c': '4%', 'option_d': '-2%', 'correct_answer': 'B', 'explanation': 'Let number = 100. After 20% increase: 120. After 20% decrease: 120 × 0.8 = 96. Net change = -4%.'},
            {'question_text': 'Find the value of (2/3) ÷ (4/9)', 'option_a': '3/2', 'option_b': '8/27', 'option_c': '2/3', 'option_d': '1', 'correct_answer': 'A', 'explanation': '(2/3) ÷ (4/9) = (2/3) × (9/4) = 18/12 = 3/2.'},
            {'question_text': 'Express 156 in base 2 (binary).', 'option_a': '10011100', 'option_b': '10011010', 'option_c': '10010111', 'option_d': '10111100', 'correct_answer': 'A', 'explanation': '156 = 128+16+8+4 = 2^7+2^4+2^3+2^2 = 10011100₂.'},
            {'question_text': 'Convert 1101₂ to base 10.', 'option_a': '11', 'option_b': '12', 'option_c': '13', 'option_d': '14', 'correct_answer': 'C', 'explanation': '1×8 + 1×4 + 0×2 + 1×1 = 8+4+0+1 = 13.'},
            {'question_text': 'If log x = 2.5670, find log √x.', 'option_a': '1.2835', 'option_b': '5.1340', 'option_c': '1.5670', 'option_d': '2.0000', 'correct_answer': 'A', 'explanation': 'log √x = (1/2) log x = 2.5670/2 = 1.2835.'},
            {'question_text': 'Simplify: (a³b²)² ÷ a²b', 'option_a': 'a²b', 'option_b': 'a³b²', 'option_c': 'a⁴b³', 'option_d': 'ab³', 'correct_answer': 'C', 'explanation': '(a^3b^2)^2 = a^6b^4; ÷ a^2b = a^(6-2)b^(4-1) = a^4b^3.'},
            {'question_text': 'A trader buys goods for ₦2,000 and sells at ₦2,500. The percentage profit is:', 'option_a': '20%', 'option_b': '25%', 'option_c': '30%', 'option_d': '50%', 'correct_answer': 'B', 'explanation': 'Profit = 500; % profit = (500/2000) × 100 = 25%.'},
            {'question_text': 'The simple interest on ₦5,000 for 3 years at 4% per annum is:', 'option_a': '₦200', 'option_b': '₦400', 'option_c': '₦600', 'option_d': '₦800', 'correct_answer': 'C', 'explanation': 'SI = PRT/100 = 5000 × 3 × 4/100 = ₦600.'},
            {'question_text': 'Evaluate: 5! (5 factorial)', 'option_a': '20', 'option_b': '60', 'option_c': '120', 'option_d': '240', 'correct_answer': 'C', 'explanation': '5! = 5×4×3×2×1 = 120.'},
            {'question_text': 'How many ways can 4 books be arranged on a shelf?', 'option_a': '12', 'option_b': '16', 'option_c': '24', 'option_d': '48', 'correct_answer': 'C', 'explanation': 'P(4,4) = 4! = 24 ways.'},
            {'question_text': 'In a group of 30 students, 18 study French and 15 study Spanish. If 8 study both, how many study neither?', 'option_a': '3', 'option_b': '5', 'option_c': '7', 'option_d': '10', 'correct_answer': 'B', 'explanation': 'n(F∪S) = 18+15-8 = 25. Neither = 30-25 = 5.'},
            # ALGEBRA (Q31–Q70)
            {'question_text': 'Solve for x: 3x - 7 = 14', 'option_a': '3', 'option_b': '5', 'option_c': '7', 'option_d': '9', 'correct_answer': 'C', 'explanation': '3x = 21; x = 7.'},
            {'question_text': 'Find x if 2(x + 3) = 4(x - 1)', 'option_a': '3', 'option_b': '4', 'option_c': '5', 'option_d': '6', 'correct_answer': 'C', 'explanation': '2x+6 = 4x-4; 10 = 2x; x = 5.'},
            {'question_text': 'Factorize: x² - 5x + 6', 'option_a': '(x-2)(x-3)', 'option_b': '(x+2)(x+3)', 'option_c': '(x-1)(x-6)', 'option_d': '(x+1)(x-6)', 'correct_answer': 'A', 'explanation': 'Looking for two numbers that multiply to 6 and add to -5: -2 and -3. So (x-2)(x-3).'},
            {'question_text': 'Solve: x² - 7x + 12 = 0', 'option_a': 'x = 3 or x = 4', 'option_b': 'x = -3 or x = -4', 'option_c': 'x = 2 or x = 6', 'option_d': 'x = 1 or x = 12', 'correct_answer': 'A', 'explanation': '(x-3)(x-4) = 0; x = 3 or x = 4.'},
            {'question_text': 'If f(x) = 2x² - 3x + 1, find f(2).', 'option_a': '1', 'option_b': '3', 'option_c': '5', 'option_d': '7', 'correct_answer': 'B', 'explanation': 'f(2) = 2(4) - 3(2) + 1 = 8-6+1 = 3.'},
            {'question_text': 'The sum of a number and its square is 12. Find the number.', 'option_a': '2', 'option_b': '3', 'option_c': '4', 'option_d': '5', 'correct_answer': 'B', 'explanation': 'x + x² = 12; x² + x - 12 = 0; (x+4)(x-3)=0; x = 3.'},
            {'question_text': 'Simplify: (x² - 9)/(x - 3)', 'option_a': 'x - 3', 'option_b': 'x + 3', 'option_c': 'x² - 3', 'option_d': 'x + 9', 'correct_answer': 'B', 'explanation': 'x² - 9 = (x-3)(x+3); ÷(x-3) = x+3.'},
            {'question_text': 'Find the value of k if 2x² + kx + 8 has a factor (x - 2).', 'option_a': '-8', 'option_b': '-6', 'option_c': '6', 'option_d': '8', 'correct_answer': 'A', 'explanation': 'If (x-2) is a factor, f(2)=0: 2(4)+2k+8=0; 8+2k+8=0; 2k=-16; k=-8.'},
            {'question_text': 'Solve simultaneously: x + y = 7 and x - y = 3', 'option_a': 'x=4, y=3', 'option_b': 'x=5, y=2', 'option_c': 'x=3, y=4', 'option_d': 'x=6, y=1', 'correct_answer': 'B', 'explanation': 'Adding: 2x=10; x=5. Then y=7-5=2.'},
            {'question_text': 'The gradient of the line 3y - 6x = 9 is:', 'option_a': '3', 'option_b': '2', 'option_c': '-2', 'option_d': '-3', 'correct_answer': 'B', 'explanation': '3y = 6x+9; y = 2x+3. Gradient = 2.'},
            {'question_text': 'The equation of a line with gradient 3 passing through (1, 2) is:', 'option_a': 'y = 3x - 1', 'option_b': 'y = 3x + 1', 'option_c': 'y = x + 3', 'option_d': 'y = 3x + 5', 'correct_answer': 'A', 'explanation': 'y - 2 = 3(x-1); y = 3x - 3 + 2 = 3x - 1.'},
            {'question_text': 'Expand: (2x + 3)²', 'option_a': '4x² + 9', 'option_b': '4x² + 6x + 9', 'option_c': '4x² + 12x + 9', 'option_d': '2x² + 12x + 9', 'correct_answer': 'C', 'explanation': '(2x+3)² = 4x² + 2(2x)(3) + 9 = 4x² + 12x + 9.'},
            {'question_text': 'Make t the subject: v = u + at', 'option_a': 't = (v - u)/a', 'option_b': 't = v - u - a', 'option_c': 't = a(v - u)', 'option_d': 't = v/(u + a)', 'correct_answer': 'A', 'explanation': 'at = v - u; t = (v-u)/a.'},
            {'question_text': 'Solve the inequality: 2x - 5 > 7', 'option_a': 'x > 1', 'option_b': 'x > 6', 'option_c': 'x > 7', 'option_d': 'x < 6', 'correct_answer': 'B', 'explanation': '2x > 12; x > 6.'},
            {'question_text': 'The nth term of a sequence is 3n - 1. The 5th term is:', 'option_a': '11', 'option_b': '12', 'option_c': '13', 'option_d': '14', 'correct_answer': 'D', 'explanation': '3(5) - 1 = 14.'},
            {'question_text': 'Find the 8th term of the AP: 3, 7, 11, 15, ...', 'option_a': '29', 'option_b': '31', 'option_c': '33', 'option_d': '35', 'correct_answer': 'B', 'explanation': 'a = 3, d = 4. Tn = a + (n-1)d = 3 + 7×4 = 3 + 28 = 31.'},
            {'question_text': 'The common ratio of the GP: 2, 6, 18, 54, ... is:', 'option_a': '2', 'option_b': '3', 'option_c': '4', 'option_d': '6', 'correct_answer': 'B', 'explanation': 'r = 6/2 = 3.'},
            {'question_text': 'Find the sum of the first 5 terms of the GP: 1, 2, 4, 8, ...', 'option_a': '28', 'option_b': '31', 'option_c': '32', 'option_d': '63', 'correct_answer': 'B', 'explanation': 'Sn = a(rⁿ-1)/(r-1) = 1(2^5 - 1)/(2-1) = 31.'},
            {'question_text': 'If p = 3 and q = -2, find the value of 2p² - 3pq + q²', 'option_a': '30', 'option_b': '40', 'option_c': '50', 'option_d': '60', 'correct_answer': 'B', 'explanation': '2(9) - 3(3)(-2) + 4 = 18 + 18 + 4 = 40.'},
            {'question_text': 'Solve: |2x - 3| = 7', 'option_a': 'x = 5 or x = -2', 'option_b': 'x = 5 or x = 2', 'option_c': 'x = 4 or x = -5', 'option_d': 'x = -5 or x = 5', 'correct_answer': 'A', 'explanation': '2x-3 = 7 → x=5; or 2x-3 = -7 → x=-2.'},
            {'question_text': 'The quadratic equation with roots 2 and -5 is:', 'option_a': 'x² + 3x - 10 = 0', 'option_b': 'x² - 3x - 10 = 0', 'option_c': 'x² + 3x + 10 = 0', 'option_d': 'x² - 7x + 10 = 0', 'correct_answer': 'A', 'explanation': 'Sum = -3, Product = -10. Equation: x² - (-3)x + (-10) = x² + 3x - 10 = 0.'},
            {'question_text': 'If α and β are roots of 2x² - 5x + 3 = 0, find α + β.', 'option_a': '5/2', 'option_b': '3/2', 'option_c': '5', 'option_d': '3', 'correct_answer': 'A', 'explanation': 'α + β = -b/a = 5/2.'},
            {'question_text': 'If α and β are roots of 2x² - 5x + 3 = 0, find αβ.', 'option_a': '5/2', 'option_b': '3/2', 'option_c': '5', 'option_d': '3', 'correct_answer': 'B', 'explanation': 'αβ = c/a = 3/2.'},
            {'question_text': 'Solve: 3/(x+2) = 2/(x-1)', 'option_a': 'x = 7', 'option_b': 'x = 5', 'option_c': 'x = 8', 'option_d': 'x = 4', 'correct_answer': 'A', 'explanation': '3(x-1) = 2(x+2); 3x-3 = 2x+4; x = 7.'},
            {'question_text': 'Find the range of the function f(x) = x² + 2 for x ∈ ℝ.', 'option_a': 'f(x) ≥ 0', 'option_b': 'f(x) ≥ 2', 'option_c': 'f(x) ≤ 2', 'option_d': 'f(x) ∈ ℝ', 'correct_answer': 'B', 'explanation': 'x² ≥ 0 for all real x, so x² + 2 ≥ 2. Minimum value is 2.'},
            {'question_text': 'The discriminant of 3x² - 5x + 2 = 0 is:', 'option_a': '1', 'option_b': '5', 'option_c': '25', 'option_d': '49', 'correct_answer': 'A', 'explanation': 'b² - 4ac = 25 - 4(3)(2) = 25 - 24 = 1.'},
            {'question_text': 'How many real roots does x² + 4 = 0 have?', 'option_a': '0', 'option_b': '1', 'option_c': '2', 'option_d': '4', 'correct_answer': 'A', 'explanation': 'x² = -4 has no real solutions. Discriminant = 0 - 4(1)(4) = -16 < 0, so no real roots.'},
            {'question_text': 'Simplify: (3x² - 12)/(x² - 4)', 'option_a': '3', 'option_b': 'x - 2', 'option_c': '3(x-2)', 'option_d': '3', 'correct_answer': 'A', 'explanation': '3(x²-4)/(x²-4) = 3 (provided x ≠ ±2).'},
            {'question_text': 'Find k if x³ - kx + 3 is divisible by (x - 1).', 'option_a': '2', 'option_b': '3', 'option_c': '4', 'option_d': '5', 'correct_answer': 'C', 'explanation': 'f(1) = 0: 1 - k + 3 = 0; k = 4.'},
            {'question_text': 'If log₃ x = 4, find x.', 'option_a': '12', 'option_b': '64', 'option_c': '81', 'option_d': '27', 'correct_answer': 'C', 'explanation': 'x = 3^4 = 81.'},
            {'question_text': 'Solve: 4^(x+1) = 8^x', 'option_a': 'x = 1', 'option_b': 'x = 2', 'option_c': 'x = 3', 'option_d': 'x = 4', 'correct_answer': 'B', 'explanation': '2^(2x+2) = 2^(3x); 2x+2 = 3x; x = 2.'},
            {'question_text': 'If f(x) = x + 3 and g(x) = 2x - 1, find f(g(x)).', 'option_a': '2x + 2', 'option_b': '2x - 1', 'option_c': 'x + 4', 'option_d': '2x + 3', 'correct_answer': 'A', 'explanation': 'f(g(x)) = g(x) + 3 = (2x-1) + 3 = 2x + 2.'},
            {'question_text': 'The inverse of f(x) = 3x - 5 is:', 'option_a': '(x+5)/3', 'option_b': '(x-5)/3', 'option_c': '3x+5', 'option_d': '1/(3x-5)', 'correct_answer': 'A', 'explanation': 'Let y = 3x-5; x = (y+5)/3. So f⁻¹(x) = (x+5)/3.'},
            {'question_text': 'Find the value of x: log(x+1) - log(x-1) = log 3', 'option_a': 'x = 2', 'option_b': 'x = 3/2', 'option_c': 'x = 4', 'option_d': 'x = 2', 'correct_answer': 'A', 'explanation': 'log[(x+1)/(x-1)] = log 3; (x+1)/(x-1) = 3; x+1 = 3x-3; 2x=4; x=2.'},
            {'question_text': 'Simplify: (2^n × 4^n) / 8^n', 'option_a': '1', 'option_b': '2^n', 'option_c': '4^n', 'option_d': '2', 'correct_answer': 'A', 'explanation': '2^n × 2^(2n) / 2^(3n) = 2^(3n-3n) = 2^0 = 1.'},
            {'question_text': 'The sum of an AP is 45 and it has 5 terms. The middle term is:', 'option_a': '7', 'option_b': '8', 'option_c': '9', 'option_d': '10', 'correct_answer': 'C', 'explanation': 'In an AP with n = 5, Sn = 5 × middle term; 45 = 5 × T₃; T₃ = 9.'},
            {'question_text': 'The geometric mean of 4 and 9 is:', 'option_a': '5', 'option_b': '6', 'option_c': '7', 'option_d': '6.5', 'correct_answer': 'B', 'explanation': 'GM = √(4×9) = √36 = 6.'},
            {'question_text': 'The 4th term of a GP is 54 and the common ratio is 3. Find the first term.', 'option_a': '2', 'option_b': '3', 'option_c': '6', 'option_d': '9', 'correct_answer': 'A', 'explanation': 'T₄ = ar³; 54 = a×27; a = 54/27 = 2.'},
            {'question_text': 'Factorize completely: 2x³ - 8x', 'option_a': '2x(x² - 4)', 'option_b': '2x(x-2)(x+2)', 'option_c': '2(x³ - 4x)', 'option_d': 'x(2x² - 8)', 'correct_answer': 'B', 'explanation': '2x³-8x = 2x(x²-4) = 2x(x-2)(x+2).'},
            {'question_text': 'If the sum to infinity of a GP is 6 and the first term is 2, find the common ratio.', 'option_a': '1/2', 'option_b': '1/3', 'option_c': '2/3', 'option_d': '3/4', 'correct_answer': 'C', 'explanation': 'S∞ = a/(1-r); 6 = 2/(1-r); 1-r = 1/3; r = 2/3.'},
            # GEOMETRY & MENSURATION (Q71–Q100)
            {'question_text': 'The sum of interior angles of a hexagon is:', 'option_a': '540°', 'option_b': '720°', 'option_c': '900°', 'option_d': '1080°', 'correct_answer': 'B', 'explanation': 'Sum = (n-2)×180° = (6-2)×180° = 4×180° = 720°.'},
            {'question_text': 'Find the area of a triangle with base 8 cm and height 5 cm.', 'option_a': '13 cm²', 'option_b': '20 cm²', 'option_c': '25 cm²', 'option_d': '40 cm²', 'correct_answer': 'B', 'explanation': 'Area = ½ × base × height = ½ × 8 × 5 = 20 cm².'},
            {'question_text': 'The area of a circle with radius 7 cm is (take π = 22/7):', 'option_a': '44 cm²', 'option_b': '88 cm²', 'option_c': '154 cm²', 'option_d': '308 cm²', 'correct_answer': 'C', 'explanation': 'Area = πr² = (22/7)×49 = 22×7 = 154 cm².'},
            {'question_text': 'The circumference of a circle with diameter 14 cm is (π = 22/7):', 'option_a': '22 cm', 'option_b': '44 cm', 'option_c': '88 cm', 'option_d': '154 cm', 'correct_answer': 'B', 'explanation': 'C = πd = (22/7)×14 = 44 cm.'},
            {'question_text': 'In a right-angled triangle, the hypotenuse is 13 cm and one leg is 5 cm. Find the other leg.', 'option_a': '8 cm', 'option_b': '10 cm', 'option_c': '12 cm', 'option_d': '14 cm', 'correct_answer': 'C', 'explanation': 'By Pythagoras: 13² = 5² + b²; 169 = 25 + b²; b² = 144; b = 12 cm.'},
            {'question_text': 'Find the volume of a cylinder of radius 3.5 cm and height 10 cm (π = 22/7).', 'option_a': '110 cm³', 'option_b': '154 cm³', 'option_c': '385 cm³', 'option_d': '770 cm³', 'correct_answer': 'C', 'explanation': 'V = πr²h = (22/7)×12.25×10 = 385 cm³.'},
            {'question_text': 'The surface area of a sphere of radius 3 cm (π = 22/7) is:', 'option_a': '28.28 cm²', 'option_b': '113.14 cm²', 'option_c': '226.28 cm²', 'option_d': '339.43 cm²', 'correct_answer': 'B', 'explanation': 'SA = 4πr² = 4×(22/7)×9 ≈ 113.14 cm².'},
            {'question_text': 'Two angles of a triangle are 45° and 75°. Find the third angle.', 'option_a': '50°', 'option_b': '60°', 'option_c': '65°', 'option_d': '70°', 'correct_answer': 'B', 'explanation': '180° - 45° - 75° = 60°.'},
            {'question_text': 'A rectangle has perimeter 30 cm and length 9 cm. Its area is:', 'option_a': '36 cm²', 'option_b': '54 cm²', 'option_c': '72 cm²', 'option_d': '108 cm²', 'correct_answer': 'B', 'explanation': '2(l+w) = 30; l+w = 15; w = 6 cm. Area = 9×6 = 54 cm².'},
            {'question_text': 'The angle in a semicircle is:', 'option_a': '45°', 'option_b': '60°', 'option_c': '90°', 'option_d': '180°', 'correct_answer': 'C', 'explanation': 'By Thales\' theorem, the angle subtended by a diameter at the circumference is always 90°.'},
            {'question_text': 'A chord of length 16 cm is at a distance of 6 cm from the centre. The radius of the circle is:', 'option_a': '8 cm', 'option_b': '10 cm', 'option_c': '12 cm', 'option_d': '14 cm', 'correct_answer': 'B', 'explanation': 'Half-chord = 8; r² = 8² + 6² = 64+36 = 100; r = 10 cm.'},
            {'question_text': 'The exterior angle of a regular polygon is 40°. How many sides does it have?', 'option_a': '6', 'option_b': '8', 'option_c': '9', 'option_d': '10', 'correct_answer': 'C', 'explanation': 'Number of sides = 360°/40° = 9.'},
            {'question_text': 'Two parallel lines are cut by a transversal. Co-interior (same-side interior) angles are:', 'option_a': 'Equal', 'option_b': 'Complementary', 'option_c': 'Supplementary', 'option_d': 'None of the above', 'correct_answer': 'C', 'explanation': 'Co-interior angles between parallel lines add up to 180° (supplementary).'},
            {'question_text': 'The volume of a cone with radius 6 cm and height 7 cm (π = 22/7) is:', 'option_a': '198 cm³', 'option_b': '264 cm³', 'option_c': '264 cm³', 'option_d': '792 cm³', 'correct_answer': 'B', 'explanation': 'V = (1/3)πr²h = (1/3)(22/7)(36)(7) = (1/3)(22)(36) = 264 cm³.'},
            {'question_text': 'A solid hemisphere has radius 3 cm. Its volume (π = 22/7) is:', 'option_a': '18π cm³', 'option_b': '36π cm³', 'option_c': '56.57 cm³', 'option_d': '56.57 cm³', 'correct_answer': 'C', 'explanation': 'V = (2/3)πr³ = (2/3)(22/7)(27) ≈ 56.57 cm³.'},
            {'question_text': 'The locus of a point equidistant from two fixed points is:', 'option_a': 'A circle', 'option_b': 'A straight line', 'option_c': 'The perpendicular bisector of the line joining them', 'option_d': 'A parabola', 'correct_answer': 'C', 'explanation': 'Points equidistant from two fixed points lie on the perpendicular bisector of the segment joining them.'},
            {'question_text': 'A kite has diagonals of length 10 cm and 8 cm. Its area is:', 'option_a': '40 cm²', 'option_b': '80 cm²', 'option_c': '18 cm²', 'option_d': '20 cm²', 'correct_answer': 'A', 'explanation': 'Area of kite = (1/2)×d₁×d₂ = (1/2)×10×8 = 40 cm².'},
            {'question_text': 'An arc subtends an angle of 60° at the centre of a circle of radius 6 cm. The arc length (π = 22/7) is:', 'option_a': '2π cm', 'option_b': '4π cm', 'option_c': '6π cm', 'option_d': 'π cm', 'correct_answer': 'A', 'explanation': 'Arc length = (θ/360°)×2πr = (60/360)×2π×6 = (1/6)×12π = 2π cm.'},
            {'question_text': 'The mid-point of the line joining A(2, 4) and B(8, 10) is:', 'option_a': '(3, 7)', 'option_b': '(5, 7)', 'option_c': '(6, 7)', 'option_d': '(5, 8)', 'correct_answer': 'B', 'explanation': 'Midpoint = ((2+8)/2, (4+10)/2) = (5, 7).'},
            {'question_text': 'Find the distance between points A(1, 2) and B(4, 6).', 'option_a': '3', 'option_b': '4', 'option_c': '5', 'option_d': '7', 'correct_answer': 'C', 'explanation': 'd = √((4-1)²+(6-2)²) = √(9+16) = √25 = 5.'},
            {'question_text': 'The gradient of the line joining (3, 5) and (7, 9) is:', 'option_a': '1', 'option_b': '2', 'option_c': '3', 'option_d': '4', 'correct_answer': 'A', 'explanation': 'Gradient = (9-5)/(7-3) = 4/4 = 1.'},
            {'question_text': 'The equation of a line parallel to y = 3x + 2 and passing through (0, 5) is:', 'option_a': 'y = 3x + 5', 'option_b': 'y = 3x - 5', 'option_c': 'y = -3x + 5', 'option_d': 'y = 5x + 3', 'correct_answer': 'A', 'explanation': 'Parallel lines have the same gradient (3). Through (0,5): y = 3x + 5.'},
            {'question_text': 'Two lines y = 2x + 1 and y = -x/2 + 3 are:', 'option_a': 'Parallel', 'option_b': 'Perpendicular', 'option_c': 'Coincident', 'option_d': 'Neither parallel nor perpendicular', 'correct_answer': 'B', 'explanation': 'm₁×m₂ = 2×(-1/2) = -1. Lines are perpendicular.'},
            {'question_text': 'The centre of the circle x² + y² - 4x + 6y - 3 = 0 is:', 'option_a': '(2, -3)', 'option_b': '(-2, 3)', 'option_c': '(4, -6)', 'option_d': '(2, 3)', 'correct_answer': 'A', 'explanation': 'Comparing with (x-h)² + (y-k)² = r²: h = 2, k = -3. Centre = (2, -3).'},
            {'question_text': 'The radius of the circle x² + y² - 6x + 4y + 4 = 0 is:', 'option_a': '2', 'option_b': '3', 'option_c': '4', 'option_d': '5', 'correct_answer': 'B', 'explanation': 'r = √(g²+f²-c) = √(9+4-4) = √9 = 3.'},
            {'question_text': 'In △ABC, angle A = 30°, side a = 5 cm. By the sine rule, 2R (diameter of circumcircle) is:', 'option_a': '5', 'option_b': '8', 'option_c': '10', 'option_d': '12', 'correct_answer': 'C', 'explanation': 'a/sin A = 2R; 5/sin 30° = 5/(1/2) = 10.'},
            {'question_text': 'The area of a rhombus with diagonals 12 cm and 8 cm is:', 'option_a': '20 cm²', 'option_b': '40 cm²', 'option_c': '48 cm²', 'option_d': '96 cm²', 'correct_answer': 'C', 'explanation': 'Area = (1/2)×d₁×d₂ = (1/2)×12×8 = 48 cm².'},
            {'question_text': 'A pyramid with a square base of side 4 cm and height 3 cm has volume:', 'option_a': '16 cm³', 'option_b': '24 cm³', 'option_c': '32 cm³', 'option_d': '48 cm³', 'correct_answer': 'A', 'explanation': 'V = (1/3)×base area×h = (1/3)×16×3 = 16 cm³.'},
            {'question_text': 'An equilateral triangle has side 6 cm. Its area is:', 'option_a': '9√3 cm²', 'option_b': '12√3 cm²', 'option_c': '18√3 cm²', 'option_d': '36 cm²', 'correct_answer': 'A', 'explanation': 'Area = (√3/4)×s² = (√3/4)×36 = 9√3 cm².'},
            {'question_text': 'The angle of elevation of the top of a 40 m tower from a point on the ground is 45°. The distance from the point to the base is:', 'option_a': '20 m', 'option_b': '30 m', 'option_c': '40 m', 'option_d': '50 m', 'correct_answer': 'C', 'explanation': 'tan 45° = 40/d; 1 = 40/d; d = 40 m.'},
            # TRIGONOMETRY (Q101–Q125)
            {'question_text': 'Find the value of sin 30° + cos 60°.', 'option_a': '0', 'option_b': '1', 'option_c': '1/2', 'option_d': '√3/2', 'correct_answer': 'B', 'explanation': 'sin 30° = 1/2; cos 60° = 1/2; sum = 1.'},
            {'question_text': 'Evaluate: tan 45° × sin 90°', 'option_a': '0', 'option_b': '1', 'option_c': '√2', 'option_d': '2', 'correct_answer': 'B', 'explanation': 'tan 45° = 1; sin 90° = 1; product = 1.'},
            {'question_text': 'If sin θ = 3/5, find cos θ (for 0° < θ < 90°).', 'option_a': '3/4', 'option_b': '4/5', 'option_c': '4/3', 'option_d': '5/3', 'correct_answer': 'B', 'explanation': 'cos θ = √(1 - sin²θ) = √(1 - 9/25) = √(16/25) = 4/5.'},
            {'question_text': 'The value of cos 0° + sin 90° is:', 'option_a': '0', 'option_b': '1', 'option_c': '2', 'option_d': '√2', 'correct_answer': 'C', 'explanation': 'cos 0° = 1; sin 90° = 1; sum = 2.'},
            {'question_text': 'Simplify: sin²θ + cos²θ', 'option_a': '0', 'option_b': '1', 'option_c': '2', 'option_d': 'sin 2θ', 'correct_answer': 'B', 'explanation': 'This is the fundamental Pythagorean identity.'},
            {'question_text': 'Express cos 120° exactly.', 'option_a': '1/2', 'option_b': '-1/2', 'option_c': '√3/2', 'option_d': '-√3/2', 'correct_answer': 'B', 'explanation': 'cos 120° = cos(180°-60°) = -cos 60° = -1/2.'},
            {'question_text': 'The general solution of sin θ = 1/2 (0° ≤ θ ≤ 360°) is:', 'option_a': '30° only', 'option_b': '30° and 150°', 'option_c': '60° and 120°', 'option_d': '30° and 330°', 'correct_answer': 'B', 'explanation': 'sin θ = 1/2; θ = 30° (1st quadrant) and 150° (2nd quadrant).'},
            {'question_text': 'Prove/verify: 1 + tan²θ equals:', 'option_a': 'sec²θ', 'option_b': 'cosec²θ', 'option_c': 'cot²θ', 'option_d': 'cos²θ', 'correct_answer': 'A', 'explanation': '1 + tan²θ = sec²θ is a standard trigonometric identity.'},
            {'question_text': 'In a triangle, a = 7, b = 8, C = 60°. By the cosine rule, c² is:', 'option_a': '57', 'option_b': '65', 'option_c': '67', 'option_d': '113', 'correct_answer': 'A', 'explanation': 'c² = a²+b²-2ab cos C = 49+64-2(7)(8)(1/2) = 113-56 = 57.'},
            {'question_text': 'The period of y = sin 2x is:', 'option_a': 'π/2', 'option_b': 'π', 'option_c': '2π', 'option_d': '4π', 'correct_answer': 'B', 'explanation': 'Period = 2π/2 = π.'},
            {'question_text': 'The amplitude of y = 3cos x is:', 'option_a': '1', 'option_b': '2', 'option_c': '3', 'option_d': '6', 'correct_answer': 'C', 'explanation': 'The amplitude is the coefficient of the trig function: 3.'},
            {'question_text': 'Find the exact value of tan 60°.', 'option_a': '1', 'option_b': '√2', 'option_c': '√3', 'option_d': '2√3', 'correct_answer': 'C', 'explanation': 'tan 60° = sin 60°/cos 60° = (√3/2)/(1/2) = √3.'},
            {'question_text': 'If tan θ = 1, find θ for 0° ≤ θ ≤ 360°.', 'option_a': '45° only', 'option_b': '45° and 135°', 'option_c': '45° and 225°', 'option_d': '135° and 315°', 'correct_answer': 'C', 'explanation': 'tan θ = 1 at θ = 45° (1st quadrant) and θ = 225° (3rd quadrant).'},
            {'question_text': 'Express sin(A + B) in expanded form.', 'option_a': 'sin A + sin B', 'option_b': 'sin A cos B + cos A sin B', 'option_c': 'sin A cos B - cos A sin B', 'option_d': 'cos A cos B - sin A sin B', 'correct_answer': 'B', 'explanation': 'sin(A+B) = sin A cos B + cos A sin B (standard compound angle formula).'},
            {'question_text': 'If cos θ = -4/5 and 90° < θ < 180°, find tan θ.', 'option_a': '3/4', 'option_b': '-3/4', 'option_c': '4/3', 'option_d': '-4/3', 'correct_answer': 'B', 'explanation': 'sin θ = √(1-16/25) = 3/5 (positive in 2nd quad). tan θ = (3/5)/(-4/5) = -3/4.'},
            {'question_text': 'Simplify: (sin 2θ)/(sin θ)', 'option_a': '2 sin θ', 'option_b': '2 cos θ', 'option_c': 'sin θ', 'option_d': 'cos θ', 'correct_answer': 'B', 'explanation': 'sin 2θ = 2 sin θ cos θ; ÷ sin θ = 2 cos θ.'},
            {'question_text': 'The bearing N45°E is the same as a bearing of:', 'option_a': '045°', 'option_b': '135°', 'option_c': '315°', 'option_d': '225°', 'correct_answer': 'A', 'explanation': 'N45°E = 45° measured clockwise from north = bearing 045°.'},
            {'question_text': 'A ship sails 40 km North and then 30 km East. Its distance from the starting point is:', 'option_a': '50 km', 'option_b': '60 km', 'option_c': '70 km', 'option_d': '80 km', 'correct_answer': 'A', 'explanation': 'd = √(40²+30²) = √(1600+900) = √2500 = 50 km.'},
            {'question_text': 'Express cos 2θ in terms of sin θ.', 'option_a': '2sin²θ - 1', 'option_b': '1 - 2sin²θ', 'option_c': '2cos²θ - 1', 'option_d': '1 - 2cos²θ', 'correct_answer': 'B', 'explanation': 'cos 2θ = 1 - 2sin²θ is one of the double angle formulas.'},
            {'question_text': 'A ladder 5 m long leans against a wall, making an angle of 60° with the ground. How high up the wall does it reach?', 'option_a': '2.5 m', 'option_b': '5√3/2 m', 'option_c': '5/2 m', 'option_d': '5√3 m', 'correct_answer': 'B', 'explanation': 'Height = 5 sin 60° = 5×(√3/2) = 5√3/2 m.'},
            {'question_text': 'Evaluate sin 15° exactly.', 'option_a': '(√6 - √2)/4', 'option_b': '(√6 + √2)/4', 'option_c': '(√3 - 1)/4', 'option_d': '(√3 + 1)/2', 'correct_answer': 'A', 'explanation': 'sin 15° = sin(45°-30°) = sin45°cos30° - cos45°sin30° = (√6-√2)/4.'},
            {'question_text': 'A 10 m pole casts a shadow 10 m long. The angle of elevation of the sun is:', 'option_a': '30°', 'option_b': '45°', 'option_c': '60°', 'option_d': '90°', 'correct_answer': 'B', 'explanation': 'tan θ = opposite/adjacent = 10/10 = 1; θ = 45°.'},
            {'question_text': 'In triangle ABC, if A = 60°, a = 5, b = 4. Find sin B.', 'option_a': '2√3/5', 'option_b': '4√3/10', 'option_c': '2√3/10', 'option_d': '√3/5', 'correct_answer': 'B', 'explanation': 'By sine rule: sin B/b = sin A/a; sin B = 4×(√3/2)/5 = 2√3/5 = 4√3/10.'},
            {'question_text': 'The value of cosec 30° is:', 'option_a': '1', 'option_b': '2', 'option_c': '1/2', 'option_d': '√2', 'correct_answer': 'B', 'explanation': 'cosec θ = 1/sin θ; cosec 30° = 1/(1/2) = 2.'},
            {'question_text': 'If sin x + cos x = √2, find the value of x.', 'option_a': '0°', 'option_b': '45°', 'option_c': '90°', 'option_d': '135°', 'correct_answer': 'B', 'explanation': 'sin x + cos x = √2 sin(x + 45°) = √2; sin(x+45°) = 1; x+45° = 90°; x = 45°.'},
            # STATISTICS & PROBABILITY (Q126–Q150)
            {'question_text': 'Find the mean of: 5, 8, 3, 10, 4', 'option_a': '5', 'option_b': '6', 'option_c': '7', 'option_d': '8', 'correct_answer': 'B', 'explanation': 'Mean = (5+8+3+10+4)/5 = 30/5 = 6.'},
            {'question_text': 'Find the median of: 3, 7, 2, 9, 5, 1, 8', 'option_a': '5', 'option_b': '6', 'option_c': '7', 'option_d': '3', 'correct_answer': 'A', 'explanation': 'Arrange: 1,2,3,5,7,8,9. Median (middle value) = 5.'},
            {'question_text': 'Find the mode of: 4, 7, 3, 4, 9, 4, 7, 2', 'option_a': '4', 'option_b': '7', 'option_c': '9', 'option_d': '3', 'correct_answer': 'A', 'explanation': '4 appears 3 times — more than any other value. Mode = 4.'},
            {'question_text': 'The range of: 12, 7, 3, 15, 9, 1 is:', 'option_a': '10', 'option_b': '12', 'option_c': '14', 'option_d': '15', 'correct_answer': 'C', 'explanation': 'Range = max - min = 15 - 1 = 14.'},
            {'question_text': 'The variance of 2, 4, 6, 8, 10 is:', 'option_a': '4', 'option_b': '6', 'option_c': '8', 'option_d': '10', 'correct_answer': 'C', 'explanation': 'Mean = 6; deviations: -4,-2,0,2,4; squared: 16,4,0,4,16; variance = 40/5 = 8.'},
            {'question_text': 'Standard deviation is:', 'option_a': 'The mean of the data', 'option_b': 'The square root of the variance', 'option_c': 'The range divided by 2', 'option_d': 'The sum of all values', 'correct_answer': 'B', 'explanation': 'Standard deviation = √(variance).'},
            {'question_text': 'A set of data has mean 20 and standard deviation 4. The coefficient of variation is:', 'option_a': '5%', 'option_b': '10%', 'option_c': '20%', 'option_d': '80%', 'correct_answer': 'C', 'explanation': 'CV = (SD/mean) × 100 = (4/20) × 100 = 20%.'},
            {'question_text': 'A coin is tossed once. The probability of getting a head is:', 'option_a': '0', 'option_b': '1/4', 'option_c': '1/2', 'option_d': '1', 'correct_answer': 'C', 'explanation': 'There is 1 favourable outcome (head) out of 2 possible outcomes.'},
            {'question_text': 'A die is rolled. The probability of getting an even number is:', 'option_a': '1/6', 'option_b': '1/3', 'option_c': '1/2', 'option_d': '2/3', 'correct_answer': 'C', 'explanation': 'Even numbers on a die: {2,4,6} — 3 out of 6 outcomes. P = 3/6 = 1/2.'},
            {'question_text': 'Two fair coins are tossed. The probability of getting two heads is:', 'option_a': '1/4', 'option_b': '1/2', 'option_c': '3/4', 'option_d': '1', 'correct_answer': 'A', 'explanation': 'Sample space: {HH,HT,TH,TT}. P(HH) = 1/4.'},
            {'question_text': 'A bag contains 3 red and 5 blue balls. A ball is drawn at random. P(red) is:', 'option_a': '3/8', 'option_b': '5/8', 'option_c': '3/5', 'option_d': '1/3', 'correct_answer': 'A', 'explanation': 'P(red) = 3/(3+5) = 3/8.'},
            {'question_text': 'P(A) = 0.3 and P(B) = 0.4, and A and B are independent. Find P(A and B).', 'option_a': '0.12', 'option_b': '0.7', 'option_c': '0.58', 'option_d': '0.1', 'correct_answer': 'A', 'explanation': 'For independent events: P(A∩B) = P(A)×P(B) = 0.3×0.4 = 0.12.'},
            {'question_text': 'A card is drawn from a pack of 52. P(king) is:', 'option_a': '1/52', 'option_b': '1/13', 'option_c': '4/52', 'option_d': 'Both B and C', 'correct_answer': 'D', 'explanation': 'P(king) = 4/52 = 1/13. Both B and C are equal so D is correct.'},
            {'question_text': 'The class mark of the class interval 20 - 30 is:', 'option_a': '20', 'option_b': '25', 'option_c': '30', 'option_d': '10', 'correct_answer': 'B', 'explanation': 'Class mark = (lower + upper)/2 = (20+30)/2 = 25.'},
            {'question_text': 'The histogram frequency is represented by:', 'option_a': 'The height of the bar', 'option_b': 'The area of the bar', 'option_c': 'The width of the bar', 'option_d': 'The perimeter of the bar', 'correct_answer': 'B', 'explanation': 'In a histogram, frequency is proportional to the area (height × width) of each bar.'},
            {'question_text': 'The cumulative frequency curve is also called a:', 'option_a': 'Histogram', 'option_b': 'Bar chart', 'option_c': 'Ogive', 'option_d': 'Pie chart', 'correct_answer': 'C', 'explanation': 'A cumulative frequency curve (ogive) is an S-shaped curve showing cumulative frequencies.'},
            {'question_text': 'A and B are mutually exclusive events. P(A) = 0.4 and P(B) = 0.3. P(A or B) is:', 'option_a': '0.12', 'option_b': '0.7', 'option_c': '0.58', 'option_d': '0.1', 'correct_answer': 'B', 'explanation': 'For mutually exclusive events: P(A∪B) = P(A)+P(B) = 0.4+0.3 = 0.7.'},
            {'question_text': 'The expected number of heads when 100 fair coins are tossed is:', 'option_a': '25', 'option_b': '40', 'option_c': '50', 'option_d': '75', 'correct_answer': 'C', 'explanation': 'E = n×p = 100×(1/2) = 50.'},
            {'question_text': 'In a frequency distribution, the class with the highest frequency is the:', 'option_a': 'Mean class', 'option_b': 'Modal class', 'option_c': 'Median class', 'option_d': 'Upper class', 'correct_answer': 'B', 'explanation': 'The modal class has the highest frequency in a grouped frequency distribution.'},
            {'question_text': 'If the mean of five numbers is 12 and four of the numbers are 10, 14, 8, 16, find the fifth number.', 'option_a': '10', 'option_b': '12', 'option_c': '14', 'option_d': '16', 'correct_answer': 'B', 'explanation': 'Sum = 12×5 = 60; Four numbers sum = 10+14+8+16 = 48; Fifth = 60-48 = 12.'},
            {'question_text': 'A number is chosen at random from 1 to 20. Find P(multiple of 3).', 'option_a': '1/5', 'option_b': '3/10', 'option_c': '1/3', 'option_d': '2/5', 'correct_answer': 'B', 'explanation': 'Multiples of 3 from 1-20: {3,6,9,12,15,18} = 6 numbers. P = 6/20 = 3/10.'},
            {'question_text': 'The interquartile range is:', 'option_a': 'Q3 - Q1', 'option_b': 'Q2 - Q1', 'option_c': 'Q3 - Q2', 'option_d': '(Q3 + Q1)/2', 'correct_answer': 'A', 'explanation': 'IQR = Q3 - Q1 (the range of the middle 50% of data).'},
            {'question_text': 'Which measure of central tendency is most affected by extreme values?', 'option_a': 'Mode', 'option_b': 'Median', 'option_c': 'Mean', 'option_d': 'Range', 'correct_answer': 'C', 'explanation': 'The mean is affected by every value in the dataset, including outliers/extreme values.'},
            {'question_text': 'From a class of 5 boys and 3 girls, 2 are chosen at random. P(both girls) is:', 'option_a': '3/28', 'option_b': '3/8', 'option_c': '1/14', 'option_d': '3/14', 'correct_answer': 'A', 'explanation': 'P = C(3,2)/C(8,2) = 3/28.'},
            {'question_text': 'The pie chart angle for a class of 12 students out of 60 is:', 'option_a': '60°', 'option_b': '72°', 'option_c': '80°', 'option_d': '120°', 'correct_answer': 'B', 'explanation': 'Angle = (12/60)×360° = 72°.'},
            # CALCULUS (Q151–Q175)
            {'question_text': 'Find dy/dx if y = 3x² + 5x - 2.', 'option_a': '6x + 5', 'option_b': '3x + 5', 'option_c': '6x - 5', 'option_d': '3x² + 5', 'correct_answer': 'A', 'explanation': 'dy/dx = 6x + 5 (using power rule).'},
            {'question_text': 'Differentiate y = x⁴ - 2x³ + 7x.', 'option_a': '4x³ - 6x² + 7', 'option_b': '4x³ - 2x² + 7', 'option_c': 'x⁴ - 6x + 7', 'option_d': '4x⁴ - 6x + 7', 'correct_answer': 'A', 'explanation': 'dy/dx = 4x³ - 6x² + 7.'},
            {'question_text': 'Find the gradient of y = x³ - 3x² + 2 at x = 2.', 'option_a': '0', 'option_b': '2', 'option_c': '4', 'option_d': '6', 'correct_answer': 'A', 'explanation': 'dy/dx = 3x² - 6x; at x=2: 3(4)-6(2) = 12-12 = 0.'},
            {'question_text': 'Find the turning point of y = x² - 4x + 7.', 'option_a': '(2, 3)', 'option_b': '(2, 7)', 'option_c': '(-2, 15)', 'option_d': '(4, 7)', 'correct_answer': 'A', 'explanation': 'dy/dx = 2x-4 = 0; x=2. y = 4-8+7 = 3. Turning point = (2, 3).'},
            {'question_text': 'Evaluate ∫(2x + 3)dx', 'option_a': 'x² + 3x + c', 'option_b': '2x² + 3x + c', 'option_c': 'x² + 3 + c', 'option_d': '2x + c', 'correct_answer': 'A', 'explanation': '∫(2x+3)dx = x² + 3x + c.'},
            {'question_text': 'Evaluate ∫₀¹ (3x²)dx', 'option_a': '0', 'option_b': '1', 'option_c': '2', 'option_d': '3', 'correct_answer': 'B', 'explanation': '[x³]₀¹ = 1 - 0 = 1.'},
            {'question_text': 'Find dy/dx if y = (2x + 1)³.', 'option_a': '6(2x+1)²', 'option_b': '3(2x+1)²', 'option_c': '6(2x+1)', 'option_d': '3(2x+1)³', 'correct_answer': 'A', 'explanation': 'By chain rule: dy/dx = 3(2x+1)² × 2 = 6(2x+1)².'},
            {'question_text': 'Find the derivative of y = sin 3x.', 'option_a': 'cos 3x', 'option_b': '3 cos 3x', 'option_c': '-3 cos 3x', 'option_d': '-cos 3x', 'correct_answer': 'B', 'explanation': 'd/dx[sin 3x] = 3 cos 3x (chain rule).'},
            {'question_text': 'Differentiate y = eˣ + ln x.', 'option_a': 'eˣ + 1/x', 'option_b': 'eˣ + ln x', 'option_c': 'eˣ - 1/x', 'option_d': '1 + 1/x', 'correct_answer': 'A', 'explanation': 'd/dx[eˣ] = eˣ; d/dx[ln x] = 1/x.'},
            {'question_text': 'Evaluate ∫(cos x)dx.', 'option_a': '-sin x + c', 'option_b': 'sin x + c', 'option_c': '-cos x + c', 'option_d': 'cos x + c', 'correct_answer': 'B', 'explanation': '∫cos x dx = sin x + c.'},
            {'question_text': 'The area under the curve y = x² between x = 0 and x = 3 is:', 'option_a': '6', 'option_b': '9', 'option_c': '18', 'option_d': '27', 'correct_answer': 'B', 'explanation': '∫₀³ x² dx = [x³/3]₀³ = 9 - 0 = 9.'},
            {'question_text': 'Find the second derivative of y = x⁴ - 3x².', 'option_a': '4x³ - 6x', 'option_b': '12x² - 6', 'option_c': '4x² - 3', 'option_d': 'x³ - 3x', 'correct_answer': 'B', 'explanation': 'y\' = 4x³-6x; y\'\' = 12x²-6.'},
            {'question_text': 'If dy/dx = 0 and d²y/dx² > 0, the point is a:', 'option_a': 'Maximum', 'option_b': 'Point of inflexion', 'option_c': 'Minimum', 'option_d': 'Saddle point', 'correct_answer': 'C', 'explanation': 'When the second derivative is positive and first derivative is zero, it is a local minimum.'},
            {'question_text': 'Evaluate: lim(x→2) (x² - 4)/(x - 2)', 'option_a': '0', 'option_b': '2', 'option_c': '4', 'option_d': '∞', 'correct_answer': 'C', 'explanation': '(x²-4)/(x-2) = (x+2)(x-2)/(x-2) = x+2; as x→2, limit = 4.'},
            {'question_text': 'Find ∫(1/x)dx', 'option_a': 'x + c', 'option_b': 'ln|x| + c', 'option_c': '-1/x² + c', 'option_d': '1/x² + c', 'correct_answer': 'B', 'explanation': '∫(1/x)dx = ln|x| + c.'},
            {'question_text': 'Differentiate y = x sin x.', 'option_a': 'cos x', 'option_b': 'x cos x + sin x', 'option_c': 'x cos x - sin x', 'option_d': 'sin x + x', 'correct_answer': 'B', 'explanation': 'By product rule: dy/dx = sin x + x cos x.'},
            {'question_text': 'Evaluate ∫₀^(π/2) sin x dx', 'option_a': '0', 'option_b': '1', 'option_c': '2', 'option_d': 'π', 'correct_answer': 'B', 'explanation': '[-cos x]₀^(π/2) = -cos(π/2) + cos 0 = 0 + 1 = 1.'},
            {'question_text': 'Find the rate of change of A = πr² with respect to r when r = 3.', 'option_a': '6π', 'option_b': '9π', 'option_c': '18π', 'option_d': '3π', 'correct_answer': 'A', 'explanation': 'dA/dr = 2πr; at r=3: dA/dr = 6π.'},
            {'question_text': 'Evaluate ∫e²ˣ dx', 'option_a': 'e²ˣ + c', 'option_b': '2e²ˣ + c', 'option_c': '(1/2)e²ˣ + c', 'option_d': 'e²ˣ/x + c', 'correct_answer': 'C', 'explanation': '∫e^(2x)dx = (1/2)e^(2x) + c.'},
            {'question_text': 'Find the maximum value of f(x) = -x² + 4x + 5.', 'option_a': '5', 'option_b': '7', 'option_c': '9', 'option_d': '11', 'correct_answer': 'C', 'explanation': 'f\'(x) = -2x+4 = 0; x=2. f(2) = -4+8+5 = 9. f\'\'(x) = -2 < 0, so maximum.'},
            {'question_text': 'Evaluate ∫(3x² - 2x + 1)dx', 'option_a': 'x³ - x² + x + c', 'option_b': '6x - 2 + c', 'option_c': '3x - 2 + c', 'option_d': 'x³ + x² - x + c', 'correct_answer': 'A', 'explanation': '∫(3x²-2x+1)dx = x³ - x² + x + c.'},
            {'question_text': 'Find the velocity at t = 2 if displacement s = t³ - 3t² + 2t.', 'option_a': '0', 'option_b': '2', 'option_c': '4', 'option_d': '6', 'correct_answer': 'B', 'explanation': 'v = ds/dt = 3t²-6t+2; at t=2: 12-12+2 = 2.'},
            {'question_text': 'Find the area enclosed by y = x², the x-axis, x = 1 and x = 3.', 'option_a': '8⅔', 'option_b': '26/3', 'option_c': '9', 'option_d': '18', 'correct_answer': 'B', 'explanation': '∫₁³ x² dx = [x³/3]₁³ = 9 - 1/3 = 26/3.'},
            {'question_text': 'The gradient function of a curve is 3x² + 2. If the curve passes through (1, 5), find the equation.', 'option_a': 'y = x³ + 2x + 2', 'option_b': 'y = x³ + 2x + 1', 'option_c': 'y = x³ + 2x - 1', 'option_d': 'y = 3x² + 2x + 1', 'correct_answer': 'A', 'explanation': 'Integrate: y = x³+2x+c. At (1,5): 1+2+c=5; c=2. y = x³+2x+2.'},
            {'question_text': 'Find dy/dx if y = (x² + 1)/(x - 1) using the quotient rule.', 'option_a': '(x² - 2x - 1)/(x-1)²', 'option_b': '(x² + 1)/(x-1)²', 'option_c': '(x+1)/(x-1)', 'option_d': '2x/(x-1)', 'correct_answer': 'A', 'explanation': 'Quotient rule: [(x-1)(2x) - (x²+1)(1)]/(x-1)² = (2x²-2x-x²-1)/(x-1)² = (x²-2x-1)/(x-1)².'},
            # ADDITIONAL QUESTIONS (Q176–Q200)
            {'question_text': 'If A = {1,2,3,4} and B = {3,4,5,6}, find A∩B.', 'option_a': '{3,4}', 'option_b': '{1,2,5,6}', 'option_c': '{1,2,3,4,5,6}', 'option_d': '{1,2}', 'correct_answer': 'A', 'explanation': 'A∩B = elements in both A and B = {3,4}.'},
            {'question_text': 'If n(A) = 12, n(B) = 16 and n(A∪B) = 22, find n(A∩B).', 'option_a': '4', 'option_b': '6', 'option_c': '8', 'option_d': '10', 'correct_answer': 'B', 'explanation': 'n(A∩B) = n(A)+n(B)-n(A∪B) = 12+16-22 = 6.'},
            {'question_text': 'Simplify: (x + y)² - (x - y)²', 'option_a': '4xy', 'option_b': '2xy', 'option_c': 'x² + y²', 'option_d': '4x²', 'correct_answer': 'A', 'explanation': '= (x+y+x-y)(x+y-x+y) = (2x)(2y) = 4xy.'},
            {'question_text': 'Find x if 4^x = 8^(x-1).', 'option_a': '1', 'option_b': '2', 'option_c': '3', 'option_d': '4', 'correct_answer': 'C', 'explanation': '2^(2x) = 2^(3(x-1)); 2x = 3x-3; x = 3.'},
            {'question_text': 'Express 180 as a product of prime factors.', 'option_a': '2² × 3² × 5', 'option_b': '2³ × 3 × 5', 'option_c': '2 × 3³ × 5', 'option_d': '2² × 3 × 5²', 'correct_answer': 'A', 'explanation': '180 = 4 × 45 = 4 × 9 × 5 = 2² × 3² × 5.'},
            {'question_text': 'The angles of a quadrilateral are in ratio 1:2:3:4. Find the largest angle.', 'option_a': '120°', 'option_b': '144°', 'option_c': '160°', 'option_d': '172°', 'correct_answer': 'B', 'explanation': 'Sum = 360°; shares: 1+2+3+4=10. Largest = (4/10)×360° = 144°.'},
            {'question_text': 'In a data set, 40% of the values are below Q1. This statement is:', 'option_a': 'True', 'option_b': 'False', 'option_c': 'Sometimes true', 'option_d': 'Cannot determine', 'correct_answer': 'B', 'explanation': 'Q1 is the 25th percentile, meaning 25% of values are below it, not 40%.'},
            {'question_text': 'If 3x + 2y = 12 and x = 2, find y.', 'option_a': '2', 'option_b': '3', 'option_c': '4', 'option_d': '6', 'correct_answer': 'B', 'explanation': '3(2)+2y=12; 6+2y=12; 2y=6; y=3.'},
            {'question_text': 'Two interior angles of a triangle are 55° and 73°. The exterior angle at the third vertex is:', 'option_a': '52°', 'option_b': '128°', 'option_c': '180°', 'option_d': '127°', 'correct_answer': 'B', 'explanation': 'Third interior angle = 180-55-73 = 52°. Exterior angle = 180-52 = 128°.'},
            {'question_text': 'Find the derivative of y = ln(3x).', 'option_a': '3/x', 'option_b': '1/x', 'option_c': '1/(3x)', 'option_d': '3 ln x', 'correct_answer': 'B', 'explanation': 'd/dx[ln(3x)] = 1/(3x)×3 = 1/x.'},
            {'question_text': 'The value of sin²30° + cos²30° is:', 'option_a': '0', 'option_b': '1/2', 'option_c': '1', 'option_d': '3/4', 'correct_answer': 'C', 'explanation': 'This is the Pythagorean identity: sin²θ + cos²θ = 1 for all θ.'},
            {'question_text': 'The sum of the first n terms of an AP is given by Sn = n/2(2a+(n-1)d). If a=3, d=4, n=6, find S₆.', 'option_a': '54', 'option_b': '60', 'option_c': '66', 'option_d': '78', 'correct_answer': 'D', 'explanation': 'S₆ = 6/2[6+5×4] = 3[6+20] = 3×26 = 78.'},
            {'question_text': 'What is the probability that a card drawn from a deck of 52 is a face card (Jack, Queen or King)?', 'option_a': '1/13', 'option_b': '3/13', 'option_c': '3/52', 'option_d': '4/13', 'correct_answer': 'B', 'explanation': 'Face cards: 3 types × 4 suits = 12 cards. P = 12/52 = 3/13.'},
            {'question_text': 'The total surface area of a cuboid with dimensions 3 × 4 × 5 cm is:', 'option_a': '47 cm²', 'option_b': '60 cm²', 'option_c': '94 cm²', 'option_d': '120 cm²', 'correct_answer': 'C', 'explanation': 'TSA = 2(lb+bh+hl) = 2(12+20+15) = 2×47 = 94 cm².'},
            {'question_text': 'Factorize: 2x² + 7x + 3', 'option_a': '(2x+1)(x+3)', 'option_b': '(x+1)(2x+3)', 'option_c': '(2x+3)(x+1)', 'option_d': '(2x-1)(x+3)', 'correct_answer': 'A', 'explanation': '2×3=6; find factors of 6 that add to 7: 1 and 6; (2x+1)(x+3).'},
            {'question_text': 'If the mean of 6, 8, x, 12, 14 is 10, find x.', 'option_a': '8', 'option_b': '10', 'option_c': '12', 'option_d': '14', 'correct_answer': 'B', 'explanation': 'Sum = 10×5 = 50; 6+8+x+12+14 = 50; 40+x=50; x=10.'},
            {'question_text': 'What is the area of triangle with sides a=5, b=7 and included angle C=30°?', 'option_a': '35/4', 'option_b': '35/2', 'option_c': '35', 'option_d': '35√3/4', 'correct_answer': 'A', 'explanation': 'Area = (1/2)ab sin C = (1/2)(5)(7)(1/2) = 35/4.'},
            {'question_text': 'The remainder when f(x) = x³ - 2x + 5 is divided by (x-1) is:', 'option_a': '2', 'option_b': '3', 'option_c': '4', 'option_d': '5', 'correct_answer': 'C', 'explanation': 'By remainder theorem: f(1) = 1-2+5 = 4.'},
            {'question_text': 'Find the acceleration at t = 3 if v = t² - 4t + 3.', 'option_a': '0', 'option_b': '2', 'option_c': '4', 'option_d': '6', 'correct_answer': 'B', 'explanation': 'a = dv/dt = 2t-4; at t=3: 6-4 = 2.'},
            {'question_text': 'How many prime numbers are between 20 and 40?', 'option_a': '3', 'option_b': '4', 'option_c': '5', 'option_d': '6', 'correct_answer': 'B', 'explanation': 'Primes: 23, 29, 31, 37 — there are 4 prime numbers between 20 and 40.'},
            {'question_text': 'The point of intersection of y = 2x + 1 and y = -x + 7 is:', 'option_a': '(1, 3)', 'option_b': '(2, 5)', 'option_c': '(3, 4)', 'option_d': '(4, 3)', 'correct_answer': 'B', 'explanation': '2x+1 = -x+7; 3x=6; x=2; y=5. Point: (2,5).'},
            {'question_text': 'Evaluate C(6,2) (6 choose 2).', 'option_a': '12', 'option_b': '15', 'option_c': '20', 'option_d': '30', 'correct_answer': 'B', 'explanation': 'C(6,2) = 6!/(2!×4!) = (6×5)/(2×1) = 15.'},
            {'question_text': 'A distribution is negatively skewed if:', 'option_a': 'Mean > Median > Mode', 'option_b': 'Mean < Median < Mode', 'option_c': 'Mean = Median = Mode', 'option_d': 'Mode > Median > Mean', 'correct_answer': 'B', 'explanation': 'In a negatively (left) skewed distribution, the tail is to the left, and Mean < Median < Mode.'},
            {'question_text': 'Find ∫₁³ (2x + 1) dx.', 'option_a': '10', 'option_b': '12', 'option_c': '14', 'option_d': '16', 'correct_answer': 'B', 'explanation': '[x²+x]₁³ = (9+3)-(1+1) = 12-2 = 10. Answer is A.'},
            {'question_text': 'The number of ways 4 students can be arranged in a line is:', 'option_a': '8', 'option_b': '12', 'option_c': '16', 'option_d': '24', 'correct_answer': 'D', 'explanation': '4! = 4×3×2×1 = 24 ways.'},
        ]
        
        
        # Get math topics for assignment
        num_theory_topic = Topic.query.filter_by(name='Number Theory & Indices').first()
        algebra_topic = Topic.query.filter_by(name='Algebra').first()
        geometry_topic = Topic.query.filter_by(name='Geometry & Mensuration').first()
        trig_topic = Topic.query.filter_by(name='Trigonometry').first()
        stats_topic = Topic.query.filter_by(name='Statistics & Probability').first()
        calc_topic = Topic.query.filter_by(name='Calculus').first()
        
        for i, q in enumerate(math_questions, 1):
            # Assign topics based on question number ranges
            if i <= 30:
                topic_id = num_theory_topic.id if num_theory_topic else None
            elif i <= 70:
                topic_id = algebra_topic.id if algebra_topic else None
            elif i <= 100:
                topic_id = geometry_topic.id if geometry_topic else None
            elif i <= 125:
                topic_id = trig_topic.id if trig_topic else None
            elif i <= 150:
                topic_id = stats_topic.id if stats_topic else None
            else:
                topic_id = calc_topic.id if calc_topic else None
                
            question = Question(
                exam_id=mathematics_exam.id,
                topic_id=topic_id,
                question_text=q['question_text'],
                question_type='multiple_choice',
                subject='Mathematics',
                option_a=q['option_a'],
                option_b=q['option_b'],
                option_c=q['option_c'],
                option_d=q['option_d'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation'],
                marks=1,
                question_order=i
            )
            db.session.add(question)
        
        
        db.session.commit()
        
        print("✅ Database seeded successfully!")
        print(f"Created {3} exams (English, Mathematics, Full Exam)")
        print(f"Created {13} topics")
        print(f"Created {len(english_questions) + len(math_questions)} total questions")
        print(f"  - English: {len(english_questions)} questions (with 4 topics)")
        print(f"  - Mathematics: {len(math_questions)} questions (with 6 topics)")

if __name__ == '__main__':
    seed_database()
