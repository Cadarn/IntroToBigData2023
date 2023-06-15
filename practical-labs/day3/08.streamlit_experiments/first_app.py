import streamlit as st
import pandas as pd
import numpy as np

st.title("Demo of Streamlit in action!")
st.subheader("This is part of The Big Data Workshop 2023")

""" 
## This is also a subheading

We're having fun with Streamlit
"""

st.sidebar.title("Controls")
st.sidebar.subheader("Sliding controls")
slider_val = st.sidebar.slider(
    label="Harry's slider: ",
    min_value=0,
    max_value=10,
    step=2,
)

st.write(f"The value of the slider is: {slider_val}")

st.write("Here comes some data loading ...")

chart_data = pd.DataFrame(
    {
    "Column 1": range(10),
    "Column 2": np.random.random(10),
    "Column 3": np.random.random(10)
    }
).set_index("Column 1")

st.write(chart_data)

st.bar_chart(chart_data)


if st.checkbox("Show dataframe"):
    st.line_chart(chart_data)

option = st.selectbox(
    "Which number is your preference?",
    [1, 2, 4, 5, 9]
)

"You selected: ", option
