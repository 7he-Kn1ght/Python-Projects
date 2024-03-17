import tkinter as tk
import requests
import json

root=tk.Tk()
root.title("Weather App")
root.wm_iconbitmap('icon.ico')

canvas=tk.Canvas(root,height=1024,width=1024)
canvas.pack()

def entry_func(city):
    
    key='e10e83c84f942a2f56bbe196bc69548b'
    url='https://api.openweathermap.org/data/2.5/weather'
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
        final= "Something is wrong!!! \nCheck the Format \nEg:Mumbai,In"
    return final

#First Frame
frame=tk.Frame(root,bg="#d6a651",bd=5)
label=tk.Label(frame,text="Welcome To the Weather App",bg="#edcd95",font="Century")
label.pack()
entry=tk.Entry(frame,width=10)
#entry.insert(0,"Enter your city here Eg.('Mumbai')")
entry.place(relx=0.15,rely=0.1,relwidth=0.30,relheight=0.10)
button=tk.Button(frame,text="Get Weather Details!!!!",width=20,height=3,command=lambda:entry_func(entry.get()))
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
button.place(relx=0.5,rely=0.1,relwidth=0.30,relheight=0.10)
button2=tk.Button(frame,text="Save the Details",width=15,height=3)
button2.pack(side="bottom")

#frame 2
frame2=tk.Frame(root,bg="#f7e4c1")
frame2.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.5)
label2=tk.Label(frame2,font=('Calisto MT',20),anchor='nw',justify='left',bd=4)
label2.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
root.mainloop()

#The error could be because of following reasons:\n1.The city entered is not valid \n2.The Server seems to be down! Try later \nNOTE:Please Enter the city name as following eg:Mumbai,IN
