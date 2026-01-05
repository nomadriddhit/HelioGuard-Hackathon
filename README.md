# ☀️ HelioGuard: AI-Powered Space Weather Monitor

![HelioGuard Banner](https://img.shields.io/badge/Status-Prototype_Ready-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit)

**HelioGuard** is a deep-tech solution designed to protect Earth's satellite infrastructure from solar superstorms. By analyzing real-time solar wind parameters from the **DSCOVR Satellite (L1 Point)**, it provides early warnings for Geomagnetic Storms (Kp Index > 5), giving operators a critical 15-60 minute window to activate "Safe Mode."

🚀 **Built for:** Hyperspace Innovation Hackathon 2K26 (Problem Statement #8)

---

## 🛰️ Key Features

* **📡 Real-Time Telemetry:** Fetches live Solar Wind Speed, Proton Density, and Temperature directly from **NOAA SWPC APIs**.
* **🤖 AI Prediction Module:** Uses a predictive logic model to forecast the **Kp Index** (Geomagnetic Storm Risk) for the next 4 hours.
* **🚨 Interactive Simulation:** Includes a "Mission Control" sidebar to simulate **G5-Class Solar Storms** and demonstrate the system's alert protocols.
* **📊 Live Dashboard:** Fully responsive visualization built with Streamlit.

---

## 🛠️ Technology Stack

* **Language:** Python 3.x
* **Data Sources:** NOAA Space Weather Prediction Center (SWPC), NASA DONKI API
* **Frontend:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Logic:** Scikit-Learn (Proposed for V2)

---

## ⚙️ Installation & Run Locally

To run this project on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/HelioGuard-Hackathon.git](https://github.com/YOUR_USERNAME/HelioGuard-Hackathon.git)
    cd HelioGuard-Hackathon
    ```

2.  **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the Dashboard:**
    ```bash
    streamlit run dashboard.py
    ```

---

## 📸 Screenshots

| Real-Time Monitoring | Storm Simulation (Red Alert) |
|:---:|:---:|
| <img width="1710" height="1073" alt="Screenshot 2026-01-05 at 12 54 25 PM" src="https://github.com/user-attachments/assets/bf576471-1c85-47e6-99ad-47e531be997d" />
<img width="1710" height="1073" alt="Screenshot 2026-01-05 at 12 54 45 PM" src="https://github.com/user-attachments/assets/10418b73-668b-49b2-9229-58aa62c53a87" />
|
<img width="1710" height="1073" alt="Screenshot 2026-01-05 at 12 55 06 PM" src="https://github.com/user-attachments/assets/53cc60f0-0072-42d0-9a5a-686e25f418b4" />
<img width="1710" height="1073" alt="Screenshot 2026-01-05 at 12 55 16 PM" src="https://github.com/user-attachments/assets/2fd8aefa-efb8-4002-945d-460bcdc2e9b7" /> |

---

## 👥 Team HelioGuard

* **Riddhit Sharma** (Team Leader)
* Akshat Kumar

**Institute:** Guru Tegh Bahadur Institute of Technology (GTBIT)

---

> *"Securing Earth's Orbit, One Solar Cycle at a Time."*
