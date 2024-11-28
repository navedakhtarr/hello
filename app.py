import streamlit as st
from PIL import Image
import base64

# Set page configuration
st.set_page_config(
    page_title="CONGRATULATIONS🥳💖",
    page_icon="💖",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-image: url('images/background.jpg');
    background-size: cover;
    background-position: center;
    background-blend-mode: darken;
    background-color: rgba(0, 0, 0, 0.5); /* Adds a semi-transparent black overlay */
    color: white;
    text-shadow: 2px 2px 5px black;
}
</style>
""", unsafe_allow_html=True)

# Function to add background image
def set_background(image_file):
    with open(image_file, "rb") as img:
        b64_img = base64.b64encode(img.read()).decode()
    bg_image_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{b64_img}");
        background-size: cover;
        background-position: center;
        color: white;
        text-shadow: 2px 2px 5px black;
    }}
    </style>
    """
    st.markdown(bg_image_style, unsafe_allow_html=True)

set_background("images/background.jpg")  # Replace with your background image

# Function to play background music
def add_background_music(file_path):
    with open(file_path, "rb") as music_file:
        music_data = music_file.read()
        b64_music = base64.b64encode(music_data).decode()
        music_html = f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64_music}" type="audio/mp3">
        Your browser does not support the audio element.
        </audio>
        """
        st.markdown(music_html, unsafe_allow_html=True)

add_background_music("audio/music.mp3")  # Replace with your MP3 file path

# Title Section
st.markdown('<h1 style="font-family: Pacifico, cursive; font-size: 50px;">💖 CONGRATULATIONS YUKI! 💖</h1>', unsafe_allow_html=True)
st.subheader("This is your appreciation for being the best nurse out there <3")
st.write(
    """
    Yuki,  
    You’ve just passed the PNLE exam, and I couldn’t be prouder!  
    Ranking **5247 out of 34,000** is a phenomenal achievement, and this page is dedicated to celebrating YOU.
    I have always believed in you even when you stop believing in yourself, you are the most hard working person I know
    and also the most humble. You are not only an amazing human being but you are a beacon, not just for me but also to every person
    in your life that knows you!! 
    Let's commemorate this moment and your hard work! 💖 ❤️
    """
)



# Photo Album Section
st.subheader("📸 Celebrating Your PNLE Success 📸")
st.write("Here are some snapshots of your journey and celebration:")

# Paths to the three images
image_paths = [
    "images/image1.JPG",  # Replace with your actual image filenames
    "images/image2.JPG",
    "images/image3.JPG"
]

# Captions for the images
captions = [
    "Your hard work paid off! 🎓",
    "Celebrating your achievement! 🎉",
    "Ready to conquer the nursing world! 🌟"
]

# Display images in a grid
cols = st.columns(len(image_paths))
for i, path in enumerate(image_paths):
    with cols[i]:
        img = Image.open(path)
        st.image(img, use_column_width=True, caption=captions[i])

# Quiz Section
st.subheader("💡 Quiz Time! How well do you know us?")
question = st.radio("Who is the best nurse in the world?", ["You", "Yuki", "key"])
if question == "Yuki":
    st.success("Correct! 🥰")
else:
    st.error("Try again! 😊")

# Interactive Celebration Button
if st.button("Celebrate! 🎉"):
    st.balloons()

# Closing Note
st.subheader("✨ Looking Ahead ✨")
st.write(
    """
    The PNLE was just the beginning of your incredible journey as a nurse.  
    Your hard work, determination, and perseverance have truly paid off.  
    Here's to a future filled with success, growth, and endless possibilities! 🌟
    """
)

# Celebration Message in an Expander
with st.expander("🎉 A Special Message for You 🎉"):
    st.write(
        """
        Dear Yuki,  
        Passing the PNLE is a huge milestone, and ranking **5247 out of 34,000**  
        makes this accomplishment even more extraordinary!  
        
        You inspire everyone around you with your dedication and passion.  
        I can't wait to see you flourish in your nursing career, touching lives and making a difference.  
        
        With immense pride and admiration,  
        Naved 💐
        """
    )

# Footer
st.write("Forever cheering for you, Naved 🎊")

