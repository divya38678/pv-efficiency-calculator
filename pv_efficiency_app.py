app:::
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import CustomersList from './pages/CustomersList';
import CustomerDetails from './pages/CustomerDetails';
import CustomerForm from './pages/CustomerForm';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/customers" element={<CustomersList />} />
          <Route path="/customers/:id" element={<CustomerDetails />} />
          <Route path="/add-customer" element={<CustomerForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

cf:
import React, { useState } from 'react';

const CustomerForm = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Validate form data
    if (!formData.firstName || !formData.lastName || !formData.email || !formData.phone) {
      alert('All fields are required.');
      return;
    }
    // Simulate form submission
    console.log('Form submitted:', formData);
    // Redirect to customer list page
    window.location.href = '/customers';
  };

  return (
    <div>
      <h2>Add Customer</h2>
      <form onSubmit={handleSubmit}>
        <label>
          First Name:
          <input
            type="text"
            name="firstName"
            value={formData.firstName}
            onChange={handleChange}
            placeholder="Please enter first name"
          />
        </label>
        <br />
        <label>
          Last Name:
          <input
            type="text"
            name="lastName"
            value={formData.lastName}
            onChange={handleChange}
            placeholder="Please enter last name"
          />
        </label>
        <br />
        <label>
          Email:
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Please enter email details"
          />
        </label>
        <br />
        <label>
          Phone:
          <input
            type="tel"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
            placeholder="Please enter phone no"
          />
        </label>
        <br />
        <button type="submit">Create Customer</button>
      </form>
    </div>
  );
};

export default CustomerForm;

cd::
import React from 'react';
import { useParams } from 'react-router-dom';

const CustomerDetails = () => {
  const { id } = useParams();
  const customer = {
    id: 1,
    firstName: 'Sundar',
    lastName: 'Pichai',
    email: 'sundar.pichai@google.com',
    phone: '1234567890',
    accounts: [
      { accountNo: '1001999', type: 'SAVINGS_ACCOUNT', branch: 'Bellandur', balance: 1000 },
      { accountNo: '1001888', type: 'SAVINGS_ACCOUNT', branch: 'Indira Nagar', balance: 2000 },
    ],
  };

  return (
    <div>
      <h2>Customer Details</h2>
      <p>ID: {customer.id}</p>
      <p>First Name: {customer.firstName}</p>
      <p>Last Name: {customer.lastName}</p>
      <p>Email: {customer.email}</p>
      <p>Phone: {customer.phone}</p>

      <h3>List of Accounts</h3>
      <table>
        <thead>
          <tr>
            <th>Account No</th>
            <th>Type</th>
            <th>Branch</th>
            <th>Balance</th>
          </tr>
        </thead>
        <tbody>
          {customer.accounts.map(account => (
            <tr key={account.accountNo}>
              <td>{account.accountNo}</td>
              <td>{account.type}</td>
              <td>{account.branch}</td>
              <td>{account.balance}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CustomerDetails;

cl:::
import React from 'react';
import { Link } from 'react-router-dom';

const CustomersList = () => {
  const customers = [
    { id: 1, firstName: 'Sundar', lastName: 'Pichai', email: 'sundar.pichai@google.com' },
    { id: 2, firstName: 'Jeff', lastName: 'Bezos', email: 'jeff.bezos@amazon.com' },
    // Add more customers as needed
  ];

  return (
    <div>
      <h2>Customers List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {customers.map(customer => (
            <tr key={customer.id}>
              <td>{customer.id}</td>
              <td>{customer.firstName}</td>
              <td>{customer.lastName}</td>
              <td>{customer.email}</td>
              <td>
                <Link to={`/customers/${customer.id}`}>Show</Link>
                <button>Edit</button>
                <button>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CustomersList;



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













