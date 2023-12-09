import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    
    input_data = [str(item).encode('ascii', 'ignore').decode() for item in input_data]

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    HighBP = st.selectbox('Are you having High Blood Pressure? (0 = No high BP, 1 = high BP)', [0, 1])
    HighChol = st.selectbox('Are you having High Cholesterol? (0 = No high Cholesterol, 1 = high Cholesterol)', [0, 1])
    BMI = st.text_input('Body Mass Index (BMI)')
    Smoker = st.selectbox('Have you smoked at least 100 cigarettes in your entire life? (0 = No, 1 = Yes)', [0,1])
    Stroke = st.selectbox('Did you ever had a stroke? (0 = No, 1 = Yes)', [0,1])
    HeartDiseaseorAttack = st.selectbox('Do you have coronary heart disease (CHD) or myocardial infarction (MI) (0 = No, 1 = Yes)', [0,1])
    Fruits = st.selectbox('Do you consume fruits 1 or more times per day (0 = No, 1 = Yes)', [0,1])
    Veggies = st.selectbox('Do you consume vegetables 1 or more times per day (0 = No, 1 = Yes)', [0,1])
    HvyAlcoholConsump = st.selectbox('Are you a heavy drinker? (0 = No, 1 = Yes)', [0,1])
    GenHlth = st.selectbox('Would you say that in general your health is: (Scale: 1-5, 1 = excellent, 2 = very good, 3 = good, 4 = fair, 5 = poor)', [1,2,3,4,5])
    PhysHlth = st.slider('For how many days during the past 30 days was your physical health not good, including physical illness and injury?', 1, 30)
    DiffWalk = st.selectbox('Do you have serious difficulty walking or climbing stairs? (0 = No, 1 = Yes)', [0,1])
    Sex = st.selectbox('Are you a female or a male? (0 = Female, 1 = Male)', [0,1])
    age_categories = {
        1: '18-24', 2: '25-29', 3: '30-34', 4: '35-39', 5: '40-44',
        6: '45-49', 7: '50-54', 8: '55-59', 9: '60-64', 10: '65-69',
        11: '70-74', 12: '75-79', 13: '80 or older'
    }

    # Display numerical representation of age categories in one line
    Age = st.selectbox('What is your age category?', [f'{num}: {category}' for num, category in age_categories.items()])
    selected_age_num = int(Age.split(':')[0])


    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([HighBP,HighChol, BMI,Smoker,Stroke,HeartDiseaseorAttack,Fruits,Veggies,HvyAlcoholConsump,GenHlth,PhysHlth,DiffWalk,Sex,selected_age_num])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
