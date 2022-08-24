import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image

# Page setting
st.set_page_config(layout="wide")

#with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

leftw = pd.read_csv('https://github.com/krishi08/gait-dashboard/blob/main/_sub93-lw-s1.csv', parse_dates=['Unnamed: 0'])

rightp = pd.read_csv('https://github.com/krishi08/gait-dashboard/blob/main/_sub93-rp-s1.csv', parse_dates=['Unnamed: 0'])

leftw = leftw.iloc[:700:]
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
b1, b2 , b3 = st.columns(3)
b1.metric("Cadence", "73 steps/min", "+8%")
b2.metric("Stride Length", "1.4 m", "-4%")
b3.metric("Knee Angle", "8°", "4%")
