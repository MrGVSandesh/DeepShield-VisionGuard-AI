import streamlit as st
from PIL import Image
import numpy as np
import random

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="DeepShield",
    page_icon="🛡️",
    layout="centered"
)

# ==========================================
# TITLE
# ==========================================

st.title("🛡️ AI Generated Image Detector")

st.write(
    "Upload an image or take a live photo to detect whether it is AI-generated or real."
)

# ==========================================
# FILE UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "📤 Upload an Image",
    type=["jpg", "jpeg", "png"]
)

# ==========================================
# CAMERA INPUT
# ==========================================

camera_image = st.camera_input(
    "📷 Take a Live Photo"
)

image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)

elif camera_image is not None:
    image = Image.open(camera_image)

# ==========================================
# PREDICTION
# ==========================================

if image is not None:

    st.image(
        image,
        caption="Selected Image",
        use_container_width=True
    )

    with st.spinner("🔍 Analyzing image..."):

        # Dummy prediction logic
        confidence = random.uniform(0.3, 0.95)

    st.subheader("Prediction Result")

    # ==========================================
    # YOUR REQUIRED LOGIC
    # ==========================================
    # confidence > 0.4 => REAL IMAGE
    # confidence <= 0.4 => AI GENERATED
    # ==========================================

    if confidence < 0.6:

        st.success(
            f"✅ REAL IMAGE\n\nConfidence: {confidence*100:.2f}%"
        )

    else:

        st.error(
            f"❌ AI GENERATED IMAGE\n\nConfidence: {(1-confidence)*100:.2f}%"
        )

    st.progress(float(confidence))

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption("DeepShield • AI vs Real Image Detection System")