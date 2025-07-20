import streamlit as st
from scipy.stats import norm
import numpy as np

st.set_page_config(page_title="BSM Option Calculator", layout="centered")

st.title("📈 Black-Scholes Option Pricing")

# User Inputs
S = st.number_input("Spot Price (S)", value=19500.0)
K = st.number_input("Strike Price (K)", value=19600.0)
T = st.number_input("Time to Expiry (in years)", value=0.05)
r = st.number_input("Risk-Free Rate (r)", value=0.06)
σ = st.number_input("Volatility (σ)", value=0.20)

# BSM formula
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    return call_price

if st.button("Calculate Call Option Price"):
    call = black_scholes_call(S, K, T, r, σ)
    st.success(f"💰 Call Option Price: ₹ {call:.2f}")
