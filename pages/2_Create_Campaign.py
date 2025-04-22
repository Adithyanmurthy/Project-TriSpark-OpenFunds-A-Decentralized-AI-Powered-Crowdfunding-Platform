import streamlit as st
from models.campaign import Campaign
import re

# Set page configuration
st.set_page_config(
    page_title="OpenFunds - Create Campaign",
    page_icon="💰",
    layout="wide",
)

# Add simple CSS
st.markdown("""
<style>
    .stApp {
        background-color: #111133;
    }
    h1, h2, h3, h4, h5, p, li, div {
        color: white;
    }
    .stButton button {
        background-color: #7C4DFF;
        color: white;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to validate BTC address format (simplified for testnet)
def is_valid_btc_address(address):
    # This is a simplified check for testnet addresses
    pattern = re.compile(r'^[123][a-km-zA-HJ-NP-Z1-9]{25,34}$')
    return bool(pattern.match(address))

# Title and description
st.title("Create a New Fundraising Campaign")
st.write("Fill out the form below to create a new fundraising campaign. All campaigns are stored locally and can be viewed on the 'View Campaigns' page.")

# Create form with standard components
with st.form("campaign_form"):
    # Campaign details
    st.subheader("Campaign Details")
    
    title = st.text_input("Campaign Title", max_chars=100, help="Enter a descriptive title for your campaign")
    
    description = st.text_area(
        "Campaign Description", 
        max_chars=500,
        height=150,
        help="Describe your campaign and why people should donate"
    )
    
    # Two columns for BTC address and amount
    col1, col2 = st.columns(2)
    
    with col1:
        btc_address = st.text_input(
            "Bitcoin Address (Testnet)", 
            help="Enter a Bitcoin testnet address for receiving donations"
        )
    
    with col2:
        target_amount = st.number_input(
            "Target Amount (BTC)", 
            min_value=0.001, 
            max_value=100.0, 
            value=1.0, 
            step=0.1,
            help="How much BTC do you want to raise?"
        )
    
    owner_name = st.text_input("Campaign Owner", help="Your name or organization name")
    
    # Submit button
    submit_button = st.form_submit_button("Create Campaign")

# Process form submission
if submit_button:
    # Validate inputs
    if not title:
        st.error("Campaign title is required.")
    elif not description:
        st.error("Campaign description is required.")
    elif not btc_address:
        st.error("Bitcoin address is required.")
    elif not is_valid_btc_address(btc_address):
        st.error("Please enter a valid Bitcoin address format.")
    elif target_amount <= 0:
        st.error("Target amount must be greater than 0.")
    elif not owner_name:
        st.error("Campaign owner name is required.")
    else:
        # Call the Campaign model to create a new campaign
        success = Campaign.create_campaign(
            title=title,
            description=description,
            btc_address=btc_address,
            target_amount=float(target_amount),
            owner_name=owner_name
        )
        
        if success:
            st.success("Campaign created successfully! 🎉")
            # Add a button to view campaigns
            if st.button("View All Campaigns"):
                st.switch_page("pages/3_View_Campaigns.py")
        else:
            st.error("An error occurred while creating the campaign. Please try again.")

# Tips for campaign creators with standard components
st.subheader("Tips for a Successful Campaign")
with st.expander("See Tips"):
    st.markdown("### How to Create a Successful Fundraising Campaign")
    
    st.markdown("**1. Choose a Clear Title**")
    st.write("Your title should be concise and describe what you're raising funds for.")
    
    st.markdown("**2. Write a Compelling Description**")
    st.write("Explain why your campaign matters and how the funds will be used.")
    
    st.markdown("**3. Set a Realistic Goal**")
    st.write("Choose a target amount that makes sense for your needs.")
    
    st.markdown("**4. Share Your Campaign**")
    st.write("Promote your campaign through social media and personal networks.")
    
    st.markdown("**5. Be Transparent**")
    st.write("Keep supporters updated on your progress and how funds are being used.")

# Display a sample campaign as inspiration
st.subheader("Example Campaign")
with st.expander("See Example"):
    st.markdown("### Community Garden Restoration Project")
    
    st.markdown("**Title:** Community Garden Restoration Project")
    
    st.markdown("**Description:** Our neighborhood garden needs restoration after recent storm damage. Funds will go toward new plants, soil, and irrigation equipment to make our shared space beautiful again.")
    
    st.markdown("**Target Amount:** 0.5 BTC")
    
    st.markdown("**Campaign Owner:** Jane Smith, Garden Committee")
    
    st.markdown("**Bitcoin Address:** 2N7DoD1edbhWw1Z1rN7HbpvzjPvF9LKjPbE")

# Sidebar
st.sidebar.title("OpenFunds")
st.sidebar.markdown("💰 Decentralized Fundraising")

# Navigation
st.sidebar.subheader("Navigation")
if st.sidebar.button("🏠 Home"):
    st.switch_page("1_Home.py")
if st.sidebar.button("➕ Create Campaign", disabled=True):
    pass
if st.sidebar.button("👁️ View Campaigns"):
    st.switch_page("pages/3_View_Campaigns.py")

# Footer
st.markdown("---")
st.write("© 2025 OpenFunds - A Decentralized Fundraising Platform")