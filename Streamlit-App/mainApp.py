### Import Libraries 
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from PIL import Image
import numpy as np

### Import Data
unicorns = pd.read_csv(r'C:\Users\frans\Documents\GitHub\Project4-WebScrap\Files\Unicorns&Countries.csv')
cities = pd.read_csv(r'C:\Users\frans\Documents\GitHub\Project4-WebScrap\Files\Top2Cities.csv')
nb_uni_country = pd.read_csv(r'C:\Users\frans\Documents\GitHub\Project4-WebScrap\Files\nb_uni_per_country.csv')

#coordinates = pd.read_csv(r'C:\Users\frans\Documents\GitHub\Project4-WebScrap\Files\coutry_coord.csv')
# unicorns = pd.read_csv(r'/Users/anacarolinaquintino/Documents/GitHub/Project4-WebScrap/Files/Unicorns&Countries.csv')
# cities = pd.read_csv(r'/Users/anacarolinaquintino/Documents/GitHub/Project4-WebScrap/Files/Top2Cities.csv')
#coordinates = pd.read_csv(r'/Users/anacarolinaquintino/Documents/GitHub/Project4-WebScrap/Files/coutry_coord.csv')
# nb_uni_country = pd.read_csv(r'/Users/anacarolinaquintino/Documents/GitHub/Project4-WebScrap/Files/nb_uni_per_country.csv')

### Set Page Format
base = 'light'
st.set_page_config(page_title='NomadVsUnicorns', page_icon=None, layout='wide', menu_items=None)
palette=['lightblue','skyblue','lightsteelblue','steelblue', 'cornflowerblue', 'royalblue']

tab1, tab2 = st.tabs(["Overview", "Country Study"])
#st.title('The unicorns of the world')

with tab1:
    st.title('The unicorns of the world')

    st.subheader('*Where are the unicorns?*')
    # image1 = Image.open('/Users/anacarolinaquintino/Documents/GitHub/Project4-WebScrap/map2.png')
    image1 = Image.open(r'C:\Users\frans\Documents\GitHub\Project4-WebScrap\map2.png')
    st.image(image1, use_column_width='always')

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('*What are the top 10 unicorns?*')
        ### Top Unicorns x Valuation
        # Grab the data
        TopUxV = unicorns[['Name','Valuation ($ Billion)']].sort_values(by = 'Valuation ($ Billion)', ascending=False)[:10]
        # Plot
        fig01, ax = plt.subplots(figsize = (10, 7))
        sns.barplot(data = TopUxV, x ='Name', y ='Valuation ($ Billion)', color = 'skyblue')
        ax.set_ylabel('Valuation (USD billion)')
        plt.xticks(fontsize=9)
        ax.set_xlabel('Unicorn Name')
        ax.set_title('Top 10 unicorns in the world')
        st.pyplot(fig01)
    
    with col2:
        ### Top Countries x Num of Unicorns
        # Plot
        #fig02, ax = plt.subplots(figsize = (10, 7))
        #sns.countplot( x = 'Country', data = unicorns, color='mediumseagreen', order=unicorns.Country.value_counts().index[:10])
        #ax.set_xlabel('Countries')
        #plt.xticks(fontsize=9)
        #ax.set_ylabel('Number of unicorns')
        #st.pyplot(fig02)
        
        st.subheader('*What are the main industries?*')
        ### Top Industries x Num of unicorns
        # Grab the data
        TopIxU = unicorns.Industry.value_counts().sort_values(ascending=False)
        labels1 = TopIxU.index
        data1 = TopIxU.values
        # Plot
        #fig04, ax = plt.subplots(figsize = (10, 7))
        #plt.pie(data, labels = labels, autopct='%.0f%%', colors=palette)
        #plt.show()
        #st.pyplot(fig04)
        
        
        df = pd.DataFrame(
        data = {'industry': labels1 , ' ' : data1},
            ).sort_values(' ', ascending = False)

        #the top 5
        df3 = df[:5].copy()

        #others
        new_row = pd.DataFrame(data = {
            'industry' : ['Others'],
            ' ' : [df[' '][5:].sum()]
        })

        #combining top 5 with others
        df4 = pd.concat([df3, new_row])

        #plotting -- for comparison left all countries and right 
        st.set_option('deprecation.showPyplotGlobalUse', False)
        df4.plot(kind = 'pie', y=' ', labels = df4['industry'],autopct='%.0f%%',legend=False,figsize = (9,4), colors=palette)
        plt.show()
        st.pyplot()
        st.empty()

    #col1, col2 = st.columns(2)
    #with col1:
  
    
    #with col2:
        ### Top Industries x Valuation
        # Grab the data
        #TopIxV = unicorns.groupby('Industry')['Valuation ($ Billion)'].sum().sort_values(ascending=False)[:4]

        # Plot
        #fig05, ax = plt.subplots(figsize = (10, 7))
        #sns.barplot( x = TopIxV.index , y = TopIxV.values, color="Green")
        #ax.set_xlabel('Industries')
        #plt.xticks(fontsize=8.5)
        #ax.set_ylabel('Sum of Valuations in USD Billion')
        #st.pyplot(fig05)

    st.subheader('*What are the best cities in the world for nomads?*')
    col1, col2, col3 = st.columns([1,3,1])
    with col1:
        st.empty()
    with col2:
       
        cities2 = cities.sort_values(by='score', ascending=False).head(10)
        cities2.rename(columns = {'city':'City', 'score':'Score'}, inplace=True)
        #st.table(cities2[['Country','City','Score']])
    
        fig07, ax = plt.subplots(figsize = (6, 3))
        sns.barplot(data = cities2, x ='City', y ='Score', color = 'skyblue')
        ax.set_ylabel('Score')
        plt.xticks(fontsize=5)
        plt.yticks(fontsize=5)
        ax.set_xlabel('City')
        ax.set_yticks(np.arange(0, 5.5, 0.5))
        st.pyplot(fig07)
        #st.table(nb_uni_country[['Country','Number of unicorns']].head(10))
    with col3:
        st.empty()

