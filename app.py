from currency_info import CURRENCY_INFO
import streamlit as st
from PIL import Image
from predict import predict_image

if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Smart Currency AI",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("💵 Smart Currency AI")

st.sidebar.image(
    "assets/logo.png",
    width=120
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Project**

    Smart Indian Currency Note Recognition System

    **Model**
    CNN (PyTorch)

    **Dataset**
    Indian Currency Notes Dataset

    **Developer**
    Dhrithi S V
    """
)

st.sidebar.markdown("---")

st.sidebar.success("🟢 AI Model Loaded Successfully")
st.sidebar.caption("Version 1.0")

st.sidebar.markdown("---")

st.sidebar.subheader("📈 Model Summary")

st.sidebar.write("**Architecture:** CNN")
st.sidebar.write("**Classes:** 9")
st.sidebar.write("**Image Size:** 128 × 128")
st.sidebar.write("**Framework:** PyTorch")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#1f4e79;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:30px;
}

.result-box{
    background:#ffffff;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.15);
    margin-top:20px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------

st.image(
    "assets/banner.png",
    width=600
)

st.divider()

# -----------------------------
# Upload
# -----------------------------
st.markdown("## 📤 Upload Currency Note")

uploaded_file = st.file_uploader(
    "Drag & Drop or Browse",
    type=["jpg", "jpeg", "png"],
    help="Supported formats: JPG, JPEG, PNG"
)

if uploaded_file:

    image = Image.open(uploaded_file)

    with st.spinner("🤖 AI is analyzing the currency note..."):

        prediction, confidence = predict_image(image)
        st.balloons()

    st.session_state.history.append({
    "Prediction": prediction,
    "Confidence": f"{confidence:.2f}%"
    })

    left, right = st.columns([1, 1])

    with left:

        st.image(
            image,
            caption="Uploaded Currency Note",
            use_container_width=True
        )

    with right:

        st.markdown("## 💵 Prediction")

        st.metric(
            label="Prediction",
            value=prediction
        )

        st.metric(
            label="Confidence",
            value=f"{confidence:.2f}%"
        )

        st.progress(confidence / 100)

        st.markdown("---")

        st.markdown("## 🏦 Currency Information")

        info = CURRENCY_INFO[prediction]

        st.write(f"**Denomination:** {info['Denomination']}")
        st.write(f"**Issued By:** {info['Issued By']}")
        st.write(f"**Color:** {info['Color']}")
        st.write(f"**Series:** {info['Series']}")
        st.write(f"**Status:** {info['Status']}")

st.markdown("---")

st.subheader("📜 Prediction History")

if st.session_state.history:

    for i, item in enumerate(reversed(st.session_state.history), start=1):

        st.write(
            f"{i}. {item['Prediction']} — {item['Confidence']}"
        )

if st.button("🗑 Clear History"):

    st.session_state.history = []

    st.rerun()

st.markdown("""
<div style='text-align:center;'>

### 💻 Developed By

**Dhrithi S V**

B.Tech Information Science

Smart Indian Currency Note Recognition System

Made with ❤️ using Streamlit & PyTorch

</div>
""", unsafe_allow_html=True)