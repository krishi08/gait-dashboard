#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
#import numpy as np
import plost
#from PIL import Image


# In[2]:


leftw = pd.read_csv('kneeresults.csv')


# In[3]:


res = leftw[['time', 'Aceeleration_x', 'Acceleration_y', 'Acceleration_Z', 'Gyro_x', 'Gyro_y', 'Gyro_z']] #only acc and gyro, timestamp


# In[4]:


res = res.replace({"'": ""}, regex=True) 
res = res.astype(float)
res['time'] = res['time'].astype(int)
leftw = res


# In[5]:


# Page setting
st.set_page_config(layout="wide")

leftw = leftw.iloc[:700:]

a1, a2, a3 = st.columns((3,3,3))
with a1:
    st.markdown('### X-Axis')
    plost.line_chart(leftw,x='time',y=('Aceeleration_x','Gyro_x'))
with a2:
    st.markdown('### Y-Axis')
    plost.line_chart(leftw,x='time',y=('Acceleration_y','Gyro_y'))
with a3:
    st.markdown('### Z-Axis')
    plost.line_chart(leftw,x='time',y=('Acceleration_Z','Gyro_z'))

b1, b2 , b3 = st.columns(3)
b1.metric("Cadence", "73 steps/min", "+8%")
b2.metric("Stride Length", "1.4 m", "-4%")
b3.metric("Knee Angle", "8°", "4%")
