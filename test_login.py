#!/usr/bin/env python
"""Test login flow to identify errors"""

from app import create_app, db
from app.models import User
import traceback

app = create_app()

with app.test_client() as client:
    with app.app_context():
        # Clean up test user
        test_user = User.query.filter_by(username='logintest').first()
        if test_user:
            db.session.delete(test_user)
            db.session.commit()
        
        # Create test user
        user = User(username='logintest', email='logintest@test.com', full_name='Login Test')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
    
    # Test login
    print("Testing login flow...")
    try:
        resp = client.post('/login', data={
            'username': 'logintest',
            'password': 'password123'
        }, follow_redirects=True)
        
        print(f"Login response status: {resp.status_code}")
        
        # Check if dashboard is accessible
        print("\nTesting dashboard access...")
        resp2 = client.get('/dashboard')
        print(f"Dashboard response status: {resp2.status_code}")
        
        if resp2.status_code != 200:
            print(f"❌ Dashboard error detected (Status {resp2.status_code})")
            # Print error details
            if b'Traceback' in resp2.data:
                print("\n⚠️ Python Exception found:")
                lines = resp2.data.decode('utf-8', errors='ignore').split('\n')
                for line in lines:
                    if 'Error' in line or 'Exception' in line or 'Traceback' in line:
                        print(f"   {line}")
        else:
            print("✅ Dashboard accessible")
        
        # Try to access profile
        print("\nTesting profile access...")
        resp3 = client.get('/profile')
        print(f"Profile response status: {resp3.status_code}")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        traceback.print_exc()
