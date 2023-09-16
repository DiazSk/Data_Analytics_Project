# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title and description of your Streamlit app
st.title("Data Analytics Project :chart_with_upwards_trend:")

st.write("This project is a data analytics exploration using Python, Matplotlib, Seaborn, and Streamlit. "
         "We will analyze a dataset that contains advertising expenses in TV, Radio, Newspaper, "
         "and their impact on product Sales. The goal is to gain insights into how different advertising "
         "channels affect sales and to visualize the data for better understanding.")

# Suggestion or Contribution on Github
st.write("Feel free to contribute or provide suggestions on the [GitHub page](https://github.com/DiazSk/Speech_Recognition).")

# Upload a CSV file for analysis
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Load the data into a DataFrame
    st.success(f"File '{uploaded_file.name}' was successfully uploaded.")
    data = pd.read_csv(uploaded_file)

    # Display the first few rows of the data
    st.subheader("Data Preview:")
    st.write(data.head())

    # Data Exploration and Visualization
    st.subheader("Data Exploration and Visualization :bar_chart:")
    
    # Summary statistics
    st.write("Summary Statistics:")
    st.write(data.describe())

    # Correlation matrix heatmap
    st.write("Correlation Matrix Heatmap:")
    corr_matrix = data.corr()
    fig, ax = plt.subplots()  # Create a figure and axes
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
    st.pyplot(fig)  # Pass the figure to st.pyplot()

    # Histogram
    st.write("Histogram:")
    selected_column = st.selectbox("Select a column for the histogram:", data.columns)
    fig, ax = plt.subplots()  # Create a figure and axes
    plt.hist(data[selected_column], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel(selected_column)
    plt.ylabel("Frequency")
    st.pyplot(fig)  # Pass the figure to st.pyplot()

    # Scatter plot
    st.write("Scatter Plot:")
    x_column = st.selectbox("Select the X-axis column:", data.columns)
    y_column = st.selectbox("Select the Y-axis column:", data.columns)
    fig, ax = plt.subplots()  # Create a figure and axes
    plt.scatter(data[x_column], data[y_column], c='green', alpha=0.5)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    st.pyplot(fig)  # Pass the figure to st.pyplot()


    # Save the plot as an image file
    plt.savefig("plot.png")
  
# Add a footer
st.text("Created by Zaid Shaikh")

