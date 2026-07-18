# 💵 Smart Indian Currency Note Recognition System

An AI-powered web application that recognizes Indian currency notes using a Convolutional Neural Network (CNN). The application allows users to upload an image of a currency note and instantly predicts its denomination along with confidence and additional information.

---

## 🚀 Features

- Upload Indian currency note images
- AI-based denomination recognition
- Confidence score
- Currency information display
- Prediction history
- Modern Streamlit interface
- Multi-page application

---

## 🛠 Technologies Used

- Python
- PyTorch
- Streamlit
- OpenCV
- PIL (Pillow)
- NumPy

---

## 🧠 Deep Learning Model

- Convolutional Neural Network (CNN)
- Image Size: **128 × 128**
- Number of Classes: **9**

Supported Currency Notes:

- ₹10 (New)
- ₹10 (Old)
- ₹20
- ₹50 (New)
- ₹50 (Old)
- ₹100 (New)
- ₹100 (Old)
- ₹200
- ₹500

---

## 📂 Project Structure

```
Smart_Currency_Recognition/
│
├── app.py
├── model.py
├── predict.py
├── labels.py
├── currency_info.py
├── requirements.txt
├── currency_model.pth
│
├── pages/
├── assets/
├── sample_images/
└── screenshots/
```

---

## ▶️ Installation

```bash
git clone <repository-link>

cd Smart_Currency_Recognition

pip install -r requirements.txt

streamlit run app.py
```

## 📈 Future Enhancements

- Detect fake currency notes
- Support real-time webcam recognition
- Mobile application
- Multi-language support

---

## 👨‍💻 Developer

**Dhrithi S V**

B.Tech Information Science

Deep Learning Project
