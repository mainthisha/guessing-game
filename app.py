import streamlit as st
st.set_page_config(page_title="My Portfolio & Guessing Game", layout="centered")
st.title("Welcome to My Portfolio & Guessing Game")
tab1, tab2 = st.tabs(["Portfolio", "Guessing Game"])

with tab1:
    import streamlit as st
    st.write("Hello , I'm Mainthisha")
    st.write("I'm a student of KGISL Institute Of Technology representing AI & DS Department")
    st.write("My goal is to get placed in good company with good package")
    st.markdown("Here is my github link ([https://github.com/mainthisha])")
with tab2:
    import streamlit as st
    import random
    st.title("Number Guessing Game")
    if "target" not in st.session_state:
        st.session_state.target=random.randint(1,100)
        st.session_state.attempts=0
        st.session_state.feedback=""
    st.write("I'm thinking of a number between 1 and 100. Try to guess it!")
    user_guess=st.number_input("Enter your guess:",min_value=1,max_value=100,step=1)
    if st.button("Submit Guess"):
        st.session_state.attempts+=1
        if user_guess<st.session_state.target:
            st.session_state.feedback= "Your Guess is too low! try a higher number."
        elif user_guess>st.session_state.target:
            st.session_state.feedback=  "Your Guess is too high! try a lower number."
        else:
            st.session_state.feedback=f"Correct! You guessed the number in {st.session_state.attempts} attempts."
            st.balloons()
            st.session_state.target=random.randint(1,100)
            st.session_state.attempts=0
    st.write(st.session_state.feedback)

    


    

