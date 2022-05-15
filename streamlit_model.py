import pickle
import streamlit as st
from PIL import Image

#add title
st.title('Airbnb Review Content Analyzer')

#read in pipe from pickle
with open('saved_models/location_pipe.pkl', 'rb') as pickle_in:
    loc_pipe = pickle.load(pickle_in)

with open('saved_models/comfort_pipe.pkl', 'rb') as pickle_in:
    comf_pipe = pickle.load(pickle_in)

with open('saved_models/cost_pipe.pkl', 'rb') as pickle_in:
    cost_pipe = pickle.load(pickle_in)

with open('saved_models/hygeine_pipe.pkl', 'rb') as pickle_in:
    hyg_pipe = pickle.load(pickle_in)

with open('saved_models/host_pipe.pkl', 'rb') as pickle_in:
    host_pipe = pickle.load(pickle_in)

#insert image
img = Image.open('images/airbnblogo.png')
st.image(img)

#code for user to enter text
your_text = st.text_area('Enter your text here', height=200, max_chars=500)

#predictions
loc_pred = loc_pipe.predict([your_text])[0]
comf_pred = comf_pipe.predict([your_text])[0]
cost_pred = cost_pipe.predict([your_text])[0]
hyg_pred = hyg_pipe.predict([your_text])[0]
host_pred = host_pipe.predict([your_text])[0]

#if statements to generate results
results_list = []

if loc_pred == 1:
    results_list.append('Location')
if comf_pred == 1:
    results_list.append('Comfort')
if cost_pred == 1:
    results_list.append('Cost')
if hyg_pred == 1:
    results_list.append('Hygiene')
if host_pred == 1:
    results_list.append('Host')
if len(results_list) == 0:
    results_list.append('No results')

#generated predictions
st.write(f'This review mentions {results_list}')
