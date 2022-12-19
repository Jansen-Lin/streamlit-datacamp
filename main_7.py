# https://www.datacamp.com/tutorial/streamlit

import streamlit as st
import numpy as np
import pandas as pd

# Display maps with Streamlit

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(df)

