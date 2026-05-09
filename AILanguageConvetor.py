import streamlit as st
from deep_translator import GoogleTranslator
st.set_page_config(page_title="AI Language Pro", page_icon="🌎")
st.title("🌎 AI Language Translator")
st.markdown("Build with Python 3.13 & Streamlit")
st.sidebar.header("Settings")
translator = GoogleTranslator()
supported_languages = translator.get_supported_languages()
target_lang = st.sidebar.selectbox("Select Target Language", supported_languages)
text_to_translate = st.text_area("Enter text to translate:", placeholder="Type something here...")
if st.button("Translate Now"):
    if text_to_translate.strip():
        try:
            with st.spinner('Translating...'):
                translation = GoogleTranslator(source='auto', target=target_lang).translate(text_to_translate)
            st.success("Success!")
            st.subheader(f"Translation ({target_lang.capitalize()}):")
            st.write(translation)
            st.download_button("Download Translation", translation, file_name="translated_text.txt")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text first.")