from flask import Blueprint, render_template, session, redirect, url_for
from services.lesson_service import get_all_courses, get_course_by_id, get_lesson

# Blueprint for all protected learning pages
dashboard_bp = Blueprint('dashboard', __name__)


def verified_required(func):
    """
    Decorator that blocks access unless the student has a verified session.
    Redirects to the access verification page otherwise.
    """
    def wrapper(*args, **kwargs):
        if not session.get('verified'):
            return redirect(url_for('auth.access_verification'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


@dashboard_bp.route('/dashboard')
@verified_required
def dashboard():
    courses = get_all_courses()
    return render_template('dashboard/dashboard.html', courses=courses)


@dashboard_bp.route('/course/<course_id>')
@verified_required
def course_view(course_id):
    course = get_course_by_id(course_id)
    return render_template('dashboard/course_view.html', course=course)


@dashboard_bp.route('/lesson/<course_id>/<lesson_id>')
@verified_required
def lesson_view(course_id, lesson_id):
    lesson_data = get_lesson(course_id, lesson_id)
    return render_template('lessons/lesson_view.html', **lesson_data)