import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
**This is my first fronted**
''')


# with st.form(key='params_for_api')
pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2023, 9, 12, 10, 00, 00))
pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2023, 9, 12, 11, 00, 00))
pickup_datetime = f'{pickup_date} {pickup_time}'
pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('pickup latitude', value=40.7614327)
dropoff_longitude = st.number_input('dropoff longitude', value=40.7614327)
dropoff_latitude = st.number_input('dropoff latitude', value=40.7614327)
passenger_count = st.number_input('passenger count', min_value=1, max_value=4, step=1, value=1)

params= dict(
    pickup_datetime = pickup_datetime,
    pickup_longitude = pickup_longitude,
    pickup_latitude = pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count = passenger_count
)


url = 'https://taxifare-d6yophmzga-ew.a.run.app/predict'  # this is my fast API address
response = requests.get(url, params=params)

prediction = response.json()
pred = prediction['fare_amount']

st.markdown('''
            Returning Results)
''')

st.header(f'The Fare Amount: ${round(pred, 2)}')
## Once we have these, let's call our API in order to retrieve a prediction
