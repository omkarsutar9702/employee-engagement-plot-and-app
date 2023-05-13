# build the app
## import libraries
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
# get the data
# config the page wide and give name
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>optimization plot</h1>",
            unsafe_allow_html=True)

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df['color'] = np.where((df[df.columns[0]] < 0.3) & (df[df.columns[1]] < 50), "Low Foucs",
    np.where((df[df.columns[0]] <0.3) & (df[df.columns[1]] >50) , "Not Critical" ,
    np.where((df[df.columns[0]]>0.3) & (df[df.columns[1]]<50) ,"improvement",
    np.where((df[df.columns[0]]>0.3) & (df[df.columns[1]]>50) & (df[df.columns[1]]<75) , "Towards Excllence","Execllence"
    ))))
    fig1 = px.scatter(df, x=df.columns[0], y=df.columns[1], color="color", color_discrete_map={
        "Execllence": "#3859a1",
        "improvement": "#b52f51",
        "Not Critical" : "grey",
        "Low Foucs" : "pink",
        "Towards Excllence" : "#a7bbe8"
        },
                      labels={
        "x_axis": "employee engagement",
        "y_axis": "customer engagement"
    })
    fig1.update_traces(marker=dict(size=20))
    fig1.add_hline(50, line_width=3, line_color="yellowgreen")
    fig1.add_hline(50, line_width=3, line_color="yellowgreen")
    fig1.add_vline(0.3, line_width=3, line_color="yellowgreen")
    fig1.add_vline(0.6, line_width=3, line_color="yellowgreen")
    fig1.add_shape(type="line", x0=0.3, y0=75, x1=1, y1=75,
                   line=dict(color="yellowgreen", width=3,))
    fig1.add_annotation(x=0.1, y=99, text="not Critical", showarrow=False)
    fig1.add_annotation(x=1, y=99, text="Execllence", showarrow=False)
    fig1.add_annotation(x=0.1, y=11, text="Low Foucs", showarrow=False)
    fig1.add_annotation(x=1, y=11, text="Improvment", showarrow=False)
    fig1.update_xaxes(range=[0.0, 1], dtick=0.1)
    fig1.update_yaxes(range=[10, 100], dtick=10)
    st.plotly_chart(fig1, use_container_width=True)
else:
    st.warning('you need to upload a excel file, where x axis is in 1st column and y axis is in 2nd column.')
