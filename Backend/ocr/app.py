from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import werkzeug
import werkzeug.datastructures
import numpy as np
from ocr import OCR
import cv2

app = Flask(__name__)
api = Api(app)
CORS(app, origins="http://localhost:5173")

fileParse = reqparse.RequestParser()        
fileParse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='provide a file')
fileParse.add_argument('is_document', type=bool, location='form', required=False, help='indicate if this file is a document')    

class OCRImage(Resource):
    def post(self):
        args = fileParse.parse_args()
        stream = args['file'].read()
        is_docs = args['is_document']
        npimg = np.frombuffer(stream, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
        cv2.imwrite("image.jpg", img)
        ocr_text = OCR(img, is_docs)
        return {'text': ocr_text}, 200
        
api.add_resource(OCRImage, '/ocr')

