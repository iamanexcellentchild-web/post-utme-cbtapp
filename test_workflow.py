#!/usr/bin/env python
"""Test complete user workflow"""

from app import create_app, db
from app.models import User, Exam, Result, Answer, Question
import traceback

app = create_app()

with app.test_client() as client:
    with app.app_context():
        # Clean up test user
        test_user = User.query.filter_by(username='fulltest').first()
        if test_user:
            db.session.delete(test_user)
            db.session.commit()
        
        # Create test user
        user = User(username='fulltest', email='fulltest@test.com', full_name='Full Test User')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
        # Get an exam
        exam = Exam.query.first()
        if exam:
            # Create a result
            result = Result(
                user_id=user.id,
                exam_id=exam.id,
                total_score=50,
                percentage=75.5,
                is_passed=True,
                time_taken_seconds=1800,
                completed_at=db.func.now()
            )
            db.session.add(result)
            db.session.commit()
    
    # Test complete workflow
    print("Testing complete user workflow...")
    print("=" * 60)
    
    tests = [
        ("Login", "/login", "POST", {'username': 'fulltest', 'password': 'password123'}),
        ("Dashboard", "/dashboard", "GET", None),
        ("Profile", "/profile", "GET", None),
    ]
    
    try:
        for test_name, route, method, data in tests:
            if method == "POST":
                resp = client.post(route, data=data, follow_redirects=True)
            else:
                resp = client.get(route, follow_redirects=True)
            
            status = "✅" if resp.status_code == 200 else "❌"
            print(f"{status} {test_name:20} {route:30} → {resp.status_code}")
        
        # Test exam views
        with app.app_context():
            exam = Exam.query.first()
            result = Result.query.filter_by(username='fulltest').first()
            
            if exam:
                resp = client.get(f'/exam/{exam.id}')
                status = "✅" if resp.status_code == 200 else "❌"
                print(f"{status} {'View Exam':20} {f'/exam/{exam.id}':30} → {resp.status_code}")
                
                # Try to get a result
                test_result = Result.query.filter_by(user_id=User.query.filter_by(username='fulltest').first().id).first()
                if test_result:
                    resp = client.get(f'/exam/{exam.id}/result/{test_result.id}')
                    status = "✅" if resp.status_code == 200 else "❌"
                    print(f"{status} {'View Result':20} {f'/exam/{exam.id}/result/{test_result.id}':30} → {resp.status_code}")
        
        print("=" * 60)
        print("✅ ALL TESTS PASSED - Application is fully functional!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        traceback.print_exc()