with tab2:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('Take a closer look at each country')
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
        sns.barplot(data = TopUxV, x ='Name', y ='Valuation ($ Billion)', color = 'skyblue')
        ax.set_ylabel('Valuation (USD billion)')
        plt.xticks(fontsize=9)
        ax.set_xlabel('Unicorn Name')
        ax.set_yticks(np.arange(0, 150, 10))
        st.pyplot(fig01)

        ### Top Industries x Num of unicorns
        # Grab the data
        TopIxU = unicorns[unicorns['Country']==ChooseCountry1].Industry.value_counts().sort_values(ascending=False)
        labels = TopIxU.index
        data = TopIxU.values

        # Plot
        #the full dataframe
        df = pd.DataFrame(
            data = {'industry': labels , ' ' : data},
            ).sort_values(' ', ascending = False)

        #the top 5
        df2 = df[:5].copy()

        #others
        new_row = pd.DataFrame(data = {
            'industry' : ['Others'],
            ' ' : [df[' '][5:].sum()]
        })

        #combining top 5 with others
        df2 = pd.concat([df2, new_row])

        #plotting -- for comparison left all countries and right 
        df2.plot(kind = 'pie', y=' ', labels = df2['industry'],autopct='%.0f%%',legend=False,figsize = (9,4), colors=palette)
        plt.show()
        st.pyplot()
        st.empty()


    with col2:
        ### Insert Filter
        ChooseCountry2 = st.selectbox('Choose another country:', unicorns['Country'].unique(), 1)

        ### Top Unicorns x Valuation
        # Grab the data
        TopUxV1 = unicorns[['Name','Valuation ($ Billion)','Country']].sort_values(by = 'Valuation ($ Billion)', ascending=False)
        TopUxV = TopUxV1[TopUxV1['Country']==ChooseCountry2][:5]
        # Plot
        fig01, ax = plt.subplots(figsize = (10, 7))
        sns.barplot(data = TopUxV, x ='Name', y ='Valuation ($ Billion)', color = 'skyblue')
        ax.set_ylabel('Valuation (USD billion)')
        plt.xticks(fontsize=9)
        ax.set_xlabel('Unicorn Name')
        ax.set_yticks(np.arange(0, 150, 10))
        st.pyplot(fig01)

        ### Top Industries x Num of unicorns
        # Grab the data
        TopIxU = unicorns[unicorns['Country']==ChooseCountry2].Industry.value_counts().sort_values(ascending=False)
        labels = TopIxU.index
        data = TopIxU.values

        # Plot
        #the full dataframe
        df = pd.DataFrame(
            data = {'industry': labels , ' ' : data},
            ).sort_values(' ', ascending = False)

        #the top 5
        df2 = df[:5].copy()

        #others
        new_row = pd.DataFrame(data = {
            'industry' : ['Others'],
            ' ' : [df[' '][5:].sum()]
        })

        #combining top 5 with others
        df2 = pd.concat([df2, new_row])

        #plotting -- for comparison left all countries and right 
        df2.plot(kind = 'pie', y=' ', labels = df2['industry'],autopct='%.0f%%',legend=False,figsize = (9,4), colors=palette)
        plt.show()
        st.pyplot()
        st.empty()
    
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('*What are the best cities for nomads in the country?*')
        df_country1 = cities[cities['Country']==ChooseCountry1].sort_values(by='score', ascending=False).head(2)
        df_country1.rename(columns = {'city':'City', 'score':'Score'}, inplace=True)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df_country1[['Country','City','Score']])
    with col2:
        st.subheader('* *')
        df_country2 = cities[cities['Country']==ChooseCountry2].sort_values(by='score', ascending=False).head(2)
        df_country2.rename(columns = {'city':'City', 'score':'Score'}, inplace=True)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df_country2[['Country','City','Score']])
    
