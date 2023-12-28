import streamlit as st
from PIL import Image
import imagehash
from datetime import datetime

# Setting page configuration
st.set_page_config(
    page_title="Data Redundancy Detection",
    page_icon=":bar_chart:",
    layout="wide",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
        .main-container {
            padding: 2rem;
        }

        .title {
            font-size: 2.5rem;
            text-align: center;
            color: #3498db;
        }

        .upload-section {
            display: flex;
            justify-content: space-around;
            align-items: center;
            margin-top: 2rem;
        }

        .image-container {
            display: flex;
            justify-content: space-around;
            align-items: center;
            margin-top: 2rem;
        }

        .image {
            max-width: 45%;
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 0.5rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .result {
            margin-top: 2rem;
            font-size: 1.5rem;
            text-align: center;
        }

        .footer {
            margin-top: 2rem;
            text-align: center;
            color: black;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def image_similarity(image1, image2):
    hash1 = imagehash.dhash(image1)
    hash2 = imagehash.dhash(image2)
    return hash1 == hash2

def main():
    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Title
    st.markdown('<h1 class="title">Image Data Redundancy Detection</h1>', unsafe_allow_html=True)

    # Upload section
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    uploaded_file1 = st.file_uploader(":file_folder: Upload the First Image file", type=["jpg", "jpeg", "png"])
    uploaded_file2 = st.file_uploader(":file_folder: Upload the Second Image file", type=["jpg", "jpeg", "png"])
    st.markdown("</div>", unsafe_allow_html=True)

    # Check for similarity and display images
    if uploaded_file1 is not None and uploaded_file2 is not None:
        image1 = Image.open(uploaded_file1)
        image2 = Image.open(uploaded_file2)

        # Image container
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(image1, caption='Image 1', use_column_width=True, output_format='JPEG')
        st.image(image2, caption='Image 2', use_column_width=True, output_format='JPEG')
        st.markdown("</div>", unsafe_allow_html=True)

        # Check for similarity
        st.markdown('<div class="result">', unsafe_allow_html=True)
        if image_similarity(image1, image2):
            st.success("The images are duplicates.")
        else:
            st.info("The images are not duplicates.")
        st.markdown("</div>", unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.text("Developed by PSG College of Technology - " + str(datetime.now().year))
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
