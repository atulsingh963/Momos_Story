"""
MOMOS STORY - Product & Menu Repository
Contains categories, cooking styles, signature products, and product validation helpers.
"""

from data.business import BUSINESS

CATEGORIES = [
    {
        "id": "veg",
        "name": "VEG MOMOS",
        "badge": "VEGETARIAN",
        "description": "Fresh vegetables, herbs and signature seasoning wrapped in soft handmade dough.",
        "image": "/static/images/products/veg-steamed.svg",
        "varieties_count": 8
    },
    {
        "id": "paneer",
        "name": "PANEER MOMOS",
        "badge": "RICH & SAVOURY",
        "description": "Creamy paneer filling blended with Indian spices for a rich, satisfying bite.",
        "image": "/static/images/products/paneer-steamed.svg",
        "varieties_count": 9
    },
    {
        "id": "chicken",
        "name": "CHICKEN MOMOS",
        "badge": "JUICY & BOLD",
        "description": "Juicy chicken filling with bold seasoning, wrapped and cooked fresh.",
        "image": "/static/images/products/chicken-steamed.svg",
        "varieties_count": 10
    }
]

STYLES = [
    {"id": "all", "name": "ALL STYLES"},
    {"id": "steamed", "name": "STEAMED"},
    {"id": "fried", "name": "FRIED"},
    {"id": "kurkure", "name": "KURKURE"},
    {"id": "tandoori", "name": "TANDOORI"},
    {"id": "special", "name": "SPECIAL"}
]

