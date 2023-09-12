import streamlit as st
import requests
import datetime

# Set a custom page title
st.set_page_config(page_title="Taxi Fare Prediction App", page_icon="🚖")

'''
# 🚖 TaxiFareModel Frontend 🚖
'''

st.markdown('''
**Welcome to the Taxi Fare Prediction App!**
''')

# Form for input
with st.form(key='params_for_api'):
    st.subheader("The Taxifare Summary are below::")
    pickup_date = st.date_input('Pickup Date', value=datetime.date(2023, 9, 12))
    pickup_time = st.time_input('Pickup Time', value=datetime.time(10, 0))
    pickup_longitude = st.number_input('Pickup Longitude', value=40.7614327)
    pickup_latitude = st.number_input('Pickup Latitude', value=40.7614327)
    dropoff_longitude = st.number_input('Dropoff Longitude', value=40.7614327)
    dropoff_latitude = st.number_input('Dropoff Latitude', value=40.7614327)
    passenger_count = st.number_input('Passenger Count', min_value=1, max_value=4, step=1, value=1)

    submitted = st.form_submit_button('Submit')

if submitted:
    # Create a datetime object
    pickup_datetime = datetime.datetime.combine(pickup_date, pickup_time)

    params = {
        'pickup_datetime': pickup_datetime.isoformat(),
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    url = 'https://taxifare-d6yophmzga-ew.a.run.app/predict'  # your FastAPI endpoint
    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json()
        pred = prediction['fare_amount']

        st.markdown('''
                    Returning Results
        ''')

        st.header(f'The Fare Amount: ${round(pred, 2)}')

        # Display the input data for reference
        st.subheader("Input Data")
        st.write(f'Pickup Date and Time: {pickup_datetime}')
        st.write(f'Pickup Longitude: {pickup_longitude}')
        st.write(f'Pickup Latitude: {pickup_latitude}')
        st.write(f'Dropoff Longitude: {dropoff_longitude}')
        st.write(f'Dropoff Latitude: {dropoff_latitude}')
        st.write(f'Passenger Count: {passenger_count}')
    else:
        st.error(f'Error: {response.status_code} - Failed to retrieve prediction from the API')
