
import numpy as np
import pandas as pd
import pickle
import streamlit as st
import plotly_express as px
from sklearn.preprocessing import StandardScaler
st.set_option('deprecation.showfileUploaderEncoding', False)
sc=StandardScaler()

X_train=pd.read_csv('x_train.csv')
X_train=X_train.iloc[:,1:]
x_train=sc.fit_transform(X_train)
global df
df=pd.read_csv('data.csv')
global numeric_columns
global non_numeric_columns



from PIL import Image

pickle_in = open("project.pkl","rb")
classifier=pickle.load(pickle_in)

page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8c3RvY2slMjBtYXJrZXR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60");
    background-size: cover;
    }
    </style>
    ''' 
# st.markdown(page_bg_img, unsafe_allow_html=True)
def function(offer_type,gender,days_of_membership,total_amount,year,age_in_range,income_in_range):
    l=[]
    if(offer_type==1):
        reward=10
        difficulty=10
        duration=168
        mobile=1
        social=1
        web=0
        bogo=1
        discount=0
        informational=0
    elif(offer_type==2):
        reward=10
        difficulty=10
        duration=120
        mobile=1
        social=1
        web=1
        bogo=1
        discount=0
        informational=0
    elif(offer_type==3):
        reward=0
        difficulty=0
        duration=96
        mobile=1
        social=0
        web=1
        bogo=0
        discount=0
        informational=1
    elif(offer_type==4):
        reward=5
        difficulty=5
        duration=168
        mobile=1
        social=0
        web=1
        bogo=1
        discount=0
        informational=0
    elif(offer_type==5):
        reward=5
        difficulty=20
        duration=240
        mobile=0
        social=0
        web=1
        bogo=0
        discount=1
        informational=0
    elif(offer_type==6):
        reward=3
        difficulty=7
        duration=168
        mobile=1
        social=1
        web=1
        bogo=0
        discount=1
        informational=0
    elif(offer_type==7):
        reward=2
        difficulty=10
        duration=240
        mobile=1
        social=1
        web=1
        bogo=0
        discount=1
        informational=0
    elif(offer_type==8):
        reward=0
        difficulty=0
        duration=72
        mobile=1
        social=1
        web=0
        bogo=0
        discount=0
        informational=1
    elif(offer_type==9):
        reward=5
        difficulty=5
        duration=120
        mobile=1
        social=1
        web=1
        bogo=1
        discount=0
        informational=0
    elif(offer_type==10):
        reward=2
        difficulty=10
        duration=168
        mobile=1
        social=0
        web=1
        bogo=0
        discount=1
        informational=0
    M=0
    F=0
    O=0
    if(gender=='F'):
        F=1
    elif(gender=='M'):
        M=1
    elif(gender=='O'):
        O=1
    y_2013=0
    y_2014=0
    y_2015=0
    y_2016=0
    y_2017=0
    y_2018=0
    if(year==2013):
        y_2013=1
    elif(year==2014):
        y_2014=1
    elif(year==2015):
        y_2015=1
    elif(year==2016):
        y_2016=1
    elif(year==2017):
        y_2017=1
    elif(year==2018):
        y_2018=1
    age_10s=0
    age_20s=0
    age_30s=0
    age_40s=0
    age_50s=0
    age_60s=0
    age_70s=0
    age_80s=0
    age_90s=0
    age_100s=0
    if(age_in_range=='10s'):
        age_10s=1
    elif(age_in_range=='20s'):
        age_20s=1
    elif(age_in_range=='30s'):
        age_30s=1
    elif(age_in_range=='40s'):
        age_40s=1
    elif(age_in_range=='50s'):
        age_50s=1
    elif(age_in_range=='60s'):
        age_60s=1
    elif(age_in_range=='70s'):
        age_70s=1
    elif(age_in_range=='80s'):
        age_80s=1
    elif(age_in_range=='90s'):
        age_90s=1
    elif(age_in_range=='100s'):
        age_100s=1
    in_40=0
    in_50=0
    in_60=0
    in_70=0
    in_80=0
    in_100=0
    in_110=0
    in_120=0
    if(income_in_range=='40k'):
        in_40=1
    if(income_in_range=='50k'):
        in_50=1
    if(income_in_range=='60k'):
        in_60=1
    if(income_in_range=='70k'):
        in_70=1
    if(income_in_range=='80k'):
        in_80=1
    if(income_in_range=='100k'):
        in_100=1
    if(income_in_range=='110k'):
        in_110=1
    if(income_in_range=='120k'):
        in_120=1
    l=[[reward,difficulty,duration,mobile,social,web,bogo,discount,informational,F,M,O,days_of_membership,total_amount,y_2013,y_2014,y_2015,y_2016,y_2017,y_2018,age_100s,age_10s,age_20s,age_30s,age_40s,age_50s,age_60s,age_70s,age_80s,age_90s,in_100,in_110,in_120,in_40,in_50,in_60,in_70,in_80]]
    return l

def welcome():
    return "Welcome All"

def membership_predict(offer_type,gender,days_of_membership,total_amount,year,age_in_range,income_in_range):
    prediction=classifier.predict(sc.transform(function(offer_type,gender,days_of_membership,total_amount,year,age_in_range,income_in_range)))
    print(prediction)
    # print(sc.transform(function(offer_type,gender,days_of_membership,total_amount,year,age_in_range,income_in_range)))
    return prediction

def main():
    st.title("Infographs")
  
    html_temp = """
    <div style="background-color:Red;padding:10px">
    <h1 style="color:orange;text-align:center;"><em>Infographs</em> </h1>
    </div>
    <br></br>
    """


    offer=('Offer-Type-1','Offer-Type-2','Offer-Type-3','Offer-Type-4','Offer-Type-5','Offer-Type-6','Offer-Type-7','Offer-Type-8','Offer-Type-9','Offer-Type-10')
    option_offer=list(range(len(offer)))
    offer_type = st.selectbox("Offer_type",option_offer,format_func=lambda x:offer[x])
    offer_type=offer_type+1
    gender_box=('M','F','O')
    gender = st.selectbox("Gender",options=list(gender_box))
    days_of_membership = st.number_input("Days Of Memebership");
    total_amount = st.number_input("Amount(Bill of the customer)")
    year = st.number_input("year")
    age_in_range = st.slider("Age",0,100);
    age_in_range=str(age_in_range)+"s";
    income_in_range = st.text_input("Income Of The Customer")
    result=""
    if st.button("Predict"):
        result=membership_predict(offer_type,gender,days_of_membership,total_amount,year,age_in_range,income_in_range)
        if(result ==1):
            st.success("The Customer Will Take Member Ship")
        elif(result==0):
            st.warning("He wont Take")
    agree=st.checkbox("Hide Graphs")
    if (not agree):
        st.sidebar.subheader("Visualization Settings")
        try:
            st.write(df)
        # numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
            numeric_columns=list(['income','total_amount','days_of_membership'])
        
            non_numeric_columns = list(df.select_dtypes(['object']).columns)
        
            non_numeric_columns.append(None)
            print(numeric_columns)
        except Exception as e:
            print(e)
            st.write("Please upload file to the application.")
        # add a select widget to the side bar
        chart_select = st.sidebar.selectbox(
            label="Select the chart type",
            options=['Histogram', 'Lineplots','Scatterplots',  'Boxplot'])

        if chart_select == 'Scatterplots':
            st.sidebar.subheader("Scatterplot Settings")
            try:
                x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
                y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
                color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
                plot = px.scatter(data_frame=df, x=x_values, y=y_values, color=color_value)
                # display the chart
                st.plotly_chart(plot)
            except Exception as e:
                print(e)
    
        if chart_select == 'Lineplots':
            st.sidebar.subheader("Line Plot Settings")
            try:
                x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
                y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
                color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
                plot = px.line(data_frame=df, x=x_values, y=y_values, color=color_value)
                st.plotly_chart(plot)
            except Exception as e:
                print(e)
    
        if chart_select == 'Histogram':
            st.sidebar.subheader("Histogram Settings")
            try:
                x = st.sidebar.selectbox('Feature', options=numeric_columns)
                bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                                         max_value=100, value=40)
                color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
                plot = px.histogram(x=x, data_frame=df, color=color_value)
                st.plotly_chart(plot)
            except Exception as e:
                    print(e)
    
        if chart_select == 'Boxplot':
            st.sidebar.subheader("Boxplot Settings")
            try:
                y = st.sidebar.selectbox("Y axis", options=numeric_columns)
                x = st.sidebar.selectbox("X axis", options=non_numeric_columns)
                color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
                plot = px.box(data_frame=df, y=y, x=x, color=color_value)
                st.plotly_chart(plot)
            except Exception as e:
                print(e)
            
        
   

if __name__=='__main__':
    main()