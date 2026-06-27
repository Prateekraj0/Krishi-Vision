<div align="center">

# 🌿 Krishi-Vision
### AI-Powered Plant Disease Detection System

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/TensorFlow-Keras-FF6F00?style=for-the-badge&logo=tensorflow"/>
<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi"/>
<img src="https://img.shields.io/badge/HTML5-CSS3-JavaScript-orange?style=for-the-badge&logo=html5"/>
<img src="https://img.shields.io/badge/OpenWeatherMap-API-yellow?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge"/>

### 🌱 Detect Plant Diseases in Seconds using Deep Learning

AI-powered crop disease detection with treatment suggestions, weather monitoring, and a modern responsive web interface.

</div>

---

# 📖 About

PlantCare AI is an intelligent web application that helps farmers, gardeners, and agriculture enthusiasts identify plant diseases simply by uploading an image of a plant leaf.

The application uses a Deep Learning model trained on thousands of plant leaf images to detect diseases with high accuracy and instantly provides:

- 🌿 Plant Name
- 🦠 Disease Name
- 📈 Confidence Score
- 💊 Treatment Suggestions
- 📚 Disease Description
- 🌦 Live Weather Information
- 🌱 Crop Disease Risk Analysis

---

# ✨ Features

## 🤖 AI Disease Detection

- Upload any plant leaf image
- Instant prediction using Deep Learning
- Confidence percentage
- Top predictions
- Supports 38 plant disease classes

---

## 🌦 Live Weather Monitoring

- Current Temperature
- Humidity
- Wind Speed
- Weather Condition
- Rain Probability
- Disease Risk Alert

Powered using **OpenWeatherMap API**

---

## 🌱 Disease Information

For every detected disease the system provides:

- Description
- Symptoms
- Causes
- Prevention
- Treatment
- Severity Level

---

## 📊 Dashboard

The application also displays:

- Total Scans
- Healthy Plants
- Diseased Plants
- Crop Health Index
- Active Users

---

# 🧠 Model Information

| Property | Value |
|----------|-------|
| Model | MobileNetV2 |
| Framework | TensorFlow / Keras |
| Input Size | 224 × 224 RGB |
| Output Classes | 38 |
| Loss Function | Categorical Crossentropy |
| Optimizer | Adam |
| Activation | Softmax |

---

# 🌿 Supported Plant Categories

✅ Apple

✅ Blueberry

✅ Cherry

✅ Corn

✅ Grape

✅ Orange

✅ Peach

✅ Pepper

✅ Potato

✅ Raspberry

✅ Soybean

✅ Squash

✅ Strawberry

✅ Tomato

---

# 📂 Project Structure

```text
PlantCare-AI/
│
├── app.py
├── index.html
├── plant_disease_model.keras
├── class_names.json
├── README.md
--
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/PlantCare-AI.git
```

```bash
cd PlantCare-AI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install fastapi
pip install uvicorn
pip install tensorflow
pip install pillow
pip install numpy
pip install python-multipart
```

or

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python app.py
```

Open your browser

```
http://localhost:8000
```

---

# 🛠 Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- FastAPI
- Python

### Deep Learning

- TensorFlow
- Keras
- MobileNetV2

### Image Processing

- Pillow
- NumPy

### Weather API

- OpenWeatherMap

---

# 🚀 Workflow

```text
Upload Image

      │

      ▼

Image Preprocessing

      │

      ▼

Deep Learning Model

      │

      ▼

Disease Prediction

      │

      ▼

Treatment Recommendation

      │

      ▼

Display Weather & Disease Risk
```

---

# 📈 Future Improvements

- 📱 Mobile Application
- 🌍 Multi-language Support
- 📸 Camera-based Detection
- 📊 Farmer Analytics Dashboard
- 🌾 Fertilizer Recommendation
- 💬 AI Chatbot for Farmers
- ☁️ Cloud Deployment
- 📍 GPS-based Weather Alerts

---

# 💡 Why PlantCare AI?

✔ Fast Disease Detection

✔ User Friendly Interface

✔ Modern Responsive Design

✔ AI Powered

✔ Live Weather Updates

✔ Treatment Suggestions

✔ Crop Health Monitoring

✔ Easy to Deploy

---

# 🤝 Contributing

Contributions are always welcome.

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 👨‍💻 Author

## **Prateek Raj**

B.Tech Computer Science (AI & ML)

Passionate about

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Computer Vision
- Data Science
- Full Stack Development

---

<div align="center">

### ⭐ If you found this project helpful, don't forget to Star the repository!

**Made with ❤️ using Python, TensorFlow & FastAPI**

</div>
