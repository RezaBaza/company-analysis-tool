import gradio as gr
from src.analyzer import stream_brochure
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

# Check if keys are loaded correctly
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:8]}")
else:
    print("Google API Key not set")

# Set up the Gradio interface for user input
def create_interface():
    return gr.Interface(
        fn=stream_brochure,
        inputs=[
            gr.Textbox(label="Company name:"),
            gr.Textbox(label="Landing page URL including http:// or https://"),
            gr.Dropdown(["GPT", "Claude"], label="Select model")
        ],
        outputs=[gr.Markdown(label="Brochure:")],
        flagging_mode="never"
    )

# Launch the interface
if __name__ == "__main__":
    interface = create_interface()
    interface.launch(share=True)
