import tkinter as tk
import requests
import json

root=tk.Tk()
root.title("Weather App")
root.wm_iconbitmap(r'C:\Users\ashis\OneDrive - Conestoga College\Documents\GitHub\Python-Projects\WeatherApp\icon.ico')

canvas=tk.Canvas(root,height=500,width=600)
canvas.pack()
back_image=tk.PhotoImage(file=r'C:\Users\ashis\OneDrive - Conestoga College\Documents\GitHub\Python-Projects\WeatherApp\img1.png')
backimg_lbl=tk.Label(root,image=back_image)
backimg_lbl.place(relwidth=1,relheight=1)

def entry_func(city):
    key='96bc4485e12368a7df3206a4a738cff7'
    url='https://api.openweathermap.org/data/2.5/weather?'
    params= {'appid': key,'q':city, 'units':'Metric'}
    response = requests.get(url,params=params)
    json_text=(response.json())
    label2['text']=weath_resp(json_text)
      
def weath_resp(json_text):
    try:
        cname=json_text['name']
        ccode=json_text['sys']['country']
        desc=json_text['weather'][0]['description']
        temp=json_text['main']['temp']
        humidity=json_text['main']['humidity']
        final= 'City: %s \nCountry: %s \nCondition: %s \nTemp: %s°C \nHumidity(in percentage):%s' %(cname,ccode,desc,temp,humidity)
    except:
        if(len(json_text)==0):
            final= "Please Enter a Valid City"
        else:
            final= "Something is wrong!!! \nCheck the Format \nEg:Mumbai,IN"
    return final
#logo frame

f=tk.Frame(root)
f.place(relx=0.45,rely=0.03,relwidth=0.135,relheight=0.15)
logoimg=tk.PhotoImage(file=r'C:\Users\ashis\OneDrive - Conestoga College\Documents\GitHub\Python-Projects\WeatherApp\sample.png')
logoimg_lbl=tk.Label(f,image=logoimg)
logoimg_lbl.place(relwidth=1,relheight=1)
#First Frame
frame=tk.Frame(root,bd=2,bg='#6794c7')
frame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.1)
entry=tk.Entry(frame,width=10,font=('Microsoft YaHei Light',15))
entry.place(relx=0.04,rely=0.1,relwidth=0.30,relheight=0.75)
buttonlogo=tk.PhotoImage(file=r'C:\Users\ashis\OneDrive - Conestoga College\Documents\GitHub\Python-Projects\WeatherApp\butlog.png')
button=tk.Button(frame,text="Get Weather",image=buttonlogo,width=20,height=3,command=lambda:entry_func(entry.get()))
button.place(relx=0.30,rely=0.1,relwidth=0.11,relheight=0.75)
info=tk.Label(frame,font=('Microsoft Tai Le',13,'bold'),bg="#6794c7",fg="#a81919",text="Type your query as Mumbai")
info.place(relx=0.42,rely=0.1,relwidth=0.55,relheight=0.90)
frame2=tk.Frame(root,bd=0.5)
frame2.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
label2=tk.Label(frame2,font=('Microsoft YaHei Light',25),bg="#6794c7",fg='#a81919',anchor='n',justify='left',bd=4)
label2.place(relx=0,rely=0,relwidth=1,relheight=1)
root.mainloop()

