import streamlit as st
import pandas as pd
import numpy as np
import altair as alt 

st.title("Alvin's Amazing App")
st.markdown("Created by: Alvin Zou")

st.header("Some stuff we need from you:")

f = st.file_uploader("Upload a CSV file containing the data:", type="csv")

st.write("")
st.write("")

if f:
    df = pd.read_csv(f)

    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
    
    df.applymap(lambda x : np.nan if x == " " else x)
    numeric_cols = [c for c in df.columns if can_be_numeric(c)]

    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, axis = 0)

    x = st.selectbox("Choose any numeric column for the x-axis", df.columns)
    y = st.selectbox("Choose any numeric column for the y-axis", df.columns)

    st.write("")
    st.write("")

    slider = st.slider("Choose number of rows displayed", min_value = 0, max_value = df.shape[0])

    st.header("The data you want:")
    st.write(f'X-axis: {x}')
    st.write(f'Y-axis: {y}')
    st.write(f'Number of rows: {slider}')

    chart = alt.Chart(df.iloc[:slider]).mark_line().encode(
        x = x, y = y
    )

    st.altair_chart(chart, use_container_width=True)
    
    st.dataframe(df.iloc[:slider])