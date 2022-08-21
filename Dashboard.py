#!/usr/bin/env python
# coding: utf-8

# In[65]:


import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image


# In[66]:


leftw = pd.read_csv('https://github.com/krishi08/gait-dashboard/blob/main/_sub93-lw-s1.csv')
rightp = pd.read_csv('https://github.com/krishi08/gait-dashboard/blob/main/_sub93-rp-s1.csv')

# https://github.com/krishi08/gait-dashboard/blob/main/_sub93-lw-s1.csv


# In[67]:


# Page setting
st.set_page_config(layout="wide")


# In[71]:


leftw = leftw.iloc[:700:]


# In[76]:


a1, a2, a3 = st.columns((3,3,3))
with a1:
    st.markdown('### X-Axis')
    plost.line_chart(leftw,x='Unnamed: 0',y=('gyroRotationX.rad.s.'[:500],'motionUserAccelerationX.G.'[:500]))
with a2:
    st.markdown('### Y-Axis')
    plost.line_chart(leftw,x='Unnamed: 0',y=('gyroRotationX.rad.s.'[:500],'motionUserAccelerationX.G.'[:500]))
with a3:
    st.markdown('### Z-Axis')
    plost.line_chart(leftw,x='Unnamed: 0',y=('gyroRotationX.rad.s.'[:500],'motionUserAccelerationX.G.'[:500]))


# In[77]:


# Row A
b1, b2 , b3 = st.columns(3)
b1.metric("Cadence", "73 steps/min", "+8%")
b2.metric("Stride Length", "1.4 m", "-4%")
b3.metric("Knee Angle", "8°", "4%")


# In[ ]:




