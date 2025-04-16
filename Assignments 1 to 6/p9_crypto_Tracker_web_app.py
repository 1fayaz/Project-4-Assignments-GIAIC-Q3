# Project 9: Crypto Price Tracker


import streamlit as st  # type:ignore
from datetime import datetime

st.set_page_config(page_title="Crypto Tracker", page_icon="📈")
st.title("🪙 Simple Crypto Price Tracker")

st.markdown("This is a simulated crypto tracker built using only Streamlit and datetime (no internet access).")

# Manual Prices
crypto_prices = {
    "Bitcoin (BTC)": 65500.12,
    "Ethereum (ETH)": 3250.45,
    "XRP": 0.62,
    "Polkadot (DOT)": 7.40,
    "TenUp (TUP)": 0.032,
    "Chainlink (LINK)": 15.90,
}

st.markdown(f"🕒 Last updated: `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`")
st.markdown("---")

for coin, price in crypto_prices.items():
    st.subheader(f"🔹 {coin}")
    st.success(f"💵 Price: ${price:,.4f} USD")


st.markdown("-----------------------------------")
st.caption("🎮 Created by cool coder = ME 😎")
