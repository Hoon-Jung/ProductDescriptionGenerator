import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    st.title("Product Description Generator")
    aidesc = ""
    desc = st.text_input("Product Information", placeholder="Enter a short product description")
    aidescription = st.empty()
    if st.button("Generate Product Description"):
        
        response = openai.ChatCompletion.create(
            model= "gpt-3.5-turbo",
            messages = [{"role": "system", "content": "write a product description for the given product"}, {"role": "user", "content": desc}],
            stream=True
        )
        
        
        for chunk in response:
            if "content" in chunk.choices[0]["delta"]:
                aidesc = aidesc + chunk.choices[0]["delta"]["content"]
                aidescription.empty()
                aidescription.write(aidesc)
