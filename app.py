import streamlit as st

st.set_page_config(
    page_title="Cloud Computing Hub",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("☁️ Cloud Computing Learning Platform")
st.markdown("### Explore the world of cloud computing through interactive demos and comprehensive guides")

# Hero section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 2rem; border-radius: 10px;'>
    <h3 style='color: #1f77b4;'>Welcome! 🎉</h3>
    <p>Use the sidebar on the left to navigate between different sections:</p>
    <ul>
    <li><b>📊 Overview</b> - Cloud computing basics</li>
    <li><b>📈 History</b> - Evolution timeline</li>
    <li><b>🔧 Services</b> - IaaS, PaaS, SaaS explained</li>
    <li><b>🚀 Demo</b> - Interactive examples</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=150)

# Quick navigation
st.markdown("---")
st.subheader("🚀 Quick Start")
st.info("Use the sidebar navigation to explore different sections of this cloud computing learning platform!")

# Status
st.success("✅ Application is running successfully!")