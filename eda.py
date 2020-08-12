# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:51:41 2020

@author: hp
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.title('Food Demand Forecasting - Analytics Vidhya')


@st.cache
def load_data(nrows):
    data = pd.read_csv('train.csv', nrows=nrows)
    return data

@st.cache
def load_center_data(nrows):
    data = pd.read_csv('fulfilment_center_info.csv',nrows=nrows)
    return data

@st.cache
def load_meal_data(nrows):
    data = pd.read_csv('meal_info.csv',nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
weekly_data = load_data(1000)
center_info_data = load_center_data(1000)
meal_data = load_meal_data(1000)

data_load_state.text("Done! (using st.cache)")

#WeeklyDemand Data
st.subheader('Weekly Demand Data')
st.write(weekly_data)
st.bar_chart(weekly_data['num_orders'])
df = pd.DataFrame(weekly_data, columns = ['num_orders','checkout_price','base_price'])
df.hist()
plt.show()
st.line_chart(df)

#Fullfilment Center Information
st.subheader('Fulfilment Center Information')
st.write(center_info_data)
st.bar_chart(center_info_data['region_code'])
st.bar_chart(center_info_data['center_type'])
hist_data = [center_info_data['center_id'],center_info_data['region_code'],center_info_data['city_code']]
group_labels = ['Center Id', 'Region Code','city code']
fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25, 15])
st.plotly_chart(fig, use_container_width=True)

st.subheader('Meal Information')
st.write(meal_data)
st.line_chart(meal_data['cuisine'])

#if st.checkbox('Show raw data'):
#    st.subheader('Raw data')
#    st.write(data)
    
    


#st.bar_chart(data['checkout_price'])
#st.button('click')
#chart = st.line_chart(data['center_id'])
#
#hist_data = [data['checkout_price'], data['base_price'], data['num_orders']]
#group_labels = ['checkout_price', 'base_price', 'num_orders']
#fig = ff.create_distplot(hist_data,group_labels, bin_size=[.1, .25, .5])
#st.plotly_chart(fig, use_container_width=True)



#from PIL import Image
#image = Image.open('designflow.jpg')
#st.image(image, caption='Sunrise by the mountains', use_column_width=True)

#st.subheader('Number of pickups by hour')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)
#
## Some number in the range 0-23
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#
#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)