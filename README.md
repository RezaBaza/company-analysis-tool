# Company Analysis Tool

This tool allows users to generate company brochures by inputting a company name and its landing page URL. It leverages AI models like GPT and Claude to analyze the company and produce a professional, data-driven brochure. The tool is implemented using Python and provides a web interface for user interaction via **Gradio**.

---

## Features
- **AI-Powered Analysis**: Generate brochures using GPT or Claude.
- **Web Scraping**: Extracts relevant content from a company's landing page.
- **Interactive Web Interface**: A simple and intuitive Gradio-powered interface.
- **Customizable Output**: Select between models for tailored analysis.

---

## Code Structure and Explanation

### 1. `app.py` - The Main Entry Point
- **Purpose**: This is the main file to run the application. It sets up and launches the Gradio interface.
- **Functionality**:
  - Initializes the Gradio interface with input fields (company name, URL, model selection).
  - Calls the `stream_brochure` function to generate and display the brochure output.
- **Outcome**: Starts a local server and opens a web interface in your browser.

---

### 2. `src/analyzer.py` - The AI Logic
- **Purpose**: Handles the interaction with AI models (GPT and Claude) and generates the text for the brochure.
- **Key Functions**:
  1. **`stream_gpt(prompt)`**:
     - Sends a request to the GPT model with the given prompt.
     - Streams back the generated text.
  2. **`stream_claude(prompt)`**:
     - Sends a request to the Claude model with the given prompt.
     - Streams back the generated text.
  3. **`stream_brochure(company_name, url, model)`**:
     - Combines inputs (company name, URL, selected model) to create a prompt.
     - Extracts webpage content using `Website` class from `website.py`.
     - Sends the prompt to the selected model (GPT or Claude).
     - Outputs the brochure text in markdown format.
- **Outcome**: Generates detailed and structured content for a company brochure.

---

### 3. `src/website.py` - Web Scraping
- **Purpose**: Scrapes the company's landing page to extract relevant content for the brochure.
- **Key Functions**:
  1. **`__init__(self, url)`**:
     - Initializes the `Website` class with a URL and fetches the webpage.
  2. **`scrape_website()`**:
     - Removes irrelevant content (scripts, styles, images) from the page using BeautifulSoup.
  3. **`get_contents()`**:
     - Extracts and returns the page title and cleaned text content.
- **Outcome**: Provides structured text from the landing page for use in AI analysis.

---

### 4. `src/__init__.py` - Package Initialization
- **Purpose**: Makes the `src` directory a Python package.
- **Outcome**: Facilitates easy imports of modules within the project.

---

### 5. `.env` - Environment Variables
- **Purpose**: Stores sensitive API keys for OpenAI, Anthropic, and Google securely.
- **Usage**:
  - Copy `.env.example` to `.env` and add your API keys.
  - Example format:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ANTHROPIC_API_KEY=your_anthropic_api_key_here
    GOOGLE_API_KEY=your_google_api_key_here
    ```

---

## Requirements

- **Python Version**: 3.7+
- **Dependencies**:
  - `gradio`
  - `openai`
  - `anthropic`
  - `google-generativeai`
  - `beautifulsoup4`
  - `requests`
  - `python-dotenv`

---

