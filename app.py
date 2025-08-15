# app.py

import streamlit as st

# Streamlit app title
st.title("Power Calculator")
st.write("Calculate the power of a number raised to an exponent.")

# Input for base number
base = st.number_input("Enter the base number:", value=2.0, step=1.0)

# Input for exponent
exponent = st.number_input("Enter the exponent:", value=3.0, step=1.0)

# Calculate power
result = base ** exponent

# Display the result
st.write(f"The result of {base} raised to the power of {exponent} is: {result}")
