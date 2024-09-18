from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from Attendance import Attendance
from Train import Train
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
        #First Image
        img=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\FC.png")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #Second Image
        img1=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\FC.png")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #Third Image
        img2=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\FC.png")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        #Background Image
        img3=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\images.jpeg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACIAL RECOGNITION ATTENDANCE",font=("Arial",35,"bold"),bg="white",fg="Black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #Student Button
        img4=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\student.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Account",command=self.student_details,cursor="hand2",font=("Arial",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        
        #Face Detection
        img5=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\face-recognition.png")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Scan",cursor="hand2",command=self.face_data,font=("Arial",15,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
        #Attendence Detection
        img6=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\face recognition banner.png")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance Details",cursor="hand2",command=self.attendance_data,font=("Arial",15,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        
        #chatbot
        img7=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\header-chat-box.png")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="ChatBot",cursor="hand2",font=("Arial",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        #Face Training
        img8=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\1_E5rexDhotCqksxqT4LKwyQ.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Training",command=self.train_data,cursor="hand2",font=("Arial",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        #Photo Sample Button
        img9=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\images.jpeg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photo Sample",cursor="hand2",command=self.open_img,font=("Arial",15,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        
        #Administrator Button
        img10=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\login.png")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Administrator",cursor="hand2",font=("Arial",15,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        
        
        #Exit Button
        img11=Image.open(r"C:\Users\sriva\OneDrive\Desktop\Face Recognition System\Images\computer-icons-button-scalable-vector-graphics-crystal-clear-action-exit-thumbnail.jpg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("Arial",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
    def open_img(self):
        os.startfile("data")
        
    #=====================functions button===================
        
    
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
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()