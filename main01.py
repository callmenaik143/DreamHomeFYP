import streamlit as st
import requests
import random

# Base URL for API calls
base_url = "https://plenty-doodles-win.loca.lt/"

# Function to login user
def login_user(username, password):
    if username == 'admin' and password == 'admin':
        print("Login successful")
        return True
    else:
        print("Failed to log in")
        return False

# Function to handle material generation
def generate_material(category_name, subcategory_name, apply_location, color_name, color_code):
    data = {
        "category_name": category_name,
        "subcategory_name": subcategory_name,
        "apply_location": apply_location,
        "color_name": color_name,
        "color_code": color_code
    }
    response = requests.post(base_url + '/generate-material', json=data)
    if response.status_code == 200:
        with open("generated_material_image.png", "wb") as f:
            f.write(response.content)
        return 'ok', "generated_material_image.png"
    return '', None

# Function to handle home generation
def generate_home(prompt):
    data = {"query": prompt}
    response = requests.post(base_url + '/generate-home', json=data)
    if response.status_code == 200:
        with open("generated_home_image.png", "wb") as f:
            f.write(response.content)
        return 'ok', "generated_home_image.png"
    return '', None

# Function to get a random home background image
def get_random_background_image():
    images = [
        "https://images.unsplash.com/photo-1502920970741-47c1bafc8d49"
    ]
    return random.choice(images)

