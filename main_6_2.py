# https://www.datacamp.com/tutorial/streamlit

import streamlit as st

# Display graphs with Streamlit (part 2)

st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')