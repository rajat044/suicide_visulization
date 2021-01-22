import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st 


df = pd.read_csv('dataset/suicide.csv')

df.drop(['country-year', ' gdp_for_year ($) ', 'gdp_per_capita ($)'], axis = 1, inplace = True)

st.title('Suicide Rate')
st.sidebar.markdown('## Select the Country')
con = st.sidebar.selectbox('', df.country.unique())

tem_df = df[(df.country == con)]

tem_y = tem_df.year.unique()
st.markdown('## Select the Year')
year = st.slider('', int(min(tem_y)), int(max(tem_y)))

tem_df = tem_df[tem_df.year == year]

fig = make_subplots(rows=1, cols=2)
try: 
	st.markdown(f'## {con} of {year}')
	if len(df) != 0: 
		p1 = go.bar(tem_df, x = 'age', y = 'suicides_no', 
			color = 'sex', barmode = 'group',
			labels = {'age': 'Age Group', 'suicides_no': 'Number of Suicides'})
		fig.add_trace(p1, row = 1, col = 1)
		st.write(p1)

		p2 = go.Figure(data=[go.Pie(labels=tem_df.age, values=tem_df.suicides_no, pull=[0, 0.2, 0, 0])])
		fig.add_trace(p2, row = 1, col = 2)
		fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
		st.write(p2)
except: 
	st.write(fig)
	st.error('Data is not available')
