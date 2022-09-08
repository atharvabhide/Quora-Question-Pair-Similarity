import streamlit as st

# st.title("Quora Question Pair Similarity Predictor")
st.markdown("<h1 style='text-align: center; color: white;'>Quora Question Pair Similarity Predictor</h1>", unsafe_allow_html=True)

st.header("Header")

st.subheader("Subheader")

st.text("lorem ipsum text ahe ha")

st.markdown(
    """
    # h1 tag
    ## h2 tag
    ### h3 tag
    #### h4 tag
    ##### h5 tag
    ###### h6 tag
    :moon: <br>
    :sunglasses: <br>
    :fire: <br>
    :100: <br>
    """
,True)

dict = {
    "name" : "Atharva",
    "age" : 19, 
    "branch" : "Computer Science"
}

st.write(dict)