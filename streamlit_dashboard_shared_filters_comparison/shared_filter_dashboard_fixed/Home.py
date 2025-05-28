
import streamlit as st
from components.filter_bar import filter_controls
from data.load_data import load_well_data

st.set_page_config(page_title="Drilling Dashboard", layout="wide", page_icon="🛢️")

st.markdown("""
    <style>
        .reportview-container .sidebar-content {{
            padding-top: 2rem;
        }}
        .sidebar .sidebar-content {{
            background-color: #f5f7fa;
        }}
        .css-1d391kg {{"margin-top": "-60px"}}
    </style>
""", unsafe_allow_html=True)

st.image("https://img.icons8.com/color/96/000000/oil-industry.png", width=60)
st.title("🛢️ Drilling Performance Dashboard")

df = load_well_data()
filter_controls(df['Well_Name'].unique(), df['Rig'].unique())

if st.session_state.get("selected_well"):
    st.success(f"Selected Well: {st.session_state.selected_well}")
else:
    st.info("No well selected yet.")
