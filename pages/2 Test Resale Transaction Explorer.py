import streamlit as st 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
# from matplotlib.backends.backend_agg import RendererAgg
import numpy as np
# import plotly.express as px


#configuration of the page
st.set_page_config(layout="wide")
st.title(':blue[HDB Resale transaction explorer]')
st.markdown("""
This app performs visualization from the open data of SG HDB Resale transaction
""")
# create selection
st.sidebar.header('Select what to display')

# Session 1 number of Resale transaction 
st.subheader('Session 1: Number of HDB resale transaction by year')
#Loading the data
# @st.cache_data
def get_data_hdb_resale_count():
    url = 'https://drive.google.com/file/d/1osPgUJJFP3SJe4F4QI2XvdNLGYVnhwX7/view?usp=share_link'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url)
    return df

def get_data_hdb_resale_count_pivot():
    df = get_data_hdb_resale_count()
    df_hdb_resale_pivot = pd.pivot_table(df, values='Number_of_Transaction', index=['town'], columns=['year'], aggfunc='mean')
    return df_hdb_resale_pivot

df_hdb_resale = get_data_hdb_resale_count_pivot()
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df_hdb_resale)

df_hdb_resale = get_data_hdb_resale_count()
st.bar_chart(df_hdb_resale, x = "year", y="Number_of_Transaction")

## Create sidebar filter 1
# flat_type = df_hdb_resale['flat_type'].unique().tolist()
# hdb_flattype_selected = st.sidebar.selectbox('Select Flat Type', flat_type, key='selected_type')

## Create sidebar filter 2
resale_year = df_hdb_resale['year']
st.write(resale_year)
resale_year_selected = st.sidebar.slider("Select Year", int(resale_year.min()), int(resale_year.max()), (int(resale_year.min()), int(resale_year.max())), 1)


# Session 2
st.subheader('Session 2: Measure of Interest')
# create a drop down list
selected_measure = st.selectbox('Choose a Measure that you are interested', ['Resale Price', 'Distance to Hawker Centre', 'Distance to Mall'], key='selected_measure')

# Create variable
if selected_measure == 'Resale Price':
    pivot_url = 'https://drive.google.com/file/d/1VniabsUyhxnT77aNUQBDcecYXQ-zHQY3/view?usp=share_link'
    column_name = 'mean_resale_price'
elif selected_measure == 'Distance to Mall':
    pivot_url = 'https://drive.google.com/file/d/1RKV3ZzPtPxxNm7EcrTBAgQCT4D3XBqEx/view?usp=share_link'
    column_name = 'mean_Mall_Nearest_Distance'
elif selected_measure == 'Distance to Hawker Centre':
    pivot_url = 'https://drive.google.com/file/d/12C_xfDkRSYitGQgcMkig8fvOfsw1w-cy/view?usp=share_link'
    column_name = 'mean_Hawker_Nearest_Distance'
df_url='https://drive.google.com/uc?id=' + pivot_url.split('/')[-2]

# create multi-select for town
hdb_town = df_hdb_resale['town'].unique().tolist()
hdb_town_selected = st.multiselect('Select Town that you would like to include: ', hdb_town, hdb_town)

#Loading the data with measure variable
def get_data_hdb_measure():
    df_hdb_selected_measure = pd.read_csv(df_url)
    return df_hdb_selected_measure

#load dataframes
df_hdb_selected_measure = get_data_hdb_measure()

## Create Masks
mask_town = df_hdb_selected_measure['town'].isin(hdb_town_selected)
# creates masks for years slicer
mask_years = df_hdb_resale['year'].between(resale_year_selected[0], resale_year_selected[1])

st.write(mask_years)
## apply mask to the data
df_hdb_selected_measure_filtered = df_hdb_selected_measure[mask_town & mask_years]

# create pivot table based on selected measure
df_pivot = pd.pivot_table(df_hdb_selected_measure_filtered, values=column_name, index=['town'], columns=['year'], aggfunc='mean')
df_pivot = np.round(df_pivot,2)
if st.checkbox(f'Show {selected_measure} data'):
    st.subheader('Raw data')
    st.write(df_pivot)

