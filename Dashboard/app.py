"""
app.py
-------
AI-Driven Smart Battery Management System (BMS) Dashboard
Entry point — run with:  streamlit run app.py

Routes between pages using a premium sidebar navigation
(streamlit-option-menu). Each page lives in /pages as an isolated module
exposing a `render()` function, keeping UI and logic cleanly separated.
"""

import streamlit as st

st.set_page_config(
    page_title="AI-Driven Smart BMS Dashboard",
    page_icon="🔋",
    layout="wide",
    initial_sidebar_state="expanded",
)

from utils import helper
from utils.data_loader import load_battery_data

try:
    from streamlit_option_menu import option_menu
    HAS_OPTION_MENU = True
except ImportError:
    HAS_OPTION_MENU = False

from modules import (
    _dashboard as dashboard,
    _prediction as prediction,
    _analytics as analytics,
    _digital_twin as digital_twin,
    _insights as insights,
    _history_page as history_page,
)

helper.inject_css()


# ----------------------------------------------------------------------
# Sidebar
# ----------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        "<div style='text-align:center; padding: 6px 0 2px;'>"
        "<div style='font-size:2.4rem;'>🔋</div>"
        "<div style='font-weight:800; font-size:1.05rem; color:#EAF1FF; letter-spacing:0.5px;'>AI-BMS PLATFORM</div>"
        "<div style='color:#8996B5; font-size:0.72rem; letter-spacing:1px;'>SMART BATTERY INTELLIGENCE</div>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

    menu_options = ["Home Dashboard", "Live Prediction", "Battery Analytics",
                     "Digital Twin", "AI Insights", "Prediction History"]
    menu_icons = ["speedometer2", "cpu", "bar-chart-line", "diagram-3", "lightbulb", "clock-history"]

    if HAS_OPTION_MENU:
        selected = option_menu(
            menu_title=None,
            options=menu_options,
            icons=menu_icons,
            default_index=0,
            styles={
                "container": {"padding": "0", "background-color": "transparent"},
                "icon": {"color": "#2E9BFF", "font-size": "16px"},
                "nav-link": {
                    "font-size": "14px", "text-align": "left", "margin": "3px 0",
                    "border-radius": "10px", "color": "#EAF1FF",
                    "--hover-color": "rgba(46,155,255,0.12)",
                },
                "nav-link-selected": {
                    "background": "linear-gradient(135deg, rgba(46,155,255,0.28), rgba(139,92,246,0.28))",
                    "color": "#FFFFFF", "font-weight": "700",
                },
            },
        )
    else:
        selected = st.radio("Navigate", menu_options, label_visibility="collapsed")

    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)
    st.markdown(
    """
    <div style='font-size:0.72rem; color:#8996B5; text-align:center; line-height:1.8;'>
        AI-Driven Smart BMS<br>
        SOC / SOH Prediction Engine<br>
        ANN Model: 
        <span style='color:#39FF9E; font-weight:700;'>
            Integrated ✓
        </span>
        <br>
        Model:
        <span style='color:#2E9BFF; font-weight:700;'>
            ANN
        </span>
        <br>
        System Status:
        <span style='color:#39FF9E; font-weight:700;'>
            Online ●
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# Shared data
# ----------------------------------------------------------------------
battery_df = load_battery_data()

# ----------------------------------------------------------------------
# Router
# ----------------------------------------------------------------------
if selected == "Home Dashboard":
    dashboard.render(battery_df)
elif selected == "Live Prediction":
    prediction.render(battery_df)
elif selected == "Battery Analytics":
    analytics.render(battery_df)
elif selected == "Digital Twin":
    digital_twin.render(battery_df)
elif selected == "AI Insights":
    insights.render(battery_df)
elif selected == "Prediction History":
    history_page.render()
