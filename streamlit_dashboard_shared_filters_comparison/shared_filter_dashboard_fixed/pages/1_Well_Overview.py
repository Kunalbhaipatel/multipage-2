
import streamlit as st
from components.filter_bar import filter_controls
from data.load_data import load_well_data

st.title("🗂️ Well Overview")
df = load_well_data()
filter_controls(df["well_name"].unique(), df["rig"].unique())

selected_well = st.session_state.get("selected_well")
if selected_well:
    st.write(f"Showing data for well: {selected_well}")
    st.dataframe(df[df["Well_Name"] == selected_well])
else:
    st.warning("No well selected.")
