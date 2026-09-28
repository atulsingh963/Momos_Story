"""
MOMOS STORY - Business Information Configuration
Centralized configuration file for restaurant location, contact numbers, hours, and branding metadata.
"""

BUSINESS = {
    "name": "MOMOS STORY",
    "short_name": "MOMOS STORY",
    "tagline": "One Momo. Endless Cravings.",
    "description": "Handcrafted steamed, fried, Kurkure, and tandoori momos served hot with signature garlic chutney.",

    # Contact & Ordering Details
    "phone": "+91 7489824723",
    "phone_raw": "917489824723",
    "whatsapp": "917489824723",
    "email": "atulsingh962006@gmail.com",

    # Location & Address
    "address": "Bhopal, Madhya Pradesh, India",
    "city": "Bhopal",
    "state": "Madhya Pradesh",
    "country": "India",

    # Store Hours
    "hours": "11:00 AM – 11:00 PM",
    "opening_hours": {
        "monday": "11:00 AM - 11:00 PM",
        "tuesday": "11:00 AM - 11:00 PM",
        "wednesday": "11:00 AM - 11:00 PM",
        "thursday": "11:00 AM - 11:00 PM",
        "friday": "11:00 AM - 11:00 PM",
        "saturday": "11:00 AM - 11:00 PM",
        "sunday": "11:00 AM - 11:00 PM"
    },

    # Social Profiles
    "social": {
        "instagram": "https://instagram.com/momosstory_official",
        "facebook": "https://facebook.com/momosstory.official"
    },

    # Brand Assets
    "logo_text": "MOMOS STORY",
    "logo_img": "/static/images/brand/logo.svg"
}
