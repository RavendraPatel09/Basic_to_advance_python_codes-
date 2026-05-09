import streamlit as st
from captcha.image import ImageCaptcha
import random
import string
st.set_page_config(page_title="Streamlit CAPTCHA", page_icon="🤖")
def generate_random_text(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
if 'captcha_text' not in st.session_state:
    st.session_state.captcha_text = generate_random_text()
def refresh_captcha():
    st.session_state.captcha_text = generate_random_text()
st.title("🤖 Secure Form Access")
st.write("Please verify that you are human.")
image_gen = ImageCaptcha(width=300, height=100)
data = image_gen.generate(st.session_state.captcha_text)
st.image(data, caption="Solve the CAPTCHA")
user_input = st.text_input("Enter the characters you see above:").strip().upper()
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Submit"):
        if user_input == st.session_state.captcha_text:
            st.success("✅ Success! You are human.")
            st.balloons()
        else:
            st.error("❌ Incorrect. Try again.")
with col2:
    if st.button("Refresh CAPTCHA"):
        refresh_captcha()
        st.rerun()
#to run streamlit run "Automatic captcha.py"