import streamlit as st

st.title("📊 Cloud Computing Overview")

st.markdown("""
## What is Cloud Computing?

Cloud computing is the delivery of computing services over the Internet ("the cloud") including:
- **Servers** - Virtual machines and computing power
- **Storage** - File storage and databases
- **Networking** - Secure network connections
- **Software** - Applications and platforms
""")

# Key characteristics
st.subheader("🌟 Key Characteristics")

with st.expander("✅ On-demand self-service"):
    st.write("Users can provision computing capabilities automatically as needed")

with st.expander("✅ Broad network access"):
    st.write("Services available over the network through standard mechanisms")

with st.expander("✅ Resource pooling"):
    st.write("Provider's computing resources pooled to serve multiple consumers")

with st.expander("✅ Rapid elasticity"):
    st.write("Capabilities can be elastically provisioned and released")

with st.expander("✅ Measured service"):
    st.write("Cloud systems automatically control and optimize resource use")

# Benefits
st.subheader("💡 Key Benefits")
benefits = {
    "Cost Efficiency": "Pay only for what you use, no upfront infrastructure costs",
    "Scalability": "Scale up or down based on demand automatically",
    "Reliability": "High availability with built-in disaster recovery",
    "Security": "Enterprise-level security features and compliance",
    "Flexibility": "Access services from anywhere with an internet connection"
}

for benefit, description in benefits.items():
    st.write(f"**{benefit}**: {description}")