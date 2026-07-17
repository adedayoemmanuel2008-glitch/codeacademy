from flask import Blueprint, render_template

# Blueprint for all public-facing pages (no login/access code required)
public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def home():
    return render_template('public/index.html')

@public_bp.route('/about')
def about():
    return render_template('public/about.html')

@public_bp.route('/contact')
def contact():
    return render_template('public/contact.html')

@public_bp.route('/privacy-policy')
def privacy_policy():
    return render_template('public/privacy_policy.html')

@public_bp.route('/terms-conditions')
def terms_conditions():
    return render_template('public/terms_conditions.html')