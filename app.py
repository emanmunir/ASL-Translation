import streamlit as st
import string

# Default images
DEFAULT_SPACE_IMAGE = 'https://asl-hands.s3.amazonaws.com/gifs/png-smiling-face-smiley-png-3896.png'
PLACEHOLDER_IMAGE = 'https://asl-hands.s3.amazonaws.com/placeholder.png'

# ASL dictionary mapping letters and numbers to corresponding S3 images
asl_images = {
    'A': 'https://asl-hands.s3.amazonaws.com/gifs/A-Sign-Language-Alphabet.gif',
    'B': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-B-in-Sign-Language-ASL.gif',
    'C': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-say-letter-C-in-ASL-sign-Language.gif',
    'D': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-D-in-Sign-Language-ASL.gif',
    'E': 'https://asl-hands.s3.amazonaws.com/gifs/The-Letter-E-in-Sign-Language.gif',
    'F': 'https://asl-hands.s3.amazonaws.com/gifs/What-is-F-in-Sign-Language-ASL.gif',
    'G': 'https://asl-hands.s3.amazonaws.com/gifs/What-is-G-in-Sign-Language-ASL.gif',
    'H': 'https://asl-hands.s3.amazonaws.com/gifs/H-in-Sign-Language-Alphabet.gif',
    'I': 'https://asl-hands.s3.amazonaws.com/gifs/What-is-I-in-Sign-Language-ASL.gif',
    'J': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-J-in-ASL-Alphabets.gif',
    'K': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-J-in-ASL-Alphabets.gif',
    'L': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-L-in-ASL-Alphabets.gif',
    'M': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-M-in-ASL-Alphabets.gif',
    'N': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-N-in-ASL-Alphabets.gif',
    'O': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-O-in-ASL-Alphabets.gif',
    'P': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-P-in-ASL-Alphabets.gif',
    'Q': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-Q-in-ASL-Alphabets.gif',
    'R': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-R-in-ASL-Alphabets.gif',
    'S': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-S-in-ASL-Alphabets.gif',
    'T': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-T-in-ASL-Alphabets.gif',
    'U': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-U-in-ASL-Alphabets.gif',
    'V': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-V-in-ASL-Alphabets.gif',
    'W': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-W-in-ASL-Alphabets.gif',
    'X': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-X-in-ASL-Alphabets.gif',
    'Y': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-Y-in-ASL-Alphabets.gif',
    'Z': 'https://asl-hands.s3.amazonaws.com/gifs/How-to-Say-Letter-Z-in-ASL-Alphabets.gif',
    '1': 'https://asl-hands.s3.amazonaws.com/LSQ_1.jpg',
    '2': 'https://asl-hands.s3.amazonaws.com/LSQ_2.jpg',
    '3': 'https://asl-hands.s3.amazonaws.com/LSQ_3.jpg',
    '4': 'https://asl-hands.s3.amazonaws.com/LSQ_4.jpg',
    '5': 'https://asl-hands.s3.amazonaws.com/LSQ_5.jpg',
    '6': 'https://asl-hands.s3.amazonaws.com/LSQ_6.jpg',
    '7': 'https://asl-hands.s3.amazonaws.com/LSQ_7.jpg',
    '8': 'https://asl-hands.s3.amazonaws.com/LSQ_8.jpg',
    '9': 'https://asl-hands.s3.amazonaws.com/LSQ_9.jpg',
    '10': 'https://asl-hands.s3.amazonaws.com/LSQ_10.jpg'
}

# Ensure 'SPACE' is in the dictionary
asl_images['SPACE'] = DEFAULT_SPACE_IMAGE

# Convert text to ASL images with corresponding letters, adding spaces between words
def text_to_asl_images(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    images_with_text = []
    words = text.upper().split()
    for i, word in enumerate(words):
        for char in word:
            image_url = asl_images.get(char, PLACEHOLDER_IMAGE)
            images_with_text.append((image_url, f"{char}"))
        if i < len(words) - 1:  # Don't add space after the last word
            images_with_text.append((DEFAULT_SPACE_IMAGE, "␣"))
    return images_with_text

# Streamlit Interface
st.title("ASL Translation App")

# Text Input
st.header("Text Input")
user_input = st.text_input("Enter text for ASL translation:")

if user_input:
    asl_translation = text_to_asl_images(user_input)
    
    st.subheader("ASL Translation")
    
    # Display ASL images
    cols = st.columns(10)
    for i, (img_url, char) in enumerate(asl_translation):
        with cols[i % 10]:
            st.image(img_url, width= 90, caption=char)
