import streamlit as st
import random
st.subheader("WELCOME TO NUMBER GUESSING GAME...")
number_to_guess = random.randint(1, 10)
st.write("I'm thinking of a number between 1 and 10. Can you guess it?")
a=st.number_input("enter your number of attempt:",min_value=1)
st.button("attempts")
if a >= int(6):
    st.write('oops your chance is over! ')

else:
    
    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)
    if st.button("Submit Guess"):
        
            if user_guess == number_to_guess:
                st.success("Congratulations! You guessed it right!")
            elif user_guess > number_to_guess:
                st.write("your guess is high.....")
            elif user_guess < number_to_guess:
                st.write("your guess is low.....")
            else:
                st.error(f"Oops! The number was {number_to_guess}. Try again!")
    
    else:
        st.button('Restart Game')
    
        
        