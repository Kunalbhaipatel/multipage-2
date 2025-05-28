
import streamlit as st
from components.filter_bar import filter_controls
from data.load_data import load_well_data
import plotly.express as px

st.set_page_config(page_title="Multi-Well/Rig Comparison", layout="wide")
st.title("📊 Multi-Well & Rig Comparison")

df = load_well_data()
filter_controls(df['Well_Name'].unique(), df['Rig'].unique())

# Multi-select filters
selected_wells = st.multiselect("Compare Wells", df['Well_Name'].unique(), default=df['Well_Name'].unique()[:3])
selected_rigs = st.multiselect("Compare Rigs", df['Rig'].unique(), default=df['Rig'].unique()[:2])

filtered_df = df[df['Well_Name'].isin(selected_wells) & df['Rig'].isin(selected_rigs)]

if not filtered_df.empty:
    st.subheader("📌 Depth by Well")
    fig1 = px.bar(filtered_df, x="Well_Name", y="Depth", color="Rig", barmode="group")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📌 Well vs Rig Distribution")
    fig2 = px.histogram(filtered_df, x="Rig", color="Well_Name", barmode="group")
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("No data to display for selected filters.")
