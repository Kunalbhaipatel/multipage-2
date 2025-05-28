
import streamlit as st
from components.filter_bar import filter_controls
from data.load_data import load_well_data
import plotly.express as px

st.title("📈 Summary Charts")
df = load_well_data()
filter_controls(df["well_name"].unique(), df["rig"].unique())

selected_well = st.session_state.get("selected_well")
if selected_well:
    subset = df[df["Well_Name"] == selected_well]
    fig = px.bar(subset, x="Well_Name", y="Depth", title="Depth by Well")
    st.plotly_chart(fig)
else:
    st.warning("No well selected.")
