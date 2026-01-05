from langchain_perplexity.chat_models import ChatPerplexity
from langchain_core.output_parsers import  StrOutputParser
from langchain_core.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv
import os

st.header("🌍 Country Info Bot")

load_dotenv()

api_key=os.getenv("PERPLEXITY_API_KEY")

model=ChatPerplexity(api_key=api_key,temperature=0.7)

prompt = PromptTemplate(
    template="""
You are a knowledgeable and helpful assistant.

Your task is to provide detailed and accurate information about a country
based on the user's input.

Country Name: {country}

Please provide the information in the following structured format:

### 🌍 Country Overview
- **Country Name:** 
- **Capital City:** 

### 🍽️ Famous Foods
List 3 to 5 popular and traditional foods of the country.
You are a helpful assistant that answers questions based on provided context.give 
               me cpital of this {country} and 
               famous food of this {country} and place to visit in {country}
               
- Food 2:
- Food 3:
- (Optional) Food 4:
- (Optional) Food 5:

### 🗺️ Famous Places to Visit
List 3 to 5 famous tourist attractions or places.
- Place 1:
- Place 2:
- Place 3:
- (Optional) Place 4:
- (Optional) Place 5:

### ✨ Quick Facts (Optional)
- Currency:
- Language:
- Best Time to Visit:

Make sure the response is:
- Clear and well-structured
- Easy to read
- Informative but concise""",
    input_variables=["country"],
    validate_template=True
)

parser = StrOutputParser()

chain=prompt|model|parser   


country_name=st.text_input("Enter the country name:")

if st.button("Get Country Info"):

    response=chain.invoke({"country":country_name})

    with open('audit/sample.txt','a',encoding='utf-8') as f:
        f.write(f'Country Name: {country_name}\n')
        f.write(f'Response: {response}\n')
        f.write('---------------------------------\n')

    if response:

        st.write(f'Information about {country_name}:')
        st.write('country information:')
        st.write(response)