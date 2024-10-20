import streamlit as st 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
# from matplotlib.backends.backend_agg import RendererAgg
import numpy as np
# import plotly.express as px

#Loading the data
@st.cache_data
def get_data_hdb_resale():
    url = 'https://drive.google.com/file/d/19P2q3RyermaGJuD88vq1ZxcMjotpq18h/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df_hdb_resale = pd.read_csv(url)
    return df_hdb_resale

#configuration of the page
st.set_page_config(layout="wide")
#load dataframes
df_hdb_resale = get_data_hdb_resale()

st.title(':blue[HDB Resale transaction explorer]')
st.markdown("""
This app performs visualization from the open data of SG HDB Resale transaction
""")
# st.write(df_hdb_resale)

# create a drop down list
selected_measure = st.selectbox('Choose a Measure that you are interested', ['Resale Price', 'Distance to Hawker Centre', 'Distance to Mall'], key='selected_measure')

# create multi-select for town
hdb_town = df_hdb_resale['town'].unique().tolist()
hdb_town_selected = st.multiselect('Select Town that you would like to exclude: ', hdb_town, hdb_town)

# create selection
st.sidebar.header('Select what to display')

# create a drop down list
flat_type = df_hdb_resale['flat_type'].unique().tolist()
hdb_flattype_selected = st.sidebar.selectbox('Select Flat Type', flat_type, key='selected_type')

nb_deputies = df_hdb_resale['year']
nb_mbrs = st.sidebar.slider("Select Year", int(nb_deputies.min()), int(nb_deputies.max()), (int(nb_deputies.min()), int(nb_deputies.max())), 1)


## Create Masks
# creates masks from the sidebar selection widgets
mask_pol_par = df_hdb_resale['town'].isin(hdb_town_selected)

# creates masks for years slicer
mask_mbrs = df_hdb_resale['year'].between(nb_mbrs[0], nb_mbrs[1])



# testing display
# df_pivot = pd.pivot_table(df, values=['resale_price', 'Mall_Nearest_Distance','Hawker_Nearest_Distance'], index=['town'], columns=['year'], aggfunc='mean')
# df_pivot = np.round(df_pivot,2)
# st.write(df_pivot)



## apply mask to the data
df_hdb_resale_filtered = df_hdb_resale[mask_pol_par & mask_mbrs]
st.write(df_hdb_resale_filtered)




# Create a Bar chart
df_count = (
    df_hdb_resale_filtered.groupby("year")
    .count()
    .reset_index()
    .rename(columns={"town": "Count"})
)
st.bar_chart(df_count, x = "year", y="Count")

# Create a Scatter Chart
st.scatter_chart(
    df_hdb_resale_filtered,
    x="floor_area_sqm",
    y="resale_price",
    color="flat_type",
)
# 


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