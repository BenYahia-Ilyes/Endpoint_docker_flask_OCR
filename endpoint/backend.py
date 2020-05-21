from flask import Flask, jsonify, request, json, make_response
from datetime import datetime


import numpy as np
import cv2


# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('scripts')

import tesseract  #print_img(img)   ,  draw_boxes(data,img)



app = Flask(__name__)


@app.route("/")
def hello():


    return jsonify({'test':'working'})




@app.route('/OCR', methods=['POST'])
def OCR():
   
   
    nparr = np.fromstring(request.data, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)




    txt = tesseract.extract_text(img)


    print(txt.encode('utf-8').strip())


    #size ='image received. size={}x{}'.format(img.shape[1], img.shape[0])

    
    Json = {'text':    txt   }


    return jsonify(Json)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' )

#app.run(host=HOST, port=PORT, threaded=True)




'''


@app.route('/test1', methods=['POST'])
def aa():
    #email = request.email

    auth = request.authorization

    email = request.get_json()['email']

    result = ""


    #access_token = create_access_token(identity = {'first_name': email })
    ch = email
    
    result = jsonify({"token":ch})
    
    return (result)




from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from flask_jwt_extended import create_access_token



bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'super-secret'


CORS(app)




@app.route('/test2', methods=['POST'])
def login():
    email = request.get_json()['email']
    result = ""


    access_token = create_access_token(identity = {'first_name': email })
    result = jsonify({"token":access_token})
    
    print (result)


    return (result)
'''