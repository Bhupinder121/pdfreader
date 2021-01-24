import pickle
from gtts import gTTS
import os
with open('text.pickle','rb')as f:
    pages = pickle.load(f)

# with open('info.pickle','rb') as f:
#     info = pickle.load(f)
previous= 3


for f in os.listdir(f"D:\\pdfreader\\templates\\1.9audio"):
    os.remove(os.path.join(f"D:\\pdfreader\\templates\\1.9audio", f))
with open('info.pickle','rb') as f:
    info = pickle.load(f)
    
if previous != info[0]:
    l=0
    previous=info[0]
    lines =str(pages[info[0]]).split('/n')
    lines = lines[0].split(".")

    for line in lines:

        if line != ''and line !=' ':
            l +=1
            print(line)
            tts = gTTS(line)
            tts.save(f"D:\\pdfreader\\templates\\1.9audio\\Para{info[1]}Line{l}.mp3")
            
# names = os.listdir(f"D:\\pdfreader\\templates\\1.9audio")
# print(names)
