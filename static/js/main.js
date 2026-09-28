/**
 * MOMOCRAFT - Main Client-side Script & Animation Engine
 * GSAP + ScrollTrigger + Dynamic Filtering + Interactive Builder
 */

document.addEventListener('DOMContentLoaded', () => {
    // Register GSAP Plugin safely
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
    }

    initNavbar();
    initHeroAnimations();
    initMouseParallax();
    initRevealAnimations();
    initCategoryAnimations();
    initMenuFilters();
    initSignatureScroll();
    initProcessTimeline();
    initMomoBuilder();
    initStoryAnimations();
    initCTAAnimations();
    initCustomCursor();
    initScrollProgress();
    initSmoothScroll();
});

/* ==========================================================================
   1. NAVBAR & SCROLL BEHAVIOR
   ========================================================================== */
function initNavbar() {
    const header = document.querySelector('.header');
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const navLinksItems = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
        
        let current = '';
        const sections = document.querySelectorAll('section[id]');
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionHeight = section.offsetHeight;
            if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });

        navLinksItems.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('open');
            navLinks.classList.toggle('open');
            document.body.classList.toggle('no-scroll');
        });

        navLinksItems.forEach(item => {
            item.addEventListener('click', () => {
                hamburger.classList.remove('open');
                navLinks.classList.remove('open');
                document.body.classList.remove('no-scroll');
            });
        });
    }
}

/* ==========================================================================
   2. HERO ANIMATIONS (Cinematic Load & Floating Momo)
   ========================================================================== */
function initHeroAnimations() {
    if (typeof gsap === 'undefined') return;

    const tl = gsap.timeline({ defaults: { ease: 'power3.out', duration: 1 } });

    // Sequential Hero Reveal (Timing < 1.5s overall)
    tl.to('.hero-line', {
        y: '0%',
        opacity: 1,
        stagger: 0.15,
        duration: 0.8
    })
    .to('.hero-eyebrow', {
        y: 0,
        opacity: 1,
        duration: 0.5
    }, '-=0.6')
    .to('.hero-desc', {
        y: 0,
        opacity: 1,
        duration: 0.5
    }, '-=0.4')
    .to('.hero-btn', {
        y: 0,
        opacity: 1,
        stagger: 0.1,
        duration: 0.5
    }, '-=0.3')
    .from('.hero-image-wrapper', {
        scale: 0.85,
        opacity: 0,
        duration: 0.8
    }, '-=0.7');

    // Continuous Floating Vertical Momo Animation
    gsap.to('.hero-main-img', {
        y: -14,
        duration: 3.5,
        repeat: -1,
        yoyo: true,
        ease: 'power1.inOut'
    });

    // Hero Scroll Out Parallax Trigger
    if (typeof ScrollTrigger !== 'undefined') {
        gsap.to('.hero-visual', {
            scrollTrigger: {
                trigger: '#home',
                start: 'top top',
                end: 'bottom top',
                scrub: 0.5
            },
            y: 60,
            scale: 0.95,
            opacity: 0.6
        });
    }
}

/* ==========================================================================
   3. HERO MOUSE PARALLAX (Desktop only)
   ========================================================================== */
function initMouseParallax() {
    const heroVisual = document.querySelector('.hero-visual');
    if (!heroVisual || window.innerWidth < 1025) return;

    const layers = document.querySelectorAll('.parallax-layer');

    heroVisual.addEventListener('mousemove', (e) => {
        const rect = heroVisual.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;

        layers.forEach(layer => {
            const depth = parseFloat(layer.getAttribute('data-depth')) || 0.1;
            const moveX = x * depth;
            const moveY = y * depth;

            if (typeof gsap !== 'undefined') {
                gsap.to(layer, {
                    x: moveX,
                    y: moveY,
                    duration: 0.5,
                    ease: 'power2.out'
                });
            } else {
                layer.style.transform = `translate(${moveX}px, ${moveY}px)`;
            }
        });
    });

    heroVisual.addEventListener('mouseleave', () => {
        layers.forEach(layer => {
            if (typeof gsap !== 'undefined') {
                gsap.to(layer, { x: 0, y: 0, duration: 0.8, ease: 'power2.out' });
            } else {
                layer.style.transform = 'translate(0px, 0px)';
            }
        });
    });
}

/* ==========================================================================
   4. REUSABLE SECTION REVEAL SYSTEM (IntersectionObserver)
   ========================================================================== */
