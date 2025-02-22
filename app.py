import streamlit as st
import pandas as pd
import plotly.express as px

# Application title
st.title("Data analysis for vehicles")

# Load CSV
df = pd.read_csv("vehicles_preprocessed.csv")

# Show data
st.header("vehicle data")
st.write(df)

# Price histogram
st.header("Price distribution")
fig = px.histogram(df, x="price", title="Price Distribution")
st.plotly_chart(fig)

# Dispersion graphic: Price vs Kilometers
st.header("Price vs Kilometers")
fig = px.scatter(df, x="odometer", y="price", title="Price vs Kilometers")
st.plotly_chart(fig)

# Checkbox to filter data
st.header("Filter vehicle condition")  
show_new_cars = st.checkbox("Show only new vehicles")
if show_new_cars:
    df_filtered = df[df["condition"] == "new"]
    st.write(df_filtered)
