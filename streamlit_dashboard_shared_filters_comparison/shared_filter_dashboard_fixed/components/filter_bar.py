import streamlit as st

def filter_controls(wells, rigs):
    st.sidebar.title("🔍 Filters")

    if len(wells) == 0 or len(rigs) == 0:
        st.sidebar.warning("⚠️ No data available to filter.")
        return

    default_well = st.session_state.get("selected_well", wells[0])
    default_rig = st.session_state.get("selected_rig", rigs[0])

    selected_well = st.sidebar.selectbox("Select Well", wells, index=wells.tolist().index(default_well))
    selected_rig = st.sidebar.selectbox("Select Rig", rigs, index=rigs.tolist().index(default_rig))

    if selected_well != st.session_state.get("selected_well"):
        st.session_state.selected_well = selected_well
    if selected_rig != st.session_state.get("selected_rig"):
        st.session_state.selected_rig = selected_rig
