# Enhanced personal portfolio application for Victor Ian

import streamlit as st
from PIL import Image

# Function for a dynamic theme toggle
def theme_toggle():
    st.sidebar.title("Choose a Theme")
    theme = st.sidebar.radio("Theme", ["Light", "Dark"])
    return theme

# Function to display the Home page
def home(theme):
    st.markdown(
        """
        <style>
        .hero {
            text-align: center;
            background-color: #4CAF50;
            color: white;
            padding: 50px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="hero"><h1>Welcome to Victor Ian\'s Photography!</h1><p>"Capturing the world one frame at a time."</p></div>', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400.png?text=Photography+Showcase", use_column_width=True)
    st.write("Explore my journey, view my gallery, and get to know me!")

# Function to display the About Me section
def about_me(theme):
    st.title("About Me")
    st.write("### Meet Victor Ian Townsend")
    st.write(
        """
        - **Age**: 14
        - **School**: Ramon Pascual Institute
        - **Passion**: Photography
        - **Camera**: Canon EOS 550D
        """
    )
    st.write("I love photography because it allows me to freeze moments in time and tell stories through visuals.")
    st.image("https://res.cloudinary.com/dihsizhut/image/upload/v1736427219/Untitled78_20250109205319_b0amyk.png", caption="My Gear")

# Function to display the Gallery
def gallery(theme):
    st.title("Photography Portfolio")
    st.write("### My Favorite Shots")
    # Placeholder for interactive carousel (currently using columns for simplicity)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://res.cloudinary.com/dihsizhut/image/upload/v1736424888/IMG_6980_novhkx.jpg", caption="Train")
    with col2:
        st.image("https://res.cloudinary.com/dihsizhut/image/upload/v1736425427/IMG_7703_uirmrh.jpg", caption="SM Sucat")
    with col3:
        st.image("https://res.cloudinary.com/dihsizhut/image/upload/v1736425532/IMG_6160_edit_410364827266216_1_vhsaki.jpg", caption="Full Moon")

    st.write("#### Upload and View Your Photos")
    uploaded_files = st.file_uploader("Upload your photos", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
    if uploaded_files:
        for uploaded_file in uploaded_files:
            st.image(uploaded_file, caption=uploaded_file.name, use_column_width=True)

# Function to display the Achievements and Goals
def achievements_and_goals(theme):
    st.title("Achievements & Future Goals")
    st.write("### Achievements")
    st.write("- Completed a beginner photography course.")
    st.write("- Won first place in a school photography contest.")
    st.write("- Published photos on a local photography blog.")

    st.write("### Future Goals")
    st.write("- Master advanced photography techniques.")
    st.write("- Travel to capture landscapes around the world.")
    st.write("- Build a professional portfolio to attract clients.")

# Function to display the Contact section
def contact(theme):
    st.title("Contact Me")
    st.write("Feel free to connect with me on the following platforms:")
    st.markdown(
        """
        - **Email**: [victorsphotographyt2i@gmail.com](mailto:victorsphotographyt2i@gmail.com)
        - **Instagram**: [@vickie.lox](https://instagram.com/vickie.lox)
        - **Facebook**: [Victor Ian Townsend](https://www.facebook.com/victor.ian.townsend)
        """
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://res.cloudinary.com/dihsizhut/image/upload/v1736426387/Untitled77_20250109203931_kd3fik.png", caption="Email")
    with col2:
        st.image("https://res.cloudinary.com/dihsizhut/image/upload/v1736426388/Untitled77_20250109203911_qa0hye.png", caption="Instagram")
    with col3:
        st.image("https://res.cloudinary.com/dihsizhut/image/upload/v1736426388/Untitled77_20250109203922_egxej8.png", caption="Facebook")

# Main function to render the app
def main():
    # Apply the theme toggle
    theme = theme_toggle()

    # Navigation
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to", ["Home", "About Me", "Gallery", "Achievements & Goals", "Contact"])

    # Page Routing
    if menu == "Home":
        home(theme)
    elif menu == "About Me":
        about_me(theme)
    elif menu == "Gallery":
        gallery(theme)
    elif menu == "Achievements & Goals":
        achievements_and_goals(theme)
    elif menu == "Contact":
        contact(theme)

# Run the app
if __name__ == "__main__":
    main()
