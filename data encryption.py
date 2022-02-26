from tkinter import *
from hashlib import *
import hashlib
selected=""
#function that takes user input 
def result():
    data1=""
    user_text=text_box1.get("1.0","end-1c")
    if selected=="md5" and user_text!="":
        data=hashlib.md5(user_text.encode())
        data1=data.hexdigest()
        show_output(data1)
    elif selected=="sha1" and user_text!="":
        data=hashlib.sha1(user_text.encode())
        data1=data.hexdigest()
        show_output(data1)
    elif selected=="sha224" and user_text!="":
        data=hashlib.sha224(user_text.encode())
        data1=data.hexdigest()
        show_output(data1)
    elif selected=="sha256" and user_text!="":
        data=hashlib.sha256(user_text.encode())
        data1=data.hexdigest()
        show_output(data1)
    elif selected=="sha384" and user_text!="":
        data=hashlib.sha384(user_text.encode())
        data1=data.hexdigest()
        show_output(data1)
    elif selected=="sha512" and user_text!="":
        data=hashlib.sha1(user_text.encode())
        data1=data.hexdigest()
        show_output(data1)
    elif user_text=="":
        show_output("Plese enter Text first")
    else:
        show_output("Plese select an Encryption type")

def show_output(n):
    text_box2.config(state="normal")
    text_box2.delete("1.0","end-1c")
    text_box2.insert(END,n)
    text_box2.config(state="disabled")
def selected_option(choice):
    global selected
    selected=clicked.get()

#reset button code
def clean():
    clicked.set("select option")
    text_box1.delete("1.0","end")
    text_box2.config(state="normal")
    text_box2.delete("1.0","end-1c")
    text_box2.config(state="disabled")
    global selected
    selected=""

bg_colour ="#007f00"
#programming window
root=Tk()
root.title("Data Encryption")
root.config(bg=bg_colour)
root.geometry("600x300")
root.resizable(False,False)

#images used in program
icon=PhotoImage(file="src/icon.png")
drop_img=PhotoImage(file="src/drop.png")
submit_image=PhotoImage(file="src/submit.png")
reset_image=PhotoImage(file="src/reset.png")


#window logo 
root.iconphoto(False ,icon)



#labels
text_label=Label(root,text="Enter Text",font="ariel 11 bold",bg=bg_colour)
text_label.grid(row=0,column=0)
drop_down_level=Label(root,text="Select Encryption Type",font="ariel 11 bold",bg=bg_colour)
drop_down_level.grid(row=1,column=0,padx=10,pady=10)
output=Label(root,text="OUTPUT",font="ariel 11 bold",bg=bg_colour)
output.grid(row=2,columnspan=2,padx=10,pady=10)

#text box to show information to the user and get input from the user
text_box1=Text(root,height=1,width =30,padx=5)
text_box1.grid(row=0,column=1,padx=10,pady=10)
text_box2=Text(root,height=3,width=35,padx=5)
text_box2.grid(row=3,columnspan=2,padx=10,pady=10)
text_box2.config(state="disabled")

#creating a list to show avalilable encription methods
methods=["md5","sha1","sha224","sha256","sha384","sha512"]

#variable to store user input from drop down menue
clicked=StringVar()
clicked.set("selcet option")

#dropdown list (option menu) to show multiple options
drop=OptionMenu(root,clicked,*methods,command=selected_option)
drop.grid(row=1,column=1)
drop.config(indicatoron=0,image=drop_img,compound="right",highlightthickness=0,bg=bg_colour,height=15)


#button to perform action
reset=Button(root,image=reset_image,command=clean,bg=bg_colour)
reset.grid(row=4,column=0,padx=10,pady=10)
submit_button=Button(root,bg=bg_colour,command=result,image=submit_image)
submit_button.grid(row=4,column=1,padx=10,pady=10)
root.mainloop()