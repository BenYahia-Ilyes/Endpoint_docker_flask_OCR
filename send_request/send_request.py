
import requests
import json
import cv2


addr = 'http://172.17.0.2:5000'



print("request to ", addr)

r = requests.get(addr)
print(json.loads(r.text))



#####################################################################


# upload and encode image as jpg
img = cv2.imread('test.jpg' , -1)
_, img_encoded = cv2.imencode('.jpg', img)


ocr_url = addr + '/OCR'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}



print("\n\n")
print("request to" , ocr_url)
# send http request with image and receive response
response = requests.post(ocr_url, data=img_encoded.tostring(), headers=headers)



# decode response
js = json.loads(response.text)
print(str(js).encode('utf-8').strip())
print("\n\n")

# expected output: {u'message': u'image received. size=124x124'}

