import boto3
import pandas as pd
import numpy as np

from boto3.dynamodb.conditions import Attr

dynamodb=boto3.resource('dynamodb',aws_access_key_id='AKIA5SXNBHVRWAL3NBJX',aws_secret_access_key='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',region_name='ap-south-1')

dynamo_db=boto3.client('dynamodb',aws_access_key_id='AKIA5SXNBHVRWAL3NBJX',aws_secret_access_key='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',region_name='ap-south-1')

dynamodb.get_available_subresources()

espfsrtable = dynamodb.Table('espfsrdata')
espfsrtable.table_status


response = dynamo_db.scan(
    TableName='espfsrdata',
    Select='ALL_ATTRIBUTES')

data = response['Items']

while 'LastEvaluatedKey' in response:
    response = dynamodb.scan(
        TableName='espfsrdata',
        Select='ALL_ATTRIBUTES',
        ExclusiveStartKey=response['LastEvaluatedKey'])

    data.extend(response['Items'])

def transform_values(items):
	returnvalues = []
	for item in items:
		keys = item.keys()
		itemloop = {}
		for value in keys:
			k, v = item.get(value).popitem()
			itemloop[value] = v
		returnvalues.append(itemloop)
	return returnvalues

transformed_values = transform_values(data)
df = pd.DataFrame.from_dict(transformed_values)


# In[26]:


import streamlit as st
import pandas as pd
import plost

ankle = df[['time', 'Aceeleration_x', 'Acceleration_y', 'Acceleration_Z', 'Gyro_x', 'Gyro_y', 'Gyro_z', 'Force_val']] #only acc and gyro, timestamp

ankle = ankle.replace({"'": ""}, regex=True) 
ankle = ankle.astype(float)
ankle['time'] = ankle['time'].astype(int)


a1, a2, a3 = st.columns((3,3,3))
import scipy.signal as signal
with a1:
    st.markdown('### X-Axis')
    sos = signal.butter(50, 22, 'lp', fs=1000, output='sos')
    sig = ankle['Aceeleration_x']
    ankle['Aceeleration_x'] = signal.sosfiltfilt(sos, sig)
    plost.line_chart(ankle,x='time',y=('Aceeleration_x', 'Gyro_x'))
with a2:
    st.markdown('### Y-Axis')
    sos = signal.butter(50, 22, 'lp', fs=1000, output='sos')
    sig = ankle['Acceleration_y']
    ankle['Acceleration_y'] = signal.sosfiltfilt(sos, sig)
    plost.line_chart(ankle,x='time',y=('Acceleration_y', 'Gyro_y'))
with a3:
    st.markdown('### Z-Axis')
    sos = signal.butter(50, 22, 'lp', fs=1000, output='sos')
    sig = ankle['Acceleration_Z']
    ankle['Acceleration_Z'] = signal.sosfiltfilt(sos, sig)
    plost.line_chart(ankle,x='time',y=('Acceleration_Z', 'Gyro_z'))
    
b1, b2 , b3 = st.columns(3)
b1.metric("Cadence", "73 steps/min", "+8%")
b2.metric("Stride Length", "1.4 m", "-4%")
b3.metric("Knee Angle", "8°", "4%")
