/* =============================================
   NAVBAR.JS — Navbar Interactivity
   SEA TECH / Code Academy
============================================= */

document.addEventListener('DOMContentLoaded', function () {

    /* ──────────────────────────────────────────
       1. ELEMENT REFERENCES
    ────────────────────────────────────────── */
    const navbar          = document.getElementById('navbar');
    const hamburgerBtn    = document.getElementById('hamburger-btn');
    const themeToggle     = document.getElementById('theme-toggle');
    const yearSpan        = document.getElementById('current-year');

    /* ──────────────────────────────────────────
       2. AUTO COPYRIGHT YEAR
       Fills the <span id="current-year"> in footer
    ────────────────────────────────────────── */
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    /* ──────────────────────────────────────────
       3. DARK MODE
       Reads saved preference from localStorage
       and applies it immediately on page load.
    ────────────────────────────────────────── */
    const savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);

    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        if (themeToggle) {
            themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
        }
        localStorage.setItem('theme', theme);
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
        });
    }

    /* ──────────────────────────────────────────
       4. SCROLL SHADOW EFFECT
       Adds .scrolled class to navbar when
       the page is scrolled down past 10px.
    ────────────────────────────────────────── */
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 10) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    /* ──────────────────────────────────────────
       5. HAMBURGER MENU TOGGLE
       Creates the mobile sidebar and overlay
       dynamically and wires up open/close logic.
    ────────────────────────────────────────── */
    if (hamburgerBtn) {

        // Create overlay element
        const overlay = document.createElement('div');
        overlay.classList.add('menu-overlay');
        document.body.appendChild(overlay);

        // Create mobile menu sidebar
        const mobileMenu = document.createElement('div');
        mobileMenu.classList.add('mobile-menu');
        mobileMenu.innerHTML = `
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
               <li><a href="https://tally.so/r/pb1RaP" target="_blank" rel="noopener">Register</a></li>
                <li><a href="/access-verification" class="navbar-cta">Start Learning</a></li>
            </ul>
        `;
        document.body.appendChild(mobileMenu);

        function openMenu() {
            mobileMenu.classList.add('open');
            overlay.classList.add('active');
            hamburgerBtn.classList.add('active');
            document.body.style.overflow = 'hidden'; // Prevent background scroll
        }

        function closeMenu() {
            mobileMenu.classList.remove('open');
            overlay.classList.remove('active');
            hamburgerBtn.classList.remove('active');
            document.body.style.overflow = '';
        }

        hamburgerBtn.addEventListener('click', function () {
            if (mobileMenu.classList.contains('open')) {
                closeMenu();
            } else {
                openMenu();
            }
        });

        // Close menu when overlay is clicked
        overlay.addEventListener('click', closeMenu);

        // Close menu when any mobile link is clicked
        mobileMenu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', closeMenu);
        });

        // Close menu on window resize if desktop width is reached
        window.addEventListener('resize', function () {
            if (window.innerWidth > 768) {
                closeMenu();
            }
        });
    }

    /* ──────────────────────────────────────────
       6. ACTIVE LINK HIGHLIGHTING
       Adds .active class to the nav link that
       matches the current page URL.
    ────────────────────────────────────────── */
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-links li a, .mobile-menu a');

    navLinks.forEach(function (link) {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

});