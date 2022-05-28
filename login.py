from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")

        #bg image
        bg_img=Image.open(r"images\bg_img.png") #r used to convert backslash into forwardslash
        bg_img=bg_img.resize((1600, 900), Image.ANTIALIAS) #ANTIALIAS-converts high level image to low level
        self.photoimgbg=ImageTk.PhotoImage(bg_img)

        bg_img=Label(self.root, image=self.photoimgbg) 
        bg_img.place(x=0, y=0, width=1600, height=900)

        frame=Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=450)

        img1=Image.open(r"images\user_icon.jpg")
        img1=img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str=Label(frame, text="Get Started", font=("times new roman", 20, "bold"), bg="white", fg="black")
        get_str.place(x=95, y=100)

        username_lbl=Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="black")
        username_lbl.place(x=70, y=155)

        self.txtuser=ttk.Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl=Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        password_lbl.place(x=70, y=225)

        self.txtpass=ttk.Entry(frame, font=("times new roman", 15))
        self.txtpass.place(x=40, y=250, width=270)

        #Icon images
        img2=Image.open(r"images\login_icon.jpg")
        img2=img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        lblimg2=Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3=Image.open(r"images\login_icon.jpg")
        img3=img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        lblimg2=Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=393, width=25, height=25)

        loginbtn=Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="#A760FF", fg="white", activeforeground="white", activebackground="black")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn=Button(frame, text="New User? Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, bg="white", fg="black", activeforeground="red", activebackground="white")
        registerbtn.place(x=15, y=350, width=160)

        forgotPassbtn=Button(frame, text="Forgot Password", command=self.forgot_pswd_window, font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, bg="white", fg="black", activeforeground="red", activebackground="white")
        forgotPassbtn.place(x=10, y=370, width=160)
        

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="Igdtuw@123":
            messagebox.showinfo("Success", "Welcome to Face Recognition System!")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Ganeshaya#20", database="login_register_data")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                       ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("Yes/No", "Access only admin") 
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

    # def clear(self):
    #     self.txtuser.set("")
    #     self.txtpass.set("")
                 


    def forgot_pswd_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Enter the valid email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Ganeshaya#20", database="login_register_data")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(), )
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error", "Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("350x450+610+170")

                l=Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), bg="white", fg="red")
                l.place(x=0, y=10, relwidth=1)

                security_Q=Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q=ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"]=("Select", "Your Birth Place", "Your Father's Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security=ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)

                new_pswd=Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                new_pswd.place(x=50, y=220)

                self.txt_new_pswd=ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_new_pswd.place(x=50, y=250, width=250)

                reset_btn=Button(self.root2, text="Reset", command=self.reset_pswd, font=("times new roman", 15, "bold"), fg="white", bg="green")
                reset_btn.place(x=100, y=290)


    def reset_pswd(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error", "Select the security question", parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error", "Enter the security answer", parent=self.root2)
        elif self.txt_new_pswd.get()=="":
            messagebox.showerror("Error", "Enter the new password", parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Ganeshaya#20", database="login_register_data")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Wrong Answer", parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_pswd.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your Password has been reset", parent=self.root2)
                self.root2.destroy()




class Register:
    def __init__(self, root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #bg image
        bgimg=Image.open(r"images\bg_img.png") 
        bgimg=bgimg.resize((1600, 900), Image.ANTIALIAS) 
        self.photoimg_bg=ImageTk.PhotoImage(bgimg)

        bgimg=Label(self.root, image=self.photoimg_bg) 
        bgimg.place(x=0, y=0, width=1600, height=900)

        #left image
        left_img=Image.open(r"images\register.jpg") 
        left_img=left_img.resize((470, 550), Image.ANTIALIAS)
        self.photoimgleft=ImageTk.PhotoImage(left_img)

        left_img=Label(self.root, image=self.photoimgleft)
        left_img.place(x=50, y=100, width=470, height=550)

        #main frame
        frame=Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl=Label(frame, text="REGISTER HERE", font=("times new roman", 25, "bold"), fg="black", bg="white")
        register_lbl.place(x=40, y=20)

        #label and entry
        fname=Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        fname.place(x=50, y=100)

        self.txt_fname=ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.txt_fname.place(x=50, y=130, width=250)

        l_name=Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname=ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        contact=Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact=ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email=Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email=ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        security_Q=Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q=ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"]=("Select", "Your Birth Place", "Your Father's Name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security=ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        pswd=Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd=ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd=Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd=ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        #checkbtn
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame, variable=self.var_check, text="I agree with the terms & conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        #Register Button
        img=Image.open(r"images\register_btn.png") 
        img=img.resize((200, 50), Image.ANTIALIAS) 
        self.photoimg=ImageTk.PhotoImage(img)
        b1=Button(frame, image=self.photoimg, command=self.register_data, borderwidth=0, cursor="hand2", bg="white")
        b1.place(x=10, y=420, width=200)

        #Login Button
        img1=Image.open(r"images\login_btn.png") 
        img1=img1.resize((200, 50), Image.ANTIALIAS) 
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame, image=self.photoimg1, command=self.return_login, borderwidth=0, cursor="hand2", bg="white")
        b1.place(x=330, y=420, width=200)

    
    #Function Declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All Fields are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error", "Passwords not matching")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Terms and Conditions must be accepted")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Ganeshaya#20", database="login_register_data")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "User already exists")
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)", (
                                                                                                self.var_fname.get(),
                                                                                                self.var_lname.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_securityQ.get(),
                                                                                                self.var_securityA.get(),
                                                                                                self.var_pass.get()
                                                                                            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully!")

    #to return from register window to login window
    def return_login(self):
        self.root.destroy()




if __name__=="__main__":
    main()