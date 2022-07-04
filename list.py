from tkinter import  *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

list1 = ["Sandwich" , "Chips" , "Soda" , "Mat" , "Tickets"]
label1 = Label(root)
label2 = Label(root)
label1["text"] = "listed items: " + str(list1)

def randomlist():
    randomlist = random.sample(range(0,4),1)
    label2["text"] = "random list : " + str(randomlist)
    

btn=Button(root,text="generate random list ",command=randomlist)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

label1.place(relx=0.5,rely=0.5,anchor=CENTER)
label2.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()