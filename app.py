import os
import requests
import gradio as gr
from openai import OpenAI
import anthropic
import google.generativeai

# Load environment variables
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

# Connect to AI models
openai = OpenAI()
claude = anthropic.Anthropic()
google.generativeai.configure()

# Import the Website class from the website.py file
from src.website import Website

def stream_brochure(company_name, url, model):
    prompt = f"Please generate a company brochure for {company_name}. Here is their landing page:\n"
    prompt += Website(url).get_contents()
    
    if model == "GPT":
        result = stream_gpt(prompt)
    elif model == "Claude":
        result = stream_claude(prompt)
    else:
        raise ValueError("Unknown model")
    
    yield from result

# Gradio interface definition
view = gr.Interface(
    fn=stream_brochure,
    inputs=[
        gr.Textbox(label="Company name:"),
        gr.Textbox(label="Landing page URL including http:// or https://"),
        gr.Dropdown(["GPT", "Claude"], label="Select model")
    ],
    outputs=[gr.Markdown(label="Brochure:")],
    flagging_mode="never"
)

view.launch(share=True)