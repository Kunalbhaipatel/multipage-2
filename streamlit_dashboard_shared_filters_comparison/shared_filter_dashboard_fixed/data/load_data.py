
import streamlit as st
import pandas as pd

@st.cache_data
def load_well_data():
    return pd.read_csv("Updated_Merged_Data_with_API_and_Location.csv")
