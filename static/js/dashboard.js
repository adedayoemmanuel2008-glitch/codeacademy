/* =============================================
   DASHBOARD.JS — Dashboard Interactivity
   SEA TECH / Code Academy
============================================= */

document.addEventListener('DOMContentLoaded', function () {

    /* ──────────────────────────────────────────
       SCROLL ENTRANCE ANIMATIONS
       Fades in course cards as they enter view
    ────────────────────────────────────────── */
    const cards = document.querySelectorAll('.dashboard-course-card');

    cards.forEach(function (card) {
        card.classList.add('fade-up');
    });

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry, index) {
            if (entry.isIntersecting) {
                // Stagger each card's animation by 80ms
                setTimeout(function () {
                    entry.target.classList.add('visible');
                }, index * 80);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    cards.forEach(function (card) {
        observer.observe(card);
    });

});