# Load custom CSS for styling
def load_css(background_image):
    st.markdown(f"""
    <style>
    body {{
        background-image: url('{background_image}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    header {{ visibility: hidden; }}
    .css-18e3th9 {{
        padding-top: 0!important;
    }}
    .fixed-header {{
        color: #ffffff;
        background-color: #2c3e50;
        font-size: 24px;
        text-align: center;
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        z-index: 1000;
        padding: 10px 0;
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .fixed-header .left {{
        flex: 1;
        display: flex;
        justify-content: flex-start;
        margin-left: 10px; /* Added margin for project name */
    }}
    .fixed-header .center {{
        flex: 2;
        display: flex;
        justify-content: center;
    }}
    .fixed-header .center a {{
        margin: 0 10px; /* Reduced spacing between the pages */
    }}
    .fixed-header .right {{
        flex: 1;
        display: flex;
        justify-content: flex-end;
        margin-right: 10px; /* Added margin between Sign In and Join Now */
    }}
    .fixed-header .right a {{
        margin-left: 10px; /* Reduced spacing between Sign In and Join Now */
    }}
    .fixed-header a {{
        color: #ffffff;
        text-decoration: none;
        font-family: 'Josefin Sans', sans-serif;
    }}
    .fixed-header .project-name {{
        font-weight: bold;
        margin-right: auto;
    }}
    .fixed-footer {{
        color: #ffffff;
        background-color: #2c3e50;
        font-size: 12px;
        text-align: center;
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 10px 0;
        z-index: 1000;
    }}
    .streamlit-tabs {{
        margin-top: 60px;
    }}
    .main > div:first-child {{
        padding-top: 100px;
    }}
    .main > div:last-child {{
        padding-bottom: 50px;
    }}
    .css-1lcbmhc {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%;
    }}
    .stForm {{
        width: 100%;
        max-width: 400px;
        padding: 2rem;
        margin: auto;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background-color: rgba(255, 255, 255, 0.9);
    }}
    .stTextInput > div > div {{
        width: 100%;
    }}
    .css-ubgok1 {{
        width: 100%;
        margin-top: 1rem;
    }}
    .download-button, .generate-button {{
        display: inline-flex;
        align-items: center;
        font-weight: 800;
        color: black; /* Black text color */
        font-size: 16px;
        border: none;
        background: none; /* Transparent background */
        cursor: pointer;
    }}
    .stApp {{
        background-color: transparent;
    }}
    .half-screen {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }}
    .half-screen > div {{
        flex: 1;
        padding: 10px;
    }}
    .pricing-section {{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        padding: 20px;
    }}
    .pricing-card {{
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 10px;
        width: 300px;
        text-align: center;
    }}
    .pricing-card h2 {{
        font-size: 24px;
        margin-bottom: 10px;
    }}
    .pricing-card p {{
        font-size: 16px;
        margin: 5px 0;
    }}
    .pricing-card .price {{
        font-size: 32px;
        margin: 15px 0;
    }}
    .pricing-card .button {{
        background-color: #2196F3;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }}
    .blog-section {{
        padding: 20px;
    }}
    .blog-card {{
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 20px;
        width: 600px;
        text-align: center;
        display: inline-block;
        vertical-align: top;
    }}
    .blog-card img {{
        width: 600px;
        height: 200px; /* Make images rectangular */
        object-fit: cover;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }}
    .blog-card h3 {{
        font-size: 20px;
        margin: 10px 100;
    }}
    .blog-card p {{
        font-size: 14px;
        padding: 0 10px 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

def main():
    background_image = get_random_background_image()
    load_css(background_image)

    st.markdown("""
        <div class="fixed-header">
            <div class="left">
                <span class="project-name">DreamHome</span>
            </div>
            <div class="center">
                <a href="#">Home</a>
                <a href="#">News</a>
                <a href="#">Blog</a>
                <a href="#">Pricing</a>
            </div>
            <div class="right">
                <a href="#">Join Now</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        tab1, tab2, tab3, tab4 = st.tabs(["Generate Floor Plan", "Pricing", "Blog", "Logout"])

        with tab1:
            option = st.selectbox("Choose method to generate floor plan:", ["Form", "Prompt"])

            if option == "Form":
                col1, col2 = st.columns([0.45, 0.55])
                with col1:
                    with st.form(key='home_plan_form'):
                        st.subheader("Home FloorPlan Generation")
                        bedrooms = st.number_input("Number of Bedrooms:", min_value=1, step=1)
                        bathrooms = st.number_input("Number of Bathrooms:", min_value=0, step=1)
                        kitchens = st.number_input("Number of Kitchens:", min_value=0, step=1)
                        dining_rooms = st.number_input("Number of Dining Rooms:", min_value=0, step=1)
                        balconies = st.number_input("Number of Balconies:", min_value=0, step=1)
                        submit_button = st.form_submit_button('Generate Home Floor Plan')

                if submit_button:
                    with st.spinner('Generating home plan...'):
                        prompt = f"create floorplan with {bedrooms} bedroom{'s' if bedrooms > 1 else ''}, "
                        if bathrooms > 0:
                            prompt += f"{bathrooms} bathroom{'s' if bathrooms > 1 else ''}, "
                        if kitchens > 0:
                            prompt += f"{kitchens} kitchen{'s' if kitchens > 1 else ''}, "
                        if dining_rooms > 0:
                            prompt += f"{dining_rooms} dining room{'s' if dining_rooms > 1 else ''}, "
                        if balconies > 0:
                            prompt += f"{balconies} balcony{'ies' if balconies > 1 else ''}, "
                        prompt = prompt.rstrip(', ')
                        status, image_path = generate_home(prompt)
                        if status == 'ok':
                            st.session_state['generated_home_image'] = image_path
                            col2.image(image_path, caption="Generated Home Floor Plan")
                            with col2:
                                with open(image_path, "rb") as file:
                                    st.download_button(
                                        label="Download Floor Plan",
                                        data=file,
                                        file_name=image_path,
                                        mime="image/png",
                                        key="download_home_plan"
                                    )
                        else:
                            st.error('Error generating home plan. Please try again.')

            elif option == "Prompt":
                col1, col2 = st.columns([0.45, 0.55])
                with col1:
                    with st.form(key='home_prompt_form'):
                        st.subheader("Home FloorPlan Generation")
                        prompt = st.text_area("Enter your prompt:", placeholder="E.g., create floorplan with 3 bedrooms, 2 bathrooms, 1 kitchen, 1 dining room, 2 balconies")
                        submit_button = st.form_submit_button('Generate Home Floor Plan')

                if submit_button:
                    if "create floorplan" not in prompt.lower():
                        prompt = "create floorplan with " + prompt
                    with st.spinner('Generating home plan...'):
                        status, image_path = generate_home(prompt)
                        if status == 'ok':
                            st.session_state['generated_home_image'] = image_path
                            col2.image(image_path, caption="Generated Home Floor Plan")
                            with col2:
                                with open(image_path, "rb") as file:
                                    st.download_button(
                                        label="Download Floor Plan",
                                        data=file,
                                        file_name=image_path,
                                        mime="image/png",
                                        key="download_home_prompt_plan"
                                    )
                        else:
                            st.error('Error generating home plan. Please try again.')

        with tab2:
            st.markdown("""
                <div class="pricing-section">
                    <div class="pricing-card">
                        <h2>Basic Plan</h2>
                        <p>Up to 3 Projects</p>
                        <p>5 Design Credits</p>
                        <p>Low resolution images</p>
                        <p>✏️ Sketch-to-Render (Limited)</p>
                        <p>Image cleanup tools</p>
                        <p>🏠 AI Generated Floorplans (10 FloorPlan)</p>
                        <p>🛋️ Restyle your images (Limited)</p>
                        <p>🖼️ Generate Renderings (Limited)</p>
                        <p class="price">$9.99</p>
                        <button class="button">Get Started</button>
                    </div>
                    <div class="pricing-card">
                        <h2>Standard Plan</h2>
                        <p>Up to 5 Projects</p>
                        <p>10 Design Credits</p>
                        <p>Medium resolution images</p>
                        <p>✏️ Sketch-to-Render (Limited)</p>
                        <p>Image cleanup tools</p>
                        <p>🏠 AI Generated Floorplans (30 FloorPlan)</p>
                        <p>🛋️ Restyle your images (Limited)</p>
                        <p>🖼️ Generate Renderings (Limited)</p>
                        <p class="price">$19.99</p>
                        <button class="button">Get Started</button>
                    </div>
                    <div class="pricing-card">
                        <h2>Premium Plan</h2>
                        <p>Unlimited Projects</p>
                        <p>Unlimited Design Credits</p>
                        <p>High resolution images</p>
                        <p>✏️ Sketch-to-Render (Unlimited)</p>
                        <p>Image cleanup tools</p>
                        <p>🏠 AI Generated Floorplans (Unlimited FloorPlan)</p>
                        <p>🛋️ Restyle your images (Unlimited)</p>
                        <p>🖼️ Generate Renderings (Unlimited)</p>
                        <p class="price">$49.99</p>
                        <button class="button">Get Started</button>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with tab3:
            st.markdown("<h2>Blog</h2>", unsafe_allow_html=True)
            st.markdown("""
            <div class="blog-section">
                <div class="blog-card">
                    <img src="https://plus.unsplash.com/premium_photo-1661954372617-15780178eb2e" alt="Blog Image 1">
                    <h3>AI in Architecture: Transforming Design Processes</h3>
                    <p>Explore how AI is revolutionizing architecture by enhancing design efficiency and creativity.</p>
                </div>
                <div class="blog-card">
                    <img src="https://images.unsplash.com/photo-1600047509358-9dc75507daeb" alt="Blog Image 2">
                    <h3>The Future of Smart Buildings</h3>
                    <p>Discover the potential of AI-powered smart buildings and their impact on urban living.</p>
                </div>
                <div class="blog-card">
                    <img src="https://images.unsplash.com/photo-1524813686514-a57563d77965" alt="Blog Image 3">
                    <h3>Sustainable Architecture with AI</h3>
                    <p>Learn how AI is driving sustainable practices in architecture, from design to construction.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with tab4:
            if st.button("Confirm Logout"):
                st.session_state['logged_in'] = False
                st.experimental_rerun()
    else:
        with st.form("Login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button("Login")
            if submit_button:
                if login_user(username, password):
                    st.session_state['logged_in'] = True
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password")
    st.markdown('<div class="fixed-footer">© 2024 All Rights Reserved.</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
