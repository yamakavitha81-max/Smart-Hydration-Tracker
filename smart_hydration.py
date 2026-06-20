import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import os

st.set_page_config(page_title="Smart Hydration Tracker", page_icon="💧")

st.title("💧 Smart Hydration Tracker")
st.write("Monitor your hydration based on weight, activity, and temperature.")

# USER INPUT
st.header("User Information")

weight = st.number_input("Enter your weight (kg)", min_value=1)

temperature = st.slider("Current Temperature (°C)", 10, 45, 25)

st.subheader("Activity Hours")

study_hours = st.number_input("Study Hours", min_value=0.0)
walk_hours = st.number_input("Walking Hours", min_value=0.0)
gym_hours = st.number_input("Gym Hours", min_value=0.0)
run_hours = st.number_input("Running Hours", min_value=0.0)

water_drank = st.number_input("Water consumed today (ml)", min_value=0)

# CALCULATION
if st.button("Calculate Hydration"):

    body_water = weight * 0.6
    base_need = weight * 35

    activity_loss = (
        study_hours * 50 +
        walk_hours * 150 +
        gym_hours * 400 +
        run_hours * 500
    )

    total_need = base_need + activity_loss

    if temperature > 30:
        total_need += 400

    hydration_percent = (water_drank / total_need) * 100

    # HYDRATION STATUS
    if hydration_percent < 50:
        rating = "❌ Poor Hydration"
    elif hydration_percent < 80:
        rating = "⚠️ Moderate Hydration"
    else:
        rating = "✅ Excellent Hydration"

    # RESULTS
    st.header("Hydration Summary")

    st.metric("Body Water Estimate", f"{body_water:.2f} L")
    st.metric("Activity Water Loss", f"{activity_loss:.0f} ml")
    st.metric("Recommended Intake", f"{total_need:.0f} ml")
    st.metric("Water Consumed", f"{water_drank} ml")

    st.subheader("Hydration Level")

    st.progress(min(int(hydration_percent),100))
    st.write(f"Hydration Level: {hydration_percent:.1f}%")
    st.write(f"Hydration Rating: {rating}")

    glasses = total_need / 250
    st.write(f"🥤 Recommended glasses of water: {glasses:.1f}")

    # PERSONAL TIPS
    st.subheader("Hydration Tips")

    if hydration_percent < 50:
        st.warning("Drink water immediately and increase intake during activities.")
    elif hydration_percent < 80:
        st.info("Try to drink 1–2 more glasses of water today.")
    else:
        st.success("Great! Your hydration level is healthy.")

    # SAVE DATA
    today = date.today()

    new_data = pd.DataFrame({
        "date":[today],
        "intake_ml":[water_drank],
        "required_ml":[total_need],
        "hydration_percent":[hydration_percent]
    })

    file = "hydration_data.csv"

    if os.path.exists(file):
        old = pd.read_csv(file)
        data = pd.concat([old,new_data],ignore_index=True)
    else:
        data = new_data

    data.to_csv(file,index=False)

    st.success("Data saved successfully!")

# HISTORY GRAPH
st.header("Hydration History")

file = "hydration_data.csv"

if os.path.exists(file):

    data = pd.read_csv(file)

    fig, ax = plt.subplots()

    ax.plot(data["date"], data["intake_ml"], marker="o", label="Water Intake")
    ax.plot(data["date"], data["required_ml"], marker="o", label="Required Intake")

    ax.set_xlabel("Date")
    ax.set_ylabel("Water (ml)")
    ax.set_title("Hydration Tracking Over Time")
    ax.legend()

    st.pyplot(fig)

    # DOWNLOAD BUTTON
    st.download_button(
        "Download Hydration Data",
        data.to_csv(index=False),
        file_name="hydration_history.csv",
        mime="text/csv"
    )

else:
    st.write("No hydration history yet.")
    
    
    
