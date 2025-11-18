import streamlit as st

def display_metric_card(title, value, delta=None):
    """Display a metric card with consistent styling"""
    if delta:
        st.metric(label=title, value=value, delta=delta)
    else:
        st.metric(label=title, value=value)

def create_comparison_table(data):
    """Create a styled comparison table"""
    return st.dataframe(data, use_container_width=True)