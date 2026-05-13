import streamlit as st
from folium.plugins import HeatMap

home_page = st.Page("views/home.py", title="Home")
dashboard_page = st.Page("views/dashboard.py", title="Dashboard")
temporal_page = st.Page("views/analise_temporal.py", title="Análise Temporal")
geografica_page = st.Page("views/analise_geografica.py", title="Análise Geográfica")

pg = st.navigation(
    [home_page, dashboard_page, temporal_page, geografica_page],
    position="sidebar",
    expanded=True
)

pg.run()
