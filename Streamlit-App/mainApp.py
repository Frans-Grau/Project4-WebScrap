### Import Libraries 
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


### Import Data
unicorns = pd.read_csv(r'C:\Users\frans\Documents\GitHub\Project4-WebScrap\Files\FinalUnicornsO3.csv')
cities = pd.read_csv(r'C:\Users\frans\Documents\GitHub\Project4-WebScrap\Files\FinalCities.csv')

### Set Page Format
base = 'light'
st.set_page_config(page_title='NomadVsUnicorns', page_icon=None, layout='wide', menu_items=None)
tab1, tab2 = st.tabs(["Overview", "Country Study"])

with tab1: 
    col1, col2 = st.columns(2)
    with col1:
        ### Top Unicorns x Valuation
        # Grab the data
        TopUxV = unicorns[['Name','Valuation ($ Billion)']].sort_values(by = 'Valuation ($ Billion)', ascending=False)[:10]

        # Plot
        fig01, ax = plt.subplots(figsize = (10, 7))
        sns.barplot(data = TopUxV, x ='Name', y ='Valuation ($ Billion)', color = 'Green')
        ax.set_ylabel('Valuation (USD billion)')
        plt.xticks(fontsize=9)
        ax.set_xlabel('Unicorn Name')
        st.pyplot(fig01)
    
    with col2:
        ### Top Countries x Num of Unicorns
        # Plot
        fig02, ax = plt.subplots(figsize = (10, 7))
        sns.countplot( x = 'Country', data = unicorns, color="Green", order=unicorns.Country.value_counts().index[:10])
        ax.set_xlabel('Countries')
        plt.xticks(fontsize=9)
        ax.set_ylabel('Number of unicorns')
        st.pyplot(fig02)
    
    col1, col2 = st.columns(2)
    with col1:
        ### Top Industries x Num of unicorns
        # Grab the data
        TopIxU = unicorns.Industry.value_counts().sort_values(ascending=False)
        labels = TopIxU.index
        data = TopIxU.values

        # Plot
        fig04, ax = plt.subplots(figsize = (10, 7))
        plt.pie(data, labels = labels, autopct='%.0f%%')
        plt.show()
        st.pyplot(fig04)
    
    with col2:
        ### Top Industries x Valuation
        # Grab the data
        TopIxV = unicorns.groupby('Industry')['Valuation ($ Billion)'].sum().sort_values(ascending=False)[:4]

        # Plot
        fig05, ax = plt.subplots(figsize = (10, 7))
        sns.barplot( x = TopIxV.index , y = TopIxV.values, color="Green")
        ax.set_xlabel('Industries')
        plt.xticks(fontsize=8.5)
        ax.set_ylabel('Sum of Valuations in USD Billion')
        st.pyplot(fig05)


with tab2:
    col1,col2 = st.columns(2)
    with col1:
        ### Insert Filter 
        ChooseCountry1 = st.selectbox('Choose your country:', unicorns['Country'].unique(), 1)
        
        ### Top Unicorns x Valuation
        # Grab the data
        TopUxV1 = unicorns[['Name','Valuation ($ Billion)','Country']].sort_values(by = 'Valuation ($ Billion)', ascending=False)
        TopUxV = TopUxV1[TopUxV1['Country']==ChooseCountry1][:5]
        # Plot
        fig01, ax = plt.subplots(figsize = (10, 7))
        sns.barplot(data = TopUxV, x ='Name', y ='Valuation ($ Billion)', color = 'Green')
        ax.set_ylabel('Valuation (USD billion)')
        plt.xticks(fontsize=9)
        ax.set_xlabel('Unicorn Name')
        st.pyplot(fig01)

        ### Top Industries x Num of unicorns
        # Grab the data
        TopIxU = unicorns[unicorns['Country']==ChooseCountry1].Industry.value_counts().sort_values(ascending=False)
        labels = TopIxU.index
        data = TopIxU.values

        # Plot
        fig04, ax = plt.subplots(figsize = (10, 7))
        plt.pie(data, labels = labels, autopct='%.0f%%')
        plt.show()
        st.pyplot(fig04)

    with col2:
        ### Insert Filter
        ChooseCountry2 = st.selectbox('Choose another country:', unicorns['Country'].unique(), 1)

        ### Top Unicorns x Valuation
        # Grab the data
        TopUxV1 = unicorns[['Name','Valuation ($ Billion)','Country']].sort_values(by = 'Valuation ($ Billion)', ascending=False)
        TopUxV = TopUxV1[TopUxV1['Country']==ChooseCountry2][:5]
        # Plot
        fig01, ax = plt.subplots(figsize = (10, 7))
        sns.barplot(data = TopUxV, x ='Name', y ='Valuation ($ Billion)', color = 'Green')
        ax.set_ylabel('Valuation (USD billion)')
        plt.xticks(fontsize=9)
        ax.set_xlabel('Unicorn Name')
        st.pyplot(fig01)

        ### Top Industries x Num of unicorns
        # Grab the data
        TopIxU = unicorns[unicorns['Country']==ChooseCountry2].Industry.value_counts().sort_values(ascending=False)
        labels = TopIxU.index
        data = TopIxU.values

        # Plot
        fig04, ax = plt.subplots(figsize = (10, 7))
        plt.pie(data, labels = labels, autopct='%.0f%%')
        plt.show()
        st.pyplot(fig04)
