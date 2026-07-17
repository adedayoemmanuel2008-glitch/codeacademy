/* =============================================
   HOME.JS — Homepage Interactivity
   SEA TECH / Code Academy
============================================= */

document.addEventListener('DOMContentLoaded', function () {

    /* ──────────────────────────────────────────
       1. FAQ ACCORDION
       Only one question open at a time.
    ────────────────────────────────────────── */
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(function (item) {
        const question = item.querySelector('.faq-question');

        question.addEventListener('click', function () {
            const isOpen = item.classList.contains('open');

            // Close all open items first
            faqItems.forEach(function (otherItem) {
                otherItem.classList.remove('open');
            });

            // If it wasn't open, open it now
            if (!isOpen) {
                item.classList.add('open');
            }
        });
    });

    /* ──────────────────────────────────────────
       2. SCROLL ENTRANCE ANIMATIONS
       Adds .visible class when elements
       enter the viewport, triggering the
       fade-up animation defined in home.css
    ────────────────────────────────────────── */
    const fadeElements = document.querySelectorAll(
        '.feature-card, .course-preview-card, .step-card, .faq-item, .stat-item'
    );

    // Add fade-up class to all animatable elements
    fadeElements.forEach(function (el) {
        el.classList.add('fade-up');
    });

    // Create an IntersectionObserver to watch when elements enter viewport
    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Stop observing once visible — animation only plays once
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,      // Trigger when 10% of element is visible
        rootMargin: '0px 0px -40px 0px'  // Slight offset from bottom
    });

    fadeElements.forEach(function (el) {
        observer.observe(el);
    });

});