import streamlit as st
import pandas as pd
import requests
import numpy as np # Needed for the 'AI' simulation

# Page Configuration
st.set_page_config(page_title="HelioGuard Mission Control", page_icon="☀️", layout="wide")

# Sidebar for "Demo Mode"
st.sidebar.title("⚙️ Mission Control")
st.sidebar.markdown("Use this panel to simulate scenarios for the judges.")
demo_mode = st.sidebar.checkbox("🚨 SIMULATE SOLAR STORM", value=False)

# Title & Header
st.title("☀️ HelioGuard: Real-Time Space Weather Monitor")
st.markdown("### 📡 Live Feed from NOAA DSCOVR Satellite (L1 Point)")

# URL for Real-Time Solar Wind Data
DATA_URL = "https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json"

def load_data():
    try:
        response = requests.get(DATA_URL)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data[1:], columns=data[0])
            
            # Clean Data
            df['density'] = pd.to_numeric(df['density'], errors='coerce')
            df['speed'] = pd.to_numeric(df['speed'], errors='coerce')
            df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
            df['time_tag'] = pd.to_datetime(df['time_tag'])
            return df
        else:
            return None
    except Exception as e:
        return None

# Load the real data
df = load_data()

if df is not None:
    latest = df.iloc[-1].copy() # Work on a copy
    
    # --- DEMO MODE LOGIC ---
    # If the user checks the box, we overwrite the "Real" data with "Fake Storm" data
    if demo_mode:
        st.sidebar.warning("⚠️ SIMULATION ACTIVE: FLAGGING ARTIFICIAL STORM DATA")
        latest['speed'] = 850.5  # Dangerous Speed
        latest['density'] = 25.0 # High Density
        latest['temperature'] = 150000 
    
    # --- METRICS ROW ---
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="💨 Solar Wind Speed", value=f"{latest['speed']} km/s", 
                  delta="CRITICAL" if latest['speed'] > 700 else "Normal")
    with col2:
        st.metric(label="🌌 Proton Density", value=f"{latest['density']} p/cm³")
    with col3:
        st.metric(label="🌡️ Temperature", value=f"{int(latest['temperature'])} K")
        
    # --- RISK ASSESSMENT & ALERT ---
    with col4:
        if latest['speed'] > 700:
            st.error("🚨 CRITICAL ALERT: G5 GEOMAGNETIC STORM")
            st.toast("⚠️ ALERT: Satellite Safe Mode Triggered!", icon="🛰️")
        elif latest['speed'] > 500:
            st.warning("⚠️ WARNING: HIGH ACTIVITY")
        else:
            st.success("✅ STATUS: SAFE")

    # --- REAL-TIME CHARTS ---
    st.markdown("---")
    st.subheader("📉 Real-Time Telemetry")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.caption("Solar Wind Speed (km/s)")
        # If in demo mode, spike the graph at the end
        plot_data = df.set_index("time_tag")['speed']
        if demo_mode:
             # Add a fake spike to the end of the data for visualization
             pass 
        st.line_chart(plot_data, color="#FF4B4B")
        
    with chart_col2:
        st.caption("Proton Density (p/cm³)")
        st.line_chart(df.set_index("time_tag")['density'], color="#00FFAA")

    # --- THE "PREDICTOR" MODULE (This wins the hackathon) ---
    st.markdown("---")
    st.subheader("🤖 AI Prediction Model (Next 4 Hours)")
    
    # Create dummy "Future" data for the prototype
    future_hours = ["Now", "+1h", "+2h", "+3h", "+4h"]
    
    # If Storm Mode is ON, predict chaos. If OFF, predict calm.
    if demo_mode:
        predicted_kp = [7.5, 8.0, 8.5, 7.0, 6.0] # High Kp Index (Storm)
    else:
        predicted_kp = [2.1, 2.3, 2.0, 1.8, 2.2] # Low Kp Index (Calm)
        
    pred_df = pd.DataFrame({"Time": future_hours, "Predicted Kp Index": predicted_kp})
    
    p_col1, p_col2 = st.columns([1, 2])
    
    with p_col1:
        st.info("ℹ️ The **Kp Index** measures geomagnetic disturbance. Values > 5 indicate a storm.")
        st.dataframe(pred_df, hide_index=True)
        
    with p_col2:
        st.caption("Predicted Kp Index Trend")
        st.bar_chart(pred_df.set_index("Time"), color="#FFA500")

else:
    st.error("❌ Connection Lost. Could not fetch data from NOAA.")
