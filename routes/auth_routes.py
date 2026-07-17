from flask import Blueprint, render_template, request, redirect, url_for, session
from services.access_code_service import is_valid_access_code

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/access-verification', methods=['GET', 'POST'])
def access_verification():

    # If already verified, skip the form and go straight to dashboard
    if session.get('verified'):
        return redirect(url_for('dashboard.dashboard'))

    error = None

    if request.method == 'POST':
        submitted_code = request.form.get('access_code', '').strip()

        if is_valid_access_code(submitted_code):
            session.permanent = True
            session['verified'] = True
            return redirect(url_for('dashboard.dashboard'))
        else:
            error = "Invalid access code. Please check your code and try again."

    return render_template('auth/access_verification.html', error=error)


@auth_bp.route('/logout')
def logout():
    session.pop('verified', None)
    return redirect(url_for('public.home'))