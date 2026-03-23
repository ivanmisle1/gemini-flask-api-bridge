# Gemini Flask API Bridge

A professional, lightweight Python backend designed to bridge applications with Google's Gemini LLM. This API is built with **Flask** and focuses on providing a stateless, scalable, and highly customizable interface for AI-driven tasks, supporting dynamic model switching via environment variables.

## Key Features

- **Model Flexibility:** Easily switch between different Gemini models (e.g., `gemini-1.5-flash`, `gemini-1.5-pro`) via configuration without changing the code.
- **Dynamic Instructions (System Prompts):** Define the AI's persona and behavior on-the-fly via the `instruction` parameter.
- **Parameter Tuning:** Support for optional `temperature` control to balance creativity and deterministic output.
- **Stateless Architecture:** Lightweight design without database dependencies, ideal for microservices and rapid deployment.
- **Standardized JSON Interface:** Clean and predictable request/response format, perfect for integration with Web, Mobile, or IoT applications.

## Tech Stack

- **Language:** Python 3.x
- **Framework:** Flask
- **AI Engine:** Google Generative AI (Gemini API)
- **Environment Management:** Python-dotenv

## Getting Start

### Prerequisites

- Python 3.10+
- A Google AI Studio API Key

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ivanmisle1/gemini-flask-api-bridge.git
   ```

2. Install the dependencies (in the root folder)

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your configuration:

   ```env
   FLASK_RUN_PORT=5000 #Optional the default port is 5000
   GOOGLE_API_KEY=your_api_key_here
   GEMINI_MODEL=gemini-1.5-flash #you can see other models here https://ai.google.dev/gemini-api/docs/models
   ```

4. Run the app

   ```bash
   flask run
   ```

## API Usage

### Endpoint: `POST /askGemini`

**Request Body (JSON):**

```json
{
  "prompt": "Is Bitcoin a good investment?",
  "instruction": "You are a professional financial consultant specialized in cryptocurrencies.",
  "temperature": 0.5
}
```

### Example Response

```json
{
  "response": "Excellent question! As a crypto market expert, I can tell you that historically..."
}
```
