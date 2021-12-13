# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 00:48:34 2021

@author: Jacsi
"""

import streamlit as st
from multiapp import MultiApp
from apps import data, clanstats # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Clan statistics", clanstats.app)
app.add_app("Data", data.app)

# The main app
app.run()
