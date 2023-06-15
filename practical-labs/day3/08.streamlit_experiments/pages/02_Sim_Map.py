import streamlit as st 
import pandas as pd
import numpy as np

st.header("Mapping data")

map_data = pd.DataFrame(
    np.random.randn(1000, 2)/ [50, 50] + [37.6, -122.5],
    columns = ["lat", "lon"]
)

st.map(map_data)