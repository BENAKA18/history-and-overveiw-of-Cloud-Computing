import streamlit as st
import pandas as pd

st.title("📈 History of Cloud Computing")

# Timeline data
timeline_data = [
    {"Year": 1960, "Event": "Time-sharing Mainframes", "Description": "Multiple users sharing single computer resources"},
    {"Year": 1999, "Event": "Salesforce.com launched", "Description": "First enterprise SaaS application"},
    {"Year": 2002, "Event": "Amazon Web Services", "Description": "AWS launched with basic web services"},
    {"Year": 2006, "Event": "Amazon EC2/S3", "Description": "Modern cloud computing begins"},
    {"Year": 2008, "Event": "Google App Engine", "Description": "Google's PaaS platform launched"},
    {"Year": 2010, "Event": "Microsoft Azure", "Description": "Microsoft's cloud platform launched"},
    {"Year": 2013, "Event": "Docker Containers", "Description": "Containerization revolutionized deployment"},
    {"Year": 2020, "Event": "COVID-19 Impact", "Description": "Massive acceleration in cloud adoption"}
]

# Display timeline
for item in timeline_data:
    with st.expander(f"**{item['Year']}**: {item['Event']}"):
        st.write(item['Description'])
        if item['Year'] == 2006:
            st.success("This marked the beginning of modern cloud computing!")
        elif item['Year'] == 2020:
            st.warning("Pandemic accelerated digital transformation worldwide")

# Market growth chart
st.subheader("📊 Cloud Market Growth")
growth_data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Market Size (Billion $)': [80, 100, 130, 160, 190, 240, 330, 490, 580, 680]
}

df = pd.DataFrame(growth_data)
st.line_chart(df.set_index('Year'))