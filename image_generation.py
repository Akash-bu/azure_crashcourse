import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

client = AzureOpenAI(
    api_version= "2024-02-01",
    azure_endpoint = "https://openai-explore-1.openai.azure.com/",
    api_key= AZURE_OPENAI_API_KEY
)

st.title("Image Generation with DALL-E")
st.write("Enter a prompt and DALL-E will generate an image based on it.")

prompt = st.text_input("Enter a prompt")

if st.button("Generate Image"):
    with st.spinner("Generating....."):
        try:
            res = client.images.generate(
            model = "dall-e-3",
            prompt=prompt,
            n=1)

            img_url = json.loads(res.model_dump_json())['data'][0]['url']
            st.image(img_url, caption="Generated Image", use_column_width=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")

