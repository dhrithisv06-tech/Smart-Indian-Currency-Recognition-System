from currency_info import CURRENCY_INFO
import streamlit as st
from PIL import Image
from predict import predict_image

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Smart Currency AI",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# SESSION STATE
# ==========================================================

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:Poppins,sans-serif;
}

.stApp{
    background: linear-gradient(
        135deg,
        #f5f3ff,
        #ede9fe,
        #e0f2fe,
        #ffffff
    );
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #f5f3ff 0%,
        #ede9fe 50%,
        #e0f2fe 100%
    );

    border-right: 2px solid #c4b5fd;
}

/* Metric Cards */

[data-testid="metric-container"]{
    background: rgba(255,255,255,0.85);
    border:1px solid #ddd6fe;
    border-radius:18px;
    box-shadow:0 8px 20px rgba(124,58,237,0.08);
}

/* Upload */

[data-testid="stFileUploader"]{
    border:2px dashed #2563eb;
    border-radius:15px;
    padding:10px;
}

img {
    border-radius:18px;
}

/* Buttons */

..stButton>button{
    background: linear-gradient(
        135deg,
        #8b5cf6,
        #6366f1
    );
}

.stButton>button:hover{
    background: linear-gradient(
        135deg,
        #7c3aed,
        #4f46e5
    );
    transform: translateY(-2px);
}

/* Footer */

.footer{
text-align:center;
color:gray;
margin-top:60px;
padding:15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "assets/logo.png",
        width=140
    )

    st.title("💵 Smart Currency AI")

    st.success("🟢 AI Model Online")

    st.markdown("---")

    st.subheader("📊 Project Details")

    st.write("""
🏷️ **Name**

Smart Indian Currency Note Recognition

👩‍💻 **Developer**

Dhrithi S V

🧠 **Model**

CNN

⚡ **Framework**

PyTorch

📂 **Dataset**

Indian Currency Notes Dataset
""")

    st.markdown("---")

    st.subheader("📈 Model Summary")

    c1,c2=st.columns(2)

    c1.metric("Classes","9")

    c2.metric("Images","1800")

    c3,c4=st.columns(2)

    c3.metric("Input","128×128")

    c4.metric("Accuracy","98.80%")

# ==========================================================
# HERO SECTION
# ==========================================================

st.image(
    "assets/banner.png",
    use_container_width=True
)

col1, col2, col3 = st.columns(3)

col1.success("🟢 AI Model Online")
col2.info("⚡ Ready for Prediction")
col3.success("📊 9 Classes Loaded")

st.divider()

# ==========================================================
# UPLOAD
# ==========================================================

st.divider()
st.markdown("## 📤 Upload Currency Note")

uploaded_file = st.file_uploader(
    "Choose a Currency Note Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    with st.spinner("🤖 AI is analyzing the uploaded currency note..."):
        prediction, confidence = predict_image(image)

    st.success("✅ Prediction Completed Successfully!")

    if (
        len(st.session_state.history) == 0 or
        st.session_state.history[-1]["Prediction"] != prediction
    ):
        st.session_state.history.append({
            "Prediction": prediction,
            "Confidence": f"{confidence:.2f}%"
        })

    st.write("")

    left, right = st.columns([1.1, 1])

    # ---------------------------------------------------
    # LEFT COLUMN
    # ---------------------------------------------------

    with left:

        st.markdown("### 🖼 Uploaded Image")

        st.image(
            image,
            use_container_width=True
        )

    # ---------------------------------------------------
    # RIGHT COLUMN
    # ---------------------------------------------------

    with right:

        st.markdown("### 🤖 AI Prediction")

        metric1, metric2 = st.columns(2)

        metric1.metric(
            "Detected Currency",
            prediction
        )

        metric2.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        st.write("")

        st.progress(confidence / 100)

        st.caption(
            f"Prediction Confidence : {confidence:.2f}%"
        )

        st.write("")

        if confidence >= 95:
            st.success("🟢 Excellent Confidence")
        elif confidence >= 80:
            st.warning("🟡 Good Confidence")
        else:
            st.error("🔴 Low Confidence")

    st.divider()

    # ---------------------------------------------------
    # CURRENCY INFORMATION
    # ---------------------------------------------------

    st.markdown("## 🏦 Currency Information")

    info = CURRENCY_INFO[prediction]

    c1, c2, c3 = st.columns(3)

    c4, c5 = st.columns(2)

    with c1:

        st.info(f"""
### 💰 Denomination

{info['Denomination']}
""")

    with c2:

        st.info(f"""
### 🏦 Issued By

{info['Issued By']}
""")

    with c3:

        st.info(f"""
### 🎨 Color

{info['Color']}
""")

    with c4:

        st.info(f"""
### 📄 Series

{info['Series']}
""")

    with c5:

        st.info(f"""
### ✅ Status

{info['Status']}
""")

    st.write("")

    st.balloons()

# ==========================================================
# DASHBOARD SUMMARY
# ==========================================================

st.divider()

st.subheader("📊 Dashboard Summary")

total_predictions = len(st.session_state.history)

if total_predictions > 0:

    latest = st.session_state.history[-1]["Prediction"]
    latest_confidence = st.session_state.history[-1]["Confidence"]

else:

    latest = "-"
    latest_confidence = "-"

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "📈 Total Predictions",
        total_predictions
    )

with col2:

    st.metric(
        "💵 Last Prediction",
        latest
    )

with col3:

    st.metric(
        "🎯 Last Confidence",
        latest_confidence
    )

# ==========================================================
# HISTORY
# ==========================================================

st.divider()

st.subheader("📜 Prediction History")

if len(st.session_state.history) == 0:

    st.info("No predictions yet. Upload an image to get started.")

else:

    for i, item in enumerate(reversed(st.session_state.history), start=1):

        with st.container(border=True):

            left, right = st.columns([3,1])

            with left:

                st.markdown(
                    f"""
### 💵 {item['Prediction']}

Prediction #{i}
"""
                )

            with right:

                st.metric(
                    "Confidence",
                    item["Confidence"]
                )

# ==========================================================
# CLEAR HISTORY
# ==========================================================

st.write("")

left, center, right = st.columns([2,1,2])

with center:

    if st.button(
        "🗑 Clear History",
        use_container_width=True
    ):

        st.session_state.history = []

        st.success("History Cleared Successfully")

        st.rerun()

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""
### 💵 Smart Currency AI

Deep Learning Based
Currency Recognition
""")

with col2:

    st.success("""
### 🧠 Technology

✔ CNN

✔ PyTorch

✔ Streamlit
""")

with col3:

    st.warning("""
### 👩‍💻 Developer

Dhrithi S V

B.Tech Information Science
""")

st.markdown("---")

st.caption(
    "© 2026 Smart Indian Currency Note Recognition System | Developed by Dhrithi S V"
)