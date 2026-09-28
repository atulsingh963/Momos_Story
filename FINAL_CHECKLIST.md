# FINAL QA CHECKLIST — MOMOS STORY PRODUCTION FOUNDATION

- [x] **Flask Application:** Starts cleanly without warnings or errors (`python app.py`).
- [x] **Homepage Rendering (`/`):** All 10 visual sections render properly with semantic HTML5 tags.
- [x] **API Endpoints:**
  - `GET /api/menu?category=veg` returns correct filtered list.
  - `GET /api/builder?filling=paneer&style=kurkure` returns matched product recommendation.
- [x] **Dynamic Filtering:** Client-side category (`veg`, `paneer`, `chicken`) and style (`steamed`, `fried`, `kurkure`, `tandoori`, `special`) filters operate without page reloads.
- [x] **Interactive Momo Builder:** Updates matched item details, pricing, pieces, and generates WhatsApp order deep-links.
- [x] **Error Handling:** Custom `404.html` and `500.html` error templates render matching brand aesthetics.
- [x] **Navigation:** Sticky glassmorphism header, active link scroll-spy, and mobile hamburger menu with scroll locking.
- [x] **Animations:** GSAP & ScrollTrigger timelines, subtle hero vertical floating, realistic CSS steam streams, mouse parallax (desktop), process progress line, and signature horizontal pinned scroll track.
- [x] **Accessibility:** Reduced motion (`prefers-reduced-motion`) support, keyboard focus outlines (`:focus-visible`), and alt text fallbacks.
- [x] **SEO Foundation:** Open Graph tags, viewport meta tags, semantic heading hierarchy, and JSON-LD `FastFoodRestaurant` structured data.
- [x] **Centralized Architecture:** All business settings (`data/business.py`) and product catalog details (`data/menu.py`) are decoupled from HTML templates.
- [x] **Image Fallback:** Graceful `onerror` fallback handling for missing images.
