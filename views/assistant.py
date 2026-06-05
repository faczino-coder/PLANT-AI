import streamlit as st
import base64
import json
from components.styles import load_styles
from components.sidebar import show_sidebar


@st.cache_resource
def load_treatment_map():
    with open("data/treatment_map.json") as f:
        return json.load(f)


def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def get_bot_response(user_input, treatment_map):
    text = user_input.lower().strip()

    greetings = ["hi","hello","hey","good morning","good afternoon","howdy"]
    if any(text.startswith(g) for g in greetings):
        return (
            "👋 Hello! I'm PlantAI Assistant.\n\n"
            "I can help you with:\n"
            "🔍 Disease information — causes and symptoms\n"
            "💊 Treatment advice — step by step\n"
            "🛡️ Prevention tips — protect your crops\n"
            "🌿 Crop health — tomato and maize guidance\n\n"
            "What would you like to know today?"
        )

    if any(t in text for t in ["thank","thanks","thank you"]):
        return "You're welcome! 😊 Feel free to ask anything about plant diseases. 🌿"

    if any(c in text for c in ["what can you do","help me","help","your features"]):
        return (
            "🤖 Here's what I can help you with:\n\n"
            "1. Disease info — ask about any disease\n"
            "2. Treatment steps — how to treat a disease\n"
            "3. Prevention tips — how to avoid diseases\n"
            "4. Crop health tips — tomato and maize care\n"
            "5. Urgency guidance — how serious is a disease?\n\n"
            "Try asking:\n"
            "What causes early blight?\n"
            "How do I treat common rust?\n"
            "How do I prevent late blight?"
        )

    if any(w in text for w in ["supported crop","which crop","what crop"]):
        return (
            "🌿 PlantAI currently supports:\n\n"
            "🍅 Tomato — 9 diseases\n"
            "🌽 Maize (Corn) — 4 diseases\n\n"
            "Upload a leaf image on the Detection page to get started!"
        )

    if "tomato" in text and any(w in text for w in
                                ["healthy","care","tips","advice","grow"]):
        return (
            "🍅 Tomato Health Tips:\n\n"
            "💧 Water at the base — never from above\n"
            "☀️ 6 to 8 hours of sunlight daily\n"
            "🌱 Apply NPK fertilizer every 2 to 3 weeks\n"
            "✂️ Remove suckers and lower leaves regularly\n"
            "🔄 Rotate crops every season\n"
            "👁️ Check leaves weekly for early signs of disease"
        )

    if any(w in text for w in ["maize","corn"]) and \
       any(w in text for w in ["healthy","care","tips","advice","grow"]):
        return (
            "🌽 Maize Health Tips:\n\n"
            "💧 Water deeply during tasseling stage\n"
            "🌱 Top-dress with nitrogen at knee-high stage\n"
            "🌾 Maintain proper plant spacing for airflow\n"
            "🐛 Scout weekly for fall armyworm\n"
            "🔄 Rotate crops each season\n"
            "🌿 Keep field free of weeds at all times"
        )

    disease_keywords = {
        "early blight"   : "Tomato___Early_blight",
        "late blight"    : "Tomato___Late_blight",
        "bacterial spot" : "Tomato___Bacterial_spot",
        "leaf mold"      : "Tomato___Leaf_Mold",
        "septoria"       : "Tomato___Septoria_leaf_spot",
        "spider mite"    : "Tomato___Spider_mites Two-spotted_spider_mite",
        "target spot"    : "Tomato___Target_Spot",
        "yellow leaf"    : "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
        "tylcv"          : "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
        "mosaic"         : "Tomato___Tomato_mosaic_virus",
        "common rust"    : "Corn_(maize)___Common_rust_",
        "rust"           : "Corn_(maize)___Common_rust_",
        "northern leaf"  : "Corn_(maize)___Northern_Leaf_Blight",
        "gray leaf"      : "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
        "grey leaf"      : "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
        "cercospora"     : "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    }

    matched_key = None
    for keyword, class_key in disease_keywords.items():
        if keyword in text:
            matched_key = class_key
            break

    if matched_key and matched_key in treatment_map:
        info = treatment_map[matched_key]

        if any(w in text for w in ["cause","causes","why","what is","what's"]):
            return (
                f"🦠 {info['disease']} — Cause\n\n"
                f"Cause: {info['cause']}\n\n"
                f"Symptoms: {info['symptoms']}\n\n"
                f"Urgency: {info['urgency']}"
            )
        elif any(w in text for w in ["treat","treatment","cure",
                                      "fix","remedy","control","how to"]):
            steps = "\n".join(
                [f"{i}. {s}" for i, s in enumerate(info["treatment"],1)]
            )
            return (
                f"💊 {info['disease']} — Treatment\n\n"
                f"{steps}\n\n"
                f"Urgency: {info['urgency']}"
            )
        elif any(w in text for w in ["prevent","prevention","avoid","protect"]):
            tips = "\n".join([f"• {t}" for t in info.get("prevention",[])])
            return f"🛡️ {info['disease']} — Prevention\n\n{tips}"
        elif any(w in text for w in ["serious","dangerous","urgent","severe"]):
            urgency_map = {
                "None"    : "✅ Healthy — no action needed.",
                "Moderate": "🟡 Moderate. Act within a week.",
                "High"    : "🟠 High. Act within 1 to 2 days.",
                "Critical — spreads very fast":
                    "🔴 CRITICAL. Act immediately.",
                "High — no cure once infected":
                    "🔴 HIGH. Remove infected plants now."
            }
            advice = urgency_map.get(info["urgency"], info["urgency"])
            return (
                f"⚠️ {info['disease']} — Severity\n\n"
                f"{advice}\n\n"
                f"Cause: {info['cause']}"
            )
        else:
            return (
                f"🌿 {info['disease']}\n\n"
                f"Crop: {info['crop']}\n"
                f"Cause: {info['cause']}\n"
                f"Symptoms: {info['symptoms']}\n"
                f"Urgency: {info['urgency']}\n\n"
                f"Ask me:\n"
                f"How to treat {info['disease'].lower()}?\n"
                f"How to prevent {info['disease'].lower()}?"
            )

    if any(w in text for w in ["detect","scan","upload","analyse","check"]):
        return (
            "🔍 To detect plant disease:\n\n"
            "1. Click Detect Disease in the sidebar\n"
            "2. Upload a clear photo of a leaf\n"
            "3. Click Analyse Leaf\n"
            "4. Get instant diagnosis and treatment"
        )

    if any(w in text for w in ["accuracy","model","reliable","how accurate"]):
        return (
            "🎯 About Our AI Model\n\n"
            "PlantAI uses MobileNetV2 trained on PlantVillage.\n\n"
            "Accuracy: 94% and above\n"
            "Training images: 12,000 and above\n"
            "Diseases: 13 classes\n"
            "Crops: Tomato and Maize"
        )

    return (
        "🤔 I did not quite understand that.\n\n"
        "Try asking:\n"
        "What causes early blight?\n"
        "How do I treat common rust?\n"
        "How do I prevent late blight?\n"
        "Give me tomato care tips\n\n"
        "Type help to see everything I can do."
    )


def show():
    st.markdown(load_styles(), unsafe_allow_html=True)
    show_sidebar("assistant")

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
                                    color:white">🤖 AI Assistant</div>
                        <div style="font-size:0.9rem;
                                    color:rgba(255,255,255,0.8);
                                    margin-top:0.3rem">
                            Ask me anything about plant diseases!
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
                    🤖 AI Assistant
                </div>
                <div style="font-size:0.9rem;color:rgba(255,255,255,0.8);
                            margin-top:0.3rem">
                    Ask me anything about plant diseases!
                </div>
            </div>
        """, unsafe_allow_html=True)

    treatment_map = load_treatment_map()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if not st.session_state.chat_history:
        st.session_state.chat_history.append({
            "role"   : "bot",
            "message": (
                "👋 Hello! I'm PlantAI Assistant.\n\n"
                "Ask me anything about plant diseases, "
                "treatments, or crop health.\n\n"
                "Type help to see what I can do!"
            )
        })

    # Quick questions
    st.markdown("""
        <div style="font-size:0.82rem;color:#888;
                    font-weight:600;margin-bottom:0.5rem">
            💡 Quick Questions:
        </div>
    """, unsafe_allow_html=True)

    q1, q2, q3, q4 = st.columns(4)
    quick = [
        ("🌿 Early Blight?",   "What causes early blight?"),
        ("🍃 Treat Rust?",     "How do I treat common rust?"),
        ("🛡️ Prevent Blight?", "How do I prevent late blight?"),
        ("🌽 Maize Care?",     "Give me maize care tips"),
    ]
    triggered = None
    for col, (label, question) in zip([q1,q2,q3,q4], quick):
        with col:
            if st.button(label, key=f"q_{label}",
                         use_container_width=True):
                triggered = question

    # Chat display
    st.markdown("""
        <div style="background:white;border-radius:16px;
                    border:1px solid #e8f0e8;height:55vh;
                    overflow-y:auto;padding:1.5rem;
                    margin:1rem 0">
    """, unsafe_allow_html=True)

    for msg in st.session_state.chat_history:
        if msg["role"] == "bot":
            content = msg["message"].replace("\n","<br>")
            st.markdown(f"""
                <div style="display:flex;justify-content:flex-start;
                            margin:0.8rem 0">
                    <div style="display:flex;align-items:flex-start;
                                gap:0.6rem">
                        <div style="background:#2d6a2d;color:white;
                                    border-radius:50%;width:32px;height:32px;
                                    display:flex;align-items:center;
                                    justify-content:center;
                                    font-size:0.9rem;flex-shrink:0">🌿</div>
                        <div style="background:#f4faf4;color:#1a1a1a;
                                    padding:0.75rem 1.1rem;
                                    border-radius:18px 18px 18px 4px;
                                    font-size:0.88rem;max-width:70%;
                                    line-height:1.5;
                                    border:1px solid #e8f0e8">
                            {content}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="display:flex;justify-content:flex-end;
                            margin:0.8rem 0">
                    <div style="display:flex;align-items:flex-start;
                                gap:0.6rem;flex-direction:row-reverse">
                        <div style="background:#e8f5e9;border-radius:50%;
                                    width:32px;height:32px;display:flex;
                                    align-items:center;justify-content:center;
                                    font-size:0.9rem;flex-shrink:0">👤</div>
                        <div style="background:#2d6a2d;color:white;
                                    padding:0.75rem 1.1rem;
                                    border-radius:18px 18px 4px 18px;
                                    font-size:0.88rem;max-width:70%;
                                    line-height:1.5">
                            {msg["message"]}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Input row
    in_col, send_col = st.columns([5, 1])
    with in_col:
        user_input = st.text_input(
            "Message",
            key              = "chat_input",
            placeholder      = "e.g. What causes early blight?",
            label_visibility = "collapsed"
        )
    with send_col:
        send = st.button("➤ Send", key="send_btn",
                         use_container_width=True)

    if triggered:
        st.session_state.chat_history.append(
            {"role":"user","message":triggered})
        st.session_state.chat_history.append(
            {"role":"bot",
             "message":get_bot_response(triggered, treatment_map)})
        st.rerun()

    if send and user_input.strip():
        st.session_state.chat_history.append(
            {"role":"user","message":user_input.strip()})
        st.session_state.chat_history.append(
            {"role":"bot",
             "message":get_bot_response(user_input.strip(), treatment_map)})
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🗑️ Clear Chat", key="clear_chat"):
        st.session_state.chat_history = []
        st.rerun()