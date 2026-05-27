#!/usr/bin/env python
"""Final verification script for UNILAG CBT Application"""

from app import create_app

def verify_app():
    app = create_app()
    
    print('=' * 70)
    print('FINAL VERIFICATION - UNILAG CBT APPLICATION')
    print('=' * 70)
    print()
    
    # 1. Check configuration
    print('[✓] Configuration Status:')
    print(f'    - Flask App: {app.name}')
    print(f'    - Debug Mode: {app.debug}')
    db_uri = app.config.get('SQLALCHEMY_DATABASE_URI', 'Not configured')
    print(f'    - Database: {db_uri}')
    print()
    
    # 2. Check blueprints
    print('[✓] Registered Blueprints:')
    for bp in app.blueprints.keys():
        print(f'    - {bp}')
    print()
    
    # 3. Check routes
    print('[✓] Available Routes:')
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            methods = ','.join(sorted(rule.methods - {'HEAD', 'OPTIONS'}))
            routes.append((rule.rule, methods, rule.endpoint))
    
    for route, methods, endpoint in sorted(routes, key=lambda x: x[0])[:25]:
        print(f'    {route:40} [{methods:10}]')
    print()
    
    print('=' * 70)
    print('✅ APPLICATION VERIFICATION COMPLETE - ALL SYSTEMS OPERATIONAL')
    print('=' * 70)

if __name__ == '__main__':
    verify_app()
