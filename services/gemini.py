from config import Config
from google import genai
from google.genai import types
import logging

client = genai.Client()

#Function that sends a prompt to the Gemini API and returns its response
def askGemini(prompt, instruction=None, temperature=0.5):
    try:
        config = types.GenerateContentConfig(
            system_instruction=instruction,
            temperature = temperature
        )

        response = client.models.generate_content(
            model=Config.GEMINI_MODEL,
            contents=prompt,
            config=config
        )

    except Exception as e:
        logging.exception("Error al obtener respuesta de gemini")
        return {f"Error al obtener respuesta de gemini: {str(e)}"}

    return response.text