function initRevealAnimations() {
    const revealElements = document.querySelectorAll('[data-reveal]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => observer.observe(el));
}

/* ==========================================================================
   5. CATEGORY CARDS ANIMATION
   ========================================================================== */
function initCategoryAnimations() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.from('.category-card', {
        scrollTrigger: {
            trigger: '#categories',
            start: 'top 75%'
        },
        y: 40,
        opacity: 0,
        duration: 0.8,
        stagger: 0.15,
        ease: 'power2.out'
    });
}

/* ==========================================================================
   6. DYNAMIC MENU FILTERING WITH GSAP FADE/SCALE TRANSITION
   ========================================================================== */
function initMenuFilters() {
    const categoryBtns = document.querySelectorAll('.category-filter');
    const styleBtns = document.querySelectorAll('.style-filter');
    const productCards = document.querySelectorAll('.product-card');
    const emptyState = document.getElementById('empty-menu');

    let currentCategory = 'all';
    let currentStyle = 'all';

    function applyFilters() {
        let visibleCards = [];

        productCards.forEach(card => {
            const cardCategory = card.getAttribute('data-category');
            const cardStyle = card.getAttribute('data-style');

            const matchesCategory = (currentCategory === 'all' || cardCategory === currentCategory);
            const matchesStyle = (currentStyle === 'all' || cardStyle === currentStyle);

            if (matchesCategory && matchesStyle) {
                visibleCards.push(card);
            }
        });

        // GSAP transition sequence for card changes
        if (typeof gsap !== 'undefined') {
            gsap.to(productCards, {
                scale: 0.9,
                opacity: 0,
                duration: 0.25,
                onComplete: () => {
                    productCards.forEach(card => {
                        card.style.display = 'none';
                    });

                    visibleCards.forEach(card => {
                        card.style.display = 'flex';
                    });

                    if (emptyState) {
                        emptyState.style.display = visibleCards.length === 0 ? 'block' : 'none';
                    }

                    if (visibleCards.length > 0) {
                        gsap.to(visibleCards, {
                            scale: 1,
                            opacity: 1,
                            duration: 0.4,
                            stagger: 0.05,
                            ease: 'power2.out'
                        });
                    }

                    if (typeof ScrollTrigger !== 'undefined') {
                        ScrollTrigger.refresh();
                    }
                }
            });
        } else {
            productCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');
                const cardStyle = card.getAttribute('data-style');
                const matches = (currentCategory === 'all' || cardCategory === currentCategory) &&
                                (currentStyle === 'all' || cardStyle === currentStyle);
                card.style.display = matches ? 'flex' : 'none';
                card.style.opacity = matches ? '1' : '0';
            });
            if (emptyState) {
                emptyState.style.display = visibleCards.length === 0 ? 'block' : 'none';
            }
        }
    }

    categoryBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            categoryBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentCategory = btn.getAttribute('data-category');
            applyFilters();
        });
    });

    styleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            styleBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentStyle = btn.getAttribute('data-style');
            applyFilters();
        });
    });

    window.selectCategoryFilter = function(catId) {
        const targetBtn = document.querySelector(`.category-filter[data-category="${catId}"]`);
        if (targetBtn) {
            targetBtn.click();
            const menuSection = document.getElementById('menu');
            if (menuSection) {
                menuSection.scrollIntoView({ behavior: 'smooth' });
            }
        }
    };
}

/* ==========================================================================
   7. SIGNATURE MOMOS HORIZONTAL PINNED SCROLL (Desktop)
   ========================================================================== */
function initSignatureScroll() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;
    if (window.innerWidth < 1025) return;

    const track = document.getElementById('signature-track');
    const pinnedWrapper = document.querySelector('.signature-pinned-wrapper');

    if (!track || !pinnedWrapper) return;

    const getScrollAmount = () => -(track.scrollWidth - window.innerWidth + 120);

    gsap.to(track, {
        x: getScrollAmount,
        ease: 'none',
        scrollTrigger: {
            trigger: '#signature',
            pin: true,
            scrub: 1,
            end: () => `+=${track.scrollWidth}`,
            invalidateOnRefresh: true
        }
    });
}

/* ==========================================================================
   8. PROCESS TIMELINE SCROLL PROGRESS LINE
   ========================================================================== */
function initProcessTimeline() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    const lineFill = document.getElementById('process-line-fill');
    if (!lineFill) return;

    gsap.to(lineFill, {
        width: '100%',
        ease: 'none',
        scrollTrigger: {
            trigger: '.process-wrapper',
            start: 'top 70%',
            end: 'bottom 60%',
            scrub: 0.5
        }
    });
}

/* ==========================================================================
   9. INTERACTIVE MOMO BUILDER ANIMATIONS
   ========================================================================== */
