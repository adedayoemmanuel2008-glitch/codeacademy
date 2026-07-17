/* =============================================
   LESSON.JS — Lesson Page Interactivity
   SEA TECH / Code Academy
============================================= */

document.addEventListener('DOMContentLoaded', function () {

    /* ──────────────────────────────────────────
       1. SCROLL TO TOP ON LOAD
       Ensures student always starts at the
       top of the lesson when navigating
    ────────────────────────────────────────── */
    window.scrollTo({ top: 0, behavior: 'smooth' });

    /* ──────────────────────────────────────────
       2. KEYBOARD NAVIGATION
       Left arrow key  → Previous Lesson
       Right arrow key → Next Lesson
       Only triggers when not typing in a field
    ────────────────────────────────────────── */
    const prevBtn = document.querySelector('.lesson-nav-left .btn');
    const nextBtn = document.querySelector('.lesson-nav-right .btn');

    document.addEventListener('keydown', function (e) {
        // Don't trigger if user is typing in an input or textarea
        if (document.activeElement.tagName === 'INPUT' ||
            document.activeElement.tagName === 'TEXTAREA') {
            return;
        }

        if (e.key === 'ArrowLeft' && prevBtn) {
            prevBtn.click();
        }

        if (e.key === 'ArrowRight' && nextBtn) {
            nextBtn.click();
        }
    });

    /* ──────────────────────────────────────────
       3. ACTIVE STATE ON ACTION BUTTONS
       Briefly highlights a button when clicked
       so student knows their click registered
    ────────────────────────────────────────── */
    const actionBtns = document.querySelectorAll('.lesson-action-btn');

    actionBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
            btn.style.opacity = '0.7';
            setTimeout(function () {
                btn.style.opacity = '1';
            }, 300);
        });
    });

});