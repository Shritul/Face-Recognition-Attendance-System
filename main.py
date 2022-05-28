from tkinter import*
from tkinter import ttk
import tkinter #ttk module contains stylish toolkit
from PIL import Image, ImageTk #Pillow library to insert images, ImageTk-crop wagerah images ko
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student 
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self, root): #constructor
        self.root=root
        self.root.geometry("1530x790+0+0") #sets geometry of tkinter frame(width X height + x_axis + y_axis)
        self.root.title("Face Recognition System") #title of windows


        #image
        img1=Image.open(r"images\facialrecognition.jpg") #r used to convert backslash into forwardslash
        img1=img1.resize((1600, 130), Image.ANTIALIAS) #ANTIALIAS-converts high level image to low level
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=15, y=0, width=1500, height=130)


        #bg image
        img3=Image.open(r"images\main_bg.jpg") 
        img3=img3.resize((1530, 710), Image.ANTIALIAS) 
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)  

        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="#7FB5FF", fg="black") 
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl=Label(title_lbl, font=("times new roman", 15, "bold"), bg="#7FB5FF", fg="black")
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        #student btn
        img4=Image.open(r"images\student.jpg") 
        img4=img4.resize((250, 220), Image.ANTIALIAS) 
        self.photoimg4=ImageTk.PhotoImage(img4)

        btn1=Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        btn1.place(x=250, y=100, width=250, height=220)

        btn1_text=Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="#001D6E", fg="white")
        btn1_text.place(x=250, y=300, width=250, height=40)

        #detect face btn
        img5=Image.open(r"images\facedetector.jpg") 
        img5=img5.resize((250, 220), Image.ANTIALIAS) 
        self.photoimg5=ImageTk.PhotoImage(img5)

        btn1=Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        btn1.place(x=650, y=100, width=250, height=220)

        btn1_text=Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="#001D6E", fg="white")
        btn1_text.place(x=650, y=300, width=250, height=40)

        #attendance btn
        img6=Image.open(r"images\attendance.png") 
        img6=img6.resize((250, 250), Image.ANTIALIAS) 
        self.photoimg6=ImageTk.PhotoImage(img6)

        btn1=Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        btn1.place(x=1050, y=100, width=250, height=220)

        btn1_text=Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="#001D6E", fg="white")
        btn1_text.place(x=1050, y=300, width=250, height=40)


        #train data btn
        img8=Image.open(r"images\traindata.jpg") 
        img8=img8.resize((250, 220), Image.ANTIALIAS) 
        self.photoimg8=ImageTk.PhotoImage(img8)

        btn1=Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        btn1.place(x=250, y=380, width=250, height=220)

        btn1_text=Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="#001D6E", fg="white")
        btn1_text.place(x=250, y=580, width=250, height=40)

        #photos btn
        img9=Image.open(r"images\photos.jpg") 
        img9=img9.resize((250, 220), Image.ANTIALIAS) 
        self.photoimg9=ImageTk.PhotoImage(img9)

        btn1=Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        btn1.place(x=650, y=380, width=250, height=220)

        btn1_text=Button(bg_img, text="Data Set", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="#001D6E", fg="white")
        btn1_text.place(x=650, y=580, width=250, height=40)


        #exit btn
        img11=Image.open(r"images\exit.jpg") 
        img11=img11.resize((250, 220), Image.ANTIALIAS) 
        self.photoimg11=ImageTk.PhotoImage(img11)

        btn1=Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit) 
        btn1.place(x=1050, y=380, width=250, height=220)

        btn1_text=Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="#001D6E", fg="white")
        btn1_text.place(x=1050, y=580, width=250, height=40)

    def open_img(self):
        os.startfile(r"data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure to exit this window?", parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    #Function Btns
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


        
if __name__== "__main__": #calling main
    root=Tk() #create an instance of tkinter frame or window
    obj=Face_Recognition_System(root)
    root.mainloop() #method on the main window which gets executed when we need to run our application

