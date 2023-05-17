import streamlit as st

st.write("Hello World !")

st.header('st.button')

if st.button('Say Hello'):
    st.write("Hello there !!! How are you ?")
else:
    st.write("Good Bye")

import numpy as np
import altair as alt
import pandas as pd

st.header('st.write')

st.write('Hello, *World!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

st.write('Below is a Dataframe:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns = ['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a', 'b', 'c']
)

st.write(c)

#------------- slider ----------- #
from datetime import time, datetime

st.header('st.slider')

st.subheader('Slider')

age = st.slider('How old are you ?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.subheader('Range slider')

values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0)
)
st.write("Values: ", values)

st.subheader('Range time slider')

appointment = st.slider(
    "Schedule your appointment: ",
    value = (time(11, 30), time(12, 45))
)
st.write("You are scheduled for: ", appointment)

st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value = datetime(2020, 1, 1, 9, 30),
    format = "MM/DD/YY - hh:mm"
)
st.write("Start time: ", start_time)

st.subheader('Duration slider')

duration = st.slider(
    "What's your duration ?",
    value = (datetime(2023, 5, 15, 10, 00), datetime(2030, 1, 16, 9, 59)),
    format = "MM/DD/YY - hh:mm"
)
st.write("Job Tenure: ", duration)


##----- Day - 9 ####

# Create a Pandas dataframe from numbers randomly generated via NumPy
# Create and display the line chart.

import streamlit as st
import pandas as pd
import numpy as np

st.header('Line Chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c']
)

st.line_chart(chart_data)

## --- Day - 10 ####

# User selects a color
# App prints out the selected color

import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    "What is your favorite color ?",
    ('Blue', 'Red', 'Green')
)

st.write('Your favorite color is ', option)

## --- Day - 11 ###
# Multi-select

import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'What are your favorite colors ?',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write('You selected: ', options)

##--- Day - 12 ###
# Checkbox widget

import streamlit as st

st.header('st.checkbox')
st.write('What would you like to order ?')

icecream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great !! Here's some more 🍦")
if coffee:
    st.write("Great !! Here's some more ☕")
if cola:
    st.write("Here you go 🥤")

## -- Day - 14 ###
# Streamlit component : Streamlit Pandas profiling : https://okld-gallery.streamlit.app/?p=pandas-profiling
# pip install streamlit_pandas_profiling

import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
# pandas profiling report is generated 
pr = df.profile_report()
st_profile_report(pr)

# --- Day - 15 ---- #
# LaTeX

import streamlit as st

st.header('st.latex')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
''')

''' Day - 16 : customizing the themes '''

# import streamlit as st

# st.title('Customizing the theme of Streamlit apps')

# st.write('Contents of the `.streamlit/config.toml` file of this app')

# st.code("""
# [theme]
# primaryColor="#F39C12"
# backgroundColor="#2E86C1"
# secondaryBackgroundColor="#AED6F1"
# textColor="#FFFFFF"
# font="monospace"
# """)

# number = st.sidebar.slider('Select a number:', 0, 10, 5)
# st.write('Selected number from slider widget is:', number)

# # --- Day 17 : Secrets #

# st.title('st.secrets')
# st.write(st.secrets['message'])

'''
It should be noted that, secrets can be stored in Streamlit Community Cloud as shown in the screenshots shown below.

If working locally, they can be stored in .streamlit/secrets.toml, but make sure to avoid uploading this to a GitHub repo when deploying the app.

'''

# --- Day 18 : file uploader --- #

import streamlit as st
import pandas as pd

st.title('st.file_uploader')
st.subheader('Input CSV')
uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info('☝️ Upload a CSV file')

# -- Day - 19 : Layout your Streamlit App -- #

# st.set_page_config(layout = "wide")
st.title('How to layout your Streamlit app')

with st.expander('About this app'):
    st.write('This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width = 250)

st.sidebar.header('Input')

user_name = st.sidebar.text_input('What is your name ?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food ?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
    if user_name != '':
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write('👈  Please enter your **name**!')

with col2:
    if user_emoji != '':
        st.write(f'{user_emoji} is your favorite **emoji**!')
    else:
        st.write('👈 Please choose an **emoji**!')

with col3:
    if user_food != '':
        st.write(f'🍴 **{user_food}** is your favorite **food**!')
    else:
        st.write('👈 Please choose your favorite **food**!')