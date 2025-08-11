import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

<script>
  let storedData = [];

  document.getElementById("myForm").onsubmit = function (e) {
    e.preventDefault();
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    storedData.push({ FirstName: firstName, LastName: lastName });
    alert("Data saved locally!");
    this.reset();
  };

  function displayData() {
    document.getElementById("output").innerHTML =
      '<pre>' + JSON.stringify(storedData, null, 2) + '</pre>';
  }
</script>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>JSON Form</title>

  <!-- Load Bootstrap CSS from CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />

  <!-- Custom styles -->
  <style>
    body {
      font-family: Arial;
      margin: 40px;
    }
    .form-group {
      margin-bottom: 20px;
    }
    #output pre {
      background: #f0f0f0;
      padding: 10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2 class="text-center">Enter Your Details</h2>
    <form id="myForm" class="row g-3">
      <div class="col-md-6">
        <label for="firstName" class="form-label">First Name:</label>
        <input type="text" id="firstName" class="form-control" placeholder="Enter First Name" required />
      </div>
      <div class="col-md-6">
        <label for="lastName" class="form-label">Last Name:</label>
        <input type="text" id="lastName" class="form-control" placeholder="Enter Last Name" required />
      </div>
      <div class="col-12">
        <button type="submit" class="btn btn-primary">Submit</button>
        <button type="button" class="btn btn-secondary" onclick="displayData()">Display JSON Data</button>
      </div>
    </form>

    <div id="output" class="mt-4"></div>
  </div>

  <!-- JavaScript for handling form submission and displaying data -->
  <script>
    // Handle form submission
    document.getElementById("myForm").onsubmit = async function (e) {
      e.preventDefault();
      const firstName = document.getElementById("firstName").value;
      const lastName = document.getElementById("lastName").value;

      const res = await fetch("/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ FirstName: firstName, LastName: lastName }),
      });

      alert(await res.text());
      this.reset();
    };

    // Fetch and display JSON data
    async function displayData() {
      const res = await fetch("/data");
      const json = await res.json();
      document.getElementById("output").innerHTML = '<pre>' + JSON.stringify(json, null, 2) + '</pre>';
    }
  </script>
</body>
</html>

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

import React, { useState } from 'react';
import './Login.css'; // reusing same styles

const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = (e) => {
    e.preventDefault();
    console.log("Registering:", { username, password });
    // Add your registration logic here (API call etc.)
  };

  return (
    <div className="login-container">
      <h2>Register</h2>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
};

export default Register;

/* Login.css */

.login-container {
  width: 300px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.login-container h2 {
  text-align: center;
  margin-bottom: 20px;
}

.login-container input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.login-container button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  border: none;
  color: white;
  font-weight: bold;
  border-radius: 4px;
  cursor: pointer;
}

.login-container button:hover {
  background-color: #0056b3;
}
This is the Checkers page for User Story 4. 
At the top, we’ve got a clean navigation bar with quick links, notifications,
and messages so users can access everything without leaving the page. 
The main section is focused on displaying checkers’ tasks and updates 
in a clear, scrollable layout, with options to take action quickly. 
The design keeps the workflow intuitive while making sure important 
information is always visible

This is the Checkers page for User Story 4, designed to let users 
quickly review applicant details and verify documents. The top section
is neatly organized into personal, employment, and loan details for quick
reference. The right panel serves as a document viewer where checkers 
can preview files like Aadhaar and photographs side by side, streamlining the verification process.




st.download_button("⬇️ Download CSV", csv, "efficiency_data.csv", "text/csv")

st.caption("Built with ❤️ using Streamlit")







