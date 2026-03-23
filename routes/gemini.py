from flask import Blueprint, request, jsonify
from services.gemini import askGemini

askGemini_bp = Blueprint("askGemini_bp", __name__)

@askGemini_bp.route("/askGemini", methods=["GET"])
def routeAskGemini():
    data = request.get_json()
    try:
        prompt = data.get("prompt")
        instruction = data.get("instruction", None)
        temperature = data.get("temperature", 0.5)
        return askGemini(prompt, instruction, temperature)
    
    except Exception as e:  
        return jsonify({"Error:": str(e)}), 500
    
@askGemini_bp.route("/askGeminiAudio", methods=["GET"])
def routeAskGeminiAudio():
    data = request.get_json()
    try:
        '''
        prompt = data.get("prompt")
        instruction = data.get("instruction", None)
        temperature = data.get("temperature", 0.5)'''
        return #askGemini(prompt, instruction, temperature)
    
    except Exception as e:  
        return jsonify({"Error:": str(e)}), 500