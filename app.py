import streamlit as st

st.set_page_config(
    page_title            = "PlantAI — Smart Plant Health",
    page_icon             = "🌿",
    layout                = "centered",
    initial_sidebar_state = "auto",
)

if "page"         not in st.session_state: st.session_state.page         = "landing"
if "prediction"   not in st.session_state: st.session_state.prediction   = None
if "image"        not in st.session_state: st.session_state.image        = None
if "image_name"   not in st.session_state: st.session_state.image_name   = None
if "chat_history" not in st.session_state: st.session_state.chat_history = []
if "history"      not in st.session_state: st.session_state.history      = []

page = st.session_state.page

if page == "landing":
    from views.landing import show
    show()
elif page == "detection":
    from views.detection import show
    show()
elif page == "result":
    from views.result import show
    show()
elif page == "assistant":
    from views.assistant import show
    show()