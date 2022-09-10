import streamlit as st
from PIL import Image

def predict_similarity(ques1, ques2, model) -> int:
    # akkhi pipeline ithe lihi :(
    return -1

if __name__ == "__main__":

    image = Image.open('quoralogo.jpg')
    st.image(image)

    # st.title("Quora Question Pair Similarity Predictor")
    st.markdown("<h1 style='text-align: center; color: white;'>Quora Question Pair Similarity Predictor</h1>"
                ,unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: white;'>This project classifies question pairs as duplicate or non-duplicate by using NLP techniques for text preprocessing and feature extraction and then applying classification algorithms on them.</p> <br>"
                ,unsafe_allow_html=True)

    st.markdown("<h4 style='text-align:center;'>Choose a model for prediction-</h4>"
                ,unsafe_allow_html=True)

    model = st.selectbox('',
                        ('Decision Tree', 'Random Forest', 'XGBoost'))

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.write('You selected-', model)

    if (model == 'Decision Tree'):
        st.write("Log loss - 0.41")
        st.write("Accuracy - 80%")

    elif (model == 'Random Forest'):
        st.write("Log loss - 0.45")
        st.write("Accuracy - 79%")

    else:
        st.write("Log loss - 0.33")
        st.write("Accuracy - 84%")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align:center;'>Enter the first question here-</h4>"
                ,unsafe_allow_html=True)
    ques1 = st.text_input("", value="", placeholder="First question text")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align:center;'>Enter the second question here-</h4>"
                ,unsafe_allow_html=True)
    ques2 = st.text_input("", value="", placeholder="Second question text")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("----", unsafe_allow_html=True)
    col1, col2, col3 , col4, col5 = st.columns(5)
    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
        predict_button = st.button('Predict the similarity!')
    st.markdown("----", unsafe_allow_html=True)

    if (predict_button):

        st.markdown("<h4 style='text-align:center'>Result-</h4>"
                    ,unsafe_allow_html=True)
    
        st.markdown("<br>", unsafe_allow_html=True)

        result = predict_similarity(ques1, ques2, model)
        if (result == 0):
            st.markdown("<h5 style='text-align:center;'>The two questions are semantically NOT SIMILAR!</h5>"
                        ,unsafe_allow_html=True)
        elif(result == 1):
            st.markdown("<h5 style='text-align:center;'>The two questions are semantically SIMILAR!</h5>"
                        ,unsafe_allow_html=True)
        else:
            st.markdown("<h5 style='text-align:center;'>Development in progress!</h5>"
                        ,unsafe_allow_html=True)