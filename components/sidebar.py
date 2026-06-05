import streamlit as st


def show_sidebar(active_page):

    st.markdown("""
        <style>
        [data-testid="stSidebarNav"] { display: none !important; }
        [data-testid="stSidebar"] { background-color: #ffffff !important; }
        [data-testid="stSidebar"] button {
            background-color: , #008000  !important;
            color: #222222 !important;
            border-radius: 8px !important;
            border: 1px solid #e8f0e8 !important;
            font-size: 0.88rem !important;
            font-weight: 500 !important;
            text-align: left !important;
            margin: 3px 0 !important;
        }
        [data-testid="stSidebar"] button:hover {
            background-color: #e8f5e9 !important;
            color: #2d6a2d !important;
            border-color: #2d6a2d !important;
        }
        [data-testid="stSidebar"] button p {
            color: #222222 !important;
        }
        [data-testid="stSidebar"] button:hover p {
            color: #2d6a2d !important;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:

        st.markdown("""
            <div style="padding:1rem 0.5rem 0.8rem;
                        border-bottom:1px solid #e8f0e8;
                        margin-bottom:1rem">
                <div style="font-size:1.2rem;font-weight:800;
                            color:#1a5c2a">🌿 PlantAI</div>
                <div style="font-size:0.72rem;color:#999;
                            margin-top:0.2rem">Smart Plant Health</div>
                <div style="font-size:0.68rem;color:#c8e6c9;
                            margin-top:0.3rem;
                            background:#f4faf4;
                            padding:0.2rem 0.5rem;
                            border-radius:10px;
                            display:inline-block">
                    👤 Guest Mode
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("**📍 Navigation**")

        if st.button("🏠 Dashboard",
                     key="sb_land",
                     use_container_width=True):
            st.session_state.page = "landing"
            st.rerun()

        if st.button("🔍 Detect Disease",
                     key="sb_detect",
                     use_container_width=True):
            st.session_state.page = "detection"
            st.rerun()

        if st.button("🤖 AI Assistant",
                     key="sb_assist",
                     use_container_width=True):
            st.session_state.page = "assistant"
            st.rerun()

        st.divider()

        st.markdown("**📋 Activity**")
        if st.button("📋 History",
                     key="sb_hist",
                     use_container_width=True):
            st.session_state.page = "detection"
            st.rerun()

        st.divider()

        st.markdown("""
            <div style="padding:0.5rem;background:#fff9e6;
                        border:1px solid #ffe082;border-radius:8px;
                        font-size:0.75rem;color:#888;text-align:center">
                🔒 Sign up coming soon<br>
                for personal accounts
            </div>
        """, unsafe_allow_html=True)