function initMomoBuilder() {
    const fillingBtns = document.querySelectorAll('.builder-filling-opt');
    const styleBtns = document.querySelectorAll('.builder-style-opt');
    const resultCard = document.getElementById('builder-result-card');
    
    const resultTitle = document.getElementById('builder-item-title');
    const resultDesc = document.getElementById('builder-item-desc');
    const resultPrice = document.getElementById('builder-item-price');
    const resultPieces = document.getElementById('builder-item-pieces');
    const resultBadge = document.getElementById('builder-item-badge');
    const resultCta = document.getElementById('builder-order-btn');

    let selectedFilling = 'veg';
    let selectedStyle = 'steamed';

    function updateBuilderResult() {
        if (typeof gsap !== 'undefined' && resultCard) {
            gsap.to(resultCard, {
                scale: 0.95,
                opacity: 0.4,
                duration: 0.15,
                onComplete: fetchResult
            });
        } else {
            fetchResult();
        }

        function fetchResult() {
            fetch(`/api/builder?filling=${selectedFilling}&style=${selectedStyle}`)
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success' && data.item) {
                        const item = data.item;
                        if (resultTitle) resultTitle.textContent = item.name;
                        if (resultDesc) resultDesc.textContent = item.description;
                        if (resultPrice) resultPrice.textContent = `₹${item.price}`;
                        if (resultPieces) resultPieces.textContent = `${item.pieces} Pieces`;
                        if (resultBadge) {
                            resultBadge.textContent = item.badge || item.style.toUpperCase();
                        }
                        if (resultCta) {
                            const message = encodeURIComponent(`Hi MOMOS STORY! I'd like to order: ${item.name} (${item.pieces} Pcs - ₹${item.price}).`);
                            const rawPhone = document.body.getAttribute('data-whatsapp') || '919876543210';
                            resultCta.href = `https://wa.me/${rawPhone}?text=${message}`;
                        }

                        if (typeof gsap !== 'undefined' && resultCard) {
                            gsap.to(resultCard, {
                                scale: 1,
                                opacity: 1,
                                duration: 0.3,
                                ease: 'back.out(1.4)'
                            });
                        }
                    }
                })
                .catch(err => {
                    console.error('Error updating builder item:', err);
                });
        }
    }

    fillingBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            fillingBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            selectedFilling = btn.getAttribute('data-filling');
            updateBuilderResult();
        });
    });

    styleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            styleBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            selectedStyle = btn.getAttribute('data-style');
            updateBuilderResult();
        });
    });

    updateBuilderResult();
}

/* ==========================================================================
   10. BRAND STORY PARALLAX
   ========================================================================== */
function initStoryAnimations() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.to('.story-parallax-img', {
        scrollTrigger: {
            trigger: '#about',
            start: 'top bottom',
            end: 'bottom top',
            scrub: 1
        },
        y: -30,
        ease: 'none'
    });
}

/* ==========================================================================
   11. ORDER CTA TEXT REVEAL ANIMATION
   ========================================================================== */
function initCTAAnimations() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.from('.cta-line-left', {
        scrollTrigger: {
            trigger: '.cta-section',
            start: 'top 80%'
        },
        x: -50,
        opacity: 0,
        duration: 0.8,
        ease: 'power2.out'
    });

    gsap.from('.cta-line-right', {
        scrollTrigger: {
            trigger: '.cta-section',
            start: 'top 80%'
        },
        x: 50,
        opacity: 0,
        duration: 0.8,
        ease: 'power2.out'
    });
}

/* ==========================================================================
   12. CUSTOM FLOATING CURSOR
   ========================================================================== */
function initCustomCursor() {
    const cursor = document.getElementById('custom-cursor');
    if (!cursor || window.innerWidth < 1025) return;

    window.addEventListener('mousemove', (e) => {
        cursor.style.left = `${e.clientX}px`;
        cursor.style.top = `${e.clientY}px`;
    });

    const hoverables = document.querySelectorAll('a, button, .product-card, .category-card, .builder-opt-btn');
    hoverables.forEach(el => {
        el.addEventListener('mouseenter', () => cursor.classList.add('active'));
        el.addEventListener('mouseleave', () => cursor.classList.remove('active'));
    });
}

/* ==========================================================================
   13. TOP SCROLL PROGRESS INDICATOR
   ========================================================================== */
function initScrollProgress() {
    const progressBar = document.getElementById('scroll-progress');
    if (!progressBar) return;

    window.addEventListener('scroll', () => {
        const totalScroll = document.documentElement.scrollHeight - window.innerHeight;
        const currentScroll = window.scrollY;
        const scrollPercent = (currentScroll / totalScroll) * 100;
        progressBar.style.width = `${scrollPercent}%`;
    });
}

/* ==========================================================================
   14. SMOOTH SCROLL ANCHORS
   ========================================================================== */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}
