
import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_well_data():
    try:
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "Updated_Merged_Data_with_API_and_Location.csv")
        df = pd.read_csv(path)

        # Normalize
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Debug: show column names
        st.write("CSV columns:", df.columns.tolist())

        # Rename aliases
        aliases = {
            "wellname": "well_name",
            "well": "well_name",
            "well_name": "well_name",
            "rig": "rig",
            "rig_name": "rig"
        }
        df.rename(columns=aliases, inplace=True)

        return df
    except Exception as e:
        st.error(f"❌ CSV Load Error: {e}")
        return pd.DataFrame(columns=["well_name", "rig"])
