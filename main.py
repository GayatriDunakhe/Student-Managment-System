from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        # Variables
        self.rollno_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        pro_title = Label(self.root, text="Student Management System", font=("times new roman", 40, "bold"),
                          bg="#B1D0E0", fg="#1A374D")
        pro_title.pack(side=TOP, fill=X)

        # this is the management frame here inserting and updating operations are perfrom
        manage_frame = Frame(self.root, bg="#92A9BD")
        manage_frame.place(x=0, y=65, width=450, height=660)

        m_title = Label(manage_frame, text="Manage Student", bg="#92A9BD", font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        # Roll number label and field
        rollno = Label(manage_frame, text="Roll No.", bg="#92A9BD", font=("times new roman", 15, "bold"))
        rollno.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        txt_rn = Entry(manage_frame, textvariable=self.rollno_var, font=("times new roman", 15, "bold"))
        txt_rn.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        # Name label and field
        name = Label(manage_frame, text="Name", bg="#92A9BD", font=("times new roman", 15, "bold"))
        name.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        txt_nm = Entry(manage_frame, textvariable=self.name_var, font=("times new roman", 15, "bold"))
        txt_nm.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        # Email label and field
        email = Label(manage_frame, text="Email", bg="#92A9BD", font=("times new roman", 15, "bold"))
        email.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        txt_em = Entry(manage_frame, textvariable=self.email_var, font=("times new roman", 15, "bold"))
        txt_em.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        # Gender label and radio combobox
        gender = Label(manage_frame, text="Gender", bg="#92A9BD", font=("times new roman", 15, "bold"))
        gender.grid(row=4, column=0, pady=10, padx=10, sticky="w")

        gender_combo = ttk.Combobox(manage_frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"), state='readonly')
        gender_combo['values'] = ("Male", "Female", "Other")
        gender_combo.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        # Contact label and field
        contact = Label(manage_frame, text="Contact", bg="#92A9BD", font=("times new roman", 15, "bold"))
        contact.grid(row=5, column=0, pady=10, padx=10, sticky="w")

        txt_con = Entry(manage_frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"))
        txt_con.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        # Data of birth label and field
        dob = Label(manage_frame, text="DOB", bg="#92A9BD", font=("times new roman", 15, "bold"))
        dob.grid(row=6, column=0, pady=10, padx=10, sticky="w")

        txt_dob = Entry(manage_frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"))
        txt_dob.grid(row=6, column=1, pady=10, padx=10, sticky="w")

        # Address label and field
        address = Label(manage_frame, text="Address", bg="#92A9BD", font=("times new roman", 15, "bold"))
        address.grid(row=7, column=0, pady=10, padx=10, sticky="w")

        self.add_txt = Text(manage_frame, width=20, height=5, font=("times new roman", 15, "bold"))
        self.add_txt.grid(row=7, column=1, pady=10, padx=10, sticky="w")

        # buttons
        btn_frame = Frame(manage_frame, bg="#92A9BD")
        btn_frame.place(x=10, y=500, width=430)

        add_btn = Button(btn_frame, text="Add", width= 10, command=self.add_students).grid(row=0, column=0, pady=20, padx=10, sticky="w")
        up_btn = Button(btn_frame, text="Update", width=10, command=self.upadte_data).grid(row=0, column=1, pady=20, padx=10, sticky="w")
        del_btn = Button(btn_frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, pady=20, padx=10, sticky="w")
        clear_btn = Button(btn_frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3  , pady=20, padx=10, sticky="w")

        # this is the details frame here all details list of student is shown ---------------------------------------------------
        detail_frame = Frame(self.root, bg="#D3DEDC")
        detail_frame.place(x=450, y=65, width=950, height=660)

        # All data
        show = Label(detail_frame, text="Student Data", bg="#D3DEDC", font=("times new roman", 20, "bold"))
        show.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # Search label and combobox
        # search = Label(detail_frame, text="Search", bg="#D3DEDC", font=("times new roman", 20, "bold"))
        # search.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # search_combo = ttk.Combobox(detail_frame, width=10, textvariable=self.search_by, font=("times new roman", 13, "bold"), state='readonly')
        # search_combo['values'] = ("roll_no", "name", "email")
        # search_combo.grid(row=0, column=1, pady=10, padx=10, sticky="w")
        #
        # txt_search = Entry(detail_frame, width=30, textvariable=self.search_txt, font=("times new roman", 15, "bold"))
        # txt_search.grid(row=0, column=2, pady=10, padx=10, sticky="w")
        #
        # search_btn = Button(detail_frame, text="Search", width=10, command=self.search_data).grid(row=0, column=3, pady=20, padx=10, sticky="w")
        # show_data = Button(detail_frame, text="Show All", width=10, command=self.fetch_data).grid(row=0, column=4  , pady=20, padx=10, sticky="w")

        # grid frame
        grid_frame = Frame(detail_frame)
        grid_frame.place(x=10, y=75, width=880, height=550)

        # Tree view
        scroll_x = Scrollbar(grid_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(grid_frame, orient=VERTICAL)
        self.stud_table = ttk.Treeview(grid_frame,
            columns=("rollno", "name", "email", "gender", "contact", "dob", "address"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)

        self.stud_table.heading("rollno", text="Roll No")
        self.stud_table.heading("name", text="Name")
        self.stud_table.heading("email", text="Email")
        self.stud_table.heading("gender", text="Gender")
        self.stud_table.heading("contact", text="Contact")
        self.stud_table.heading("dob", text="DOB")
        self.stud_table.heading("address", text="Address")
        self.stud_table['show'] = "headings"

        self.stud_table.column("rollno", width=100)
        self.stud_table.column("name", width=120)
        self.stud_table.column("email", width=120)
        self.stud_table.column("gender", width=120)
        self.stud_table.column("contact", width=120)
        self.stud_table.column("dob", width=120)
        self.stud_table.column("address", width=150)

        self.stud_table.pack(fill=BOTH, expand=1)

        self.stud_table.bind("<ButtonRelease-1>", self.get_row)

        self.fetch_data()

    #Add Functions --------------------------------------------------------------------------------------------
    def add_students(self):
        if self.rollno_var.get() == "" or self.name_var == "":
            messagebox.showerror("Error", "All fields are required!!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="student_management")
            cur = con.cursor()
            cur.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s)', (
                self.rollno_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.add_txt.get('1.0', END)
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record is added")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.stud_table.delete(*self.stud_table.get_children())
            for row in rows:
                self.stud_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.rollno_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.add_txt.delete("1.0", END)

    def get_row(self, ev):
        curosor_row = self.stud_table.focus()
        contents =self.stud_table.item(curosor_row)
        row = contents['values']
        # print(row)
        self.rollno_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.add_txt.delete("1.0", END)
        self.add_txt.insert(END,row[6])

    def upadte_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management")
        cur = con.cursor()
        cur.execute('update students set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where roll_no=%s',
            (self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.add_txt.get('1.0', END),
            self.rollno_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s", self.rollno_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management")
        cur = con.cursor()
        cur.execute("select * from students where" + str(self.search_by.get()) + "LIKE %" +
                    str(self.search_txt.get()) + "%")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.stud_table.delete(*self.stud_table.get_children())
            for row in rows:
                self.stud_table.insert('', END, values=row)
            con.commit()
        con.close()

root = Tk()
stud = Student(root)
root.mainloop()