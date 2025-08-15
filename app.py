# app.py

import streamlit as st

# --- Page Configuration and Styling ---
# Use st.set_page_config to set the page title, icon, and layout
st.set_page_config(
    page_title="My Pretty Streamlit App",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for a more polished look
# We're using st.markdown with unsafe_allow_html=True to inject CSS
st.markdown("""
<style>
    /* Main container styling */
    .stApp {
        background-color: #f0f2f6; /* A soft, light gray background */
        color: #333; /* Dark gray text for readability */
        font-family: 'Inter', sans-serif;
    }

    /* Styling for the main header */
    .st-emotion-cache-1j71z8z {
        font-size: 2.5rem;
        font-weight: 700;
        color: #4b8bba; /* A nice blue color for the header */
        text-align: center;
        padding-bottom: 20px;
        border-bottom: 2px solid #ddd;
    }
    
    /* Styling for the input fields */
    .stTextInput label {
        font-weight: 600;
        color: #4b8bba;
    }
    .stTextInput input {
        border-radius: 8px;
        border: 2px solid #ccc;
        padding: 10px;
        transition: all 0.3s ease;
    }
    .stTextInput input:focus {
        border-color: #4b8bba;
        box-shadow: 0 0 8px rgba(75, 139, 186, 0.5);
    }
    
    /* Styling for the submit button */
    .st-emotion-cache-1xarlq2 {
        background-color: #4b8bba;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s ease;
    }
    .st-emotion-cache-1xarlq2:hover {
        background-color: #3a6b9a;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    /* Styling for the output section */
    .stMarkdown h3 {
        color: #2e8b57; /* A pleasant green for success message */
        border-bottom: 1px solid #2e8b57;
        padding-bottom: 5px;
        margin-top: 20px;
    }
    .stMarkdown p {
        background-color: #e6f2ee; /* Light green background for the results */
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #2e8b57;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# --- App Content ---
st.title("User Profile Generator ✨")
st.markdown("Enter your details below and see the magic happen!")

# Create a form to group the inputs and button
with st.form(key='my_form'):
    # Text input fields to collect user data
    name = st.text_input("Enter your name:")
    favorite_color = st.text_input("What is your favorite color?")
    short_bio = st.text_area("Tell us a little about yourself:")

    # Create a submit button for the form
    submit_button = st.form_submit_button(label='Generate Profile')

# --- Display Output on button click ---
# Use an if statement to check if the button was clicked
if submit_button:
    # Check if all fields are filled
    if name and favorite_color and short_bio:
        # Display the collected information using a nice format
        st.success("Profile Generated Successfully!")
        st.markdown("### Your Profile")
        st.write(f"**Name:** {name}")
        st.write(f"**Favorite Color:** {favorite_color}")
        st.write(f"**Bio:** {short_bio}")
    else:
        # Show a warning if any field is empty
        st.warning("Please fill out all the fields before submitting.")