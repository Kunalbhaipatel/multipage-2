import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_well_data():
    try:
        # Dynamically find the root directory
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        csv_path = os.path.join(root_path, "Updated_Merged_Data_with_API_and_Location.csv")
        df = pd.read_csv(csv_path)

        # Normalize column names
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
        df.rename(columns={
            "well_name": "well_name",
            "wellname": "well_name",
            "rig": "rig"
        }, inplace=True)

        return df
    except Exception as e:
        st.error(f"❌ Could not load CSV: {e}")
        return pd.DataFrame(columns=["well_name", "rig"])