MENU = [
    # --- VEG MOMOS (8 Items) ---
    {
        "id": "veg-steamed",
        "name": "Classic Veg Momos",
        "category": "veg",
        "style": "steamed",
        "price": 60,
        "pieces": 8,
        "badge": "CLASSIC",
        "description": "Fresh vegetable filling wrapped in soft handmade momo dough.",
        "image": "/static/images/products/veg-steamed.svg"
    },
    {
        "id": "veg-fried",
        "name": "Fried Veg Momos",
        "category": "veg",
        "style": "fried",
        "price": 70,
        "pieces": 8,
        "badge": "",
        "description": "Golden fried momos with a crisp outside and flavourful vegetable filling.",
        "image": "/static/images/products/veg-fried.svg"
    },
    {
        "id": "veg-spicy",
        "name": "Spicy Veg Momos",
        "category": "veg",
        "style": "steamed",
        "price": 70,
        "pieces": 8,
        "badge": "SPICY",
        "description": "Classic vegetable momos with an extra spicy seasoning.",
        "image": "/static/images/products/veg-steamed.svg"
    },
    {
        "id": "veg-peri-peri",
        "name": "Peri Peri Veg Momos",
        "category": "veg",
        "style": "fried",
        "price": 80,
        "pieces": 8,
        "badge": "FIERY",
        "description": "Crispy fried vegetable momos coated with bold peri peri seasoning.",
        "image": "/static/images/products/veg-fried.svg"
    },
    {
        "id": "veg-kurkure",
        "name": "Kurkure Veg Momos",
        "category": "veg",
        "style": "kurkure",
        "price": 90,
        "pieces": 8,
        "badge": "CRISPY",
        "description": "Extra-crispy coated momos with a crunchy golden shell.",
        "image": "/static/images/products/veg-kurkure.svg"
    },
    {
        "id": "veg-tandoori",
        "name": "Tandoori Veg Momos",
        "category": "veg",
        "style": "tandoori",
        "price": 100,
        "pieces": 8,
        "badge": "SMOKY",
        "description": "Smoky tandoori-style vegetable momos packed with bold spices.",
        "image": "/static/images/products/veg-tandoori.svg"
    },
    {
        "id": "veg-chilli-garlic",
        "name": "Chilli Garlic Veg Momos",
        "category": "veg",
        "style": "special",
        "price": 90,
        "pieces": 8,
        "badge": "CHILLI",
        "description": "Vegetable momos tossed with chilli and aromatic garlic flavours.",
        "image": "/static/images/products/veg-steamed.svg"
    },
    {
        "id": "veg-afghani",
        "name": "Afghani Veg Momos",
        "category": "veg",
        "style": "special",
        "price": 110,
        "pieces": 8,
        "badge": "CREAMY",
        "description": "Creamy, rich and mildly spiced vegetable momos.",
        "image": "/static/images/products/veg-steamed.svg"
    },

    # --- PANEER MOMOS (9 Items) ---
    {
        "id": "paneer-steamed",
        "name": "Classic Paneer Momos",
        "category": "paneer",
        "style": "steamed",
        "price": 80,
        "pieces": 8,
        "badge": "CLASSIC",
        "description": "Soft paneer filling seasoned with aromatic spices inside delicate momo wrappers.",
        "image": "/static/images/products/paneer-steamed.svg"
    },
    {
        "id": "paneer-fried",
        "name": "Fried Paneer Momos",
        "category": "paneer",
        "style": "fried",
        "price": 90,
        "pieces": 8,
        "badge": "",
        "description": "Crispy golden paneer momos with a rich and savoury filling.",
        "image": "/static/images/products/paneer-fried.svg"
    },
    {
        "id": "paneer-spicy",
        "name": "Spicy Paneer Momos",
        "category": "paneer",
        "style": "steamed",
        "price": 90,
        "pieces": 8,
        "badge": "SPICY",
        "description": "Paneer momos with an extra kick of chilli and spices.",
        "image": "/static/images/products/paneer-steamed.svg"
    },
    {
        "id": "paneer-peri-peri",
        "name": "Peri Peri Paneer Momos",
        "category": "paneer",
        "style": "fried",
        "price": 100,
        "pieces": 8,
        "badge": "FIERY",
        "description": "Crispy paneer momos finished with bold peri peri seasoning.",
        "image": "/static/images/products/paneer-fried.svg"
    },
    {
        "id": "paneer-kurkure",
        "name": "Kurkure Paneer Momos",
        "category": "paneer",
        "style": "kurkure",
        "price": 110,
        "pieces": 8,
        "badge": "CRISPY",
        "description": "Crunchy coated momos with a rich paneer centre.",
        "image": "/static/images/products/paneer-kurkure.svg"
    },
    {
        "id": "paneer-tandoori",
        "name": "Tandoori Paneer Momos",
        "category": "paneer",
        "style": "tandoori",
        "price": 120,
        "pieces": 8,
        "badge": "SMOKY",
        "description": "Smoky tandoori paneer momos with a spicy grilled finish.",
        "image": "/static/images/products/paneer-tandoori.svg"
    },
    {
        "id": "paneer-chilli",
        "name": "Chilli Paneer Momos",
        "category": "paneer",
        "style": "special",
        "price": 110,
        "pieces": 8,
        "badge": "INDO-CHINESE",
        "description": "Paneer momos with chilli-forward Indo-Chinese flavours.",
        "image": "/static/images/products/paneer-steamed.svg"
    },
    {
        "id": "paneer-cheese",
        "name": "Cheese Paneer Momos",
        "category": "paneer",
        "style": "special",
        "price": 120,
        "pieces": 8,
        "badge": "CHEESY",
        "description": "Paneer and cheese packed into soft, flavourful momos.",
        "image": "/static/images/products/paneer-steamed.svg"
    },
    {
        "id": "paneer-afghani",
        "name": "Afghani Paneer Momos",
        "category": "paneer",
        "style": "special",
        "price": 130,
        "pieces": 8,
        "badge": "CREAMY",
        "description": "Rich creamy paneer momos with a smooth Afghani-style coating.",
        "image": "/static/images/products/paneer-steamed.svg"
    },

    # --- CHICKEN MOMOS (10 Items) ---
    {
        "id": "chicken-steamed",
        "name": "Classic Chicken Momos",
        "category": "chicken",
        "style": "steamed",
        "price": 90,
        "pieces": 8,
        "badge": "CLASSIC",
        "description": "Juicy seasoned chicken filling wrapped in soft handmade dough.",
        "image": "/static/images/products/chicken-steamed.svg"
    },
    {
        "id": "chicken-fried",
        "name": "Fried Chicken Momos",
        "category": "chicken",
        "style": "fried",
        "price": 100,
        "pieces": 8,
        "badge": "",
        "description": "Crispy golden chicken momos with a juicy centre.",
        "image": "/static/images/products/chicken-fried.svg"
    },
    {
        "id": "chicken-spicy",
        "name": "Spicy Chicken Momos",
        "category": "chicken",
        "style": "steamed",
        "price": 100,
        "pieces": 8,
        "badge": "SPICY",
        "description": "Juicy chicken momos with bold chilli seasoning.",
        "image": "/static/images/products/chicken-steamed.svg"
    },
    {
        "id": "chicken-peri-peri",
        "name": "Peri Peri Chicken Momos",
        "category": "chicken",
        "style": "fried",
        "price": 110,
        "pieces": 8,
        "badge": "FIERY",
        "description": "Crispy chicken momos coated with fiery peri peri seasoning.",
        "image": "/static/images/products/chicken-fried.svg"
    },
    {
        "id": "chicken-kurkure",
        "name": "Kurkure Chicken Momos",
        "category": "chicken",
        "style": "kurkure",
        "price": 120,
        "pieces": 8,
        "badge": "CRISPY",
        "description": "Extra-crunchy coating surrounding juicy chicken filling.",
        "image": "/static/images/products/chicken-kurkure.svg"
    },
    {
        "id": "chicken-tandoori",
        "name": "Tandoori Chicken Momos",
        "category": "chicken",
        "style": "tandoori",
        "price": 130,
        "pieces": 8,
        "badge": "SMOKY",
        "description": "Smoky grilled chicken momos inspired by tandoori flavours.",
        "image": "/static/images/products/chicken-tandoori.svg"
    },
    {
        "id": "chicken-chilli",
        "name": "Chilli Chicken Momos",
        "category": "chicken",
        "style": "special",
        "price": 120,
        "pieces": 8,
        "badge": "HOT & SPICY",
        "description": "Chicken momos tossed with chilli-forward Indo-Chinese flavours.",
        "image": "/static/images/products/chicken-steamed.svg"
    },
    {
        "id": "chicken-cheese",
        "name": "Cheese Chicken Momos",
        "category": "chicken",
        "style": "special",
        "price": 130,
        "pieces": 8,
        "badge": "CHEESY",
        "description": "Juicy chicken and melted cheese packed into delicious momos.",
        "image": "/static/images/products/chicken-steamed.svg"
    },
    {
        "id": "chicken-afghani",
        "name": "Afghani Chicken Momos",
        "category": "chicken",
        "style": "special",
        "price": 140,
        "pieces": 8,
        "badge": "CREAMY",
        "description": "Rich, creamy chicken momos with a mild and indulgent flavour.",
        "image": "/static/images/products/chicken-steamed.svg"
    },
    {
        "id": "chicken-schezwan",
        "name": "Schezwan Chicken Momos",
        "category": "chicken",
        "style": "special",
        "price": 120,
        "pieces": 8,
        "badge": "SPICY",
        "description": "Chicken momos with a bold Schezwan-style spicy finish.",
        "image": "/static/images/products/chicken-steamed.svg"
    }
]

