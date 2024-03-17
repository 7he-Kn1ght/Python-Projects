import tkinter as tk
import sys
from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
sample=tk.Tk()

class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'script.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')

def newb():
    password = askstring('Prompt', 'Enter your password?')
    con_password = askstring('Prompt', 'Confirm your password')
    if(password==con_password):
        f = open("data.txt", "w+")
        f.write(password)
        f.close()
        enc.encrypt_file("data.txt")
        print("Please restart the program to complete the setup")
        sample.destroy()
        time.sleep(15)
        sys.exit()
        
    else:
        print("password mismatch")
        sys.exit()
    
def main_func():
        sample.destroy()
        root=tk.Tk()
        root.title('DAHAKA ENCRYPTION MONSTER')
        canvas=tk.Canvas(root,width=600,height=700)
        canvas.pack()
        frame=tk.Frame(root)
        frame.place(relwidth=1,relheight=1)
        image=Image.open("23.jpg")
        photo=ImageTk.PhotoImage(image)
        label=tk.Label(frame,image=photo)
        label.img=photo
        label.place(relheight=1,relwidth=1)
        label1=tk.Label(root,bd=2,fg='#f52020',font=20,bg='#ad9050',text="*-*-*-*-*MENU*-*-*-*-*\n1.Encrypt the file\n2.Decrypt the file\n3.Encrypt the all files in dir\n4.Decrypt the all files in dir",anchor='n')
        label1.place(relx=0.20,rely=0.02,relheight=0.88,relwidth=0.6)
        entrybox1=tk.Entry(label1)
        entrybox1.place(relx=0.12,rely=0.2,relheight=0.05,relwidth=0.35)
        button1=tk.Button(label1,text="Select One Option!",fg='#f52020',command=lambda:choice_func(entrybox1.get()))
        button1.place(relx=0.49,rely=0.2,relheight=0.05,relwidth=0.35)
        frame2=tk.Frame(label1)
        frame2.place(relx=0.12,rely=0.35,relheight=0.5,relwidth=0.7)
        label2=tk.Label(frame2)
        label2.place(relheight=1,relwidth=1)
        def choice_func(choice):
            if choice == '1':
                label2['text']="You have selected to perform Option 1"
                enc.encrypt_file(askstring('Prompt', 'Enter the file name:'))
                label2['text']="Action Performed!!"
            elif choice == '2':
                label2['text']="You have selected to perform Option 2"
                enc.decrypt_file(askstring('Prompt', 'Enter the file name:'))
                label2['text']="Action Performed!!"
            elif choice == '3':
                label2['text']="You have selected to perform Option 3"
                enc.encrypt_all_files()
                label2['text']="Action Performed!!"
            elif choice == '4':
                label2['text']="You have selected to perform Option 4"
                enc.decrypt_all_files()
                label2['text']="Action Performed!!"
            else:
                label2['text']="Please select a valid option!"
        root.mainloop()
def currb():
    password = askstring('Prompt', 'Enter your password?')
    enc.decrypt_file("data.txt.enc")
    p = ''
    with open("data.txt", "r") as f:
        p = f.readlines()
    if p[0] == password:
        enc.encrypt_file("data.txt")
        main_func()  
    else:
        print("wrong pass")
        sample.destroy()
    
   
def file_check():
    if os.path.isfile('data.txt.enc'):
        currb()
    else:
        newb()
            

    

    


file_check() 
sample.mainloop()







