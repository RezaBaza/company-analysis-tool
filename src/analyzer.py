from src.website import Website
from openai import OpenAI
import google.generativeai
import anthropic

# Function to stream results from OpenAI's GPT model
def stream_gpt(prompt):
    openai = OpenAI()
    messages = [
        {"role": "system", "content": "Your company analysis system message here."},
        {"role": "user", "content": prompt}
    ]
    stream = openai.chat.completions.create(model='gpt-4o-mini', messages=messages, stream=True)
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result

# Function to stream results from Anthropic's Claude model
def stream_claude(prompt):
    claude = anthropic.Anthropic()
    result = claude.messages.stream(
        model="claude-3-haiku-20240307", max_tokens=1000, temperature=0.7,
        system="Your company analysis system message here.",
        messages=[{"role": "user", "content": prompt}]
    )
    response = ""
    for text in result:
        response += text or ""
        yield response

# Function to generate a company brochure by scraping a website and selecting the model
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
