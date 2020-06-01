from flask import Flask, jsonify, request, json, make_response
from flask_sqlalchemy import SQLAlchemy



import numpy as np
import cv2
import os



import tesseract 
import models

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





@app.route("/")
def hello():
    return jsonify({'test':'working'})




@app.route('/OCR', methods=['POST'])
def OCR():
   

    #GET image from  recieved JSON and decode it 
    nparr = np.fromstring(request.data, np.uint8)  
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)


    #extract text from image using tesseract
    txt = tesseract.extract_text(img)   
    #print(txt.encode('utf-8').strip())

    
    Json = {'text':    txt   }


    #####################################################################################
    #   save image and its content in a postgres database and send back the content     #
    #####################################################################################
    try:
        img=models.Image(
            image=request.data,
            infos=txt
        )
        db.session.add(img)
        db.session.commit()
        return jsonify(Json)
    except Exception as e:
	    return(str(e))
    #####################################################################################



@app.route("/get/<id_>")
def get_by_id(id_):
    try:



        # get the binary encoded image from the database     
        row=models.Image.query.filter_by(id=id_).first()
        img_encoded=row.image
        img_words = row.infos


        #decode the image
        img_arr = np.fromstring(img_encoded, np.uint8)
        img_decoded = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)


        #save the image
        imgname=img_words +".jpg"
        cv2.imwrite(imgname, img_decoded) 


        return " Image id={} , extracted and saved in local \n".format(row.id)

    except Exception as e:
	    return(str(e))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' )
