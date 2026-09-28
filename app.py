import os
from flask import Flask, render_template, jsonify, request
from data.business import BUSINESS
from data.menu import CATEGORIES, STYLES, MENU, SIGNATURE_MOMOS, REVIEWS, HOW_IT_WORKS

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-momocraft-dev-key')

@app.context_processor
def inject_global_data():
    return {
        'business': BUSINESS
    }

@app.route('/')
def index():
    return render_template(
        'index.html',
        categories=CATEGORIES,
        styles=STYLES,
        menu=MENU,
        signature_momos=SIGNATURE_MOMOS,
        reviews=REVIEWS,
        how_it_works=HOW_IT_WORKS
    )

@app.route('/api/menu')
def api_menu():
    category = request.args.get('category', 'all').lower()
    style = request.args.get('style', 'all').lower()
    
    filtered = MENU
    if category != 'all':
        filtered = [item for item in filtered if item['category'] == category]
    if style != 'all':
        filtered = [item for item in filtered if item['style'] == style]
        
    return jsonify({
        'status': 'success',
        'count': len(filtered),
        'items': filtered
    })

@app.route('/api/builder')
def api_builder():
    filling = request.args.get('filling', 'veg').lower()
    style = request.args.get('style', 'steamed').lower()
    
    # Direct match search
    matched = next((item for item in MENU if item['category'] == filling and item['style'] == style), None)
    
    # Fallback to category item if exact style not available
    if not matched:
        matched = next((item for item in MENU if item['category'] == filling), None)
        
    if matched:
        return jsonify({
            'status': 'success',
            'found': True,
            'item': matched
        })
    else:
        return jsonify({
            'status': 'error',
            'found': False,
            'message': 'No matching momo found for this combination.'
        }), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() in ['true', '1', 't']
    app.run(host='127.0.0.1', port=5000, debug=debug_mode)
