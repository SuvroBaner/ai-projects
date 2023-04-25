import streamlit as st
import openai
import os

st.title("Chatting with ChatGPT")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''
    Thisis a web application that allows you to interact with the OpenAI ChatGPT model.
    Enter **query** in the **text box** and **press enter** to receive a **response** from
    the ChatGPT
    '''
)

model_engine = "text-davinci-003"
openai.api_key = os.environ["OPENAI_API_KEY"]

def callChatGPT(user_query):
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = user_query,
        max_tokens = 1024,
        n = 1,
        temperature = 0.5,
    )

    response = completion.choices[0].text
    return response

def main():
    '''
    This function gets the user input, pass it to the ChatGPT function and displays the response
    '''
    # get the user input -
    user_query = st.text_input("Enter query here, to exit enter :q", "What is Python ?")
    if user_query != ":q" or user_query != "":
        response = callChatGPT(user_query)
        return st.write(f"{user_query} {response}")
    
if __name__ == '__main__':
    main()
    
