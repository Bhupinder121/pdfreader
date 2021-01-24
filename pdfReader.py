import pdfminer
from io import StringIO
import io
import pickle
import pyttsx3
import threading
import keyboard

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

import time

from gtts import gTTS
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate", 140)
engine.setProperty('voice',voices[1].id)
stop =False

with open('text.pickle','rb')as f:
    pages = pickle.load(f)

def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
            
            text = fake_file_handle.getvalue()
            yield text
    
            # close open handles
            converter.close()
            fake_file_handle.close()
    
def extract_text(pdf_path):
    
    # try:
    #     with open('text.pickle','rb')as f:
    #         Text = pickle.load(f)
    #     return Text

    Text = []
    for page in extract_text_by_page(pdf_path):
        Text.append(page)
    with open('text.pickle','wb') as f:
        pickle.dump(Text,f)
    return Text
        

def gettingText():
    pages = []
    global stop
    Text = extract_text(('D:\pdfreader\pdf\TheGoal.pdf'))
    j =0
    stop = False
    for i in Text:
        i = str(i)
        words = i.split()
        gotTheWord =False
        text = ''
        for word in words:
            if word=='Captured':
                j = 0
                words.remove(word)
                gotTheWord = True
            elif gotTheWord==True:
                words.remove(word)
            else:
                text += ' '+(word)  
        pages.append(text)
    stop = False
    with open('text.pickle','wb') as f:
        pickle.dump(pages,f)
    print(pages)
    
        
def something():
    Cn = []
    # with open('info.pickle','rb') as f:
    #     info = pickle.load(f)
    names = os.listdir(f"D:\\pdfreader\\templates\\1.9audio")
    for f in os.listdir(f"D:\\pdfreader\\templates\\1.9audio"):
        if f != names[-7] and f != names[-8]:
            os.remove(os.path.join(f"D:\\pdfreader\\templates\\1.9audio", f))
    with open('info.pickle','rb') as f:
        info = pickle.load(f)
        
    
    l=0
    previous=info[0]
    lines =str(pages[previous]).split('/n')
    lines = lines[0].split(".")
    for line in lines:
        if line != '' and line !=' ':
            l +=1
            Cn.append(line)
            tts = gTTS(line)
            tts.save(f"D:\\pdfreader\\templates\\1.9audio\\Para{info[1]}Line{l}.mp3")
            
        



        
def Read():
    for f in os.listdir(f"D:\\pdfreader\\templates\\audio"):
        os.remove(os.path.join(f"D:\\pdfreader\\templates\\audio", f))
    
    with open('info.pickle','rb') as f:
        info = pickle.load(f)
    page = info[0]
    p =info[1]
    l = info[2]
    #9,391  
    if page<=391:
        lines = []

        with open('lines.pickle','rb') as f:
            lines = pickle.load(f)

        for i in range(0,2):
            if len(lines)==0:
                page +=1
                p+=1
                l=1
                info=[page,p,l]
                lines =str(pages[page]).split('/n')
                lines = lines[0].split(".")
                with open('info.pickle','wb') as f:
                    pickle.dump(info,f)
                with open('lines.pickle','wb') as f:
                    pickle.dump(lines,f)
                t1 = threading.Thread(target=something)
                t1.start()  

            with open('info.pickle','rb') as f:
                info = pickle.load(f)
            page = info[0]
            p =info[1]
            l = info[2]
            with open('lines.pickle','rb') as f:
                lines = pickle.load(f)
            if lines[0] != '' and lines[0] !=' ':
                tts = gTTS(lines[0])
                tts.save(f"D:\\pdfreader\\templates\\audio\\Para{p}Line{l}.mp3")
                l +=1
                lines.remove(lines[0])
                with open('lines.pickle','wb') as f:
                    pickle.dump(lines,f)
                with open('info.pickle','wb') as f:
                    info=[page,p,l]
                    pickle.dump(info,f)
            else:
                lines.remove(lines[0])
                with open('lines.pickle','wb') as f:
                    pickle.dump(lines,f)
                names =os.listdir(f"D:\\pdfreader\\templates\\audio")
                if len(names)==0:
                    return Read()
                
                
            
        
    
        
        
    # with open('info.pickle','wb') as f:
    #     l = [page,p]
    #     pickle.dump(l,f)               
            

# for f in os.listdir(f"D:\\pdfreader\\templates\\1.9audio"):
#     os.remove(os.path.join(f"D:\\pdfreader\\templates\\1.9audio", f))
# for f in os.listdir(f"D:\\pdfreader\\templates\\audio"):
#     os.remove(os.path.join(f"D:\\pdfreader\\templates\\audio", f))



Read()



   