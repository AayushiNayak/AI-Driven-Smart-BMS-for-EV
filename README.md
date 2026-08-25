# 🔋 AI-Driven Smart Battery Management System for Electric Vehicles

An AI-based Battery Management System (BMS) for **Lithium-Ion batteries** that uses a **Machine Learning / Deep Learning-based predictive framework** to estimate the **State of Charge (SOC)** and **State of Health (SOH)**. The project also includes an interactive **Streamlit dashboard** for battery monitoring, prediction, analytics, and visualization.

---

## 📌 Project Overview

Battery Management Systems are essential for monitoring the performance, safety, and reliability of Lithium-Ion batteries used in Electric Vehicles (EVs).

This project develops a data-driven BMS framework using an **Artificial Neural Network (ANN)** trained on the **NASA Battery Dataset** to estimate:

* 🔋 **State of Charge (SOC)**
* ❤️ **State of Health (SOH)**

The trained model is integrated into a **Streamlit-based dashboard** that allows users to enter battery parameters, generate predictions, visualize battery conditions, and analyze prediction history.

---

## 🎯 Objectives

* Develop an AI-based framework for battery condition estimation.
* Estimate SOC and SOH using battery operational parameters.
* Train and evaluate an ANN regression model.
* Apply feature scaling and preprocessing to battery data.
* Evaluate model performance using regression metrics.
* Develop an interactive Streamlit dashboard.
* Provide battery status and prediction visualization.

---

## 🧠 AI/ML Methodology

The overall workflow of the project is:

```text
NASA Battery Dataset
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
Feature Scaling
        ↓
ANN Model Training
        ↓
SOC & SOH Prediction
        ↓
Model Evaluation
        ↓
Model Serialization
        ↓
Streamlit Dashboard
        ↓
Interactive Prediction & Visualization
```

---

## 📊 Dataset

The project uses the **NASA Battery Dataset** for model development and evaluation.

The selected input features are:

| Feature                | Description                    |
| ---------------------- | ------------------------------ |
| `Voltage_measured`     | Measured battery voltage       |
| `Current_measured`     | Measured battery current       |
| `Temperature_measured` | Battery temperature            |
| `Current_charge`       | Charging current               |
| `Voltage_charge`       | Charging voltage               |
| `Cycle`                | Battery charge/discharge cycle |

### Target Variables

* **SOC — State of Charge**
* **SOH — State of Health**

---

## 🤖 ANN Model

A feedforward Artificial Neural Network was developed for multi-output regression.

### Architecture

```text
Input Layer
6 Features
    ↓
Dense Layer — 128 neurons
ReLU
    ↓
Dropout — 20%
    ↓
Dense Layer — 64 neurons
ReLU
    ↓
Dropout — 20%
    ↓
Dense Layer — 32 neurons
ReLU
    ↓
Output Layer — 2 neurons
    ↓
SOC + SOH
```

### Training Configuration

| Parameter      | Value                     |
| -------------- | ------------------------- |
| Model          | Artificial Neural Network |
| Problem Type   | Multi-output Regression   |
| Hidden Layers  | 3                         |
| Neurons        | 128 → 64 → 32             |
| Activation     | ReLU                      |
| Output Neurons | 2                         |
| Optimizer      | Adam                      |
| Loss Function  | Mean Squared Error (MSE)  |
| Regularization | Dropout                   |
| Dropout Rate   | 0.2                       |
| Batch Size     | 64                        |
| Maximum Epochs | 25                        |
| Early Stopping | Yes                       |
| Random State   | 42                        |

---

## 🖥️ Streamlit Dashboard

The trained model is integrated into an interactive Streamlit dashboard.

### Dashboard Modules

```text
🔋 AI-BMS PLATFORM
│
├── 🏠 Home Dashboard
├── ⚡ Live Prediction
├── 📊 Battery Analytics
├── 🛰 Digital Twin
├── 📜 Prediction History
└── 💡 AI Insights
```

### Live Prediction

Users can provide:

* Voltage
* Current
* Temperature
* Charging voltage
* Charging current
* Cycle count
* Battery capacity
* Time

The dashboard generates:

* SOC prediction
* SOH prediction
* Battery status
* Prediction confidence
* Inference time
* Estimated remaining capacity

---

## 🛠️ Technology Stack

### Programming

* Python

### AI / Machine Learning

* TensorFlow
* Keras
* Scikit-learn
* Artificial Neural Networks
* Regression Modeling

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib

### Dashboard

* Streamlit

### Model & Data Storage

* Keras `.keras`
* Joblib `.pkl`
* CSV

### Development Tools

* Kaggle Notebook
* Visual Studio Code
* Git
* GitHub

---

## 📁 Project Structure

```text
AI_BMS_Dashboard/
│
├── app.py
│
├── models/
│   ├── ann_soc_soh_model.keras
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── data/
│   ├── battery_50k.csv
│   └── history.csv
│
├── pages/
│   ├── _dashboard.py
│   ├── _prediction.py
│   ├── _analytics.py
│   ├── _digital_twin.py
│   ├── _insights.py
│   └── _history_page.py
│
├── utils/
│   ├── model_loader.py
│   ├── prediction_service.py
│   ├── data_loader.py
│   ├── history_manager.py
│   ├── charts.py
│   └── helper.py
│
├── metrics.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI_BMS_Dashboard
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

Start the Streamlit application using:

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## 💾 Model Files

The dashboard requires the following trained model resources:

```text
models/
├── ann_soc_soh_model.keras
├── scaler.pkl
└── feature_columns.pkl
```

* `ann_soc_soh_model.keras` → trained ANN model
* `scaler.pkl` → fitted feature scaler
* `feature_columns.pkl` → training feature order

Keeping the feature order and preprocessing consistent is important for correct inference.

---

## 🔬 Research Contribution

The project combines:

* Data-driven battery modeling
* Machine Learning
* Deep Learning
* ANN-based SOC/SOH estimation
* Battery analytics
* Interactive visualization
* Software-based BMS simulation

The system provides a software foundation that can later be extended toward real-time battery monitoring and IoT-enabled applications.

---

## 👩‍💻 Author

**Aayushi Nayak**

B.Tech — Computer Science & Engineering

---

---

⭐ If you find this project useful, consider giving the repository a star!
