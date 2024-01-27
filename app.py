import pandas as pd 
import numpy as np 
import streamlit as st 
import pickle
loaded_model = pickle.load(open('trained_model.sav','rb'))

st.set_page_config(layout = "wide",
                   page_title = "House price prediction"
)  


def main():
    st.title("House Price Prediction")
    st.info("""**Average Area Income** - Average income of residents in the region\n
**Average Area House Age** - Average age of houses in the region\n
**Average Area Number of Rooms** - Average number of rooms per house in the region\n
**Average Area Number of Bedrooms** - Average number of bedrooms per house in the region\n
**Area Population** - Population of the region the house is located in\n
""")


    p1 ,p2,p3,p4,p5= st.columns([1,2,2,2,1])
    income = p2.text_input("Average Area Income")
    house_age = p3.text_input("Average Area House Age")
    number_of_rooms = p4.text_input("Average Area Number of Rooms")

    p1 ,p2,p3,p4,p5= st.columns([2,2,0.2,2,2])
    number_of_bedrooms = p2.text_input("Average Area Number of Bedrooms")
    population = p4.text_input("Area Population")

    

    if st.button('Calculate'):
        input_array = np.array([float(income),float(house_age),float(number_of_rooms),float(number_of_bedrooms),float(population)])
        input_array = input_array.reshape(1,-1)
        predicted_value = loaded_model.predict(input_array)
        if predicted_value[0]>0:
            st.success(f"Predicted value: **{round(predicted_value[0])} $**")
        else:
            st.success("Not found")



    


if __name__ == '__main__':
     main()    
    
    