SIGNATURE_MOMOS = [
    {
        "id": "sig-kurkure",
        "name": "Kurkure Momos",
        "tagline": "The Ultimate Crunch",
        "category": "Veg / Paneer / Chicken",
        "description": "Coated in our secret crunchy batter and fried to golden perfection. Served with spicy garlic chutney.",
        "badge": "BESTSELLER",
        "image": "/static/images/products/chicken-kurkure.svg"
    },
    {
        "id": "sig-tandoori",
        "name": "Tandoori Momos",
        "tagline": "Charcoal Smoked & Marinated",
        "category": "Veg / Paneer / Chicken",
        "description": "Marinated in spicy hung curd and roasted over live charcoal for that authentic dhaba smoky flavour.",
        "badge": "CHEF'S SPECIAL",
        "image": "/static/images/products/paneer-tandoori.svg"
    },
    {
        "id": "sig-cheese",
        "name": "Cheese Burst Momos",
        "tagline": "Gooey & Indulgent",
        "category": "Paneer / Chicken",
        "description": "Stuffed with extra mozzarella and processed cheddar that melts into rich creaminess in every bite.",
        "badge": "MUST TRY",
        "image": "/static/images/products/paneer-steamed.svg"
    },
    {
        "id": "sig-peri-peri",
        "name": "Peri Peri Momos",
        "tagline": "Zesty & Fiery Spice",
        "category": "Veg / Paneer / Chicken",
        "description": "Tossed in African peri-peri chili dust for a tangy, spicy explosion that hits all the right spots.",
        "badge": "SPICY",
        "image": "/static/images/products/veg-fried.svg"
    },
    {
        "id": "sig-afghani",
        "name": "Afghani Momos",
        "tagline": "Silky Creamy Goodness",
        "category": "Veg / Paneer / Chicken",
        "description": "Drenched in rich cashew and cream marinade with mild aromatic spices for a royal experience.",
        "badge": "CREAMY",
        "image": "/static/images/products/veg-steamed.svg"
    },
    {
        "id": "sig-chilli-garlic",
        "name": "Chilli Garlic Momos",
        "tagline": "Indo-Chinese Flavor Bomb",
        "category": "Veg / Paneer / Chicken",
        "description": "Wok-tossed in dark soy sauce, crispy fried garlic, green chilies, and scallions.",
        "badge": "POPULAR",
        "image": "/static/images/products/chicken-steamed.svg"
    }
]

