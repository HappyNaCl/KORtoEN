from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from translate import TextTranslator

app = Flask(__name__)
api = Api(app)
CORS(app, origins="http://localhost:5173")

class TranslateText(Resource):
    def post(self):
        # Support both form and JSON input
        text = request.form.get('text') or request.json.get('text')
        
        if not text or not text.strip():
            return {'message': "Text to translate is required and cannot be empty"}, 400

        try:
            translated_text = TextTranslator(text)
            return {'translated_text': translated_text}, 200

        except Exception as e:
            return {'message': f"Error during translation: {str(e)}"}, 500

api.add_resource(TranslateText, '/translate')

if __name__ == '__main__':
    app.run(port=5001)
