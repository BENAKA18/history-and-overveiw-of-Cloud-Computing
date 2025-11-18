import streamlit as st
import time
import random

st.title("🚀 Interactive Demos")

st.markdown("""
## Experience Cloud Concepts

Try these interactive demonstrations to understand cloud computing in action!
""")

# Cost Calculator
st.subheader("💰 Cloud Cost Calculator")

col1, col2 = st.columns(2)

with col1:
    instances = st.slider("Number of Virtual Machines", 1, 50, 5)
    storage_gb = st.slider("Storage (GB)", 50, 1000, 200)
    users = st.slider("Number of Users", 1, 100, 10)

with col2:
    service_tier = st.selectbox("Service Tier", ["Basic ($0.05/hr)", "Standard ($0.12/hr)", "Premium ($0.25/hr)"])
    region = st.selectbox("Region", ["US East", "US West", "Europe", "Asia"])

if st.button("Calculate Monthly Cost"):
    with st.spinner("Calculating..."):
        time.sleep(1)
        
        # Calculate costs
        if "Basic" in service_tier:
            instance_cost = instances * 0.05 * 24 * 30
        elif "Standard" in service_tier:
            instance_cost = instances * 0.12 * 24 * 30
        else:
            instance_cost = instances * 0.25 * 24 * 30
            
        storage_cost = storage_gb * 0.10
        user_cost = users * 5
        
        total_cost = instance_cost + storage_cost + user_cost
        
        st.success(f"💵 Estimated Monthly Cost: **${total_cost:,.2f}**")
        
        # Breakdown
        st.write("**Cost Breakdown:**")
        st.write(f"- Instances: ${instance_cost:,.2f}")
        st.write(f"- Storage: ${storage_cost:,.2f}")
        st.write(f"- Users: ${user_cost:,.2f}")

# Auto-scaling Demo
st.subheader("📈 Auto-scaling Simulation")

if st.button("Simulate Traffic Spike"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    chart_data = [50]  # Start with 50 users
    
    for i in range(1, 101):
        # Simulate traffic pattern
        if i < 25:
            # Normal traffic
            new_users = chart_data[-1] + random.randint(-5, 5)
        elif i < 60:
            # Traffic spike
            new_users = chart_data[-1] + random.randint(5, 20)
        else:
            # Scaling down
            new_users = max(50, chart_data[-1] - random.randint(2, 10))
            
        chart_data.append(new_users)
        progress_bar.progress(i)
        
        if i < 25:
            status_text.text("🌤️ Normal traffic...")
        elif i < 60:
            status_text.text("⚡ Traffic spike detected! Auto-scaling...")
        else:
            status_text.text("📉 Scaling down resources...")
            
        st.line_chart(chart_data)
        time.sleep(0.1)
    
    status_text.text("✅ Auto-scaling completed successfully!")
    st.balloons()

# Cloud Provider Comparison
st.subheader("🏢 Cloud Provider Comparison")

provider = st.selectbox("Select a cloud provider:", ["Amazon Web Services (AWS)", "Microsoft Azure", "Google Cloud Platform (GCP)"])

if "AWS" in provider:
    st.info("""
    **Amazon Web Services (AWS)**
    - Market Leader (32% market share)
    - Most comprehensive service catalog
    - Strong in compute and storage
    - Best for: Enterprises, startups, web applications
    """)
elif "Azure" in provider:
    st.info("""
    **Microsoft Azure**
    - Strong enterprise integration
    - Excellent hybrid cloud solutions
    - Great for Microsoft ecosystem
    - Best for: Enterprises, Windows environments
    """)
else:
    st.info("""
    **Google Cloud Platform (GCP)**
    - Strong in data analytics and AI/ML
    - Excellent global network
    - Competitive pricing
    - Best for: Data-intensive applications, AI/ML
    """)

st.success("🎉 Explore all the demos above to see cloud computing in action!")