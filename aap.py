import streamlit as st
from PIL import Image
from utils import input_image_details, get_gemini_response

# Initialize our streamlit app
st.set_page_config(page_title="Multilanguage Invoice Extractor")

st.header("Multilanguage Invoice Extractor")
input_prompt = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt_default = """You are an expert in understanding invoices. We will upload an image as an invoice,
and you will have to answer any questions based on the uploaded invoice image"""

# If submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt_default, image_data, input_prompt)
    st.subheader("The Response is")
    st.write(response)