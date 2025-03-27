import streamlit as st
from transformers import pipeline

# Set the model you want to use for the chatbot (Hugging Face model)
chatbot = pipeline("text-generation", model="openai-community/gpt2")

# Set the title of the Streamlit app with a description of what it does
st.title("Marc's Advanced ChatBot")
st.markdown("""
    This chatbot uses the **Mistral 7B model** from Hugging Face to generate responses to your questions.
    Feel free to ask anything and get detailed answers.
    If it doesn't understand, it will ask for clarification.
""")

# Define the function that generates a response from the chatbot
def generate_response(questionToAsk):
    try:
        # Generate response from the Hugging Face model
        response = chatbot(questionToAsk, max_length=200, do_sample=True)
        
        # Display the chatbot's response in the Streamlit app interface
        st.info("**Bot's Response**: " + response[0]['generated_text'])
        
    except Exception as e:
        # Handle potential errors and provide feedback to the user
        st.error(f"Error: {e}. Please try again later.")

# Create a form in the Streamlit app for the user to input their question
with st.form("my_form"):
    # Create a text area where the user can type their question
    text = st.text_area(
        "Enter your question below:",  # Label for the text area
        "Ask anything and press Submit to get an answer.",  # Default text in the text area
    )
    
    # Create a Submit button for the form
    submitted = st.form_submit_button("Submit")
    
    # If the Submit button is pressed, call the function to get the chatbot's response
    if submitted:
        # Check if the user has entered a question
        if text.strip() != "":
            generate_response(text)  # Pass the user's input (text) to generate a response
        else:
            # If the input is empty, display a warning message
            st.warning("Please enter a question before submitting!")

# Optional: Add a reset button for users to start a new conversation
if st.button("Reset"):
    st.experimental_rerun()  # Rerun the app to reset everything
