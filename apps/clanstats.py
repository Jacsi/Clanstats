import streamlit as st
import pandas as pd 
import altair as alt
import datetime
from gsheetsdb import connect

@st.cache
def get_data():
    gsheet_url = "https://docs.google.com/spreadsheets/d/1k4hK_Zhr5aBHEHiXOndhLiJfTixgM9qXPjJhfm4y4sU/edit?usp=sharing"
    conn = connect()
    rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
    df = pd.DataFrame(rows)
    #create a datetime coloumn # time didn't work with streamlit   
    df['Timestamp'] =  pd.to_datetime(df['Timestamp'], format="%d.%m.%Y %H:%M").dt.date
    return df

def app():
    st.title('Clanstats')

    st.write('This is a small prototype to display clan statistics (XP, Gold, Gems) of three member.  Feel free to click around.')
    st.write("This sample data set contains data in the period from 05/20/2021 to 06/16/2021")
    df = get_data()

    data = df
    
    #filter the date
    startdatedefault = df['Timestamp'].min()
    enddatedefault = df['Timestamp'].max()


    col1,col2 = st.beta_columns(2)
    
    startdate = col1.date_input("Start Date", value=startdatedefault)
    enddate =col2.date_input("End Date", value = enddatedefault)
    
    dffilter = df[(df['Timestamp'] > startdate) & (df['Timestamp'] < enddate)]
    
    datagrouped = dffilter.groupby(['User']).sum()
    st.write("### the group by", datagrouped)
    
    chartdata = dffilter.groupby(['User', 'Timestamp']).sum() \
  .groupby(level=0).cumsum().reset_index()
    
  #chartvalue
    value = st.radio(
     "Which value do you want to see in the chart?",
     ('XP', 'Gold', 'Gems'))
    
    chart = alt.Chart(chartdata).mark_line().encode(
    x='Timestamp:T',
    y=value+":Q",
    color='User:N'
)

    st.altair_chart(chart, use_container_width=False)
    