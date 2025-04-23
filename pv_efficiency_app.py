import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="PV Efficiency Calculator", page_icon="☀️")

# App title
st.title("☀️ PV System Efficiency Calculator")
st.markdown("Estimate your solar panel system's efficiency and download reports!")

# First efficiency calculator based on energy
st.header("📊 Input System Parameters (kWh-based)")

solar_input = st.number_input("Total solar energy received (kWh)", min_value=0.0)
output_energy = st.number_input("Output energy from PV system (kWh)", min_value=0.0)

if solar_input > 0:
    efficiency = (output_energy / solar_input) * 100
    st.success(f"✅ Efficiency = {efficiency:.2f}%")
else:
    st.warning("⚠️ Please enter a valid solar input.")

# Plot simulated efficiency data
st.header("📈 Efficiency Over Time (Sample Data)")

days = list(range(1, 8))
efficiency_data = [70, 72, 68, 74, 69, 71, 73]

fig, ax = plt.subplots()
ax.plot(days, efficiency_data, marker='o', color='orange')
ax.set_xlabel("Day")
ax.set_ylabel("Efficiency (%)")
ax.set_title("Weekly PV System Efficiency")

st.pyplot(fig)

# Second efficiency calculator based on panel area and irradiance
st.header("🔧 Panel-Based Efficiency Calculator (W/m²)")

def calculate_pv_efficiency(area_m2, irradiance_w_m2, output_power_w):
    input_power = irradiance_w_m2 * area_m2
    if input_power == 0:
        return 0
    efficiency = (output_power_w / input_power) * 100
    return round(efficiency, 2)

area = st.number_input("Solar Panel Area (in m²)", min_value=0.1, value=1.6, step=0.1)
irradiance = st.number_input("Solar Irradiance (in W/m²)", min_value=100, value=1000, step=50)
output_power = st.number_input("Output Power (in W)", min_value=1, value=280, step=10)

if st.button("Calculate Efficiency"):
    efficiency = calculate_pv_efficiency(area, irradiance, output_power)
    st.success(f"⚡ Efficiency: {efficiency}%")
    st.progress(min(int(efficiency), 100))

# CSV export
st.markdown("---")
st.header("📥 Download Efficiency Data")

df = pd.DataFrame({
    "Day": days,
    "Efficiency (%)": efficiency_data
})
st.dataframe(df)

csv = df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download CSV", csv, "efficiency_data.csv", "text/csv")

st.caption("Built with ❤️ using Streamlit")

