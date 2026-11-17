from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Raja Shekhar | Data Modeling and BI Leader", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit's own chrome so only the portfolio shows
st.markdown("""
<style>
#MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {display:none !important}
.block-container {padding:0 !important; max-width:100% !important}
iframe {border:0; width:100%}
</style>
""", unsafe_allow_html=True)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=1100, scrolling=True)
