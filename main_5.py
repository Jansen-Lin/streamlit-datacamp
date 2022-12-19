# https://www.datacamp.com/tutorial/streamlit

import streamlit as st

# Sidebar and container

# Sidebar
st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender", ["Male", "Female"])

# Container
container = st.container()
container.write("This is written inside the container")
st.write("This is written outside the container")

