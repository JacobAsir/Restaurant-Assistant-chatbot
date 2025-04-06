import streamlit as st
import random
from datetime import datetime, time
import os
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="𝘾𝙚𝙧𝙞-𝙈𝙚𝙧",
    page_icon="🍽️",
    layout="wide"
)

# Custom CSS for styling with fixed image dimensions
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #FF5733;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #333;
        margin-top: 2rem;
    }
    .menu-category {
        font-size: 1.5rem;
        font-weight: 500;
        color: #444;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #FF5733;
        padding-bottom: 0.5rem;
    }
    .menu-item-title {
        font-weight: 600;
        margin-top: 0.5rem;
        margin-bottom: 0.2rem;
        font-size: 1rem;
    }
    .menu-item-price {
        font-size: 1.2rem;
        color: #FF5733;
        font-weight: 500;
    }
    .review-card {
        background-color: #f5f5f5;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }
    .review-comment {
        margin-top: 0.5rem;
        font-size: 0.95rem;
        color: #000000 !important;
        font-weight: 400;
    }
    .reservation-form {
        background-color: #f9f9f9;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .star-rating {
        color: #FFD700;
        font-size: 1.2rem;
    }
    footer {
        text-align: center;
        color: #666;
        padding: 1rem;
        margin-top: 2rem;
        border-top: 1px solid #ddd;
    }
    .reviewer-name {
        font-weight: 600;
        color: #000000;
    }
    .dark-text {
        color: #000000 !important;
    }
    .review-card p {
        color: #000000 !important;
    }
    .menu-item-container {
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 15px;
        text-align: center;
        background-color: #1f1f1f;
    }
    .menu-item-name {
        font-weight: bold;
        margin: 8px 0 5px 0;
        font-size: 1.1rem;
    }
    .menu-item-price-display {
        color: #FF5733;
        font-weight: 500;
        font-size: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Restaurant header
st.markdown('<h1 class="main-header">𝘾𝙚𝙧𝙞-𝙈𝙚𝙧</h1>', unsafe_allow_html=True)

# Define your menu items - use only local image paths
food_items = [
    {"name": "Classic Burger", "price": "$12.99", "image": "images/food/photo-1568901346375-23c9450c58cd.jpeg"},
    {"name": "Margherita Pizza", "price": "$14.99", "image": "images/food/photo-1564936281291-294551497d81.jpeg"},
    {"name": "Grilled Salmon", "price": "$22.99", "image": "images/food/photo-1519708227418-c8fd9a32b7a2.jpeg"},
    {"name": "Caesar Salad", "price": "$9.99", "image": "images/food/photo-1550304943-4f24f54ddde9.jpeg"},
    {"name": "Spaghetti Carbonara", "price": "$16.99", "image": "images/food/photo-1612874742237-6526221588e3.jpeg"},
    {"name": "Steak Frites", "price": "$24.99", "image": "images/food/photo-1600891964092-4316c288032e.jpeg"},
    {"name": "Fish & Chips", "price": "$15.99", "image": "images/food/photo-1579888944880-d98341245702.jpeg"},
    {"name": "Chicken Curry", "price": "$17.99", "image": "images/food/photo-1631292784640-2b24be784d5d.jpeg"},
    {"name": "Mushroom Risotto", "price": "$14.99", "image": ""},
    {"name": "Beef Tacos", "price": "$13.99", "image": ""}
]

# Beverage item data - use only local image paths
beverage_items = [
    {"name": "Classic Mojito", "price": "$8.99", "image": "images/beverages/photo-1551538827-9c037cb4f32a.jpeg"},
    {"name": "Fresh Orange Juice", "price": "$4.99", "image": "images/beverages/photo-1621506289937-a8e4df240d0b.jpeg"},
    {"name": "Cappuccino", "price": "$5.99", "image": "images/beverages/photo-1572442388796-11668a67e53d.jpeg"},
    {"name": "Iced Tea", "price": "$3.99", "image": "images/beverages/photo-1556679343-c7306c1976bc.jpeg"},
    {"name": "Red Wine", "price": "$9.99", "image": "images/beverages/photo-1510812431401-41d2bd2722f3.jpeg"},
    {"name": "Craft Beer", "price": "$7.99", "image": "images/beverages/photo-1566633806327-68e152aaf26d.jpeg"},
    {"name": "Mango Smoothie", "price": "$6.99", "image": "images/beverages/photo-1623065422902-30a2d299bbe4.jpeg"},
    {"name": "Hot Chocolate", "price": "$4.99", "image": "images/beverages/photo-1542990253-0d0f5be5f0ed.jpeg"},
    {"name": "Lemonade", "price": "$3.99", "image": "images/beverages/photo-1621263764928-df1444c5e859.jpeg"},
    {"name": "Espresso", "price": "$3.49", "image": ""}
]


# Special offers data - use only local image paths
special_items = [
    {"name": "Weekend Brunch Set", "price": "$24.99", "image": "images/specials/photo-1550547660-d9450f859349.jpeg"},
    {"name": "Family Feast", "price": "$59.99", "image": "images/specials/photo-1555939594-58d7cb561ad1.jpeg"},
    {"name": "Chef's Special Pasta", "price": "$19.99", "image": "images/specials/photo-1608897013039-887f21d8c804.jpeg"},
    {"name": "Seafood Platter", "price": "$39.99", "image": "images/specials/photo-1590759668628-05b0fc34bb70.jpeg"},
    {"name": "Dessert Sampler", "price": "$15.99", "image": "images/specials/photo-1488477181946-6428a0291777.jpeg"},
    {"name": "Bottomless Mimosas", "price": "$22.99", "image": "images/specials/photo-1600271886742-f049cd451bba.jpeg"},
    {"name": "Happy Hour Deal", "price": "$17.99", "image": "images/specials/photo-1551024709-8f23befc6f87.jpeg"},
    {"name": "Vegetarian Combo", "price": "$21.99", "image": "images/specials/photo-1610970881699-44a5587cabec.jpeg"},
    {"name": "Date Night Special", "price": "$49.99", "image": "images/specials/photo-1559622214-f8a9850965bb.jpeg"},
    {"name": "Kids Meal Deal", "price": "$11.99", "image": "images/specials/photo-1619096252214-ef06c45683e3.jpeg"}
]

# Function to display menu items with consistent image sizing
def display_menu_items(items, start_idx, end_idx):
    # Use 5 columns for a good display on most screens
    cols = st.columns(5)
    
    for i, item in enumerate(items[start_idx:end_idx]):
        with cols[i % 5]:
            with st.container():
                # Create container for the menu item
                st.markdown('<div class="menu-item-container">', unsafe_allow_html=True)
                
                # Check if image exists
                if item['image'] and os.path.exists(item['image']):
                    # Use Streamlit's image display with fixed height
                    # This creates a wrapper around the image for styling
                    img = Image.open(item['image'])
                    # Resize to a more manageable size while maintaining aspect ratio
                    img_width, img_height = img.size
                    aspect_ratio = img_width / img_height
                    new_height = 200
                    new_width = int(aspect_ratio * new_height)
                    img = img.resize((new_width, new_height), Image.LANCZOS)
                    
                    # Display image
                    st.image(img, use_container_width=True)
                else:
                    # If image doesn't exist, use a placeholder with fixed height
                    st.markdown(
                        '<div style="background-color:#2e2e2e;height:200px;display:flex;align-items:center;justify-content:center;border-radius:4px;"><span style="color:#aaa;">No Image</span></div>',
                        unsafe_allow_html=True
                    )
                
                # Item name and price
                st.markdown(f'<div class="menu-item-name">{item["name"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="menu-item-price-display">{item["price"]}</div>', unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)

# Navigation tabs
tabs = st.tabs(["📋 Menu", "📅 Reservations", "⭐ Reviews"])

# Menu tab
with tabs[0]:
    st.markdown('<h2 class="sub-header">Our Menu</h2>', unsafe_allow_html=True)
    
    # Food section
    st.markdown('<h3 class="menu-category">Food</h3>', unsafe_allow_html=True)
    display_menu_items(food_items, 0, 5)
    
    with st.expander("See More Food Items"):
        display_menu_items(food_items, 5, 10)
    
    # Beverages section
    st.markdown('<h3 class="menu-category">Beverages</h3>', unsafe_allow_html=True)
    display_menu_items(beverage_items, 0, 5)
    
    with st.expander("See More Beverages"):
        display_menu_items(beverage_items, 5, 10)
    
    # Special Offers section
    st.markdown('<h3 class="menu-category">Special Offers</h3>', unsafe_allow_html=True)
    display_menu_items(special_items, 0, 5)
    
    with st.expander("See More Special Offers"):
        display_menu_items(special_items, 5, 10)

# Reviews tab
with tabs[2]:
    st.markdown('<h2 class="sub-header">Customer Reviews</h2>', unsafe_allow_html=True)
    
    # Sample reviews
    reviews = [
        {"name": "Sarah L.", "rating": 5, "comment": "Absolutely loved the food here! The Classic Burger is to die for. The service was also exceptional and they were very accommodating with my dietary restrictions."},
        {"name": "Michael T.", "rating": 4, "comment": "Great ambiance and excellent service. The food was delicious but slightly pricey. I would definitely recommend the Grilled Salmon and Red Wine combination."},
        {"name": "Jennifer K.", "rating": 5, "comment": "Best restaurant in town! The special offers are amazing value, especially the Family Feast which easily fed our party of 5 with leftovers to take home."},
        {"name": "Robert P.", "rating": 4, "comment": "Fantastic craft beers and the Weekend Brunch Set was excellent. My only minor complaint is that the place gets quite busy on weekends, so reservations are a must."},
        {"name": "Emma S.", "rating": 5, "comment": "The seafood platter was incredibly fresh and well-prepared. Will definitely return! The staff went above and beyond to make our anniversary dinner special."}
    ]
    
    # Display reviews with improved UI and guaranteed visibility
    for i, review in enumerate(reviews):
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f"<div style='background-color:#FF5733;color:white;border-radius:50%;width:40px;height:40px;display:flex;justify-content:center;align-items:center;margin:0 auto;'><span>{review['rating']}</span></div>", unsafe_allow_html=True)
            with col2:
                # Using explicit styling to ensure text is visible regardless of theme
                st.markdown(f'''
                <div class="review-card">
                    <div class="reviewer-name">{review['name']}</div>
                    <div class="star-rating">{"★" * review['rating'] + "☆" * (5 - review['rating'])}</div>
                    <p style="color: #000000; margin-top: 10px; font-size: 16px;">{review['comment']}</p>
                </div>
                ''', unsafe_allow_html=True)
    
    # Add a review
    st.markdown('<h3 style="margin-top:2rem;">Leave a Review</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 3])
    with col1:
        rating = st.slider("Your Rating", 1, 5, 5, key="rating_slider")
    with col2:
        name = st.text_input("Your Name", key="review_name")
    
    review_text = st.text_area("Your Review", placeholder="Share your dining experience with us...", height=100, key="review_text")
    
    if st.button("Submit Review", key="submit_review"):
        if name and review_text:
            st.success("Thank you for your review! It will appear after moderation.")
        else:
            st.warning("Please fill in all fields to submit your review.")

# Reservations tab
with tabs[1]:
    st.markdown('<h2 class="sub-header">Make a Reservation</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="reservation-form">', unsafe_allow_html=True)
        
        # Improved date picker with min/max date constraints
        today = datetime.now().date()
        reservation_date = st.date_input("Select Date", min_value=today, key="res_date")
        
        # Time picker with reasonable restaurant hours
        reservation_time = st.time_input("Select Time", value=time(19, 0), step=900, key="res_time")  # 15 min increments
        
        # More structured guest selection
        guest_count = st.select_slider("Number of Guests", options=[1, 2, 3, 4, 5, 6, 7, 8, 'Large Group (9+)'], key="guest_count")
        
        if guest_count == 'Large Group (9+)':
            large_group = st.number_input("Exact Number of Guests", min_value=9, max_value=30, value=10, key="large_group")
        
        # More comprehensive contact information
        col_a, col_b = st.columns(2)
        with col_a:
            first_name = st.text_input("First Name", key="res_first_name")
        with col_b:
            last_name = st.text_input("Last Name", key="res_last_name")
            
        phone = st.text_input("Phone Number", key="res_phone")
        email = st.text_input("Email", key="res_email")
        
        # Special occasions and requests
        occasion = st.selectbox("Special Occasion?", ["None", "Birthday", "Anniversary", "Business Meeting", "Other"], key="res_occasion")
        
        if occasion == "Other":
            other_occasion = st.text_input("Please specify", key="res_other_occasion")
        
        special_requests = st.text_area("Special Requests or Dietary Requirements", height=100, key="res_special_requests")
        
        # Submit button with confirmation
        if st.button("Reserve Table", key="reserve_button"):
            if first_name and last_name and phone:
                st.success("Reservation request submitted! We'll contact you shortly to confirm.")
                
                # Display confirmation details
                st.markdown("### Reservation Details:")
                st.markdown(f"""
                **Name:** {first_name} {last_name}  
                **Date & Time:** {reservation_date} at {reservation_time.strftime('%I:%M %p')}  
                **Party Size:** {guest_count if guest_count != 'Large Group (9+)' else large_group}  
                **Contact:** {phone} | {email}
                """)
            else:
                st.warning("Please fill in all required fields (name and phone number).")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<h3>Order for Pickup/Delivery</h3>', unsafe_allow_html=True)
        
        # More appealing order interface
        with st.container():
            st.markdown('<div class="reservation-form">', unsafe_allow_html=True)
            
            order_type = st.radio("Order Type", ["Pickup", "Delivery"], key="order_type")
            
            if order_type == "Delivery":
                st.text_input("Street Address", key="del_street_address")
                col_c, col_d = st.columns(2)
                with col_c:
                    st.text_input("City", key="del_city")
                with col_d:
                    st.text_input("Postal/ZIP Code", key="del_zip_code")
            
            # Simplified order interface with categories
            st.subheader("Select Your Items")
            
            # Food order dropdown
            food_order = st.multiselect(
                "Food Items", 
                options=[item["name"] + " - " + item["price"] for item in food_items],
                key="order_food_items"
            )
            
            # Beverage order dropdown
            beverage_order = st.multiselect(
                "Beverage Items", 
                options=[item["name"] + " - " + item["price"] for item in beverage_items],
                key="order_beverage_items"
            )
            
            # Special offers dropdown
            special_order = st.multiselect(
                "Special Offers", 
                options=[item["name"] + " - " + item["price"] for item in special_items],
                key="order_special_items"
            )
            
            # Additional instructions
            additional_instructions = st.text_area("Additional Instructions", placeholder="Any special preparation instructions, allergies, etc.", height=100, key="order_instructions")
            
            # Timing options
            timing_option = st.radio("When do you want your order?", ["As Soon As Possible", "Schedule for Later"], key="order_timing")
            
            if timing_option == "Schedule for Later":
                scheduled_date = st.date_input("Select Date for Order", min_value=today, key="order_date")
                scheduled_time = st.time_input("Select Time for Order", value=time(19, 0), step=900, key="order_time")
            
            # Contact information
            st.subheader("Contact Information")
            contact_name = st.text_input("Your Name", key="order_contact_name")
            contact_phone = st.text_input("Contact Number", key="order_contact_phone")
            
            # Payment method selection
            payment_method = st.selectbox("Payment Method", ["Credit Card", "Cash on Delivery/Pickup", "Mobile Payment"], key="payment_method")
            
            if st.button("Place Order", key="place_order"):
                if (food_order or beverage_order or special_order) and contact_name and contact_phone:
                    st.success("Order placed successfully! You'll receive a confirmation shortly.")
                    
                    # Display order summary
                    total_items = len(food_order) + len(beverage_order) + len(special_order)
                    st.markdown(f"### Order Summary: {total_items} item(s)")
                    
                    # In a real app, this would calculate totals and send to a database
                else:
                    st.warning("Please select at least one item and provide contact information.")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Add an informational note about delivery
            if order_type == "Delivery":
                st.info("Delivery available within 5 miles of our location. Delivery fee: $3.99")

# Footer with restaurant information
st.markdown('''
<footer>
    <p><strong>𝘾𝙚𝙧𝙞-𝙈𝙚𝙧 Restaurant</strong></p>
    <p>123 Culinary Street, Foodville | Phone: (555) 123-4567 | Email: info@ceri-mer.com</p>
    <p>Hours: Mon-Thu: 11am-10pm, Fri-Sat: 11am-11pm, Sun: 10am-9pm</p>
    <p>&copy; 2025 𝘾𝙚𝙧𝙞-𝙈𝙚𝙧. All rights reserved.</p>
</footer>
''', unsafe_allow_html=True)