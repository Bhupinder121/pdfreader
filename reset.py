import pickle
import os
page =9
p =1
l = 1
with open('text.pickle','rb')as f:
    pages = pickle.load(f)


with open('info.pickle','wb') as f:
    l = [page,p,l]
    pickle.dump(l,f)
lines =str(pages[page]).split('/n')
lines = lines[0].split(".")
for i in lines:
    if i =='' and i == ' ':
        lines.remove(i)  

with open('lines.pickle','wb') as f:
    pickle.dump(lines,f)

