# https://www.datacamp.com/tutorial/streamlit

import streamlit as st
import time

# Display progress and status with Streamlit

st.balloons()

st.subheader("Progress bar")
st.progress(10)

st.subheader("Wait the execution")
with st.spinner('Wait for it...'):
    time.sleep(10)

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))