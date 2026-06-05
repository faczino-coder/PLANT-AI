import streamlit as st
import base64
from components.styles import load_styles
from components.sidebar import show_sidebar


def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def show():
    st.markdown(load_styles(), unsafe_allow_html=True)
    show_sidebar("detection")

    # ── Banner ────────────────────────────────────────────────────────────────
    try:
        b64 = img_to_base64("assets/hero_bg.jpg")
        src = f"data:image/jpeg;base64,{b64}"
        st.markdown(f"""
            <div style="position:relative;width:100%;height:180px;
                        overflow:hidden;border-radius:12px;
                        margin-bottom:1.5rem">
                <img src="{src}"
                     style="width:100%;height:180px;
                            object-fit:cover;display:block"/>
                <div style="position:absolute;inset:0;
                            background:linear-gradient(
                                135deg,rgba(10,40,10,0.80) 0%,
                                rgba(15,55,15,0.50) 100%
                            );
                            display:flex;align-items:center;
                            padding:0 2.5rem">
                    <div>
                        <div style="font-size:1.8rem;font-weight:800;
                                    color:white">🔍 Detect Disease</div>
                        <div style="font-size:0.9rem;
                                    color:rgba(255,255,255,0.8);
                                    margin-top:0.3rem">
                            Upload a photo or use your camera
                            for an instant AI diagnosis
                        </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown("""
            <div style="background:linear-gradient(135deg,#1a5c2a,#2d8a3e);
                        padding:2.5rem;border-radius:12px;
                        margin-bottom:1.5rem">
                <div style="font-size:1.8rem;font-weight:800;color:white">
                    🔍 Detect Disease
                </div>
                <div style="font-size:0.9rem;
                            color:rgba(255,255,255,0.8);margin-top:0.3rem">
                    Upload a photo or use your camera for an instant diagnosis
                </div>
            </div>
        """, unsafe_allow_html=True)

    # ── Main layout ───────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    main_col, gap_col, side_col = st.columns([2, 0.2, 1])

    with main_col:

        # ── Tabs — Upload or Camera ───────────────────────────────────────────
        tab1, tab2 = st.tabs(["📁  Upload Image", "📷  Use Camera"])

        uploaded_file  = None
        camera_capture = None

        with tab1:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
                <div style="background:white;
                            border:2px dashed #c8e6c9;
                            border-radius:16px;
                            padding:2.5rem 2rem;
                            text-align:center;
                            margin:0 1rem 1rem 1rem">
                    <div style="font-size:2.5rem;margin-bottom:0.8rem">📤</div>
                    <div style="font-size:1rem;font-weight:600;
                                color:#1a1a1a;margin-bottom:0.4rem">
                        Drag and drop an image here
                    </div>
                    <div style="font-size:0.82rem;color:#888">
                        JPG, PNG, JPEG &nbsp;|&nbsp; Max 10MB
                    </div>
                </div>
            """, unsafe_allow_html=True)

            uploaded_file = st.file_uploader(
                "Choose a leaf image",
                type             = ["jpg","jpeg","png"],
                key              = "leaf_upload",
                label_visibility = "collapsed"
            )

            if uploaded_file:
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("""
                    <div style="margin:0 1rem">
                        <div style="font-size:0.82rem;font-weight:600;
                                    color:#2d6a2d;margin-bottom:0.5rem">
                            📸 Image Preview
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                col_a, col_b, col_c = st.columns([0.5, 3, 0.5])
                with col_b:
                    st.image(uploaded_file,
                             caption="Uploaded leaf image",
                             use_column_width=True)

        with tab2:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
                <div style="background:white;
                            border:2px dashed #c8e6c9;
                            border-radius:16px;
                            padding:2rem;
                            text-align:center;
                            margin:0 1rem 1rem 1rem">
                    <div style="font-size:2.5rem;margin-bottom:0.8rem">📷</div>
                    <div style="font-size:1rem;font-weight:600;
                                color:#1a1a1a;margin-bottom:0.3rem">
                        Take a photo of your leaf
                    </div>
                    <div style="font-size:0.82rem;color:#888">
                        Point your camera at a single leaf
                        in good lighting and click capture
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col_a, col_b, col_c = st.columns([0.3, 3, 0.3])
            with col_b:
                camera_capture = st.camera_input(
                    "Point camera at leaf",
                    label_visibility = "collapsed",
                    key              = "camera_snap"
                )

            if camera_capture:
                st.success("✅ Photo captured! Click Analyse Leaf below.")

        # ── Tips box ──────────────────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
            <div style="background:#f4faf4;
                        border:1px solid #c8e6c9;
                        border-radius:12px;
                        padding:1.2rem 1.5rem;
                        margin:0 1rem">
                <div style="font-weight:700;color:#2d6a2d;
                            margin-bottom:0.8rem;font-size:0.9rem">
                    📋 Tips for best results
                </div>
                <div style="font-size:0.83rem;color:#555;line-height:2.1">
                    ✅  Take a clear close-up of a single leaf<br>
                    ✅  Make sure the leaf fills most of the frame<br>
                    ✅  Use good natural lighting — avoid shadows<br>
                    ✅  Avoid blurry or dark images<br>
                    ✅  Supported crops: Tomato and Maize only
                </div>
            </div>
        """, unsafe_allow_html=True)

        # ── Analyse button ────────────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        btn_a, btn_b, btn_c = st.columns([0.5, 3, 0.5])
        with btn_b:
            analyse_btn = st.button(
                "🔍 Analyse Leaf",
                key                 = "analyse_btn",
                use_container_width = True
            )

        # ── Handle both upload and camera ─────────────────────────────────────
        active_image = uploaded_file or camera_capture

        if active_image and analyse_btn:
            if uploaded_file:
                st.session_state.image      = uploaded_file.getvalue()
                st.session_state.image_name = uploaded_file.name
            else:
                st.session_state.image      = camera_capture.getvalue()
                st.session_state.image_name = "camera_capture.jpg"
            st.session_state.page = "result"
            st.rerun()
        elif analyse_btn and not active_image:
            st.warning(
                "⚠️ Please upload an image or take a photo first."
            )

    # ── Right side column ─────────────────────────────────────────────────────
    with side_col:

        # Recent uploads
        st.markdown("""
            <div style="background:white;
                        border:1px solid #e8f0e8;
                        border-radius:16px;
                        padding:1.5rem;
                        margin-bottom:1rem">
                <div style="font-weight:700;font-size:0.95rem;
                            color:#1a1a1a;margin-bottom:1rem">
                    🕘 Recent Uploads
                </div>
        """, unsafe_allow_html=True)

        history = st.session_state.get("history", [])
        if history:
            for item in reversed(history[-5:]):
                dot = "#2d6a2d" \
                    if "healthy" in item["disease"].lower() \
                    else "#e74c3c"
                st.markdown(f"""
                    <div style="display:flex;align-items:center;
                                gap:0.8rem;padding:0.75rem;
                                background:#f9faf9;border-radius:10px;
                                margin-bottom:0.5rem;
                                border:1px solid #e8f0e8">
                        <div style="font-size:1.6rem">🍃</div>
                        <div style="flex:1;min-width:0">
                            <div style="font-size:0.82rem;font-weight:600;
                                        color:#1a1a1a;overflow:hidden;
                                        text-overflow:ellipsis;
                                        white-space:nowrap">
                                {item['name']}
                            </div>
                            <div style="font-size:0.74rem;color:#888">
                                {item['disease']}
                            </div>
                        </div>
                        <div style="width:9px;height:9px;
                                    border-radius:50%;
                                    background:{dot};
                                    flex-shrink:0">
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="text-align:center;
                            padding:2rem 1rem;color:#ccc">
                    <div style="font-size:2rem;margin-bottom:0.5rem">
                        📂
                    </div>
                    <div style="font-size:0.85rem">No uploads yet</div>
                    <div style="font-size:0.75rem;margin-top:0.3rem;
                                color:#ddd">
                        Your recent scans will appear here
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Supported crops
        st.markdown("""
            <div style="background:white;
                        border:1px solid #e8f0e8;
                        border-radius:16px;
                        padding:1.5rem">
                <div style="font-weight:700;font-size:0.95rem;
                            color:#1a1a1a;margin-bottom:1rem">
                    🌿 Supported Crops
                </div>
                <div style="background:#f4faf4;border-radius:8px;
                            padding:0.7rem 1rem;margin-bottom:0.5rem;
                            display:flex;justify-content:space-between;
                            align-items:center;font-size:0.85rem;
                            font-weight:600;color:#2d6a2d">
                    🍅 Tomato
                    <span style="background:#e8f5e9;color:#2d6a2d;
                                 padding:0.15rem 0.5rem;
                                 border-radius:10px;
                                 font-size:0.72rem">9 diseases</span>
                </div>
                <div style="background:#f4faf4;border-radius:8px;
                            padding:0.7rem 1rem;
                            display:flex;justify-content:space-between;
                            align-items:center;font-size:0.85rem;
                            font-weight:600;color:#2d6a2d">
                    🌽 Maize (Corn)
                    <span style="background:#e8f5e9;color:#2d6a2d;
                                 padding:0.15rem 0.5rem;
                                 border-radius:10px;
                                 font-size:0.72rem">4 diseases</span>
                </div>
            </div>
        """, unsafe_allow_html=True)