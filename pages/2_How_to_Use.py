import streamlit as st

st.set_page_config(page_title="How to Use", page_icon="📖")

st.title("📖 User Guide")

st.markdown("""
### Step 1

Upload an image of an Indian currency note.

### Step 2

Wait a few seconds.

### Step 3

The AI model predicts the denomination.

### Step 4

View the confidence score and currency details.

---

### Supported Notes

- ₹10 (New)
- ₹10 (Old)
- ₹20
- ₹50 (New)
- ₹50 (Old)
- ₹100 (New)
- ₹100 (Old)
- ₹200
- ₹500
""")