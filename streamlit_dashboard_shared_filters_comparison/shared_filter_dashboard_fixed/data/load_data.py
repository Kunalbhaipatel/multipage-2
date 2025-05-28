import streamlit as st
import pandas as pd

@st.cache_data
def load_well_data():
    try:
        df = pd.read_csv("Updated_Merged_Data_with_API_and_Location.csv")
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Rename flexible aliases
        df.rename(columns={
            "wellname": "well_name",
            "well_name": "well_name",
            "rig": "rig"
        }, inplace=True)

        return df
    except Exception as e:
        st.error(f"❌ Could not load CSV: {e}")
        return pd.DataFrame(columns=["well_name", "rig", "depth"])
