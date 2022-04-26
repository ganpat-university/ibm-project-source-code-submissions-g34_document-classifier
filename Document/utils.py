from traceback import print_tb
from PIL import Image
import pytesseract
import numpy as np
import os
import unicodedata,re
from html import unescape
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
data={"chequebook":["BearerPay","SAVINGS ACCOUNT","IFSC Code"],"pancard":["INCOME TAX DEPARTMENT","Permanent Account Number"],
      "driving_license":["DL No","VEHICLES","DRIVE","LMV"],"voter_id":["ELECTION COMMISSION OF INDIA","ELECTOR PHOTO IDENTITY CARD","ELECTION","ELECTOR","ELECTOR’S","ELECTION COMMISSION"],
     "salary_slip":["SALARY SLIP","Basic Salary","Pay Slip","Deductions","Basics","Employee ID","PROVIDENT FUND"]}
import spacy
nlp = spacy.load('en_core_web_sm')


from spacy.matcher import PhraseMatcher
phrase_matcher = PhraseMatcher(nlp.vocab)
phrases = data["chequebook"]
pancard=data["pancard"]
driving=data["driving_license"]
voter_id=data["voter_id"]
salary_slip=data["salary_slip"]

patterns = [nlp(text) for text in phrases]
patterns2 = [nlp(text) for text in pancard]
patterns3 = [nlp(text) for text in driving]
patterns4 = [nlp(text) for text in voter_id]
patterns5 = [nlp(text) for text in salary_slip]

phrase_matcher.add('chequebook', None, *patterns)
phrase_matcher.add('pancard', None, *patterns2)
phrase_matcher.add('driving', None, *patterns3)
phrase_matcher.add('voter_id', None, *patterns4)
phrase_matcher.add('salary_slip', None, *patterns5)

def test_data(txt):
    ls=[]
    sentence = nlp(txt)
    matched_phrases = phrase_matcher(sentence) 
    for match_id, start, end in matched_phrases:
        string_id = nlp.vocab.strings[match_id]  
        ls.append(string_id)
    print(ls)
    return ls
        

# find most frequent
# element in a list

def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num

def clean_text(texts):
    txt = unescape(texts.strip())
    txt = unicodedata.normalize('NFKC', txt)
    txt=txt.replace('\n',' ').replace('\\',' ')
    return txt

def demo(f):
    # for filename in os.listdir("E:\DocumentClassifier\img\images"):
        # f=r"E:/DocumentClassifier/img/images/"+
        img1 = np.array(Image.open(f))
        texts = pytesseract.image_to_string(img1)
        # print(texts)
        clean_txt=clean_text(texts)
        result=test_data(clean_txt)
        if len(result)>0:
            res=most_frequent(result)
            return res
        else:
            res="Unidentified"
        # print(filename,res)
    


# img1 = np.array(Image.open('Sample.jpg'))
# texts = pytesseract.image_to_string(img1)
# txt = unescape(texts.strip())
# txt = unicodedata.normalize('NFKC', txt)
# txt=txt.replace('\n',' ').replace('\\',' ')

# test_data(txt)
