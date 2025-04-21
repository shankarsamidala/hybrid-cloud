import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime

st.set_page_config(page_title="Hybrid Cloud Manager", layout="wide")
st.title("☁️ Hybrid Cloud Management Dashboard")

# Sidebar filters
st.sidebar.header("🌐 Filter Cloud Environment")
cloud_choice = st.sidebar.selectbox("Select Cloud Provider", ["All", "AWS", "Azure", "Private Cloud"])

def get_cloud_resources():
    return pd.DataFrame([
        {
            "ID": "i-aws-01",
            "Cloud": "AWS",
            "Status": "Running",
            "IP": "13.234.56.78",
            "SSH Key": "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA7v0QZ9VjklVfzXmV0b1QkmYyAWS01FakeKey== user@aws01",
            "CPU": 67,
            "Memory": 58,
            "Cost($/hr)": 0.12
        },
        {
            "ID": "i-azure-01",
            "Cloud": "Azure",
            "Status": "Stopped",
            "IP": "20.44.12.91",
            "SSH Key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0X9FakeAzureKey1uJWpqFiM28NzT== user@az01",
            "CPU": 0,
            "Memory": 0,
            "Cost($/hr)": 0.10
        },
        {
            "ID": "i-pvt-01",
            "Cloud": "Private Cloud",
            "Status": "Running",
            "IP": "10.0.0.45",
            "SSH Key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCPrivateKey7yPOTnGb9rkVmJt3M1H== user@pvt01",
            "CPU": 32,
            "Memory": 45,
            "Cost($/hr)": 0.07
        },
        {
            "ID": "i-aws-02",
            "Cloud": "AWS",
            "Status": "Running",
            "IP": "13.229.77.43",
            "SSH Key": "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAzxc1AWSKeyTwo8vmqqeqd9MeN5y== user@aws02",
            "CPU": 85,
            "Memory": 70,
            "Cost($/hr)": 0.15
        },
        {
            "ID": "i-azure-02",
            "Cloud": "Azure",
            "Status": "Running",
            "IP": "40.112.52.15",
            "SSH Key": "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAazureKey2T0vx7oPFl56KwFakeValue== user@az02",
            "CPU": 50,
            "Memory": 55,
            "Cost($/hr)": 0.11
        },
    ])



# Filter logic
df = get_cloud_resources()
if cloud_choice != "All":
    df = df[df["Cloud"] == cloud_choice]

# Display data
st.subheader("📋 Cloud Resources Overview")
st.dataframe(df, use_container_width=True)

# Actions
st.subheader("🔧 Manage Resources")
selected_instance = st.selectbox("Choose Instance", df["ID"].tolist())
action = st.radio("Action", ["Start", "Stop", "Restart"])

if st.button("Execute"):
    st.success(f"✅ Action '{action}' executed on instance '{selected_instance}' at {datetime.now().strftime('%H:%M:%S')}")

# Metrics
st.subheader("📈 Cloud Resource Usage")
cpu_data = df["CPU"]
mem_data = df["Memory"]
labels = df["ID"]

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(labels, cpu_data, label="CPU Usage", color="skyblue")
ax.bar(labels, mem_data, label="Memory Usage", bottom=cpu_data, color="lightgreen")
ax.set_ylabel("Usage (%)")
ax.set_title("Stacked CPU + Memory Usage")
ax.legend()
st.pyplot(fig)

# Cost summary
st.subheader("💰 Estimated Hourly Cost")
total_cost = df["Cost($/hr)"].sum()
st.metric(label="Total Cost", value=f"${total_cost:.2f}/hr")
