import streamlit as st
import numpy as np
import base64
import json
import io
from PIL import Image
import tensorflow as tf
from components.styles import load_styles
from components.sidebar import show_sidebar


@st.cache_resource
def load_model():
    import gdown
    import os
    model_path = "models/plant_disease_model.h5"
    if not os.path.exists(model_path):
        os.makedirs("models", exist_ok=True)
        with st.spinner("⏳ Loading AI model for first time..."):
            gdown.download(
                "https://drive.google.com/uc?id=1afkCBR7LyK2kbg7LoxFZesLbN3ba1Sr2",
                model_path,
                quiet=False
            )
    return tf.keras.models.load_model(model_path)

@st.cache_resource
def load_configs():
    with open("data/label_map.json")     as f: label_map     = json.load(f)
    with open("data/treatment_map.json") as f: treatment_map = json.load(f)
    return label_map, treatment_map


def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def predict(image, model, label_map):
    img_array   = np.array(image.resize((224,224)).convert("RGB")) / 255.0
    predictions = model.predict(np.expand_dims(img_array,0), verbose=0)[0]
    top3_idx    = predictions.argsort()[-3:][::-1]
    return [
        {
            "class"     : label_map["idx_to_class"][str(i)],
            "confidence": float(predictions[i]) * 100
        }
        for i in top3_idx
    ]


