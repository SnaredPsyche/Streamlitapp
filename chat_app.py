import openai
import streamlit as st

openai.api_key = "YOUR_OPENAI_API_KEY"

def main():
    st.title("ChatGPT Streamlit App")
    user_input = st.text_input("You:", "")
    
    if user_input:
        response = generate_response(user_input)
        st.text("ChatGPT:", response)

def generate_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the desired engine here
        prompt=user_input,
        max_tokens=50  # Adjust the response length as needed
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    main()
