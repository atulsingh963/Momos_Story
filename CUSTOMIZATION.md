# MOMOS STORY — Client Customization Guide

This document explains how to substitute fictional/demo branding, photography, menu offerings, pricing, and contact details with real client information.

---

## 📍 1. Brand & Business Configuration

All global business information is located in:

```text
data/business.py
```

To update business details, edit the `BUSINESS` dictionary:

```python
BUSINESS = {
    "name": "YOUR BRAND NAME",
    "short_name": "YOUR BRAND",
    "tagline": "Your Brand Tagline",
    "phone": "+91 XXXXXXXXXX",
    "whatsapp": "91XXXXXXXXXX",
    "email": "contact@yourdomain.com",
    "address": "Street Address, City, State",
    "hours": "11:00 AM – 11:00 PM",
    "social": {
        "instagram": "https://instagram.com/your_handle",
        "facebook": "https://facebook.com/your_page"
    }
}
```

---

## 🥟 2. Menu Products, Categories & Pricing

All menu products and categories are configured in:

```text
data/menu.py
```

### Adding or Editing Products

Edit the `MENU` list in `data/menu.py`:

```python
{
    "id": "unique-product-id",
    "name": "Product Name",
    "category": "veg",        # Options: 'veg', 'paneer', 'chicken'
    "style": "steamed",        # Options: 'steamed', 'fried', 'kurkure', 'tandoori', 'special'
    "price": 120,              # Price in ₹
    "pieces": 8,               # Number of pieces
    "badge": "BESTSELLER",     # Badge text (or "" if none)
    "description": "Item description text.",
    "image": "/static/images/products/your-image.jpg"
}
```

> **Note:** The backend automatically validates that `category` and `style` keys strictly conform to valid options.

---

## 📷 3. Food & Brand Photography

Directory structure for assets:

```text
static/
└── images/
    ├── brand/         # Logo files (logo.svg, logo.png)
    ├── hero/          # Main hero visuals
    └── products/      # Food photography (1:1 aspect ratio recommended)
```

### Recommended Image Ratios & Formats
- **Product Cards:** `1:1` aspect ratio (e.g., 600×600px, WebP, JPG, or SVG)
- **Category Cards:** `4:3` or `1:1` aspect ratio
- **Hero Visual:** `1:1` transparent background PNG/SVG or high-res WebP

---

## 🎨 4. Website Colors & Theme

Theme variables are configured in:

```text
static/css/style.css
```

To change brand colors, edit the CSS root variables:

```css
:root {
  --color-primary: #B42318;      /* Deep Red */
  --color-accent: #F97316;       /* Orange Accent */
  --color-cream: #FFF7ED;        /* Warm Cream */
  --color-dark: #171717;         /* Dark Charcoal Background */
  --color-card-bg: #222222;     /* Card Background */
}
```

---

## ⚙️ 5. Client Customization Checklist

```text
[ ] Update data/business.py with real phone & WhatsApp number.
[ ] Update data/business.py with store address and hours.
[ ] Replace logo in static/images/brand/ if available.
[ ] Update products and prices in data/menu.py.
[ ] Upload real momo food photography to static/images/products/.
[ ] Replace sample reviews in data/menu.py with real customer reviews.
[ ] Test WhatsApp ordering CTA links.
[ ] Verify local server start using `python app.py`.
```
