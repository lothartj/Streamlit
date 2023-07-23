# Import necessary libraries for Streamlit and plotting
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
inventory_data = pd.read_excel("Inventory Analysis Matrix (1).xlsx")

# Define the Streamlit App function
def inventory_analysis_app():
    st.title("Inventory Analysis Dashboard")
    
    # Dropdown for selecting Row Ref. No.
    selected_row_ref = st.selectbox('Select a product by Row Ref. No.', inventory_data['Row Ref. No.'].tolist())
    
    # Filter data for the selected product
    selected_data = inventory_data[inventory_data['Row Ref. No.'] == selected_row_ref].iloc[0]
    
    # Plotting the line chart for sales from Current Period to Period 10
    periods = ['Current Period', 'Period 1', 'Period 2', 'Period 3', 'Period 4', 'Period 5', 'Period 6', 'Period 7', 'Period 8', 'Period 9', 'Period 10']
    plt.figure(figsize=(12, 6))
    plt.plot(periods, selected_data[periods], marker='o', color='b')
    plt.title(f"Sales for {selected_data['Description']}")
    plt.xlabel('Period')
    plt.ylabel('Units Sold')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    st.pyplot(plt.gcf())
    
    # Displaying product details below the chart
    st.write("**Description:**", selected_data['Description'])
    st.write("**Inventory:**", selected_data['Inventory'])
    st.write("**Unit Cost:**", selected_data['Unit Cost'])
    st.write("**Stock Value:**", selected_data['Stock Value'])

    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

if __name__ == '__main__':
    inventory_analysis_app()
