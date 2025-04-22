import streamlit as st
import os
from pathlib import Path

# Import database initialization to ensure database is created
from db.database import init_db

# Initialize database
init_db()

# Set page configuration
st.set_page_config(
    page_title="OpenFunds - Decentralized Fundraising App",
    page_icon="💰",
    layout="wide",
)

# Add custom CSS
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary: #7C4DFF;
        --secondary: #00E5FF;
        --background: #111122;
        --text: #FFFFFF;
        --accent: #FF4081;
        --success: #00E676;
        --warning: #FFAB40;
    }
    
    /* Global styling */
    .stApp {
        background: linear-gradient(135deg, #111122, #1A237E);
    }
    
    h1, h2, h3 {
        color: var(--text);
        font-weight: 600;
    }
    
    h1 {
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        margin-bottom: 0.5em;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.5em 2em;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(124, 77, 255, 0.4);
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-12oz5g7 {
        background: rgba(20, 20, 40, 0.7);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1A237E, #311B92);
    }
    
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .stMetric label {
        color: var(--secondary);
    }
    
    /* Card containers */
    .dashboard-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .dashboard-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background-color: var(--primary);
        background-image: linear-gradient(90deg, var(--primary), var(--accent));
    }
    
    /* Dataframe styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        border: none;
    }
    
    .dataframe th {
        background-color: var(--primary);
        color: white;
    }
    
    /* Footer */
    footer {
        background: rgba(20, 20, 40, 0.5);
        padding: 1rem;
        border-radius: 10px;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Display home page content
st.title("OpenFunds – Decentralized Fundraising App")

# Logo section - using a modern gradient design
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 30px; background: linear-gradient(135deg, rgba(124, 77, 255, 0.2), rgba(0, 229, 255, 0.2)); border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);">
        <div style="font-size: 4em; margin-bottom: 10px;">💰</div>
        <h2 style="background: linear-gradient(90deg, #7C4DFF, #00E5FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2em; font-weight: 700; margin-bottom: 10px;">OpenFunds</h2>
        <p style="color: #FFFFFF; font-size: 1.2em; opacity: 0.8;">Decentralized Fundraising Platform</p>
    </div>
    """, unsafe_allow_html=True)

# Welcome section with How It Works and Features
st.write("## Welcome to OpenFunds!")
st.write("OpenFunds is a modern decentralized fundraising platform that empowers creators and supporters to connect directly through blockchain technology.")

st.write("### How It Works")

# How It Works cards using separate markdown blocks to avoid HTML issues
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div style="background: rgba(124, 77, 255, 0.1); padding: 20px; border-radius: 15px; text-align: center;">
        <div style="font-size: 2em; margin-bottom: 10px;"></div>
        <h4>Create</h4>
        <p>Set up your campaign with a compelling story and funding goal</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: rgba(0, 229, 255, 0.1); padding: 20px; border-radius: 15px; text-align: center;">
        <div style="font-size: 2em; margin-bottom: 10px;"></div>
        <h4>Share</h4>
        <p>Share your campaign with friends, family, and supporters</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: rgba(255, 64, 129, 0.1); padding: 20px; border-radius: 15px; text-align: center;">
        <div style="font-size: 2em; margin-bottom: 10px;"></div>
        <h4>Fund</h4>
        <p>Accept Bitcoin donations directly to your wallet</p>
    </div>
    """, unsafe_allow_html=True)

# Features list using native Streamlit components
st.write("### Features")
st.write("- **Decentralized** - No middlemen, donations go directly to creators")
st.write("- **Transparent** - All campaigns and funding are publicly visible")
st.write("- **Secure** - Built on blockchain technology for maximum security")
st.write("- **Simple** - Easy to use interface with no technical knowledge required")

# Footer
st.markdown("""
<footer>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <div>
            <p>© 2025 OpenFunds - A Decentralized Fundraising Platform</p>
        </div>
        <div style="display: flex; gap: 15px;">
            <span style="opacity: 0.7;">Follow us:</span>
            <a href="#" style="color: #00acee; text-decoration: none;">Twitter</a>
            <a href="#" style="color: #00acee; text-decoration: none;">Facebook</a>
            <a href="#" style="color: #00acee; text-decoration: none;">Instagram</a>
        </div>
    </div>
</footer>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.image("https://img.icons8.com/fluency/96/cryptocurrency.png", width=80)
st.sidebar.markdown("<h3 style='text-align: center;'>OpenFunds</h3>", unsafe_allow_html=True)

# Navigation using buttons instead of HTML that's showing incorrectly
st.sidebar.markdown("### Navigation")

# Home button
if st.sidebar.button("🏠 Home", key="home_nav", use_container_width=True):
    st.switch_page("pages/1_Home.py")

# Create Campaign button
if st.sidebar.button("➕ Create Campaign", key="create_nav", use_container_width=True):
    st.switch_page("pages/2_Create_Campaign.py")

# View Campaigns button
if st.sidebar.button("👁️ View Campaigns", key="view_nav", use_container_width=True):
    st.switch_page("pages/3_View_Campaigns.py")

# Import some stats for the sidebar
from models.campaign import Campaign
import pandas as pd

# Get statistics data
campaigns = Campaign.get_all_campaigns()
total_campaigns = len(campaigns) if campaigns else 0

# Calculate total fundraising
total_btc = 0
if campaigns:
    for campaign in campaigns:
        total_btc += campaign['current_amount']

# Display statistics
st.sidebar.markdown("### Dashboard Stats")

# Use Streamlit metrics instead of custom HTML for sidebar stats
col1, col2 = st.sidebar.columns(2)
with col1:
    st.sidebar.metric("Campaigns", f"{total_campaigns}")
    
with col2:
    st.sidebar.metric("Total BTC", f"{total_btc:.4f}")