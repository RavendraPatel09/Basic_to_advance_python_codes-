import streamlit as st
st.set_page_config(page_title="StreamlitTube", layout="wide")
st.sidebar.title("Sam YouTube")
st.sidebar.button("Home")
st.sidebar.button("Subscriptions")
st.sidebar.button("Library")
st.sidebar.button("Trending")
st.title("Search")
search_query = st.text_input("Search for videos...", placeholder="Try 'Python Tutorials'")
videos = [
    {"title": "Learning Streamlit", "author": "CodeMaster", "views": "1.2M", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
    {"title": "Python for Data Science", "author": "DataWhiz", "views": "800K", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
    {"title": "AI in 2026", "author": "FutureTech", "views": "2M", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
]
cols = st.columns(3) 
for i, video in enumerate(videos):
    with cols[i % 3]:
        st.image("https://via.placeholder.com/400x225.png?text=Thumbnail", use_container_width=True)
        st.subheader(video["title"])
        st.caption(f"{video['author']} • {video['views']} views")
        if st.button(f"Watch Now", key=i):
            st.video(video["url"])