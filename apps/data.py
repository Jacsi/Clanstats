import streamlit as st
import pandas as pd 
import datetime
from gsheetsdb import connect

def get_data():
    gsheet_url = "https://docs.google.com/spreadsheets/d/1k4hK_Zhr5aBHEHiXOndhLiJfTixgM9qXPjJhfm4y4sU/edit?usp=sharing"
    conn = connect()
    rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
    df = pd.DataFrame(rows)
    
    #df = pd.read_csv(r"C:\Users\JSiet\Documents\Userstats.csv", sep = ";")
    df.drop(5)
    df.drop(5)
    #create a datetime coloumn # time didn't work with streamlit   
    df['Timestamp'] =  pd.to_datetime(df['Timestamp'], format="%d.%m.%Y %H:%M").dt.date
    return df

def app():
    st.title('Data')

    st.write("This is the `Data` page of the app.")

    df = get_data()

    data = df
    st.write("### the Data", data)
    
    
    
