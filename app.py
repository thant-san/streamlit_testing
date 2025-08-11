import streamlit as st

# Read secret with fallback value to avoid KeyError
secret_value = st.secrets.get("test", "Secret 'test' not found")

st.title("Secrets Demo")
st.write(f"Value of 'test': {secret_value}")
st.write("This app demonstrates how to access secrets in Streamlit.")