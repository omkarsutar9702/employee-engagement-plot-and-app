# ### build the app
# ## import libraries
# import pandas as pd
# import plotly.express as px
# import streamlit as st
# ### get the data

# ## config the page wide and give name
# st.set_page_config(layout="wide")
# st.markdown("<h1 style='text-align: center;'>optimization plot</h1>", unsafe_allow_html=True)


# #read csv
# df = pd.read_csv("E:/VS-Code python/optimazation plot/dummy_data.csv")
# ### plot the graph 
# col1 , col2 = st.columns(2)
# with col1:
#     st.markdown("<h3 style='text-align: center;'>Overall plot</h3>", unsafe_allow_html=True)
#     select_axis = st.sidebar.selectbox("select y axis" , ['y_axis' , 'Target' , 'persentage'])
#     st.write("you have selected", select_axis )    
#     if 'y_axis' in select_axis:
#         groupby_Man = df.groupby(['Manager']).mean()
#         fig1 = px.scatter(groupby_Man, x = 'x_axis' , y ='y_axis',
#                         labels={
#                             "x_axis":"employee engagement",
#                             "y_axis": "customer engagement"
#                         })
#         fig1.add_hline(3.5 , line_width = 3 , line_color = "yellowgreen")
#         fig1.add_vline(3.5 , line_width = 3 , line_color = "yellowgreen")
#         fig1.update_xaxes(range=[1,5] , dtick = 1)
#         fig1.update_yaxes(range=[1,5] , dtick = 1)
#         fig1.add_annotation(x=4.5 , y=4.5 , text=round(groupby_Man[(groupby_Man['x_axis'] > 3.5) & (groupby_Man['y_axis'] >3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         fig1.add_annotation(x=4.5 , y=1.5 , text=round(groupby_Man[(groupby_Man['x_axis'] > 3.5) & (groupby_Man['y_axis'] <3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         fig1.add_annotation(x=1.5 , y=1.5 , text=round(groupby_Man[(groupby_Man['x_axis'] < 3.5) & (groupby_Man['y_axis'] <3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         fig1.add_annotation(x=1.5 , y=4.5 , text=round(groupby_Man[(groupby_Man['x_axis'] < 3.5) & (groupby_Man['y_axis'] >3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         st.plotly_chart(fig1 , use_container_width=True)

#     elif 'Target' in select_axis:
#         groupby_Man= df.groupby(['Manager']).mean()
#         fig1 = px.scatter(groupby_Man , x = 'x_axis' , y ='Target', 
#                         labels={
#                             "x_axis":"employee engagement",
#                             "y_axis": "customer engagement"
#                         })
#         fig1.update_xaxes(range=[1,5] , dtick = 1)
#         fig1.update_yaxes(range=[10,100] , dtick = 10)
#         fig1.add_vline(3.5 , line_width = 3 , line_color = "yellowgreen")
#         fig1.add_annotation(x=1.5 , y=90 , text=round(groupby_Man[(groupby_Man['x_axis'] < 3.5) & (groupby_Man['y_axis'] <3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         fig1.add_annotation(x= 4.5, y=90 , text=round(groupby_Man[(groupby_Man['x_axis'] > 3.5) & (groupby_Man['y_axis'] >3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         st.plotly_chart(fig1 , use_container_width=True)

#     else:
#         groupby_Man= df.groupby(['Manager']).mean()
#         fig1 = px.scatter(groupby_Man , x = 'x_axis' , y ='persentage', 
#                         labels={
#                             "x_axis":"employee engagement"
#                         })
#         fig1.update_xaxes(range=[1,5] , dtick = 1)
#         fig1.update_yaxes(range=[10,200] , dtick = 20)
#         fig1.add_vline(3.5 , line_width = 3 , line_color = "yellowgreen")
#         fig1.add_annotation(x=1.5 , y=90 , text=round(groupby_Man[(groupby_Man['x_axis'] < 3.5) & (groupby_Man['y_axis'] <3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         fig1.add_annotation(x= 4.5, y=90 , text=round(groupby_Man[(groupby_Man['x_axis'] > 3.5) & (groupby_Man['y_axis'] >3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         st.plotly_chart(fig1 , use_container_width=True)
    
# st.write("******")
# ### filter plot
# with col2:
#     st.markdown("<h3 style='text-align: center;'>Filter plot</h3>", unsafe_allow_html=True)
#     city=st.sidebar.selectbox("select city" , df['City'].unique())
#     state=st.sidebar.selectbox("select state" , df['State'].unique())
#     st.write("you have selected", city , "and" , state)
#     def filter_plot(x , y):
#         filter= df[(df['City'] == x) & (df['State'] == y)]
#         group= filter.groupby(['Manager']).mean()
#         fig = px.scatter(group , x = 'x_axis' , y = 'y_axis',  labels={
#                         "x_axis":"employee engagement",
#                         "y_axis": "customer engagement"
#                     })
#         fig.add_hline(3.5 , line_width = 3 , line_color = "yellowgreen")
#         fig.add_vline(3.5 , line_width = 3 , line_color = "yellowgreen")
#         fig.update_xaxes(range=[1,5] , dtick = 1)
#         fig.update_yaxes(range=[1,5] , dtick = 1)
#         fig.add_annotation(x=4.5 , y=4.5 , text=round(groupby_Man[(groupby_Man['x_axis'] > 3.5) & (groupby_Man['y_axis'] >3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         fig.add_annotation(x=4.5 , y=1.5 , text=round(groupby_Man[(groupby_Man['x_axis'] > 3.5) & (groupby_Man['y_axis'] <3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         fig.add_annotation(x=1.5 , y=1.5 , text=round(groupby_Man[(groupby_Man['x_axis'] < 3.5) & (groupby_Man['y_axis'] <3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         fig.add_annotation(x=1.5 , y=4.5 , text=round(groupby_Man[(groupby_Man['x_axis'] < 3.5) & (groupby_Man['y_axis'] >3.5)]['Target'].mean(axis=0) , 2), showarrow=False)
#         return st.plotly_chart(fig , use_container_width=True)
#     filter_plot(city , state)

