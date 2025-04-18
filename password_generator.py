import streamlit as st
import random
import string

def generate_password(Length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
        
    return ''.join(random.choice(characters) for _ in range(Length))

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=8, max_value=30, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"Generated Password: {password}")

    


