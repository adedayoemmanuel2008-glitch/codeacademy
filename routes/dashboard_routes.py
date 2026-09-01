from flask import (Blueprint, render_template, redirect,
                   url_for, session, current_app)
from services.lesson_service import get_all_courses, get_course_by_id, get_lesson
from services.access_code_service import (
    get_active_session_for_code,
    release_code
)

dashboard_bp = Blueprint('dashboard', __name__)


def verified_required(f):
    """
    Decorator that protects dashboard routes.
    Checks:
    1. Session has verified flag
    2. Session version matches current app version
    3. Session ID matches the one stored in JSON
    If any check fails — log out and redirect to access page.
    """
    from functools import wraps

    @wraps(f)
    def decorated_function(*args, **kwargs):

        # Check 1 — is user verified?
        if not session.get('verified'):
            return redirect(url_for('auth.access_verification'))

        # Check 2 — session version matches?
        current_version = current_app.config.get('SESSION_VERSION', 1)
        session_version = session.get('session_version', None)

        if session_version != current_version:
            # Version mismatch — force logout
            code = session.get('access_code')
            if code:
                release_code(code)
            session.clear()
            return redirect(url_for('auth.access_verification'))

        # Check 3 — session ID matches JSON?
        code       = session.get('access_code')
        session_id = session.get('session_id', '')

        if code and session_id:
            stored_sid = get_active_session_for_code(code)
            if stored_sid != session_id:
                # Someone else logged in with this code
                # or code was reset — force logout
                session.clear()
                return redirect(url_for('auth.access_verification'))

        return f(*args, **kwargs)

    return decorated_function


@dashboard_bp.route('/dashboard')
@verified_required
def dashboard():
    courses = get_all_courses()
    return render_template(
        'dashboard/dashboard.html',
        courses=courses
    )


@dashboard_bp.route('/course/<course_id>')
@verified_required
def course_view(course_id):
    course = get_course_by_id(course_id)
    if not course:
        return redirect(url_for('dashboard.dashboard'))
    return render_template(
        'dashboard/course_view.html',
        course=course
    )


@dashboard_bp.route('/lesson/<course_id>/<lesson_id>')
@verified_required
def lesson_view(course_id, lesson_id):
    result = get_lesson(course_id, lesson_id)
    if not result:
        return redirect(url_for('dashboard.course_view',
                                course_id=course_id))
    return render_template(
        'lessons/lesson_view.html',
        lesson=result['lesson'],
        course_id=course_id,
        previous_lesson_id=result['previous_lesson_id'],
        next_lesson_id=result['next_lesson_id']
    )