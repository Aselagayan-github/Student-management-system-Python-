import collections
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
from pymongo import MongoClient #pip install mongo

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System (Asela Gayan Pushpakumara)")
        self.root.geometry("1530x790+0+0")
        
        # MongoDB connection
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['student_management']
        self.collection = self.db['students']
        
        #===================================variables==========

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_phoneno=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        
        
        #1ST
        img1 = Image.open(r"images\7th.jpg")
        img1 = img1.resize((540, 160))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        self.btn_1=Button(self.root,image=self.photoimg1,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)
        
          #2ND
        img2 = Image.open(r"images\5th.jpg")
        img2 = img2.resize((540, 160))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        self.btn_2=Button(self.root,image=self.photoimg2,cursor="hand2")
        self.btn_2.place(x=540,y=0,width=540,height=160)
        
          #3RD
        img3 = Image.open(r"images\6th.jpg")
        img3 = img3.resize((540, 160))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        self.btn_3=Button(self.root,image=self.photoimg3,cursor="hand2")
        self.btn_3.place(x=1000,y=0,width=540,height=160)
        
        #bg image
        img4 = Image.open(r"images\university.jpg")
        img4 = img4.resize((1530, 710))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbiling = Label(self.root, image=self.photoimg4, bd=2, relief=RIDGE)
        lbiling.place(x=0, y=120, width=1530, height=690)
        
        lbl_title = Label(lbiling,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="Black",fg="red",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1530,height=50)
        
        #MANAGE FRAME
        
        manage_frame=Frame(lbiling,bd=2,relief=RIDGE,bg="white")
        manage_frame.place(x=15,y=55,width=1480,height=600)
        
        #left frame
        DetaLeftFrame = LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",15,"bold"),fg="red",bg="white")
        DetaLeftFrame.place(x=10,y=10,width=660,height=500)
        
        #left frame image
        img5 = Image.open(r"images\university.jpg")
        img5 = img5.resize((650, 120))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        my_leftimage = Label(DetaLeftFrame, image=self.photoimg5, bd=2, relief=RIDGE)
        my_leftimage.place(x=0, y=0, width=650, height=120)
        
        #current course lablefrme information
        std_lbl_info_frame=LabelFrame(DetaLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",15,"bold"),fg="red",bg="white")
        std_lbl_info_frame.place(x=0,y=120,width=650,height=115)
        
        #lable and combo box
        
        #department
        
        Department=Label(std_lbl_info_frame,text="Department : ",font=("arial",12,"bold"),bg="white")
        Department.grid(row=0,column=0,padx=8,sticky=W)
        
        comdp=ttk.Combobox(std_lbl_info_frame,font=("arial",12,"bold"),width=17,state="readonly",textvariable=self.var_dep)
        comdp["value"]=("Select Department","Faculty of Business","Faculty of Engineering","Faculty of IT","Faculty of Science")
        comdp.current(0)
        comdp.grid(row=0,column=1,padx=8,pady=10)
        
        #course
        
        course=Label(std_lbl_info_frame,text="Course : ",font=("arial",12,"bold"),padx=2,pady=6,bg="white")
        course.grid(row=0,column=2,padx=8,sticky=W)
        
        comcour=ttk.Combobox(std_lbl_info_frame,font=("arial",12,"bold"),width=17,state="readonly",textvariable=self.var_course)
        comcour["value"]=("Select course","BSc Business and Management","BSc Digital Marketing","BEng Automotive Engineering","BSc Civil Engineering","BEng Mechanical Engineering","BEng Biomedical Engineering","BSc Software Engineering","BSc Information Technology","BSc in Nursing","BSc in Psychology")
        comcour.current(0)
        comcour.grid(row=0,column=3,padx=8,pady=10)
        
        #year
        
        year=Label(std_lbl_info_frame,text="Year : ",font=("arial",12,"bold"),bg="white")
        year.grid(row=1,column=0,padx=8,sticky=W)
        
        comye=ttk.Combobox(std_lbl_info_frame,font=("arial",12,"bold"),width=17,state="readonly",textvariable=self.var_year)
        comye["value"]=("Select year","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025")
        comye.current(0)
        comye.grid(row=1,column=1,padx=8,pady=10)
        
        
        #Semester
        
        Semester=Label(std_lbl_info_frame,text="Semester : ",font=("arial",12,"bold"),bg="white")
        Semester.grid(row=1,column=2,padx=8,sticky=W)
        
        comSem=ttk.Combobox(std_lbl_info_frame,font=("arial",12,"bold"),width=17,state="readonly",textvariable=self.var_sem)
        comSem["value"]=("Select Semester","semester-1","semester-2","semester-3","semester-4")
        comSem.current(0)
        comSem.grid(row=1,column=3,padx=8,pady=10)
        
        
        #Student details lablefrme information
        std_lbl_details_frame=LabelFrame(DetaLeftFrame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",15,"bold"),fg="red",bg="white")
        std_lbl_details_frame.place(x=0,y=225,width=650,height=250)
        
        #id
        sid=Label(std_lbl_details_frame,text="Student Id : ",font=("arial",12,"bold"),padx=2,pady=7)
        sid.grid(row=0,column=0,sticky=W)

        textid=ttk.Entry(std_lbl_details_frame,width=22,font=("arial",12,"bold"),textvariable=self.var_id)
        textid.grid(row=0,column=1,padx=8,pady=7)
        
        #name
        sname=Label(std_lbl_details_frame,text="Student Name : ",font=("arial",12,"bold"),padx=2,pady=7)
        sname.grid(row=0,column=2,sticky=W)

        textname=ttk.Entry(std_lbl_details_frame,width=21,font=("arial",12,"bold"),textvariable=self.var_name)
        textname.grid(row=0,column=3,padx=8,pady=7)
        
        
        #gender
        
        gender=Label(std_lbl_details_frame,text="Gender : ",font=("arial",12,"bold"))
        gender.grid(row=1,column=0,sticky=W,padx=2,pady=5)


        comg=ttk.Combobox(std_lbl_details_frame,font=("arial",12,"bold"),width=20,state="readonly",textvariable=self.var_gender)
        comg["value"]=("Select Gender","Male","Female")
        comg.current(0)
        comg.grid(row=1,column=1,padx=8,pady=7)
        
        #phone no

        pno=Label(std_lbl_details_frame,text="Mobile : ",font=("arial",12,"bold"),padx=2,pady=7)
        pno.grid(row=1,column=2,sticky=W)

        textpno=ttk.Entry(std_lbl_details_frame,width=22,font=("arial",12,"bold"),textvariable=self.var_phoneno)
        textpno.grid(row=1,column=3,padx=8,pady=7)
        
        #email

        email=Label(std_lbl_details_frame,text="Email : ",font=("arial",12,"bold"),padx=2,pady=7)
        email.grid(row=2,column=0,sticky=W)

        textemail=ttk.Entry(std_lbl_details_frame,width=22,font=("arial",12,"bold"),textvariable=self.var_email)
        textemail.grid(row=2,column=1,padx=8,pady=7)
        
        #address

        address=Label(std_lbl_details_frame,text="Address : ",font=("arial",12,"bold"),padx=2,pady=6)
        address.grid(row=2,column=2,sticky=W)

        textaddress=ttk.Entry(std_lbl_details_frame,width=22,font=("arial",12,"bold"),textvariable=self.var_address)
        textaddress.grid(row=2,column=3,padx=8,pady=7)
        
         #========================buttons=======================
         #button frame
        buttonFrame = LabelFrame(DetaLeftFrame,bd=2,relief=RIDGE)
        buttonFrame.place(x=0,y=400,width=1450,height=37)
        
        btnadd=Button(buttonFrame,text="Add",font=("arial",11,"bold"),width=13,bg="blue",fg="gold",command=self.Add_data)
        btnadd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(buttonFrame,text="Update",font=("arial",11,"bold"),width=13,bg="blue",fg="gold",command=self.update)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(buttonFrame,text="Delete",font=("arial",11,"bold"),width=13,bg="blue",fg="gold",command=self.delete)
        btnDelete.grid(row=0,column=2,padx=1)

        btnRest=Button(buttonFrame,text="Reset",font=("arial",11,"bold"),width=13,bg="blue",fg="gold",command=self.reset)
        btnRest.grid(row=0,column=3,padx=1)
        
        btnlogout=Button(buttonFrame,text="Logout",font=("arial",11,"bold"),width=13,bg="blue",fg="gold",command=self.logout)
        btnlogout.grid(row=0,column=4,padx=1)

        
         #Right frame
        DetaRightFrame = LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",15,"bold"),fg="red",bg="white")
        DetaRightFrame.place(x=680,y=10,width=780,height=540)
        
         #right frame image
        img6 = Image.open(r"images\9th.jpg")
        img6 = img6.resize((780, 200))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        my_rightimage = Label(DetaRightFrame, image=self.photoimg6, bd=2, relief=RIDGE)
        my_rightimage.place(x=0, y=0, width=780, height=200)
        
        #right frame
        searchFrame = LabelFrame(DetaRightFrame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",15,"bold"),fg="red",bg="white")
        searchFrame.place(x=0,y=200,width=770,height=70)
        
        lblsearch=Label(searchFrame,text="Search By : ",font=("arial",12,"bold"),bg="black",fg="white",width=10)
        lblsearch.grid(row=0,column=0,sticky=W,padx=7)

        self.search_var=StringVar()
        com_search=ttk.Combobox(searchFrame,font=("arial",12,"bold"),width=18,state="readonly",textvariable=self.search_var)
        com_search["value"]=("select option","Student Id","Phone")
        com_search.current(0)
        com_search.grid(row=0,column=1,padx=2,sticky=W,pady=7)
        
        self.text_search=StringVar()
        textsearch=ttk.Entry(searchFrame,width=29,font=("arial",11,"bold"),textvariable=self.text_search)
        textsearch.grid(row=0,column=2,padx=5)

        btnsearch=Button(searchFrame,text="Search",font=("arial",11,"bold"),width=10,bg="blue",fg="gold",command=self.search)
        btnsearch.grid(row=0,column=3,padx=5)

        btnshowall=Button(searchFrame,text="Show all",font=("arial",11,"bold"),width=10,bg="blue",fg="gold",command=self.fetch_data)
        btnshowall.grid(row=0,column=4,padx=5)
        
        #====================show data table================

        details_table=Frame(DetaRightFrame,bd=4,relief=RIDGE)
        details_table.place(x=0,y=260,width=750,height=250)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Deatils_table=ttk.Treeview(details_table,column=("dep","course","year","sem","id","name","gender","email","phone","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Deatils_table.xview)
        scroll_y.config(command=self.Cust_Deatils_table.yview)

        self.Cust_Deatils_table.heading("dep",text="Department")
        self.Cust_Deatils_table.heading("course",text="Course")
        self.Cust_Deatils_table.heading("year",text="Year")
        self.Cust_Deatils_table.heading("sem",text="Semester")
        self.Cust_Deatils_table.heading("id",text="Id")
        self.Cust_Deatils_table.heading("name",text="Name")
        self.Cust_Deatils_table.heading("gender",text="Gender")
        self.Cust_Deatils_table.heading("email",text="Email")
        self.Cust_Deatils_table.heading("phone",text="Phone")
        self.Cust_Deatils_table.heading("address",text="Address")

        self.Cust_Deatils_table["show"]="headings"

        self.Cust_Deatils_table.column("dep",width=100)
        self.Cust_Deatils_table.column("course",width=100)
        self.Cust_Deatils_table.column("year",width=100)
        self.Cust_Deatils_table.column("sem",width=100)
        self.Cust_Deatils_table.column("id",width=100)
        self.Cust_Deatils_table.column("name",width=100)
        self.Cust_Deatils_table.column("gender",width=100)
        self.Cust_Deatils_table.column("email",width=100)
        self.Cust_Deatils_table.column("phone",width=100)
        self.Cust_Deatils_table.column("address",width=100)

        self.Cust_Deatils_table.pack(fill=BOTH,expand=1)
        self.Cust_Deatils_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
    def logout(self):
        answer = messagebox.askyesno("Logout", "Do you want to log out of this system?")
        if answer:
            self.root.destroy() 
            
    def Add_data(self):
        # Retrieve data from the tkinter variables
        department = self.var_dep.get()
        course = self.var_course.get()
        year = self.var_year.get()
        semester = self.var_sem.get()
        student_id = self.var_id.get()
        student_name = self.var_name.get()
        gender = self.var_gender.get()
        phone = self.var_phoneno.get()
        email = self.var_email.get()
        address = self.var_address.get()
        
        if any(not field for field in [department, course, year, semester, student_id, student_name, gender, phone, email, address]):
           messagebox.showerror("Error", "One or more fields are empty. Please fill in all fields.")
        elif not student_id:
           messagebox.showerror("Error", "ID number must be entered.")
        else:
        
        # Prepare data to insert into MongoDB
         student_data = {
            "Department": department,
            "Course": course,
            "Year": year,
            "Semester": semester,
            "Student ID": student_id,
            "Name": student_name,
            "Gender": gender,
            "Phone": phone,
            "Email": email,
            "Address": address
         }
        
        # Insert data into MongoDB
        result = self.collection.insert_one(student_data)
        
        # Display success or failure message
        if result.inserted_id:
            messagebox.showinfo("Success", "Student data added successfully!")
            self.fetch_data()
            self.var_dep.set("Select Department")
            self.var_course.set("Select Course")
            self.var_year.set("Select Year")
            self.var_sem.set("Select Semester")
            self.var_id.set("")
            self.var_name.set("")
            self.var_gender.set("Select Gender")
            self.var_phoneno.set("")
            self.var_email.set("")
            self.var_address.set("")
            self.text_search.set("")
            self.search_var.set("Select Option")
        else:
            messagebox.showerror("Error", "Failed to add student data.")
      
    def fetch_data(self):
        # Clear the existing table data
        records = self.Cust_Deatils_table.get_children()
        for record in records:
            self.Cust_Deatils_table.delete(record)

        # Fetch data from MongoDB
        for data in self.collection.find():
            self.Cust_Deatils_table.insert('', 'end', values=(
                data["Department"],
                data["Course"],
                data["Year"],
                data["Semester"],
                data["Student ID"],
                data["Name"],
                data["Gender"],
                data["Email"],
                data["Phone"],
                data["Address"]
            ))

    def get_cursor(self, event=""):
        # Get the selected row
        cursor_row = self.Cust_Deatils_table.focus()
        contents = self.Cust_Deatils_table.item(cursor_row)
        row = contents['values']

        # Update the entry widgets with the selected row's data
        self.var_dep.set(row[0])
        self.var_course.set(row[1])
        self.var_year.set(row[2])
        self.var_sem.set(row[3])
        self.var_id.set(row[4])
        self.var_name.set(row[5])
        self.var_gender.set(row[6])
        self.var_email.set(row[7])
        self.var_phoneno.set(row[8])
        self.var_address.set(row[9])
        
    def update(self):
       selected_item = self.Cust_Deatils_table.selection()
       if not selected_item:
        messagebox.showerror("Error", "Please select a student record to update.")
       else:
        selected_item = selected_item[0]
        student_id = self.Cust_Deatils_table.item(selected_item)['values'][4]
        department = self.var_dep.get()
        course = self.var_course.get()
        year = self.var_year.get()
        semester = self.var_sem.get()
        student_name = self.var_name.get()
        gender = self.var_gender.get()
        phone = self.var_phoneno.get()
        email = self.var_email.get()
        address = self.var_address.get()

        # Check if any field is empty
        if any(not field for field in [department, course, year, semester, student_name, gender, phone, email, address]):
            messagebox.showerror("Error", "One or more fields are empty. Please fill in all fields.")
        elif not student_id:
            messagebox.showerror("Error", "ID number must be entered.")
        else:
            self.collection.update_one(
                {"Student ID": student_id},
                {
                    "$set": {
                        "Department": department,
                        "Course": course,
                        "Year": year,
                        "Semester": semester,
                        "Name": student_name,
                        "Gender": gender,
                        "Phone": phone,
                        "Email": email,
                        "Address": address
                    }
                }
            )
            messagebox.showinfo("Success", "Student information updated successfully")
            self.fetch_data()
            self.var_dep.set("Select Department")
            self.var_course.set("Select Course")
            self.var_year.set("Select Year")
            self.var_sem.set("Select Semester")
            self.var_id.set("")
            self.var_name.set("")
            self.var_gender.set("Select Gender")
            self.var_phoneno.set("")
            self.var_email.set("")
            self.var_address.set("")
            self.text_search.set("")
            self.search_var.set("Select Option")

    
    def delete(self):
        selected_item = self.Cust_Deatils_table.selection()[0]
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this student's record?")
        if confirmation:
            self.collection.delete_one({"Student ID": self.Cust_Deatils_table.item(selected_item)['values'][4]})
            messagebox.showinfo("Success", "Student information deleted successfully")
            self.fetch_data()
            
            self.var_dep.set("Select Department")
            self.var_course.set("Select Course")
            self.var_year.set("Select Year")
            self.var_sem.set("Select Semester")
            self.var_id.set("")
            self.var_name.set("")
            self.var_gender.set("Select Gender")
            self.var_phoneno.set("")
            self.var_email.set("")
            self.var_address.set("")
            self.text_search.set("")
            self.search_var.set("Select Option")
        
    def reset(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select Gender")
        self.var_phoneno.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.text_search.set("")
        self.search_var.set("Select Option")
        
    def search(self):
      
      selected_option = self.search_var.get()
      keyword = self.text_search.get()

      if selected_option == "select option":
        messagebox.showerror("Error", "Please select a search option")
      elif keyword == "":
        messagebox.showerror("Error", "Please enter a keyword to search")
      else:
        # Clear existing table data
        self.Cust_Deatils_table.delete(*self.Cust_Deatils_table.get_children())

        # Define the query based on the selected option and keyword
        if selected_option == "Student Id":
            query = {"Student ID": {'$regex': '.*' + keyword + '.*', '$options': 'i'}}
        elif selected_option == "Phone":
            query = {"Phone": {'$regex': '.*' + keyword + '.*', '$options': 'i'}}

        # Fetch data matching the query from MongoDB
        for record in self.collection.find(query):
            self.Cust_Deatils_table.insert('', 'end', values=(
                record["Department"],
                record["Course"],
                record["Year"],
                record["Semester"],
                record["Student ID"],
                record["Name"],
                record["Gender"],
                record["Phone"],
                record["Email"],
                record["Address"]
            ))
    

      
    
    
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
        