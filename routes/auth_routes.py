import uuid
from flask import (Blueprint, current_app, render_template, request,
                   redirect, url_for, session)
from services.access_code_service import (
    get_code_status,
    activate_code,
    release_code,
    get_active_session_for_code
)

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/access-verification', methods=['GET', 'POST'])
def access_verification():

    # ── Already logged in — go straight to dashboard ──
    if session.get('verified') and session.get('access_code'):
        code        = session['access_code']
        session_id  = session.get('session_id', '')
        stored_sid  = get_active_session_for_code(code)

        # Verify this is the same browser session
        if session_id and session_id == stored_sid:
            return redirect(url_for('dashboard.dashboard'))
        else:
            # Session mismatch — clear and ask to login again
            session.clear()

    error = None

    if request.method == 'POST':
        submitted_code = request.form.get('access_code', '').strip()
        status         = get_code_status(submitted_code)

        if status == 'not_found':
            error = ("Invalid access code. "
                     "Please check your code and try again.")

        elif status == 'in_use':
            error = ("This access code is currently in use. "
                     "If this is your code, please wait for "
                     "the other session to expire or contact support.")

        elif status == 'available':
            # Generate a unique session ID for this login
            new_session_id = str(uuid.uuid4())

            # Activate the code in JSON
            activate_code(submitted_code, new_session_id)

            # Store everything in Flask session
            session.permanent             = True
            session['verified']           = True
            session['access_code']        = submitted_code
            session['session_id']         = new_session_id
            session['session_version'] = current_app.config.get('SESSION_VERSION', 1)

            return redirect(url_for('dashboard.dashboard'))

    return render_template(
        'auth/access_verification.html',
        error=error
    )


@auth_bp.route('/logout')
def logout():
    # Release the code in JSON so others can use it
    code = session.get('access_code')
    if code:
        release_code(code)

    # Clear the Flask session completely
    session.clear()

    return redirect(url_for('public.home'))