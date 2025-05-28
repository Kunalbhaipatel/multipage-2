
import streamlit as st
from components.filter_bar import filter_controls
from data.load_data import load_well_data

st.title("🗂️ Well Overview")
df = load_well_data()
filter_controls(df['Well_Name'].unique(), df['Rig'].unique())

selected_well = st.session_state.get("selected_well")
if selected_well:
    st.write(f"Showing well info for: {selected_well}")
    st.dataframe(df[df["Well_Name"] == selected_well])
else:
    st.warning("No well selected.")
