import streamlit as st
import base64
from components.styles import load_styles
from components.sidebar import show_sidebar


def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def show():
    st.markdown(load_styles(), unsafe_allow_html=True)

   
    show_sidebar("landing")

    # ── Load images ───────────────────────────────────────────────────────────
    try:
        hero_b64   = img_to_base64("assets/hero_bg.jpg")
        tomato_b64 = img_to_base64("assets/tomato.jpg")
        maize_b64  = img_to_base64("assets/maize.jpg")
        tomato_src = f"data:image/jpeg;base64,{tomato_b64}"
        maize_src  = f"data:image/jpeg;base64,{maize_b64}"
        has_hero   = True
    except:
        has_hero   = False
        tomato_src = ""
        maize_src  = ""

    # ── Hero background via CSS ───────────────────────────────────────────────
    if has_hero:
        st.markdown(f"""
            <style>
            .hero-wrap {{
                background-image: url('data:image/jpeg;base64,{hero_b64}');
                background-size: cover;
                background-position: center;
            }}
            </style>
        """, unsafe_allow_html=True)

    bg      = "hero-wrap" if has_hero else ""
    overlay = ("background:linear-gradient("
               "135deg,rgba(10,40,10,0.92) 0%,"
               "rgba(5,30,5,0.40) 100%)")

    # ════════════════════════════════════════════════════════════════════════
    # NAVBAR
    # ════════════════════════════════════════════════════════════════════════
    st.markdown(f"""
        <div class="{bg}" style="width:100%">
            <div style="{overlay};padding:1rem 3rem;
                        border-bottom:1px solid rgba(255,255,255,0.1)">
                <div style="display:flex;align-items:center;gap:0.6rem">
                    <span style="font-size:1.5rem">🌿</span>
                    <div>
                        <div style="font-size:1rem;font-weight:800;
                                    color:white">PlantAI</div>
                        <div style="font-size:0.65rem;
                                    color:rgba(255,255,255,0.6)">
                            Smart Plant Health
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # HERO CONTENT
    # ════════════════════════════════════════════════════════════════════════
    st.markdown(f"""
        <div class="{bg}" style="width:100%">
            <div style="{overlay};padding:4rem 4rem 2rem">
                <div style="max-width:52%">
                    <div style="display:inline-block;
                                background:rgba(255,255,255,0.15);
                                border:1px solid rgba(255,255,255,0.3);
                                color:white;padding:0.3rem 1rem;
                                border-radius:20px;font-size:0.75rem;
                                font-weight:600;letter-spacing:1px;
                                text-transform:uppercase;
                                margin-bottom:1.5rem">AI POWERED 🌿</div>
                    <div style="font-size:3.2rem;font-weight:900;
                                color:white;line-height:1.1;
                                margin-bottom:1.2rem">
                        Smart AI for<br>
                        <span style="color:#4cda6e">Plant</span> Health
                    </div>
                    <div style="font-size:1rem;
                                color:rgba(255,255,255,0.85);
                                line-height:1.7;margin-bottom:1rem;
                                max-width:460px">
                        Detect plant diseases early, get accurate diagnosis,
                        and protect your crops with AI.
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ── Mini features bar ─────────────────────────────────────────────────────
    st.markdown(f"""
        <div class="{bg}" style="width:100%">
            <div style="{overlay};padding:0 4rem 2rem">
                <div style="display:flex;gap:2.5rem;flex-wrap:wrap;
                            padding-top:2rem;
                            border-top:1px solid rgba(255,255,255,0.15)">
                    <div style="display:flex;align-items:center;gap:0.6rem">
                        <span style="font-size:1.2rem;color:#4cda6e">⏱️</span>
                        <div>
                            <div style="font-size:0.83rem;font-weight:600;
                                        color:white">Instant Detection</div>
                            <div style="font-size:0.72rem;
                                        color:rgba(255,255,255,0.6)">
                                Results in seconds
                            </div>
                        </div>
                    </div>
                    <div style="display:flex;align-items:center;gap:0.6rem">
                        <span style="font-size:1.2rem;color:#4cda6e">🎯</span>
                        <div>
                            <div style="font-size:0.83rem;font-weight:600;
                                        color:white">High Accuracy</div>
                            <div style="font-size:0.72rem;
                                        color:rgba(255,255,255,0.6)">
                                Deep learning model
                            </div>
                        </div>
                    </div>
                    <div style="display:flex;align-items:center;gap:0.6rem">
                        <span style="font-size:1.2rem;color:#4cda6e">💊</span>
                        <div>
                            <div style="font-size:0.83rem;font-weight:600;
                                        color:white">Treatment Guides</div>
                            <div style="font-size:0.72rem;
                                        color:rgba(255,255,255,0.6)">
                                Actionable solutions
                            </div>
                        </div>
                    </div>
                    <div style="display:flex;align-items:center;gap:0.6rem">
                        <span style="font-size:1.2rem;color:#4cda6e">🤖</span>
                        <div>
                            <div style="font-size:0.83rem;font-weight:600;
                                        color:white">AI Assistant</div>
                            <div style="font-size:0.72rem;
                                        color:rgba(255,255,255,0.6)">
                                24/7 Plant Support
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ── Magnifier visual ──────────────────────────────────────────────────────
    st.markdown(f"""
        <div class="{bg}" style="width:100%">
            <div style="{overlay};padding:0 4rem 4rem;
                        display:flex;justify-content:flex-end">
                <div style="width:300px;height:300px;position:relative;
                            margin-right:4rem">
                    <div style="width:300px;height:300px;border-radius:50%;
                                border:6px solid rgba(76,218,110,0.6);
                                box-shadow:0 0 0 12px rgba(76,218,110,0.08),
                                           0 0 50px rgba(76,218,110,0.2);
                                overflow:hidden;position:relative;
                                background:rgba(0,40,0,0.4)">
                        <div style="position:absolute;inset:0;
                                    display:flex;align-items:center;
                                    justify-content:center;
                                    font-size:5rem;opacity:0.9">🍃</div>
                        <div style="position:absolute;bottom:25px;left:50%;
                                    transform:translateX(-50%);
                                    background:rgba(76,218,110,0.2);
                                    border:1px solid rgba(76,218,110,0.5);
                                    border-radius:8px;padding:0.3rem 0.7rem;
                                    font-size:0.72rem;color:#4cda6e;
                                    font-weight:600;white-space:nowrap">
                            🔍 Disease Detected
                        </div>
                    </div>
                    <div style="position:absolute;bottom:-45px;right:-8px;
                                width:12px;height:65px;
                                background:linear-gradient(180deg,
                                    #a0a0a0,#606060);
                                border-radius:6px;
                                transform:rotate(45deg);
                                transform-origin:top center;
                                box-shadow:2px 2px 6px rgba(0,0,0,0.4)">
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    # ── Nav strip with popovers ───────────────────────────────────────────────
    st.markdown("""
        <div style="background:#1a5c2a;padding:0.3rem 0;width:100%">
        </div>
    """, unsafe_allow_html=True)

    p1,p2,p3,p4,p5,p6 = st.columns([0.5,1,1,1,1,2])

    with p1:
        st.markdown("""
            <div style="padding:0.5rem;text-align:center;
                        font-size:0.8rem;font-weight:600;color:#4cda6e">
                🌿 Explore
            </div>
        """, unsafe_allow_html=True)

    with p2:
        with st.popover("✨ Features"):
            st.markdown("### ✨ Our Features")
            st.divider()
            st.markdown("**🔍 Instant Detection**")
            st.write("Upload a leaf photo and get a full diagnosis in seconds.")
            st.markdown("**🎯 High Accuracy**")
            st.write("Powered by MobileNetV2 with 94%+ accuracy.")
            st.markdown("**💊 Treatment Guides**")
            st.write("Every diagnosis comes with step-by-step treatment advice.")
            st.markdown("**🤖 AI Assistant**")
            st.write("Chat with our plant health bot anytime for farming advice.")
            st.markdown("**📋 Scan History**")
            st.write("Track your past scans and monitor crop health over time.")

    with p3:
        with st.popover("⚙️ How It Works"):
            st.markdown("### ⚙️ How PlantAI Works")
            st.divider()
            st.markdown("**Step 1 — Upload 📸**")
            st.write("Take a clear photo of a single leaf and upload it.")
            st.markdown("**Step 2 — AI Analyses 🧠**")
            st.write("Our model scans the image for disease patterns.")
            st.markdown("**Step 3 — Diagnosis 🔍**")
            st.write("Get disease name, confidence score, cause and symptoms.")
            st.markdown("**Step 4 — Treatment 💊**")
            st.write("Follow the treatment guide for your specific disease.")
            st.markdown("**Step 5 — Ask More 🤖**")
            st.write("Use the AI Assistant for follow-up questions.")

    with p4:
        with st.popover("🌿 Crops"):
            st.markdown("### 🌿 Supported Crops")
            st.divider()
            st.markdown("**🍅 Tomato — 9 diseases**")
            for d in ["Early Blight","Late Blight","Bacterial Spot",
                      "Leaf Mold","Septoria Leaf Spot","Spider Mites",
                      "Target Spot","Yellow Leaf Curl Virus","Mosaic Virus"]:
                st.write(f"• {d}")
            st.divider()
            st.markdown("**🌽 Maize (Corn) — 4 diseases**")
            for d in ["Common Rust","Northern Leaf Blight",
                      "Gray Leaf Spot","Healthy"]:
                st.write(f"• {d}")
            st.info("🔜 More crops coming soon!")

    with p5:
        with st.popover("ℹ️ About Us"):
            st.markdown("### ℹ️ About PlantAI")
            st.divider()
            st.markdown("**🌿 What is PlantAI?**")
            st.write("An AI-powered plant disease detection system built "
                     "to help farmers detect crop diseases early.")
            st.markdown("**🎯 Our Mission**")
            st.write("Make accurate agricultural diagnosis accessible "
                     "to every farmer — no expertise needed.")
            st.markdown("**🧠 Our Technology**")
            st.write("Built on MobileNetV2, trained on the PlantVillage "
                     "dataset with 12,000+ leaf images.")
            st.markdown("**📊 Performance**")
            st.write("• Model Accuracy: 94%+")
            st.write("• Diseases Covered: 13 classes")
            st.write("• Supported Crops: Tomato & Maize")

    # Style the nav strip buttons
    st.markdown("""
        <style>
        [data-testid="stPopover"] button {
            background: #1a5c2a !important;
            border: 1px solid #2d8a3e !important;
            border-radius: 6px !important;
            color: #ffffff !important;
            font-size: 0.88rem !important;
            font-weight: 600 !important;
            width: 100% !important;
        }
        [data-testid="stPopover"] button:hover {
            background: #2d8a3e !important;
            color: #4cda6e !important;
        }
        [data-testid="stPopover"] button p {
            color: #ffffff !important;
            font-weight: 600 !important;
        }
        [data-testid="stPopover"] button:hover p {
            color: #4cda6e !important;
        }
        </style>
    """, unsafe_allow_html=True)


    # ── CTA Buttons ───────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    b1,b2,b3,b4,b5 = st.columns([1,1.5,0.2,1.5,1])
    with b2:
        if st.button("🌿 Detect Disease",
                     key="hero_detect",
                     use_container_width=True):
            st.session_state.page = "detection"
            st.rerun()
    with b4:
        if st.button("💬 Chat with Assistant",
                     key="hero_chat",
                     use_container_width=True):
            st.session_state.page = "assistant"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # WHITE SECTION — Crops + Features + Stats
    # ════════════════════════════════════════════════════════════════════════
    st.markdown("""
        <div style="background:#ffffff;padding:2rem 1rem 0.5rem">
            <div style="font-size:0.78rem;font-weight:700;color:#2d6a2d;
                        text-transform:uppercase;letter-spacing:1.5px;
                        margin-bottom:1.5rem">🌿 Supported Crops</div>
        </div>
    """, unsafe_allow_html=True)

    left_col, right_col = st.columns([1,1], gap="large")

    with left_col:
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            if tomato_src:
                st.markdown(f"""
                    <div style="border-radius:14px;overflow:hidden;
                                box-shadow:0 4px 20px rgba(0,0,0,0.08)">
                        <img src="{tomato_src}"
                             style="width:100%;height:200px;
                                    object-fit:cover;display:block"/>
                        <div style="padding:0.8rem;text-align:center;
                                    font-weight:700;background:white">
                            🍅 Tomato
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style="border-radius:14px;background:#f4faf4;
                                height:240px;display:flex;
                                flex-direction:column;align-items:center;
                                justify-content:center;font-size:3rem">
                        🍅
                        <div style="font-size:0.95rem;font-weight:700;
                                    margin-top:0.5rem">Tomato</div>
                    </div>
                """, unsafe_allow_html=True)

        with c2:
            if maize_src:
                st.markdown(f"""
                    <div style="border-radius:14px;overflow:hidden;
                                box-shadow:0 4px 20px rgba(0,0,0,0.08)">
                        <img src="{maize_src}"
                             style="width:100%;height:200px;
                                    object-fit:cover;display:block"/>
                        <div style="padding:0.8rem;text-align:center;
                                    font-weight:700;background:white">
                            🌽 Maize (Corn)
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style="border-radius:14px;background:#f4faf4;
                                height:240px;display:flex;
                                flex-direction:column;align-items:center;
                                justify-content:center;font-size:3rem">
                        🌽
                        <div style="font-size:0.95rem;font-weight:700;
                                    margin-top:0.5rem">Maize (Corn)</div>
                    </div>
                """, unsafe_allow_html=True)

    with right_col:
        st.markdown("""
            <div style="font-size:0.78rem;font-weight:700;color:#2d6a2d;
                        text-transform:uppercase;letter-spacing:1.5px;
                        margin-bottom:1rem">🌿 Features</div>
        """, unsafe_allow_html=True)

        f1,f2,f3,f4 = st.columns(4)
        features = [
            ("🔍","Instant Detection","Results in seconds"),
            ("🎯","High Accuracy","Deep learning model"),
            ("💊","Treatment Guides","Actionable solutions"),
            ("🤖","AI Assistant","24/7 Plant Support"),
        ]
        for col,(icon,title,sub) in zip([f1,f2,f3,f4],features):
            with col:
                st.markdown(f"""
                    <div style="background:#f9faf9;border:1px solid #e8f0e8;
                                border-radius:12px;padding:1rem 0.6rem;
                                text-align:center">
                        <div style="font-size:1.6rem;
                                    margin-bottom:0.5rem">{icon}</div>
                        <div style="font-size:0.78rem;font-weight:700;
                                    color:#1a1a1a;
                                    margin-bottom:0.2rem">{title}</div>
                        <div style="font-size:0.7rem;color:#888">{sub}</div>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
            <div style="font-size:0.78rem;font-weight:700;color:#2d6a2d;
                        text-transform:uppercase;letter-spacing:1.5px;
                        margin-bottom:1rem">🌿 Statistics</div>
        """, unsafe_allow_html=True)

        s1,s2,s3,s4 = st.columns(4)
        stats = [
            ("🛡️","94.2%","Model Accuracy"),
            ("🌱","2+","Supported Crops"),
            ("🐛","20+","Diseases Detected"),
            ("👥","1000+","Users Trust Us"),
        ]
        for col,(icon,value,label) in zip([s1,s2,s3,s4],stats):
            with col:
                st.markdown(f"""
                    <div style="background:#f9faf9;border:1px solid #e8f0e8;
                                border-radius:12px;padding:1rem 0.6rem;
                                text-align:center">
                        <div style="font-size:1.6rem;
                                    margin-bottom:0.3rem">{icon}</div>
                        <div style="font-size:1.4rem;font-weight:800;
                                    color:#2d6a2d">{value}</div>
                        <div style="font-size:0.7rem;color:#888;
                                    margin-top:0.2rem">{label}</div>
                    </div>
                """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # TRUST BAR
    # ════════════════════════════════════════════════════════════════════════
    st.markdown("""
        <div style="background:#f4faf4;border-top:1px solid #e8f0e8;
                    border-bottom:1px solid #e8f0e8;padding:1.5rem 2rem;
                    display:flex;align-items:center;
                    justify-content:space-between;flex-wrap:wrap;gap:1rem">
            <div style="display:flex;align-items:center">
                <span style="font-size:1.8rem;background:white;
                             border-radius:50%;width:40px;height:40px;
                             display:inline-flex;align-items:center;
                             justify-content:center;border:2px solid #e8f0e8;
                             margin-right:-6px">👨‍🌾</span>
                <span style="font-size:1.8rem;background:white;
                             border-radius:50%;width:40px;height:40px;
                             display:inline-flex;align-items:center;
                             justify-content:center;border:2px solid #e8f0e8;
                             margin-right:-6px">👩‍🌾</span>
                <span style="font-size:1.8rem;background:white;
                             border-radius:50%;width:40px;height:40px;
                             display:inline-flex;align-items:center;
                             justify-content:center;border:2px solid #e8f0e8;
                             margin-right:-6px">👨‍🍀</span>
                <span style="font-size:1.8rem;background:white;
                             border-radius:50%;width:40px;height:40px;
                             display:inline-flex;align-items:center;
                             justify-content:center;
                             border:2px solid #e8f0e8">👩‍🍀</span>
                <div style="margin-left:1rem">
                    <div style="font-weight:700;color:#2d6a2d;
                                font-size:0.9rem">1K+</div>
                    <div style="font-size:0.75rem;color:#666">
                        Happy Farmers
                    </div>
                </div>
            </div>
            <div style="display:flex;align-items:center;gap:0.8rem;
                        color:#666;font-size:0.85rem">
                <strong style="color:#1a1a1a">Available on</strong>
                <span style="font-size:1.3rem">🌐</span>
                <span style="font-size:1.3rem">▶️</span>
                <span style="font-size:1.3rem">🍎</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    tb1,tb2,tb3 = st.columns([1,1,5])
    with tb1:
        if st.button("Get Started →",
                     key="trust_gs",
                     use_container_width=True):
            st.session_state.page = "detection"
            st.rerun()
    with tb2:
        if st.button("Learn More →",
                     key="trust_lm",
                     use_container_width=True):
            st.session_state.page = "detection"
            st.rerun()

    # ════════════════════════════════════════════════════════════════════════
    # FOOTER
    # ════════════════════════════════════════════════════════════════════════
    st.markdown("""
        <div style="display:flex;justify-content:space-between;
                    align-items:center;padding:1.2rem 2rem;
                    background:white;border-top:1px solid #e8f0e8;
                    flex-wrap:wrap;gap:1rem">
            <div style="font-size:0.82rem;color:#999">
                © 2026 PlantAI. All rights reserved.
            </div>
            <div style="display:flex;gap:1rem;font-size:1.3rem">
                <span>📘</span>
                <span>🐦</span>
                <span>📸</span>
            </div>
        </div>
    """, unsafe_allow_html=True)