def show():
    st.markdown(load_styles(), unsafe_allow_html=True)
    show_sidebar("detection")
    # ── Banner ────────────────────────────────────────────────────────────────
    try:
        b64 = img_to_base64("assets/tomato.jpg")
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
                                    color:white">📊 Prediction Result</div>
                        <div style="font-size:0.9rem;
                                    color:rgba(255,255,255,0.8);
                                    margin-top:0.3rem">
                            AI-powered diagnosis of your uploaded leaf
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
                    📊 Prediction Result
                </div>
                <div style="font-size:0.9rem;color:rgba(255,255,255,0.8);
                            margin-top:0.3rem">
                    AI-powered diagnosis of your uploaded leaf
                </div>
            </div>
        """, unsafe_allow_html=True)

    # ── Check image ───────────────────────────────────────────────────────────
    if not st.session_state.get("image"):
        st.warning("⚠️ No image found. Please upload a leaf image first.")
        if st.button("← Go to Detection", key="go_detect"):
            st.session_state.page = "detection"
            st.rerun()
        return

    model                    = load_model()
    label_map, treatment_map = load_configs()

    image      = Image.open(
        io.BytesIO(st.session_state.image)).convert("RGB")
    image_name = st.session_state.get("image_name", "leaf.jpg")

    with st.spinner("🔍 Analysing your leaf..."):
        top3       = predict(image, model, label_map)
        best       = top3[0]
        best_class = best["class"]
        confidence = best["confidence"]
        info       = treatment_map.get(best_class, None)

    # Save to history
    if "history" not in st.session_state:
        st.session_state.history = []
    disease_name = info["disease"] if info else best_class.replace("_"," ")
    crop_name    = info["crop"]    if info else "Unknown"
    entry = {
        "name": image_name, "disease": disease_name,
        "crop": crop_name,  "confidence": confidence
    }
    if not st.session_state.history or \
       st.session_state.history[-1]["name"] != image_name:
        st.session_state.history.append(entry)

    is_healthy = "healthy" in best_class.lower()
    urgency    = info["urgency"]  if info else "Unknown"
    cause      = info["cause"]    if info and info["cause"] else ""
    symptoms   = info["symptoms"] if info and info["symptoms"] else ""

    if is_healthy:
        conf_color   = "#2d6a2d"
        border_color = "#c8e6c9"
        bg_color     = "#f4faf4"
        icon         = "✅"
    elif "critical" in urgency.lower():
        conf_color   = "#e74c3c"
        border_color = "#ffcdd2"
        bg_color     = "#fff5f5"
        icon         = "🚨"
    else:
        conf_color   = "#e67e22"
        border_color = "#ffe0b2"
        bg_color     = "#fffbf5"
        icon         = "⚠️"

    # ── Result layout ─────────────────────────────────────────────────────────
    img_col, res_col = st.columns([1, 1.5], gap="large")

    with img_col:
        st.image(image, use_column_width=True,
                 caption=f"📸 {image_name}")

        # Top 3
        st.markdown("""
            <div style="background:white;border:1px solid #e8f0e8;
                        border-radius:14px;padding:1.2rem;margin-top:1rem">
                <div style="font-size:0.78rem;font-weight:700;color:#888;
                            text-transform:uppercase;letter-spacing:0.5px;
                            margin-bottom:0.8rem">
                    📊 Top 3 Predictions
                </div>
        """, unsafe_allow_html=True)

        for i, pred in enumerate(top3, 1):
            name = (pred["class"]
                    .replace("Corn_(maize)___","Corn: ")
                    .replace("Tomato___","Tomato: ")
                    .replace("_"," "))
            conf      = pred["confidence"]
            bar_color = "#2d6a2d" if i == 1 else "#a5d6a7"
            fw        = "700" if i == 1 else "400"
            bar_html  = (
                f"<div style='background:#e8f0e8;border-radius:6px;"
                f"height:6px;overflow:hidden'>"
                f"<div style='width:{conf}%;height:6px;"
                f"background:{bar_color};border-radius:6px'></div>"
                f"</div>"
            )
            row_html = (
                f"<div style='margin-bottom:0.8rem'>"
                f"<div style='display:flex;justify-content:space-between;"
                f"font-size:0.8rem;margin-bottom:3px'>"
                f"<span style='color:#333;font-weight:{fw}'>#{i} {name}</span>"
                f"<span style='color:{bar_color};font-weight:600'>"
                f"{conf:.1f}%</span></div>"
                + bar_html
                + "</div>"
            )
            st.markdown(row_html, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with res_col:
        # Build result card safely
        urgency_badge = (
            f"<span style='background:{conf_color}20;color:{conf_color};"
            f"padding:0.25rem 0.8rem;border-radius:20px;"
            f"font-size:0.8rem;font-weight:700'>{urgency}</span>"
        )
        conf_bar = (
            f"<div style='background:#e8f0e8;border-radius:10px;"
            f"height:10px;overflow:hidden'>"
            f"<div style='width:{confidence}%;height:10px;"
            f"background:{conf_color};border-radius:10px'></div>"
            f"</div>"
        )
        cause_html = (
            f"<div style='margin-top:0.8rem'>"
            f"<div style='font-size:0.78rem;font-weight:700;color:#1a1a1a;"
            f"text-transform:uppercase;letter-spacing:0.5px;"
            f"margin-bottom:0.4rem'>🦠 Cause</div>"
            f"<div style='font-size:0.88rem;color:#555'>{cause}</div>"
            f"</div>"
        ) if cause else ""

        symptoms_html = (
            f"<div style='margin-top:0.8rem'>"
            f"<div style='font-size:0.78rem;font-weight:700;color:#1a1a1a;"
            f"text-transform:uppercase;letter-spacing:0.5px;"
            f"margin-bottom:0.4rem'>👁️ Symptoms</div>"
            f"<div style='font-size:0.88rem;color:#555'>{symptoms}</div>"
            f"</div>"
        ) if symptoms else ""

        result_html = (
            f"<div style='background:{bg_color};border:1px solid {border_color};"
            f"border-radius:16px;padding:1.8rem;margin-bottom:1rem'>"
            f"<div style='font-size:1.6rem;font-weight:800;color:#1a1a1a'>"
            f"{icon} {disease_name}"
            f"<span style='display:inline-block;background:#e8f5e9;"
            f"color:#2d6a2d;padding:0.2rem 0.8rem;border-radius:20px;"
            f"font-size:0.8rem;font-weight:600;margin-left:0.8rem;"
            f"vertical-align:middle'>{crop_name}</span>"
            f"</div>"
            f"<div style='font-size:0.75rem;color:#888;margin:0.8rem 0 0.3rem;"
            f"font-weight:600;text-transform:uppercase'>Confidence Score</div>"
            f"<div style='font-size:1.4rem;font-weight:800;color:{conf_color};"
            f"margin-bottom:0.4rem'>{confidence:.1f}%</div>"
            + conf_bar
            + f"<div style='margin-top:0.8rem'>{urgency_badge}</div>"
            + cause_html
            + symptoms_html
            + "</div>"
        )
        st.markdown(result_html, unsafe_allow_html=True)

        # Treatment card
        if info:
            st.markdown("""
                <div style="background:white;border:1px solid #e8f0e8;
                            border-radius:16px;padding:1.8rem">
                    <div style="font-size:0.78rem;font-weight:700;
                                color:#1a1a1a;text-transform:uppercase;
                                letter-spacing:0.5px;margin-bottom:0.8rem">
                        💊 Treatment Steps
                    </div>
            """, unsafe_allow_html=True)

            for step in info["treatment"]:
                st.markdown(f"""
                    <div style="display:flex;align-items:flex-start;
                                gap:0.6rem;font-size:0.88rem;color:#333;
                                margin:0.5rem 0;line-height:1.5">
                        <span style="color:#2d6a2d;font-weight:700;
                                     flex-shrink:0">✓</span>
                        <span>{step}</span>
                    </div>
                """, unsafe_allow_html=True)

            if info.get("prevention"):
                st.markdown("""
                    <div style="font-size:0.78rem;font-weight:700;
                                color:#1a1a1a;text-transform:uppercase;
                                letter-spacing:0.5px;
                                margin:1.2rem 0 0.8rem">
                        🛡️ Prevention
                    </div>
                """, unsafe_allow_html=True)
                for tip in info["prevention"]:
                    st.markdown(f"""
                        <div style="display:flex;align-items:flex-start;
                                    gap:0.6rem;font-size:0.88rem;color:#333;
                                    margin:0.5rem 0;line-height:1.5">
                            <span style="color:#1565c0;flex-shrink:0">🔹</span>
                            <span>{tip}</span>
                        </div>
                    """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        # Buttons
        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2 = st.columns(2)
        with b1:
            if st.button("📥 Download Report",
                         key="dl_rpt",
                         use_container_width=True):
                report = (
                    f"PLANTAI DIAGNOSIS REPORT\n"
                    f"{'='*30}\n"
                    f"Image      : {image_name}\n"
                    f"Crop       : {crop_name}\n"
                    f"Disease    : {disease_name}\n"
                    f"Confidence : {confidence:.1f}%\n"
                    f"Urgency    : {urgency}\n\n"
                    f"CAUSE\n{cause or 'N/A'}\n\n"
                    f"SYMPTOMS\n{symptoms or 'N/A'}\n\n"
                    f"TREATMENT\n"
                )
                if info:
                    for i, s in enumerate(info["treatment"], 1):
                        report += f"{i}. {s}\n"
                    report += "\nPREVENTION\n"
                    for t in info.get("prevention", []):
                        report += f"• {t}\n"
                report += "\nGenerated by PlantAI\n"
                st.download_button(
                    "📄 Save Report",
                    data      = report,
                    file_name = f"PlantAI_Report.txt",
                    mime      = "text/plain",
                    key       = "save_rpt"
                )
        with b2:
            if st.button("🔍 New Prediction",
                         key="new_pred",
                         use_container_width=True):
                st.session_state.image = None
                st.session_state.page  = "detection"
                st.rerun()

        st.markdown("""
            <div style="text-align:center;color:#bbb;font-size:0.78rem;
                        margin-top:2rem;padding-top:1rem;
                        border-top:1px solid #e8f0e8">
                ⚠️ For guidance only.
                Consult a professional agronomist for severe cases.
            </div>
        """, unsafe_allow_html=True)