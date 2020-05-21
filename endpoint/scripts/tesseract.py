
import pytesseract
from pytesseract import Output




def extract_text(img): 







    custom_config = r' --psm 6 '
    txt = pytesseract.image_to_string(img, config=custom_config )
               
        





    return(txt)




   
    