import json
import os

COURSES_INDEX_PATH = os.path.join('data', 'courses_index.json')
COURSES_FOLDER_PATH = os.path.join('data', 'courses')


def get_all_courses():
    """Returns the list of all courses for the dashboard (id, name, icon, description)."""
    with open(COURSES_INDEX_PATH, 'r') as file:
        return json.load(file)


def get_course_by_id(course_id):
    """
    Returns the full data for one course, including its list of lessons.
    Used by the course_view page to list all lessons in that course.
    """
    course_file_path = os.path.join(COURSES_FOLDER_PATH, f'{course_id}.json')

    with open(course_file_path, 'r') as file:
        return json.load(file)


def get_lesson(course_id, lesson_id):
    """
    Returns a single lesson's full data, plus the correct previous/next lesson IDs
    so the lesson page can render working Previous/Next buttons.
    """
    course = get_course_by_id(course_id)
    lessons = course['lessons']

    # Find the index of the current lesson in the list
    current_index = None
    for index, lesson in enumerate(lessons):
        if lesson['id'] == lesson_id:
            current_index = index
            break

    if current_index is None:
        return None  # Lesson not found

    current_lesson = lessons[current_index]

    # Determine previous lesson id (None if this is the first lesson)
    previous_lesson_id = lessons[current_index - 1]['id'] if current_index > 0 else None

    # Determine next lesson id (None if this is the last lesson)
    next_lesson_id = lessons[current_index + 1]['id'] if current_index < len(lessons) - 1 else None

    return {
        'course_id': course_id,
        'lesson': current_lesson,
        'previous_lesson_id': previous_lesson_id,
        'next_lesson_id': next_lesson_id
    }