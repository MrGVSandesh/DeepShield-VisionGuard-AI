# 🛡️ DeepShield - AI Generated Image Detection System

DeepShield is an AI-powered image forensics application that detects whether an uploaded image is **Real** or **AI-Generated** using Deep Learning and Computer Vision techniques.

The project is designed to help identify synthetic media and improve digital content authenticity verification.

---

<img width="583" height="633" alt="image" src="https://github.com/user-attachments/assets/305c8633-eac2-49c0-9796-0df186e8b830" />


## 🚀 Features

- Detects AI-generated and real images
- User-friendly Streamlit web interface
- Real-time image prediction
- Deep Learning based classification
- Upload and analyze images instantly
- Lightweight and deployable on Streamlit Cloud

---

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- OpenCV
- NumPy
- Pillow (PIL)

---

## 📂 Project Structure

```bash
DeepShield/
│
├── app.py
├── model.h5
├── requirements.txt
├── runtime.txt
├── README.md
└── assets/
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/deepshield.git
cd deepshield
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / Mac
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## ☁️ Streamlit Deployment

### runtime.txt

```txt
python-3.10
```

### requirements.txt

```txt
streamlit
tensorflow==2.15.0
numpy
pillow
opencv-python-headless
```

---

## 📸 How It Works

1. Upload an image
2. Model preprocesses image
3. Deep learning model analyzes visual patterns
4. Prediction displayed:
   - ✅ Real Image
   - ⚠️ AI Generated Image

---

## 🎯 Applications

- Fake media detection
- Digital forensics
- Cybersecurity
- Social media verification
- AI-generated content analysis

---

## 🔮 Future Enhancements

- Confidence score visualization
- Heatmap detection
- Video deepfake detection
- Multi-model ensemble prediction
- Mobile application deployment

---

## 👨‍💻 Author

**Sai Sandesh Udandarao**

---

## 📜 License

This project is developed for educational and research purposes.