# create bar chart
st.bar_chart(df_hdb_selected_measure_filtered, x = "year", y=column_name, color="town", stack=False)




# # create multi-select for town
# hdb_town = df_hdb_resale['town'].unique().tolist()
# hdb_town_selected = st.multiselect('Select Town that you would like to exclude: ', hdb_town, hdb_town)

# # create selection
# st.sidebar.header('Select what to display')

# # create a drop down list
# flat_type = df_hdb_resale['flat_type'].unique().tolist()
# hdb_flattype_selected = st.sidebar.selectbox('Select Flat Type', flat_type, key='selected_type')

# nb_deputies = df_hdb_resale['year']
# nb_mbrs = st.sidebar.slider("Select Year", int(nb_deputies.min()), int(nb_deputies.max()), (int(nb_deputies.min()), int(nb_deputies.max())), 1)


# ## Create Masks
# # creates masks from the sidebar selection widgets
# mask_pol_par = df_hdb_resale['town'].isin(hdb_town_selected)

# # creates masks for years slicer
# mask_mbrs = df_hdb_resale['year'].between(nb_mbrs[0], nb_mbrs[1])



# # testing display based on selection
# if selected_measure == 'Resale Price':
#     df_pivot = pd.pivot_table(df_hdb_resale, values='resale_price', index=['town'], columns=['year'], aggfunc='mean')
# elif selected_measure == 'Distance to Hawker Centre':
#     df_pivot = pd.pivot_table(df_hdb_resale, values='Hawker_Nearest_Distance', index=['town'], columns=['year'], aggfunc='mean')
# elif selected_measure == 'Distance to Mall':
#     df_pivot = pd.pivot_table(df_hdb_resale, values='Mall_Nearest_Distance', index=['town'], columns=['year'], aggfunc='mean')
# df_pivot = np.round(df_pivot,2)
# st.write(df_pivot)

# # testing bar char based selection
# # st.bar_chart(source, x="year", y="yield", color="site", stack=False)
# df_mean = (
#     df_hdb_resale[['year', 'town', 'resale_price']].groupby(["year", "town"])
#     .mean()
#     .reset_index()
#     .rename(columns={"resale_price": "mean_resale_price"})
# )
# st.bar_chart(df_mean, x = "year", y="mean_resale_price",color="town", stack=False)

# # test

# ## apply mask to the data
# df_hdb_resale_filtered = df_hdb_resale[mask_pol_par & mask_mbrs]
# st.write(df_hdb_resale_filtered)



# # Create a Bar chart
# df_count = (
#     df_hdb_resale_filtered.groupby("year")
#     .count()
#     .reset_index()
#     .rename(columns={"town": "Count"})
# )
# st.bar_chart(df_count, x = "year", y="Count")

# # Create a Scatter Chart
# st.scatter_chart(
#     df_hdb_resale_filtered,
#     x="floor_area_sqm",
#     y="resale_price",
#     color="flat_type",
# )
# # 


## not working
# matplotlib.use("agg")
# _lock = RendererAgg.lock

# # setting color
# pol_par = df_hdb_resale_filtered['town'].value_counts()
# #merge the two dataframe to get a column with the color
# df = pd.merge(pd.DataFrame(pol_par), df_hdb_resale, left_index=True, right_on='abreviated_name')
# colors = df['color'].tolist()

# # chart
# row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.beta_columns((0.2, 1, .2, 1, .2))
# with row0_1, _lock:
#     st.header("HDB")
#     fig, ax = plt.subplots(figsize=(5, 5))
#     ax.pie(pol_par, labels=(pol_par.index + ' (' + pol_par.map(str)
#     + ')'), wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white'
#     }, colors=colors)
#     #display a white circle in the middle of the pie chart
#     p = plt.gcf()
#     p.gca().add_artist(plt.Circle( (0,0), 0.7, color='white'))
#     st.pyplot(fig)