# DEMO CONTENT — REPLACE WITH REAL CUSTOMER REVIEWS
REVIEWS = [
    {
        "name": "Aarav",
        "rating": 5,
        "comment": "The Kurkure momos are insanely crispy. Definitely coming back for these.",
        "location": "Bhopal",
        "is_sample": True
    },
    {
        "name": "Riya",
        "rating": 5,
        "comment": "The paneer momos were fresh and packed with filling. Loved them.",
        "location": "Bhopal",
        "is_sample": True
    },
    {
        "name": "Rahul",
        "rating": 5,
        "comment": "Tandoori chicken momos have an amazing smoky flavour.",
        "location": "Bhopal",
        "is_sample": True
    }
]

HOW_IT_WORKS = [
    {
        "step": "01",
        "title": "FRESH FILLING",
        "description": "Prepared with carefully selected ingredients and balanced seasoning."
    },
    {
        "step": "02",
        "title": "HAND WRAPPED",
        "description": "Each momo is shaped to hold the filling and flavour inside."
    },
    {
        "step": "03",
        "title": "PERFECTLY COOKED",
        "description": "Steamed, fried, tandoori or crisped depending on your choice."
    },
    {
        "step": "04",
        "title": "SERVED HOT",
        "description": "Fresh, hot and ready to satisfy your momo craving."
    }
]

def validate_menu_data():
    """Lightweight validation to ensure schema integrity across all products."""
    required_keys = {"id", "name", "category", "style", "price", "pieces", "description", "badge", "image"}
    valid_categories = {"veg", "paneer", "chicken"}
    valid_styles = {"steamed", "fried", "kurkure", "tandoori", "special"}

    for index, item in enumerate(MENU):
        missing = required_keys - set(item.keys())
        if missing:
            raise ValueError(f"Product at index {index} missing keys: {missing}")
        if item["category"] not in valid_categories:
            raise ValueError(f"Product '{item['name']}' has invalid category: {item['category']}")
        if item["style"] not in valid_styles:
            raise ValueError(f"Product '{item['name']}' has invalid style: {item['style']}")
    return True

# Execute runtime validation
validate_menu_data()
