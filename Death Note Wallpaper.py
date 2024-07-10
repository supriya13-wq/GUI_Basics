from tkinter import *
import os
from PIL import ImageTk,Image

root= Tk()

def next_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter+=1

counter = 1
root.title('Death Note Images')
root.configure(background='grey')
root.geometry('300x300')
root.resizable(False,False)
#adding tExt
text_label = Label(root,text="Anime Images")
text_label.pack(pady=(8,5))
text_label.config(font=('verdana',12),fg='Black',bg='grey')


#image insertion
img_array=[]
files = os.listdir('Designs')
for file in files:
    img = Image.open(os.path.join('Designs',file))
    resized_img = img.resize((250,150))
    img_array.append(ImageTk.PhotoImage(resized_img))
img_label = Label(root,image=img_array[0])
img_label.pack(pady=(10,5))

#button
next_btn = Button(root,text='NEXT',fg='white',bg='black',width=15,height=2,command=next_img)
next_btn.pack(pady=(10,5))












root.mainloop()