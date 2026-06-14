"""
Combined Database Seeding Script for UNILAG Post-UTME Practice Platform.
Generates 400 unique questions per subject:
- Use of English: 400 questions
- General Paper: 400 questions
- Mathematics: 400 questions
"""

from app import create_app, db
from app.models import Exam, Question, Topic, Result, Answer


def clear_subject(subject):
    """Delete all questions, topics, and exams for a given subject."""
    exam = Exam.query.filter_by(subject=subject).first()
    if exam:
        results = Result.query.filter_by(exam_id=exam.id).all()
        for r in results:
            Answer.query.filter_by(result_id=r.id).delete()
        Result.query.filter_by(exam_id=exam.id).delete()
        Question.query.filter_by(exam_id=exam.id).delete()
        db.session.delete(exam)
    Topic.query.filter_by(subject=subject).delete()
    db.session.commit()
    print(f"Cleared existing {subject} data.")


def seed_english():
    clear_subject('English')

    topics = [
        Topic(name='Lexis & Structure', subject='English', description='Word choice, vocabulary, sentence completion'),
        Topic(name='Grammar & Syntax', subject='English', description='Concord, tenses, clauses, sentence types'),
        Topic(name='Advanced Grammar', subject='English', description='Subjunctive, inversion, conditionals'),
        Topic(name='Vocabulary', subject='English', description='Synonyms, antonyms, idioms, contextual meaning'),
        Topic(name='Oral English', subject='English', description='Stress, intonation, vowel/consonant sounds'),
        Topic(name='Phrasal Verbs & Collocations', subject='English', description='Idiomatic verb phrases and word partnerships'),
        Topic(name='Analogies', subject='English', description='Word relationships and logical pairs'),
        Topic(name='Sentence Structure & Clause Types', subject='English', description='Simple, compound, complex; clause functions'),
        Topic(name='Verb Tenses & Aspect', subject='English', description='Time reference, perfective, progressive'),
        Topic(name='Agreement & Concord', subject='English', description='Subject-verb, pronoun-antecedent agreement'),
        Topic(name='Connectors & Logical Relations', subject='English', description='Conjunctions, transitions, cause-effect'),
        Topic(name='Meaning & Paraphrase', subject='English', description='Sentence meaning, inference, paraphrasing'),
        Topic(name='Ambiguity & Interpretation', subject='English', description='Structural and lexical ambiguity'),
        Topic(name='Word Order & Inversion', subject='English', description='Subject-verb inversion, fronting, cleft sentences'),
        Topic(name='Semantic Roles & Thematic Relations', subject='English', description='Agent, patient, theme, instrument'),
    ]
    for t in topics:
        db.session.add(t)
    db.session.commit()

    exam = Exam(
        title="Use of English",
        subject="English",
        description="400 UNILAG-style English questions",
        duration_minutes=60,
        total_questions=400,
        passing_score=50
    )
    db.session.add(exam)
    db.session.commit()

    lexis = Topic.query.filter_by(name='Lexis & Structure', subject='English').first()
    grammar = Topic.query.filter_by(name='Grammar & Syntax', subject='English').first()
    adv_grammar = Topic.query.filter_by(name='Advanced Grammar', subject='English').first()
    vocab = Topic.query.filter_by(name='Vocabulary', subject='English').first()
    oral = Topic.query.filter_by(name='Oral English', subject='English').first()
    phrasal = Topic.query.filter_by(name='Phrasal Verbs & Collocations', subject='English').first()
    analogies_topic = Topic.query.filter_by(name='Analogies', subject='English').first()
    structure_topic = Topic.query.filter_by(name='Sentence Structure & Clause Types', subject='English').first()
    tense_topic = Topic.query.filter_by(name='Verb Tenses & Aspect', subject='English').first()
    agreement_topic = Topic.query.filter_by(name='Agreement & Concord', subject='English').first()
    connectors_topic = Topic.query.filter_by(name='Connectors & Logical Relations', subject='English').first()
    meaning_topic = Topic.query.filter_by(name='Meaning & Paraphrase', subject='English').first()
    ambiguity_topic = Topic.query.filter_by(name='Ambiguity & Interpretation', subject='English').first()
    wordorder_topic = Topic.query.filter_by(name='Word Order & Inversion', subject='English').first()
    semantic_topic = Topic.query.filter_by(name='Semantic Roles & Thematic Relations', subject='English').first()

    all_english = []

    # ===== OLD ENGLISH: LEXIS & STRUCTURE (40 questions) =====
    lexis_items = [
        ("The boy was punished because he ___ his teacher's instructions.", "ignored", "disobeyed", "violated", "omitted", "B"),
        ("Hardly had she finished speaking ___ the bell rang.", "when", "than", "then", "but", "A"),
        ("The workers have complained that their salaries are not ___ with the work they do.", "consistent", "compatible", "commensurate", "convenient", "C"),
        ("The teacher encouraged the students to look ___ new words in the dictionary.", "into", "up", "out", "over", "B"),
        ("He has a good command ___ the English language.", "for", "on", "over", "of", "D"),
        ("We were advised to abstain ___ bad habits.", "of", "from", "off", "with", "B"),
        ("My uncle, together with his children, ___ arriving today.", "are", "were", "is", "have been", "C"),
        ("He is the man ___ broke the window.", "whom", "whose", "which", "who", "D"),
        ("If I ___ you, I would accept the offer.", "were", "was", "am", "be", "A"),
        ("Not only does she sing, but she ___ plays the piano.", "also", "too", "either", "as well", "A"),
        ("The thief was caught because someone had given him ___.", "out", "away", "off", "in", "B"),
        ("The committee will meet to ___ the issue.", "dissolve", "discard", "deliberate", "disseminate", "C"),
        ("I am not used to ___ early.", "waking", "wake", "woken", "woke", "A"),
        ("He prefers tea ___ coffee.", "than", "than to", "to", "over", "C"),
        ("The teacher asked the students to be quiet, but ___ listened.", "neither", "none", "nobody", "few", "D"),
        ("We were warned ___ the dangers of reckless driving.", "about", "on", "with", "for", "A"),
        ("She looked forward to ___ her friend.", "see", "seeing", "seen", "saw", "B"),
        ("I don't mind ___ for a few minutes.", "to wait", "wait", "waiting", "waited", "C"),
        ("The man is not only rich ___ generous.", "also", "and", "but also", "or", "C"),
        ("The manager said he would look ___ the matter.", "up", "into", "off", "after", "B"),
        ("His parents objected ___ his plans.", "to", "with", "at", "on", "A"),
        ("The girl was accused ___ stealing the book.", "for", "of", "about", "on", "B"),
        ("The driver was penalized ___ speeding.", "of", "for", "with", "on", "B"),
        ("He was so tired that he ___ asleep during the lecture.", "falls", "fell", "fallen", "falling", "B"),
        ("The principal insisted that the student ___ suspended.", "be", "is", "was", "has been", "A"),
        ("The boy asked me if I ___ him a pen.", "can borrow", "could lend", "can lend", "could borrow", "B"),
        ("The culprit confessed ___ the crime.", "to committing", "to commit", "committing", "having commit", "A"),
        ("The man was accused of ___ his position.", "abusing", "insulting", "abasing", "misusing", "A"),
        ("The lady looks ___ in her new dress.", "beautiful", "beautifully", "beauty", "beauteous", "A"),
        ("We were advised to work hard ___ we fail.", "in order that", "unless", "so that", "lest", "D"),
        ("I told them to go home, ___?", "didn't I", "don't I", "hadn't I", "haven't I", "A"),
        ("They are not used to ___ this kind of hardship.", "face", "facing", "faced", "be facing", "B"),
        ("Many people are allergic ___ dust.", "from", "of", "to", "with", "C"),
        ("The movie is interesting, ___?", "is it", "isn't it", "was it", "wasn't it", "B"),
        ("He came late to school ___ the heavy rain.", "due to", "because", "although", "even though", "A"),
        ("The ___ of the meeting was to discuss the school fees.", "purpose", "propose", "proposal", "proposement", "A"),
        ("Neither the teacher nor the students ___ present.", "is", "are", "was", "were", "B"),
        ("He is not ___ to go to the party.", "enough tall", "tall enough", "taller enough", "enough taller", "B"),
        ("If he had studied harder, he ___ passed.", "will have", "would have", "would", "will", "B"),
        ("That bag is hers, isn't ___?", "she", "it", "he", "her", "B"),
    ]
    for q in lexis_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': lexis.id})

    # ===== OLD ENGLISH: GRAMMAR & SYNTAX (40 questions) =====
    grammar_items = [
        ("The girl, as well as her brothers, ___ going on a trip.", "are", "were", "is", "have", "C"),
        ("If she had known earlier, she ___ have told you.", "will", "would", "should", "would have", "D"),
        ("The teacher, together with his assistants, ___ coming now.", "are", "is", "were", "have been", "B"),
        ("Neither the boys nor their sister ___ the answer.", "know", "knows", "are knowing", "has know", "B"),
        ("I am used to ___ early every day.", "get up", "getting up", "gets up", "got up", "B"),
        ("She ___ her homework before dinner.", "has finished", "had finished", "is finishing", "will finish", "B"),
        ("Each of the players ___ a medal.", "receive", "have received", "receives", "receiving", "C"),
        ("We had hardly reached the station ___ it began to rain.", "than", "that", "when", "then", "C"),
        ("She would rather you ___ now.", "go", "went", "gone", "going", "B"),
        ("Had they arrived earlier, they ___ the bus.", "would have caught", "will catch", "caught", "would catch", "A"),
        ("He behaves as though he ___ the boss.", "is", "were", "was", "be", "B"),
        ("He insisted that the boy ___ punished.", "be", "is", "should being", "was", "A"),
        ("Scarcely had he entered the hall ___ the lights went off.", "when", "than", "but", "and", "A"),
        ("She has been singing since the program ___ .", "began", "begins", "begin", "begun", "A"),
        ("It's high time we ___ the truth.", "know", "knew", "known", "will know", "B"),
        ("He speaks English better than ___ in his class.", "any student", "any other student", "every student", "all student", "B"),
        ("The more she cried, ___.", "the more she felt relieved", "she felt more relieved", "more she felt relieved", "the most she felt relieved", "A"),
        ("The baby is too weak ___.", "to cried", "to be crying", "to cry", "for crying", "C"),
        ("I would have helped you if I ___ earlier.", "knew", "know", "have known", "had known", "D"),
        ("No sooner had they left ___ it started to rain.", "when", "than", "then", "that", "B"),
        ("He ran so fast that he ___ the race.", "will win", "wins", "won", "had won", "C"),
        ("He jumped ___ the river to save the child.", "in", "into", "onto", "of", "B"),
        ("The house was infested ___ rats.", "with", "by", "of", "from", "A"),
        ("She always prides herself ___ her honesty.", "for", "in", "on", "at", "C"),
        ("The politician is accused ___ corruption.", "on", "for", "with", "of", "D"),
        ("The food is not suitable ___ infants.", "to", "for", "of", "at", "B"),
        ("You had better ___ your homework before going out.", "finish", "finishing", "finished", "had finish", "A"),
        ("If I were you, I ___ accept the offer.", "will", "shall", "would", "must", "C"),
        ("He can't help ___ at the joke.", "to laugh", "laughing", "laughed", "laugh", "B"),
        ("Would you mind ___ the window?", "to open", "open", "opening", "opened", "C"),
        ("I made him ___ the ground.", "cleaning", "to clean", "clean", "cleaned", "C"),
        ("The plane had already taken off before we ___ the airport.", "reached", "reach", "had reached", "were reaching", "A"),
        ("Neither James nor his friends ___ the news.", "knows", "knowing", "know", "knews", "C"),
        ("A number of students ___ absent today.", "was", "were", "is", "be", "B"),
        ("The president and commander-in-chief ___ visiting today.", "is", "are", "were", "have", "A"),
        ("He would have succeeded if he ___ harder.", "works", "has worked", "had worked", "have worked", "C"),
        ("The boy looks as if he ___ a ghost.", "sees", "seen", "has seen", "had seen", "D"),
        ("The room is too small for the children to play ___ it.", "with", "into", "on", "in", "D"),
        ("We are looking forward to ___ you next week.", "see", "seeing", "saw", "seen", "B"),
        ("Neither the books nor the pen ___ on the table.", "is", "are", "have", "were", "A"),
    ]
    for q in grammar_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': grammar.id})

    # ===== OLD ENGLISH: ADVANCED GRAMMAR (30 questions) =====
    advanced_items = [
        ("Were he more considerate, he ___ have acted that way.", "wouldn't", "shouldn't", "won't", "might", "A"),
        ("He talked about the incident as though he ___ there.", "was", "has been", "had been", "will be", "C"),
        ("Scarcely had he left the room ___ the fight started.", "than", "when", "but", "that", "B"),
        ("No sooner had she stepped out ___ the visitors arrived.", "than", "when", "that", "but", "A"),
        ("If only he ___ earlier, he would have been on time.", "leaves", "left", "had left", "would have left", "C"),
        ("It is imperative that she ___ the deadline.", "meets", "met", "meet", "meeting", "C"),
        ("He behaved as if nothing ___ happened.", "have", "had", "has", "was", "B"),
        ("The teacher demanded that every student ___ quiet.", "be", "is", "should be", "must be", "A"),
        ("Neither the chairman nor his assistants ___ present at the meeting.", "was", "were", "has been", "is", "B"),
        ("The boy would not have failed if he ___ his teacher's advice.", "has taken", "had taken", "took", "would take", "B"),
        ("Such behaviour is not only unacceptable but also ___.", "condemned", "condemnable", "condemning", "to condemn", "B"),
        ("Her argument was lucid and ___ enough to win the debate.", "cogent", "coherent", "confusing", "cohesive", "A"),
        ("The company is known for its ___ treatment of staff.", "benevolent", "malevolent", "lenient", "negligent", "A"),
        ("Had the doctor arrived earlier, the patient ___.", "might survive", "might have survived", "could survive", "will have survived", "B"),
        ("The lawyer argued his point with such ___ that the jury was convinced.", "vehemence", "vengeance", "violence", "validity", "A"),
        ("I wish I ___ your advice last year.", "took", "had taken", "have taken", "take", "B"),
        ("Had he known the rules, he ___ have made that mistake.", "wouldn't", "won't", "shouldn't", "would", "A"),
        ("The workers insisted that the management ___ their salaries.", "increase", "increases", "increased", "must increase", "A"),
        ("If it were not for her pride, she ___ apologized.", "will have", "would have", "must have", "has", "B"),
        ("The Vice Chancellor, accompanied by his aides, ___ addressing the press.", "are", "is", "were", "be", "B"),
        ("His explanation was not only unconvincing but also ___.", "verbose", "redundant", "repetitive", "contradictory", "D"),
        ("___ we proceed, let's review what we've covered.", "Before", "Until", "Unless", "Meanwhile", "A"),
        ("The film was so compelling that it held me ___.", "spellbound", "enchanted", "trapped", "attentive", "A"),
        ("She never misses an opportunity to ___ her wealth.", "flaunt", "flout", "display", "flourish", "A"),
        ("The government plans to ___ subsidies gradually.", "phase in", "phase out", "fade in", "pull out", "B"),
        ("The two parties finally came to a ___ after weeks of negotiation.", "concession", "conclusion", "compromise", "commitment", "C"),
        ("The activist was known for her ___ opposition to injustice.", "vehement", "violent", "vocal", "strong", "A"),
        ("His argument was filled with logical ___.", "flaws", "fails", "falls", "faults", "A"),
        ("The military seized power in a bloodless ___.", "coup", "coop", "siege", "regime", "A"),
        ("The teacher spoke so authoritatively ___ the entire class was silent.", "that", "which", "when", "as", "A"),
    ]
    for q in advanced_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': adv_grammar.id})
    # ===== OLD ENGLISH: VOCABULARY (30 questions) =====
    vocab_items = [
        ("The manager's response was rather inflammatory. 'Inflammatory' means:", "thoughtful", "insightful", "provoking", "calming", "C"),
        ("The senator's speech was filled with platitudes. 'Platitudes' means:", "wise sayings", "clichés", "jokes", "arguments", "B"),
        ("She has a penchant for classical music. 'Penchant' means:", "dislike", "distaste", "fondness", "phobia", "C"),
        ("The witness gave a lucid account. 'Lucid' means:", "confusing", "clear", "lengthy", "doubtful", "B"),
        ("His obnoxious behavior irritated everyone. 'Obnoxious' means:", "pleasant", "rude", "generous", "timid", "B"),
        ("Her actions were commendable. 'Commendable' means:", "deserving praise", "shameful", "confusing", "unnoticed", "A"),
        ("He was reluctant to take up the position. 'Reluctant' means:", "unwilling", "happy", "proud", "delighted", "A"),
        ("The criminal was found to be remorseless. 'Remorseless' means:", "ashamed", "regretful", "unapologetic", "confused", "C"),
        ("The president abdicated his responsibilities. 'Abdicated' means:", "accepted", "rejected", "took over", "resigned", "D"),
        ("Their efforts were futile. 'Futile' means:", "effective", "worthwhile", "useless", "important", "C"),
        ("The general led a covert operation. 'Covert' means:", "open", "secret", "hasty", "confused", "B"),
        ("He was meticulous in his research. 'Meticulous' means:", "careless", "thorough", "indifferent", "partial", "B"),
        ("She's known for her altruism. 'Altruism' means:", "selfishness", "generosity", "indifference", "arrogance", "B"),
        ("The idea was preposterous. 'Preposterous' means:", "logical", "sensible", "absurd", "factual", "C"),
        ("He showed tenacity in pursuing his goals. 'Tenacity' means:", "laziness", "hesitation", "determination", "weakness", "C"),
        ("Her explanation was specious. 'Specious' means:", "believable", "misleading", "simple", "true", "B"),
        ("The director's comment was acerbic. 'Acerbic' means:", "polite", "harsh", "helpful", "boring", "B"),
        ("The scholar is known for his erudition. 'Erudition' means:", "ignorance", "foolishness", "scholarship", "arrogance", "C"),
        ("He became belligerent when provoked. 'Belligerent' means:", "quiet", "aggressive", "sorrowful", "cautious", "B"),
        ("The general's speech was full of hyperbole. 'Hyperbole' means:", "modesty", "exaggeration", "falsehood", "facts", "B"),
        ("His dormant ambition was reawakened. 'Dormant' means:", "dead", "latent", "exposed", "intense", "B"),
        ("He was always gregarious. 'Gregarious' means:", "reserved", "sociable", "irritable", "mysterious", "B"),
        ("The artist's latest work is truly exquisite. 'Exquisite' means:", "ugly", "painful", "beautiful", "complex", "C"),
        ("The government made a tacit agreement. 'Tacit' means:", "secret", "silent", "open", "strong", "B"),
        ("He was caught red-handed.", "innocently", "by surprise", "in the act", "in disguise", "C"),
        ("He was adamant in his refusal. 'Adamant' means:", "unsure", "flexible", "unyielding", "rude", "C"),
        ("Her response was ambiguous. 'Ambiguous' means:", "unclear", "rude", "direct", "positive", "A"),
        ("The teacher's remarks were incisive. 'Incisive' means:", "vague", "sharp", "unnecessary", "slow", "B"),
        ("He was aloof at the gathering. 'Aloof' means:", "friendly", "warm", "distant", "attentive", "C"),
        ("The judge was known for his probity. 'Probity' means:", "dishonesty", "integrity", "kindness", "authority", "B"),
    ]
    for q in vocab_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': vocab.id})

    # ===== OLD ENGLISH: ORAL ENGLISH (30 questions) =====
    oral_items = [
        ("In which word is the vowel sound different? (seat, beat, sit, neat)", "seat", "beat", "sit", "neat", "C"),
        ("Choose the odd one: boot, root, foot, loot", "boot", "root", "foot", "loot", "C"),
        ("Different consonant sound: chew, chain, chart, chef", "chew", "chain", "chart", "chef", "D"),
        ("Which contains /ʌ/ sound? full, cut, pool, cool", "full", "cut", "pool", "cool", "B"),
        ("'th' pronounced /ð/ in: thing, thought, this, think", "thing", "thought", "this", "think", "C"),
        ("Odd initial sound: judge, jungle, genre, ginger", "judge", "jungle", "genre", "ginger", "C"),
        ("Contains diphthong /eɪ/: cat, said, pain, bed", "cat", "said", "pain", "bed", "C"),
        ("Same vowel as 'hat': car, heart, cup, bat", "car", "heart", "cup", "bat", "D"),
        ("Word with plosive consonant: fan, bag, ship, zoo", "fan", "bag", "ship", "zoo", "B"),
        ("Final sound in 'judge': /tʃ/, /dʒ/, /ʒ/, /d/", "/tʃ/", "/dʒ/", "/ʒ/", "/d/", "B"),
        ("Word with /ɔ:/ sound: hot, sort, hut, cat", "hot", "sort", "hut", "cat", "B"),
        ("/ʃ/ present in: pleasure, mission, genre, vision", "pleasure", "mission", "genre", "vision", "B"),
        ("Consonant in 'photo': /p/, /f/, /v/, /θ/", "/p/", "/f/", "/v/", "/θ/", "B"),
        ("/əʊ/ diphthong: caught, boat, bet, box", "caught", "boat", "bet", "box", "B"),
        ("'sure' begins with: /ʃ/, /s/, /z/, /ʒ/", "/ʃ/", "/s/", "/z/", "/ʒ/", "A"),
        ("Stressed syllable in 'education': first, second, third, fourth", "first", "second", "third", "fourth", "C"),
        ("Stress on second syllable: CONtract, conTRACT, REcord, PREsent", "CONtract", "conTRACT", "REcord", "PREsent", "B"),
        ("Stress in 'photograph': first, second, third, none", "first", "second", "third", "none", "A"),
        ("WH-question intonation usually: rises, falls, flat, rises then falls", "rises", "falls", "flat", "rises then falls", "B"),
        ("'Are you coming?' ends with: falling, rising, level, high", "falling", "rising", "level", "high", "B"),
        ("Primary stress on first syllable: apply, produce (verb), record (noun), permit (verb)", "apply", "produce (verb)", "record (noun)", "permit (verb)", "C"),
        ("Stress in 'presentation': first, second, third, fourth", "first", "second", "third", "fourth", "C"),
        ("Rising intonation common in: commands, statements, yes/no questions, exclamations", "commands", "statements", "yes/no questions", "exclamations", "C"),
        ("Stress in 'understand': first, second, third, all equal", "first", "second", "third", "all equal", "C"),
        ("Stress in 'economy': first, second, third, fourth", "first", "second", "third", "fourth", "B"),
        ("Falling intonation example: 'Is he there?', 'Come in.', 'Are you okay?', 'Will she come?'", "Is he there?", "Come in.", "Are you okay?", "Will she come?", "B"),
        ("Stress pattern for 'democracy': DEM-o-cracy, de-MO-cracy, de-mo-CRA-cy, dem-o-CRA-cy", "DEM-o-cracy", "de-MO-cracy", "de-mo-CRA-cy", "dem-o-CRA-cy", "B"),
        ("Intonation in a list rises on each item except: last, first, second, all", "last", "first", "second", "all", "A"),
        ("Sentence stress highlights: articles, auxiliary verbs, content words, pronouns", "articles", "auxiliary verbs", "content words", "pronouns", "C"),
        ("Rising intonation typical: 'I love it.', 'What are you doing?', 'Can I help you?', 'They left early.'", "I love it.", "What are you doing?", "Can I help you?", "They left early.", "C"),
    ]
    for q in oral_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': oral.id})

    # ===== OLD ENGLISH: PHRASAL VERBS (30 questions) =====
    pv_items = [
        ("She came ___ a rare antique while cleaning the attic.", "upon", "about", "to", "across", "A"),
        ("We need to get ___ this obstacle to succeed.", "through", "across", "over", "around", "C"),
        ("The thieves made ___ with a large sum of money.", "away", "off", "out", "up", "A"),
        ("He finally gave ___ to the pressure and resigned.", "out", "up", "away", "in", "D"),
        ("I couldn't make ___ what he was saying due to the noise.", "off", "over", "out", "up", "C"),
        ("We'll have to put ___ the meeting till next week.", "out", "off", "down", "aside", "B"),
        ("She was brought ___ by her grandmother.", "up", "off", "on", "to", "A"),
        ("He's really taken ___ his new role as team leader.", "on", "to", "in", "up", "A"),
        ("The company had to cut ___ on spending due to losses.", "up", "out", "back", "off", "C"),
        ("The project fell ___ due to lack of funding.", "down", "apart", "away", "through", "B"),
        ("The child burst ___ crying.", "into", "out", "in", "off", "A"),
        ("I need to look ___ this word in the dictionary.", "at", "into", "for", "up", "D"),
        ("We must carry ___ with our plans despite the delay.", "through", "out", "on", "away", "C"),
        ("They were held ___ by heavy traffic.", "up", "out", "in", "back", "A"),
        ("She tried to bring ___ a change in the system.", "up", "in", "about", "on", "C"),
        ("He was completely taken ___ by the news.", "off", "aback", "aside", "down", "B"),
        ("The scandal will surely blow ___ soon.", "over", "up", "off", "by", "A"),
        ("I need to brush ___ on my French before the trip.", "in", "up", "out", "off", "B"),
        ("The plane took ___ an hour late.", "away", "off", "out", "up", "B"),
        ("He turned ___ the offer because it was too risky.", "off", "around", "down", "out", "C"),
        ("She was completely worn ___ after the long shift.", "in", "down", "up", "out", "D"),
        ("You must stick ___ the rules.", "at", "with", "to", "on", "C"),
        ("He always looks ___ his younger brother.", "after", "for", "to", "out", "A"),
        ("We finally ran ___ of petrol.", "up", "down", "off", "out", "D"),
        ("He tried to pass ___ the fake watch as genuine.", "out", "off", "over", "in", "B"),
        ("The committee called ___ the strike after negotiations.", "off", "in", "back", "up", "A"),
        ("You should back ___ from this conflict.", "off", "out", "down", "away", "A"),
        ("I don't know how she puts ___ with his behavior.", "on", "out", "up", "over", "C"),
        ("The rumor turned ___ to be false.", "down", "out", "over", "in", "B"),
        ("Let me go ___ the document one more time.", "off", "through", "in", "back", "B"),
    ]
    for q in pv_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': phrasal.id})

    # ===== OLD ENGLISH: ANALOGIES (30 questions) =====
    analogy_items = [
        ("Ephemeral : Transient :: Permanent : ?", "Deliberate", "Enduring", "Changing", "Temporary", "B"),
        ("Obsolete : Modern :: Archaic : ?", "Ancient", "Futuristic", "Antique", "Contemporary", "D"),
        ("Ornithologist : Birds :: Herpetologist : ?", "Mammals", "Reptiles", "Insects", "Fishes", "B"),
        ("Symphony : Composer :: Theorem : ?", "Engineer", "Mathematician", "Scientist", "Philosopher", "B"),
        ("Allegory : Story :: Satire : ?", "Mockery", "Humor", "Irony", "Critique", "D"),
        ("Germinate : Seed :: Hatch : ?", "Bird", "Nest", "Egg", "Chick", "C"),
        ("Enervate : Strength :: Obscure : ?", "Light", "Darkness", "Clarity", "Ambiguity", "C"),
        ("Anarchy : Order :: Chaos : ?", "Revolution", "Structure", "Peace", "System", "D"),
        ("Quintessence : Essence :: Apex : ?", "Zenith", "Base", "Bottom", "Low", "A"),
        ("Sculptor : Statue :: Architect : ?", "Builder", "Design", "House", "Blueprint", "C"),
        ("Dogma : Doctrine :: Hypothesis : ?", "Conclusion", "Proof", "Theory", "Assumption", "C"),
        ("Equivocate : Mislead :: Elaborate : ?", "Simplify", "Explain", "Confuse", "Extend", "B"),
        ("Manuscript : Author :: Score : ?", "Singer", "Musician", "Composer", "Dancer", "C"),
        ("Cacophony : Sound :: Muddle : ?", "Sight", "Order", "Confusion", "Logic", "C"),
        ("Philanthropist : Generosity :: Misogynist : ?", "Woman", "Hatred", "Chauvinism", "Contempt", "D"),
        ("Capitulate : Resist :: Succumb : ?", "Confront", "Yield", "Withstand", "Obey", "C"),
        ("Debacle : Failure :: Windfall : ?", "Success", "Loss", "Gain", "Disaster", "C"),
        ("Predator : Prey :: Capitalist : ?", "Consumer", "Socialist", "Market", "Profit", "A"),
        ("Cipher : Code :: Puzzle : ?", "Mystery", "Riddle", "Solution", "Game", "B"),
        ("Lexicon : Words :: Anthology : ?", "Books", "Stories", "Poems", "Works", "C"),
        ("Acumen : Insight :: Lethargy : ?", "Laziness", "Fatigue", "Alertness", "Energy", "A"),
        ("Nocturnal : Bat :: Diurnal : ?", "Moon", "Human", "Owl", "Snake", "B"),
        ("Macabre : Death :: Risqué : ?", "Comedy", "Indecency", "Mystery", "Caution", "B"),
        ("Eulogy : Praise :: Lampoon : ?", "Abuse", "Humor", "Ridicule", "Exaggeration", "C"),
        ("Conundrum : Riddle :: Paradigm : ?", "Standard", "Puzzle", "Paradox", "Problem", "A"),
        ("Prophecy : Predict :: Diagnosis : ?", "Treat", "Cure", "Determine", "Identify", "D"),
        ("Articulate : Speak :: Agile : ?", "Leap", "Run", "Move", "Jump", "C"),
        ("Gluttony : Food :: Avarice : ?", "Power", "Wealth", "Ambition", "Authority", "B"),
        ("Tyrant : Autocracy :: Voter : ?", "Democracy", "Majority", "Government", "President", "A"),
        ("Catalyst : Reaction :: Key : ?", "Lock", "Door", "Security", "Entry", "D"),
    ]
    for q in analogy_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': analogies_topic.id})

    # ===== NEW ENGLISH: SENTENCE STRUCTURE (30 questions) =====
    struct_qs = [
        ("Identify the sentence type: 'Although she was tired, she finished her homework.'", "Simple", "Compound", "Complex", "Compound-complex", "C", "One independent + one dependent clause"),
        ("Which of the following is a compound sentence?", "The boy who came late was punished.", "She ran fast and won the race.", "After the rain stopped, we went out.", "I like rice, but my brother prefers yam.", "D", "Two independent clauses joined by 'but'"),
        ("'The man that I saw yesterday is my uncle.' The underlined clause is:", "Noun clause", "Adjective clause", "Adverb clause", "Main clause", "B", "Modifies 'the man'"),
        ("Which sentence contains a noun clause?", "He asked where the book was.", "The house which was built in 1990 collapsed.", "She arrived after the show had started.", "Running quickly, he escaped.", "A", "'where the book was' acts as object"),
        ("'Had I known, I would have come earlier.' The sentence expresses:", "A real condition", "A future possibility", "An unreal past condition", "A command", "C", "Inverted form of 'If I had known'"),
        ("Identify the subordinate clause: 'The student who studies hard will succeed.'", "The student", "who studies hard", "will succeed", "The student will succeed", "B", "Relative clause modifying 'the student'"),
        ("Which sentence is grammatically incorrect because of faulty subordination?", "Because he was late, so he missed the bus.", "Although he was tired, he kept working.", "She left after the movie ended.", "If you study, you will pass.", "A", "Cannot use both 'because' and 'so'"),
        ("'The more you practice, the better you become.' This is an example of:", "Parallel structure", "Comparative correlative", "Ellipsis", "Anaphora", "B", "Correlative construction"),
        ("Choose the sentence with correct parallel structure:", "She likes dancing, to sing, and jogging.", "He is smart, hardworking, and shows kindness.", "The teacher asked us to read, write, and solve problems.", "I enjoy swimming, to run, and bike.", "C", "All infinitives parallel"),
        ("Which sentence uses an appositive correctly?", "My brother a doctor lives abroad.", "My brother, a doctor, lives abroad.", "My brother a doctor, lives abroad.", "My brother lives abroad a doctor.", "B", "Appositive set off by commas"),
        ("Identify the independent clause: 'If you heat ice, it melts.'", "If you heat ice", "it melts", "you heat ice", "If you heat ice, it melts", "B", "Main clause that can stand alone"),
        ("'I will come provided that you invite me.' The underlined phrase expresses:", "Condition", "Cause", "Concession", "Purpose", "A", "'provided that' introduces a condition"),
        ("Which sentence contains a dangling modifier?", "Running down the street, the bus left me.", "While running down the street, I missed the bus.", "I missed the bus because I was running.", "Running down the street made me miss the bus.", "A", "Modifier illogically modifies 'the bus'"),
        ("'What he said was quite surprising.' The subject is:", "What he said", "was", "quite surprising", "he", "A", "Noun clause as subject"),
        ("Identify the sentence pattern: 'The committee elected him chairman.'", "SVO", "SVOC", "SVOO", "SVC", "B", "Subject + Verb + Object + Object Complement"),
        ("'No sooner had he arrived than the fight started.' This structure shows:", "Comparison", "Immediate succession", "Cause-effect", "Concession", "B", "One event happens immediately after another"),
        ("Choose the correct sentence:", "The reason why he failed is because he didn't study.", "The reason why he failed is that he didn't study.", "The reason why he failed is due to he didn't study.", "The reason he failed is because of not studying.", "B", "After 'reason' use 'that' not 'because'"),
        ("'She is the girl whose father is a doctor.' 'Whose' indicates:", "Possession", "Person", "Thing", "Place", "A", "'Whose' shows ownership"),
        ("Which sentence uses a cleft sentence for emphasis?", "It was John that broke the vase.", "John broke the vase yesterday.", "Did John break the vase?", "Breaking the vase was John.", "A", "It-cleft: It was X that Y"),
        ("'The house needs painting.' The verb 'needs' is followed by a:", "Gerund", "Past participle", "Infinitive", "Bare infinitive", "A", "Need + gerund"),
        ("Identify the adverbial clause: 'He spoke as if he were the owner.'", "He spoke", "as if he were the owner", "the owner", "He spoke as if", "B", "Clause of manner"),
        ("Which sentence is a run-on?", "I love rice it is my favourite food.", "I love rice, it is my favourite food.", "I love rice; it is my favourite food.", "I love rice because it is my favourite food.", "A", "Two independent clauses without punctuation"),
        ("'To live in a big city is my dream.' The infinitive phrase functions as:", "Subject", "Object", "Complement", "Adverbial", "A", "Infinitive phrase is the subject"),
        ("Choose the sentence with correct subjunctive mood:", "I suggest that he goes to the doctor.", "I suggest that he go to the doctor.", "I suggest that he went to the doctor.", "I suggest that he is going to the doctor.", "B", "Subjunctive: base form 'go'"),
        ("'Were she here, she would help us.' This implies:", "She is here", "She is not here", "She may come", "She helped us", "B", "Unreal present condition"),
        ("Identify the type of 'that' clause: 'I believe that he is honest.'", "Noun clause (object)", "Adjective clause", "Adverb clause", "Relative clause", "A", "That-clause as object of 'believe'"),
        ("Which sentence contains an absolute phrase?", "The test being over, the students left.", "The students left after the test.", "Because the test was over, the students left.", "The test ended, so the students left.", "A", "Noun + participle not grammatically attached"),
        ("'That she succeeded surprised nobody.' The grammatical function is:", "Subject", "Direct object", "Subject complement", "Object of preposition", "A", "Noun clause as subject"),
        ("Which sentence has a misplaced modifier?", "I only eat vegetables on Mondays.", "She almost drove her children to school every day.", "He nearly lost all his money.", "They quickly finished the food.", "B", "'almost' misplaced"),
        ("'Both the teacher and the students ___ present.' Choose the correct verb.", "was", "is", "were", "has", "C", "Both...and takes plural verb"),
    ]
    for q in struct_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': structure_topic.id})

    # ===== NEW ENGLISH: VERB TENSES (25 questions) =====
    tense_qs = [
        ("She ___ her homework before dinner last night.", "has finished", "had finished", "finished", "was finishing", "B", "Past perfect for action before another past action"),
        ("By next year, I ___ my degree.", "will complete", "complete", "will have completed", "am completing", "C", "Future perfect"),
        ("He ___ in Lagos since 2010.", "lived", "has lived", "was living", "had lived", "B", "Present perfect with 'since'"),
        ("When I arrived, the meeting ___ already ___.", "has / begun", "had / begun", "was / begun", "did / begin", "B", "Past perfect"),
        ("The baby ___ for two hours when the mother finally woke up.", "cried", "had been crying", "has been crying", "was crying", "B", "Past perfect continuous"),
        ("Choose the correct sequence: 'If I ___ you, I ___ apologize.'", "am / will", "were / would", "was / would", "had been / would have", "B", "Unreal present condition"),
        ("She ___ to music every morning when I call her.", "listens", "listened", "is listening", "has listened", "A", "Simple present for habitual action"),
        ("They ___ the match because of rain when we arrived.", "cancelled", "had cancelled", "were cancelling", "have cancelled", "B", "Past perfect"),
        ("Next week at this time, we ___ in the air to London.", "will fly", "will be flying", "are flying", "fly", "B", "Future continuous"),
        ("The soup ___ good. I think I'll have another bowl.", "tastes", "is tasting", "tasted", "has tasted", "A", "Stative verb in simple present"),
        ("She ___ on this project for months before it was approved.", "worked", "had been working", "has worked", "was working", "B", "Past perfect continuous"),
        ("I ___ never ___ to Abuja before my last trip.", "have / been", "had / been", "did / go", "was / going", "B", "Past perfect"),
        ("By 2030, the population ___ by 20%.", "will increase", "will have increased", "is increasing", "increases", "B", "Future perfect"),
        ("He ___ as a teacher for five years now.", "worked", "has been working", "is working", "works", "B", "Present perfect continuous"),
        ("When she saw the mess, she ___ furious.", "got", "has got", "had got", "was getting", "A", "Simple past"),
        ("I ___ to call you yesterday, but I forgot.", "intended", "had intended", "was intending", "have intended", "B", "Past perfect for unfulfilled intention"),
        ("The train ___ at 6 PM tomorrow.", "leaves", "will leave", "is leaving", "is going to leave", "A", "Simple present for scheduled future"),
        ("She ___ to the party if she had been invited.", "would come", "would have come", "will come", "came", "B", "Past unreal condition"),
        ("I ___ a strange noise while I ___ dinner.", "heard / was preparing", "was hearing / prepared", "heard / prepared", "have heard / prepare", "A", "Simple past interrupting past continuous"),
        ("Up to now, nobody ___ the missing child.", "found", "has found", "had found", "finds", "B", "Present perfect with 'up to now'"),
        ("He is always ___ late. I'm tired of it.", "coming", "come", "comes", "came", "A", "'always' + present continuous for annoyance"),
        ("The concert ___ before we ___ the venue.", "started / reached", "had started / reached", "has started / reached", "was starting / reached", "B", "Past perfect + simple past"),
        ("I promise I ___ you as soon as I arrive.", "will call", "call", "am calling", "would call", "A", "Future simple"),
        ("She ___ her leg while she ___.", "broke / was skiing", "was breaking / skied", "broke / skied", "had broken / skied", "A", "Simple past interrupting past continuous"),
        ("We ___ for an hour before the bus arrived.", "waited", "had been waiting", "have waited", "were waiting", "B", "Past perfect continuous"),
    ]
    for q in tense_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': tense_topic.id})

    # ===== NEW ENGLISH: AGREEMENT & CONCORD (25 questions) =====
    agree_qs = [
        ("Either the boys or the girl ___ to blame.", "are", "is", "were", "have", "B", "Verb agrees with nearer subject (girl → singular)"),
        ("The team ___ playing well in their last match.", "was", "were", "are", "have", "B", "Collective noun as individuals"),
        ("Each of the students ___ a textbook.", "have", "has", "are having", "were", "B", "'Each' takes singular verb"),
        ("Neither the manager nor his assistants ___ present.", "was", "were", "is", "has", "B", "Nearer subject 'assistants' (plural)"),
        ("The news ___ shocking.", "are", "were", "is", "have", "C", "'News' is singular uncountable"),
        ("Mathematics ___ my favourite subject.", "are", "were", "is", "have", "C", "Subject names are singular"),
        ("A number of students ___ absent today.", "was", "is", "are", "has", "C", "'A number of' + plural noun + plural verb"),
        ("The number of applicants ___ increased.", "have", "has", "are", "were", "B", "'The number of' + singular verb"),
        ("Not only the students but also the teacher ___ present.", "were", "are", "was", "have", "C", "Nearer subject 'teacher' (singular)"),
        ("Every man, woman, and child ___ given a gift.", "were", "are", "was", "have", "C", "Compound subjects with 'every' take singular verb"),
        ("One of the boys ___ to be elected.", "are hoping", "hope", "hopes", "were hoping", "C", "Subject is 'one' (singular)"),
        ("The politician, along with his aides, ___ coming now.", "are", "were", "is", "have", "C", "'along with' doesn't affect verb number"),
        ("Half of the cake ___ eaten.", "were", "are", "was", "have", "C", "'Half of' + singular noun → singular verb"),
        ("Half of the apples ___ rotten.", "was", "is", "were", "has", "C", "'Half of' + plural noun → plural verb"),
        ("The jury ___ divided in their opinions.", "was", "is", "were", "has", "C", "Members as individuals → plural verb"),
        ("Physics ___ a difficult subject for many.", "are", "were", "is", "have", "C", "Subject names are singular"),
        ("There ___ several reasons for the delay.", "is", "was", "are", "has", "C", "Existential 'there' + plural noun → plural verb"),
        ("Neither of the answers ___ correct.", "are", "were", "is", "have", "C", "'Neither of' + singular verb (formal)"),
        ("The committee ___ issued its report.", "have", "are", "has", "were", "C", "Collective noun as a unit → singular"),
        ("Bread and butter ___ my favourite breakfast.", "are", "were", "is", "have", "C", "Compound seen as one concept → singular"),
        ("He is one of those people who ___ always late.", "is", "are", "was", "has", "B", "'who' refers to 'people' (plural)"),
        ("The singer and actor ___ arrived.", "have", "are", "is", "has", "D", "One person with two roles → singular"),
        ("The singer and the actor ___ arrived.", "has", "is", "have", "was", "C", "Two different persons → plural"),
        ("Either you or he ___ to do the work.", "have", "are", "is", "was", "C", "Nearer subject 'he' (singular)"),
        ("All of the furniture ___ been sold.", "have", "are", "were", "has", "D", "'Furniture' is uncountable → singular"),
    ]
    for q in agree_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': agreement_topic.id})

    # ===== NEW ENGLISH: CONNECTORS (25 questions) =====
    conn_qs = [
        ("He worked hard; ____, he failed the exam.", "therefore", "nevertheless", "consequently", "moreover", "B", "Contrast"),
        ("____ the rain, we went out.", "Despite", "Because of", "Although", "Due to", "A", "Despite + noun phrase"),
        ("She will succeed ____ she works hard.", "unless", "provided that", "whereas", "otherwise", "B", "Condition"),
        ("He is very rich; ____, he is not happy.", "therefore", "however", "moreover", "consequently", "B", "Contrastive connector"),
        ("____ it was late, we decided to continue.", "Because", "Even though", "Since", "As", "B", "Concession"),
        ("You must finish your homework ____ you cannot go out.", "otherwise", "so that", "therefore", "because", "A", "Otherwise = if not"),
        ("He studied hard ____ he could pass the exam.", "so that", "in order to", "because", "although", "A", "Purpose"),
        ("____ he is young, he is very responsible.", "Despite", "Although", "Because", "As", "B", "Concession"),
        ("The project was successful ____ many challenges.", "despite", "although", "because of", "due to", "A", "Despite + noun phrase"),
        ("I was tired, ____ I went to bed early.", "however", "therefore", "moreover", "nevertheless", "B", "Cause-effect"),
        ("____ the increase in price, demand has not fallen.", "Because of", "Due to", "In spite of", "As a result of", "C", "Contrast"),
        ("He is intelligent; ____, he lacks experience.", "consequently", "therefore", "on the other hand", "so", "C", "Contrasting qualities"),
        ("We left early ____ we would avoid traffic.", "so that", "because", "although", "unless", "A", "Purpose clause"),
        ("____ you apologize, I will not forgive you.", "If", "Unless", "Provided", "When", "B", "Unless = if not"),
        ("She was late ____ the traffic jam.", "because of", "due to the fact that", "owing to", "all of the above", "D", "All express cause"),
        ("He works hard; his brother, ____, is lazy.", "therefore", "consequently", "on the contrary", "moreover", "C", "Contrast between two persons"),
        ("____ the doctor's advice, he continued smoking.", "Despite", "Although", "Even though", "Because of", "A", "Despite + noun phrase"),
        ("He didn't study; ____, he failed.", "however", "moreover", "consequently", "nevertheless", "C", "Cause-effect result"),
        ("____ the weather was bad, we enjoyed the trip.", "Because", "Although", "Since", "As", "B", "Concession"),
        ("She is both intelligent ____ hardworking.", "and", "but", "or", "so", "A", "Correlative 'both...and'"),
        ("He speaks not only English ____ French.", "but also", "and also", "as well as", "also", "A", "Correlative 'not only...but also'"),
        ("It was very cold, ____ we lit a fire.", "so", "but", "or", "for", "A", "Result"),
        ("We must hurry; ____, we'll miss the train.", "otherwise", "therefore", "consequently", "so", "A", "Otherwise = if not"),
        ("He is poor ____ happy.", "but", "so", "for", "and", "A", "Contrast"),
        ("____ he arrived, the meeting started.", "No sooner had", "Hardly had", "As soon as", "All of the above", "D", "All indicate immediate sequence"),
    ]
    for q in conn_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': connectors_topic.id})

    # ===== NEW ENGLISH: MEANING & PARAPHRASE (30 questions) =====
    meaning_qs = [
        ("Choose the option that best explains: 'He is the black sheep of the family.'", "He has dark skin", "He is the most successful", "He is a disgrace to the family", "He is the eldest", "C", "Idiom: a person who brings shame"),
        ("'The manager turned a deaf ear to our complaints.' This means:", "He ignored the complaints", "He listened carefully", "He became angry", "He referred to someone else", "A", "Pretended not to hear"),
        ("Which sentence has the same meaning as: 'Only John passed the test.'", "John passed and so did others.", "Everyone passed except John.", "No one passed except John.", "John was the only one who failed.", "C", "'Only John' means John alone passed"),
        ("Paraphrase: 'He gave up the ghost.'", "He died", "He saw a ghost", "He surrendered", "He gave a speech", "A", "Idiom meaning to die"),
        ("'You cannot eat your cake and have it.' This means:", "You should enjoy life", "You cannot have two incompatible things", "Cake is perishable", "Sharing is caring", "B", "Cannot use a resource and still retain it"),
        ("Choose the sentence that means the same as: 'She is too weak to walk.'", "She is so weak that she cannot walk.", "She is very weak but she can walk.", "She is weak enough to walk.", "She is not weak enough to walk.", "A", "'Too...to' expresses impossibility"),
        ("'I have had enough of your excuses.' Means:", "I want more excuses", "I am tired of your excuses", "Your excuses are valid", "I accept your excuses", "B", "No longer willing to tolerate"),
        ("'He is a man of straw.' Means he is:", "Very tall", "Weak and unreliable", "Made of straw", "A farmer", "B", "Idiom: no substance"),
        ("Which sentence best paraphrases 'He seldom visits us'?", "He visits us often", "He never visits us", "He rarely visits us", "He visits us regularly", "C", "Seldom = rarely"),
        ("'All that glitters is not gold.' Means:", "Everything shiny is valuable", "Some things that look valuable are not", "Gold shines", "Don't trust your eyes", "B", "Appearances can be deceptive"),
        ("'She broke down in tears.' This means:", "She destroyed something", "She started crying suddenly", "She stopped crying", "She fell down", "B", "Lost emotional control"),
        ("'He is at sixes and sevens.' Means he is:", "Confused", "Happy", "Angry", "Aged", "A", "Idiom: in a state of disorder"),
        ("Paraphrase: 'He came out with flying colours.'", "He failed badly", "He was very successful", "He used many colours", "He painted", "B", "Idiom: great success"),
        ("'I can't make head or tail of this letter.' Means:", "I cannot read it", "I cannot understand it at all", "The letter has no head or tail", "The letter is torn", "B", "Cannot understand anything"),
        ("'She let the cat out of the bag.' Means:", "She set an animal free", "She revealed a secret", "She was cruel to animals", "She closed a bag", "B", "Disclosed a secret"),
        ("'He put his foot in his mouth.' Means:", "He ate quickly", "He said something embarrassing", "He injured himself", "He was silent", "B", "Said something foolish"),
        ("'The car broke down on the highway.' Means:", "The car exploded", "The car stopped functioning", "The car was broken into", "The car was speeding", "B", "Stop working"),
        ("'She is as cool as a cucumber.' Means she is:", "Cold", "Very calm", "Slimy", "Green", "B", "Simile: very composed"),
        ("Paraphrase: 'His failure is a bolt from the blue.'", "It was expected", "It was a complete surprise", "It was caused by lightning", "It was minor", "B", "Sudden unexpected event"),
        ("'He kicked the bucket.' Means:", "He started a new job", "He died", "He played football", "He broke a bucket", "B", "Slang for die"),
        ("'She has a heart of gold.' Means she is:", "Rich", "Kind", "Precious", "Cold", "B", "Very generous and kind"),
        ("'His argument is full of hot air.' Means:", "He is angry", "His argument is empty/meaningless", "He is using hot air balloons", "He is persuasive", "B", "Empty talk"),
        ("'She left him in the lurch.' Means:", "She helped him", "She abandoned him in difficulty", "She pushed him", "She married him", "B", "Desert someone in trouble"),
        ("'The teacher gave the students a piece of her mind.' Means:", "She taught a lesson", "She scolded them severely", "She shared her thoughts kindly", "She gave them a test", "B", "Express anger or criticism"),
        ("'He is sitting on the fence.' Means:", "He is undecided", "He is resting", "He is high up", "He is neutral", "A", "Avoid taking sides"),
        ("'The CEO called the meeting off.' Means:", "He started the meeting", "He cancelled the meeting", "He postponed the meeting", "He attended the meeting", "B", "Phrasal verb: cancel"),
        ("'I will look into the matter.' Means:", "I will ignore it", "I will investigate it", "I will watch it", "I will forget it", "B", "Phrasal verb: investigate"),
        ("'He bit off more than he could chew.' Means:", "He ate too much", "He took on more than he could handle", "He choked on food", "He was greedy", "B", "Took on too much"),
        ("'She burned the midnight oil.' Means:", "She was careless", "She worked late into the night", "She started a fire", "She wasted oil", "B", "Worked very late"),
        ("'He turned over a new leaf.' Means:", "He read a book", "He changed for the better", "He gardened", "He turned a page", "B", "Reformed oneself"),
    ]
    for q in meaning_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': meaning_topic.id})

    # ===== NEW ENGLISH: AMBIGUITY (20 questions) =====
    ambig_qs = [
        ("'Flying planes can be dangerous.' This sentence is ambiguous because:", "It lacks a subject", "It could mean planes that fly are dangerous OR the act of flying planes is dangerous", "The verb is wrong tense", "It contains passive voice", "B", "Structural ambiguity"),
        ("'I saw the man with the telescope.' Which interpretation is possible?", "I used a telescope to see the man", "The man had a telescope", "Both A and B", "None", "C", "Ambiguous attachment"),
        ("'The chicken is ready to eat.' This can mean:", "The chicken is hungry", "The chicken is cooked", "Both A and B", "Neither", "C", "Semantic ambiguity"),
        ("'Visiting relatives can be boring.' What are the two meanings?", "Relatives who visit are boring / The act of visiting relatives is boring", "Relatives travel a lot / Relatives are boring", "Only one meaning", "Relatives are boring to visit", "A", "Gerund vs participle ambiguity"),
        ("'I shot the elephant in my pyjamas.' The ambiguity arises from:", "The elephant wearing pyjamas", "The speaker wearing pyjamas while shooting", "Both interpretations", "The verb 'shot'", "C", "Modifier attachment"),
        ("'John saw his father driving a Mercedes.' Who is driving?", "John is driving", "His father is driving", "It's ambiguous", "Neither", "C", "Ambiguous: 'driving' could modify John or father"),
        ("'The police stopped the man with a gun.' This is ambiguous because:", "The man had a gun", "The police used a gun", "Both meanings possible", "None", "C", "Prepositional phrase attachment"),
        ("'They are cooking apples.' This could mean:", "They are cooking some apples", "The apples are used for cooking", "Both A and B", "Only A", "C", "Verb phrase vs compound noun"),
        ("'The German teacher' is ambiguous because:", "Teacher from Germany", "Teacher of German language", "Both", "Neither", "C", "Ambiguous modifier"),
        ("'He looked at the man with one eye.' Interpretations:", "The man has one eye", "He used one eye to look", "Both", "Neither", "C", "Attachment ambiguity"),
        ("'I left the car in the garage that was broken.' What is ambiguous?", "The car was broken", "The garage was broken", "Both possible", "The verb 'left'", "C", "Relative clause attachment"),
        ("'The student said the teacher is stupid on Monday.' Which is ambiguous?", "When the student spoke", "When the teacher was stupid", "Both", "Neither", "C", "Adverbial 'on Monday' attachment"),
        ("'I saw her duck.' Interpretations:", "I saw her lower her head", "I saw a duck belonging to her", "Both", "Only one", "C", "Lexical ambiguity"),
        ("'The shooting of the hunters was terrible.' Ambiguity:", "Hunters were shot", "Hunters did the shooting", "Both", "Neither", "C", "Active or passive structural ambiguity"),
        ("'He hit the man with a stick.' Means:", "He used a stick to hit the man", "The man had a stick", "Both", "Only A", "C", "Classic prepositional ambiguity"),
        ("'Time flies like an arrow.' Is ambiguous because:", "It has no subject", "Multiple grammatical parses are possible", "The tense is wrong", "The comparison is false", "B", "Can be parsed multiple ways"),
        ("'She told her sister she had won.' What is ambiguous?", "Who won", "Who was told", "Both", "Neither", "A", "Pronoun reference ambiguity"),
        ("'I didn't say he stole the money.' The ambiguity involves:", "The word 'money'", "Stress on different words changes meaning", "The tense", "The subject", "B", "Each stressed word shifts meaning"),
        ("'Beautiful girls and boys attended.' What is ambiguous?", "Whether 'beautiful' modifies both nouns", "The gender of attendees", "Both", "Neither", "A", "Scope of adjective modification"),
        ("'He saw the man on the hill with a telescope.' How many ambiguities?", "One", "Two", "Three", "None", "C", "Who had telescope, who was on hill, what saw"),
    ]
    for q in ambig_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': ambiguity_topic.id})

    # ===== NEW ENGLISH: WORD ORDER & INVERSION (25 questions) =====
    wordorder_qs = [
        ("Correct the word order: 'Never I have seen such a sight.'", "Never have I seen such a sight.", "Never I have seen such a sight.", "Never seen I have such a sight.", "Never have seen I such a sight.", "A", "Inversion after negative adverbs"),
        ("Choose the correct inverted sentence:", "Only after the show did he leave.", "Only after the show he left.", "Only after the show left he.", "Only after the show he did leave.", "A", "'Only after' + clause triggers inversion"),
        ("'Hardly had I arrived when the meeting started.' This means:", "I arrived long before the meeting", "The meeting started immediately after I arrived", "I arrived after the meeting", "The meeting started before I arrived", "B", "Inversion showing immediate sequence"),
        ("Which sentence has correct inversion after 'so'?", "So beautiful was the girl that everyone stared.", "So beautiful the girl was that everyone stared.", "So was the girl beautiful that everyone stared.", "So beautiful was that the girl everyone stared.", "A", "'So + adjective' triggers inversion"),
        ("'Little did they know the truth.' Normal word order:", "They little knew the truth.", "They did little know the truth.", "Little they knew the truth.", "They knew the truth little.", "A", "Normal order: subject + adverb + verb"),
        ("Choose the correct inversion after 'Not only':", "Not only did he steal, but he also lied.", "Not only he stole, but he also lied.", "Not only stole he, but he also lied.", "Not only he did steal, but also he lied.", "A", "Auxiliary 'did' before subject"),
        ("'Under no circumstances ___ you tell anyone.'", "should", "shouldn't", "will", "would", "A", "Inversion: Under no circumstances should you"),
        ("Correct: 'Seldom we have seen such talent.'", "Seldom have we seen such talent.", "Seldom we have seen such talent.", "Seldom we see such talent.", "Seldom saw we such talent.", "A", "Inversion with 'seldom'"),
        ("'No sooner ___ than the fight started.'", "he arrived", "did he arrive", "arrived he", "he did arrive", "B", "Inversion: No sooner did he arrive"),
        ("'Only by working hard ___ succeed.'", "you will", "will you", "you can", "can you", "B", "Inversion: Only by... will you succeed"),
        ("'Were I rich, I would travel the world.' This means:", "I am rich", "I am not rich", "I will be rich", "I was rich", "B", "Unreal present condition"),
        ("Which sentence is correct?", "Had he known, he would have apologized.", "He had known, he would have apologized.", "Had known he, he would have apologized.", "Had he know, he would have apologized.", "A", "Inversion in past unreal condition"),
        ("'So loudly did he shout that everyone heard.' Normal order:", "He shouted so loudly that everyone heard.", "He did shout so loudly that everyone heard.", "So loudly he shouted that everyone heard.", "He so loudly shouted that everyone heard.", "A", "Standard SV order"),
        ("'In no way ___ this be tolerated.'", "should", "shouldn't", "will not", "does", "A", "Inversion: In no way should this be tolerated"),
        ("Choose the correct inverted sentence:", "Never before have I seen such beauty.", "Never before I have seen such beauty.", "Never before I saw such beauty.", "Never before have seen I such beauty.", "A", "Inversion with 'never before'"),
        ("'Only then ___ the truth.'", "he realized", "did he realize", "realized he", "he did realize", "B", "Inversion after 'only then'"),
        ("'Had they arrived earlier, they ___ the bus.'", "would have caught", "will catch", "caught", "would catch", "A", "Inverted conditional: past unreal"),
        ("'Not once ___ during the meeting.'", "he spoke", "did he speak", "spoke he", "he did speak", "B", "Inversion with 'not once'"),
        ("'Should you need any help, call me.' This expresses:", "A real future condition", "An unreal condition", "A past condition", "A command", "A", "Inversion of 'If you should need'"),
        ("Which sentence has incorrect word order?", "Never have I met such a kind person.", "Rarely does he come on time.", "Only after the game began did he arrive.", "Only after the game began he arrived.", "D", "Missing inversion after 'only after'"),
        ("'At no time ___ the door unlocked.'", "she left", "did she leave", "left she", "she did leave", "B", "Inversion with 'at no time'"),
        ("'No sooner had the bell rung than the students ran out.' The meaning:", "The bell rang after the students ran out", "The students ran out immediately after the bell rang", "Simultaneous", "Students ran out before the bell", "B", "No sooner...than = immediate succession"),
        ("'Little ___ that he was being watched.'", "he knew", "did he know", "knew he", "he did know", "B", "Inversion with 'little'"),
        ("'Such was her beauty that everyone admired her.' The structure emphasizes:", "Her beauty was great", "Everyone admired her", "Both", "Neither", "A", "Inversion to highlight degree"),
        ("Choose the sentence with fronting for emphasis:", "It was the money that he wanted.", "He wanted the money badly.", "The money, he wanted desperately.", "What he wanted was money.", "C", "Topicalization/fronting"),
    ]
    for q in wordorder_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': wordorder_topic.id})

    # ===== NEW ENGLISH: SEMANTIC ROLES (20 questions) =====
    semantic_qs = [
        ("In 'John broke the window', the semantic role of 'John' is:", "Patient", "Agent", "Theme", "Experiencer", "B", "John performs the action → Agent"),
        ("In 'The window broke', the role of 'the window' is:", "Agent", "Patient", "Instrument", "Location", "B", "Undergoes change → Patient"),
        ("'The key opened the door.' The key is:", "Agent", "Instrument", "Patient", "Experiencer", "B", "Means by which action is done → Instrument"),
        ("In 'Mary felt a sharp pain', Mary is:", "Agent", "Patient", "Experiencer", "Theme", "C", "Experiences sensation → Experiencer"),
        ("'He gave his friend a book.' The role of 'a book' is:", "Recipient", "Theme", "Agent", "Goal", "B", "Entity transferred → Theme"),
        ("'She received a gift.' The role of 'she' is:", "Agent", "Patient", "Recipient", "Experiencer", "C", "One who receives → Recipient"),
        ("In 'The stone hit the window', the stone is:", "Agent", "Instrument", "Theme", "Patient", "B", "Used to hit → Instrument"),
        ("'I heard a strange noise.' The role of 'I' is:", "Agent", "Experiencer", "Patient", "Theme", "B", "Perception verb → Experiencer"),
        ("'The hammer broke the glass.' The hammer is:", "Agent", "Instrument", "Patient", "Force", "B", "Tool → Instrument"),
        ("In 'The soup tastes salty', the soup is:", "Theme", "Experiencer", "Agent", "Attribute", "A", "Entity with property → Theme"),
        ("'He sold the car to his brother.' The brother is:", "Recipient", "Goal", "Beneficiary", "All of the above", "D", "Goal/Recipient of transfer"),
        ("'The letter was written by Mary.' Mary is:", "Agent", "Patient", "Instrument", "Theme", "A", "By-phrase indicates Agent"),
        ("'The explosion shattered the windows.' The windows are:", "Agent", "Patient", "Instrument", "Location", "B", "Undergo effect → Patient"),
        ("'She baked a cake for him.' 'Him' is:", "Recipient", "Beneficiary", "Goal", "All of the above", "D", "Beneficiary/Recipient"),
        ("'The train arrived late.' The train is:", "Agent", "Theme", "Patient", "Instrument", "B", "Entity that moves → Theme"),
        ("'He stained the table with ink.' The ink is:", "Instrument", "Material", "Agent", "Patient", "A", "Means → Instrument"),
        ("'The boy threw the ball.' The ball is:", "Theme", "Patient", "Both A and B", "Instrument", "C", "Ball is affected/moved → Theme/Patient"),
        ("In 'He benefited from the scholarship', the scholarship is:", "Source", "Instrument", "Agent", "Theme", "A", "Source of benefit"),
        ("'The wall collapsed.' The role of 'the wall' is:", "Agent", "Patient", "Theme", "Experiencer", "C", "Undergoes change of state → Theme"),
        ("'She put the book on the table.' 'On the table' is:", "Theme", "Goal", "Source", "Instrument", "B", "Destination of movement → Goal"),
    ]
    for q in semantic_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': semantic_topic.id})

    # ===== INSERT ALL ENGLISH QUESTIONS =====
    for i, q in enumerate(all_english):
        question = Question(
            exam_id=exam.id,
            topic_id=q['topic'],
            question_text=q['text'],
            question_type='multiple_choice',
            subject='English',
            option_a=q['a'], option_b=q['b'], option_c=q['c'], option_d=q['d'],
            correct_answer=q['ans'],
            explanation=q.get('exp', f"The correct answer is {q['ans']}."),
            marks=1,
            question_order=i + 1
        )
        db.session.add(question)

    db.session.commit()
    print(f"✅ Seeded {len(all_english)} English questions.")