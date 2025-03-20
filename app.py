import streamlit as st
import pickle
import os

import streamlit as st

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")
import streamlit as st

# Hide Streamlit UI Elements
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Background Image with Scroll Support
page_bg_img = """
    <style>
    .stApp {
        background: url("https://www.shutterstock.com/image-photo/doctor-utilizing-advanced-digital-tablet-600nw-2481904799.jpg") no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """
st.markdown(page_bg_img, unsafe_allow_html=True)

# Aesthetic Enhancements
st.markdown(
    """
    <style>

    .title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80px; /* Adjust height to match the black box */
        width: 100%;
        background: rgba(0, 0, 0, 0.6); /* Keep black box */
        border-radius: 15px;
        text-align: center;
    }

    .title-text {
        font-size: 35px;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
    }
    # /* Title Styling */
    # .title {
    #     font-size: 50px;
    #     font-weight: bold;
    #     text-align: center;
    #     color: white;
    #     text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
    #     margin-bottom: 20px;
    # }

    # /* Content Box for Readability */
    # .content-box {
    #     background: rgba(0, 0, 0, 0.6);
    #     padding: 30px;
    #     border-radius: 15px;
    #     color: white;
    #     max-width: 700px;
    #     margin: auto;
    # }

    /* Adjust Streamlit sliders */
    div[data-testid="stSlider"] {
        background: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 10px;
    }

    </style>
 <div class="title-container">
        <span class="title-text">Disease Prediction System</span>
    </div>
    """,
    unsafe_allow_html=True
)


# Title
st.markdown("<div class='title'>Disease Prediction System</div>", unsafe_allow_html=True)

# Main Content Box
st.markdown("<div class='content-box'>", unsafe_allow_html=True)
st.markdown("### Select a Disease to Predict", unsafe_allow_html=True)

# ✅ Only ONE Select Box to Avoid Duplicates
selected = st.selectbox(
    '',
    ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Lung Cancer Prediction', 'Hypo-Thyroid Prediction']
)

# st.markdown("### Enter the following details:", unsafe_allow_html=True)

# ✅ Remove any other duplicate st.selectbox() before loading models

# ------------------------ Model Loading ------------------------
if os.path.exists(r"Models"):
    base_dir = r"Models"
else:
    base_dir = os.path.join(os.getcwd(), "models")  # Adjust for Streamlit deployment

# Function to load models safely
def load_model(filename):
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            return pickle.load(f)
    else:
        print(f"Warning: Model file '{filename}' not found.")
        return None  # Return None if model file is missing

if "models" not in st.session_state:
    st.session_state["models"] = {}
# Load models dynamically
loaded_models = {
    'diabetes': load_model('diabetes_model.sav'),
    'heart_disease': load_model('heart_disease_model.sav'),
    'parkinsons': load_model('parkinsons_model.sav'),
    'lung_cancer': load_model('lungs_disease_model.sav'),
    'thyroid': load_model('Thyroid_model.sav')
}

st.session_state.models.update(loaded_models)

st.write("Models loaded successfully!")  # Debugging step


def display_input(label, tooltip, key, type="number"):
    return st.number_input(label, key=key, help=tooltip, step=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes')
    st.write("Enter the following details to predict diabetes:")

    Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies')
    Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose')
    BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure')
    SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness')
    Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin')
    BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction')
    Age = display_input('Age of the Person', 'Enter age of the person', 'Age')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        if 'diabetes' not in st.session_state.models or st.session_state.models['diabetes'] is None:
            st.error("Diabetes model is not available!")
        else:
            diab_prediction = st.session_state.models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease')
    st.write("Enter the following details to predict heart disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
    slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        if 'heart_disease' not in st.session_state.models or st.session_state.models['heart_disease'] is None:
            st.error("Heart disease model is not available!")
        else:
            heart_prediction = st.session_state.models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
            st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.write("Enter the following details to predict Parkinson's disease:")

    fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
    fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
    flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
    Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
    Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
    RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
    PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
    DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
    Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
    Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
    APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
    APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
    APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
    DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
    NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
    HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
    RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
    DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
    spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
    spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
    D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
    PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer")
    st.write("Enter the following details to predict lung cancer:")

    GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
    AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
    SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
    YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
    ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
    PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
    CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
    FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
    ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
    WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
    COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
    SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
    CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        st.success(lungs_diagnosis)

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid")
    st.write("Enter the following details to predict hypo-thyroid disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
    on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
    tsh = display_input('TSH Level', 'Enter TSH level', 'tsh', 'number')
    t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)', 'Enter if T3 was measured', 't3_measured', 'number')
    t3 = display_input('T3 Level', 'Enter T3 level', 't3', 'number')
    tt4 = display_input('TT4 Level', 'Enter TT4 level', 'tt4', 'number')

    thyroid_diagnosis = ''
    if st.button("Thyroid Test Result"):
        thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        thyroid_diagnosis = "The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease"
        st.success(thyroid_diagnosis)
