import streamlit as st

st.title("🔧 Cloud Service Models")

st.markdown("""
## Three Main Service Models

Understanding IaaS, PaaS, and SaaS is crucial for cloud computing.
""")

# Service model selector
model = st.radio(
    "Choose a service model to explore:",
    ["IaaS - Infrastructure as a Service", 
     "PaaS - Platform as a Service", 
     "SaaS - Software as a Service"]
)

if "IaaS" in model:
    st.subheader("🖥️ Infrastructure as a Service (IaaS)")
    st.image("https://www.simplilearn.com/ice9/free_resources_article_thumb/IaaS-Examples.jpg", width=400)
    st.write("""
    **What you manage:**
    - Applications
    - Data
    - Runtime
    - Middleware
    - Operating System
    
    **What provider manages:**
    - Virtualization
    - Servers
    - Storage
    - Networking
    
    **Examples:** AWS EC2, Google Compute Engine, Azure Virtual Machines
    """)
    
elif "PaaS" in model:
    st.subheader("⚙️ Platform as a Service (PaaS)")
    st.image("https://www.simplilearn.com/ice9/free_resources_article_thumb/PaaS-Examples.jpg", width=400)
    st.write("""
    **What you manage:**
    - Applications
    - Data
    
    **What provider manages:**
    - Runtime
    - Middleware
    - Operating System
    - Virtualization
    - Servers
    - Storage
    - Networking
    
    **Examples:** Heroku, Google App Engine, AWS Elastic Beanstalk
    """)
    
else:
    st.subheader("📊 Software as a Service (SaaS)")
    st.image("https://www.simplilearn.com/ice9/free_resources_article_thumb/SaaS-Examples.jpg", width=400)
    st.write("""
    **What you manage:**
    - Nothing!
    
    **What provider manages:**
    - Applications
    - Data
    - Runtime
    - Middleware
    - Operating System
    - Virtualization
    - Servers
    - Storage
    - Networking
    
    **Examples:** Gmail, Salesforce, Microsoft Office 365, Slack
    """)

# Comparison table
st.subheader("📋 Quick Comparison")
comparison = {
    "Service Model": ["IaaS", "PaaS", "SaaS"],
    "Control Level": ["High", "Medium", "Low"],
    "Management Effort": ["High", "Medium", "Low"],
    "Flexibility": ["High", "Medium", "Low"]
}

st.table(comparison)