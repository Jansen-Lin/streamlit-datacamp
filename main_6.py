# https://www.datacamp.com/tutorial/streamlit

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt

# Display graphs with Streamlit

rand = np.random.normal(1,2,size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.subheader("matplotlib.pyplot figure")
st.pyplot(fig) # matplotlib.pyplot figure

df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])

st.subheader("line chart")
st.line_chart(df) # line chart
st.subheader("bar chart")
st.bar_chart(df) # bar chart
st.subheader("area chart")
st.area_chart(df) # area chart

df2 = pd.DataFrame(
   np.random.randn(500, 3),
   columns=['x','y','z'])

c = alt.Chart(df2).mark_circle().encode(
   x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])
st.subheader("altair chart")
st.altair_chart(c, use_container_width=True) # display altair chart