from tkinter import*
from tkinter import ttk
import random
import sys
from datetime import datetime
from tkinter import messagebox

def main():
    win = Tk()
    app = loginPage(win)
    win.mainloop()
    
class loginPage:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant Management System")
        
        self.title_label = Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        self.main_frame = Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=500,y=250,width=600,height=400)
        
        self.login_lbl = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,bg="lightgrey",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)
        
        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="lightgrey",font=('sans-serif',18))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)
        
        self.entus_lbl = Label(self.entry_frame,text="Enter Username: ",bg="lightgrey",font=('sans-serif',15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)
        
        #================variables==========================
        
        username = StringVar()
        password = StringVar()
        
        #===================================================
        
        self.entus_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)
        
        self.entpass_lbl = Label(self.entry_frame,text="Enter paaword: ",bg="lightgrey",font=('sans-serif',15))
        self.entpass_lbl.grid(row=1,column=0,padx=2,pady=2)
        
        self.entpass_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=password,show="*")
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)
        
        #=================function====================
        
        def check_login():
            '''this function will check login'''
            if username.get() == "" and password.get() == "":
                self.billing_btn.config(state="normal")
            else:
                pass #-----> massage box
            
            
        def reset():
             username.set("")
             password.set("")
            
        def billing_sect():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)
        
        #=============================================
        
        #================buttons======================
        
        self.button_frame = LabelFrame(self.entry_frame,text="Options",font=('Arial',15),bg="lightgrey",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=500,height=100)
        
        self.login_btn = Button(self.button_frame,text="Login",font=('Arial',10),bd=15, width=10,command=check_login)
        #self.login_btn = ttk.Button(self.button_frame,text="Login", width=10)
        self.login_btn.grid(row=1,column=0,padx=20,pady=5)
        
        self.billing_btn = Button(self.button_frame,text="Billing",font=('Arial',10),bd=15, width=10,command=billing_sect)
        self.billing_btn.grid(row=1,column=1,padx=20,pady=5)
        self.billing_btn.config(state="disabled")
        
        self.reset_btn = Button(self.button_frame,text="Reset",font=('Arial',10),bd=15, width=10,command=reset)
        self.reset_btn.grid(row=1,column=2,padx=20,pady=5)
        
        #=============================================  
class Window2:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1300x750+0+0")
        self.win.title("Restaurant Management System")
                
        self.title_label = Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        self.win.resizable(0,0)
        
        #============== variables ==================
        
        bill_no = random.randint(100,9999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)
        
        calc_var = StringVar()
        
        cust_nm = StringVar()
        cust_cot = StringVar()
        date_pr = StringVar()
        item_pur = StringVar()
        item_qty = StringVar()
        cone = StringVar()
        
        date_pr.set(datetime.now())
        
        total_list = []
        self.grd_total = 0
        
        #============================================
        
        #==============ENTRY=========================
        
        self.entry_frame = LabelFrame(self.win,text="Enter Details",background="lightgrey",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)
        
        self.bill_no_lbl = Label(self.entry_frame,text="Bill Number :",font=('arial',15) ,bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)
         
        self.bill_no_ent = Entry(self.entry_frame,bd=5,font=('arial',15) ,bg="lightgrey",textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")
         
        self.cust_nm_lbl = Label(self.entry_frame,text="Customer Name :",font=('arial',15) ,bg="lightgrey")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)
         
        self.cust_nm_ent = Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('arial',15) ,bg="lightgrey")
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)
        
        self.cust_cont_lbl = Label(self.entry_frame,text="Customer Contact :",font=('arial',15) ,bg="lightgrey")
        self.cust_cont_lbl.grid(row=2,column=0,padx=2,pady=2)
         
        self.cust_cont_ent = Entry(self.entry_frame,bd=5,textvariable=cust_cot,font=('arial',15) ,bg="lightgrey")
        self.cust_cont_ent.grid(row=2,column=1,padx=2,pady=2)
        
        self.cust_lbl = Label(self.entry_frame,text="Date :",font=('arial',15) ,bg="lightgrey")
        self.cust_lbl.grid(row=3,column=0,padx=2,pady=2)
         
        self.date_ent = Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('arial',15) ,bg="lightgrey")
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)
        self.date_ent.config(state="disabled")
        
        
        self.item_purchased_lbl = Label(self.entry_frame,text="Items purchased :",font=('arial',15) ,bg="lightgrey")
        self.item_purchased_lbl.grid(row=4,column=0,padx=2,pady=2)
         
        self.item_purchased_ent = Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('arial',15) ,bg="lightgrey")
        self.item_purchased_ent.grid(row=4,column=1,padx=2,pady=2)
        
        self.item_qlty_lbl = Label(self.entry_frame,text="Item Quantity :",font=('arial',15) ,bg="lightgrey")
        self.item_qlty_lbl.grid(row=5,column=0,padx=2,pady=2)
         
        self.item_qlty_ent = Entry(self.entry_frame,bd=5,textvariable=item_qty ,font=('arial',15) ,bg="lightgrey")
        self.item_qlty_ent.grid(row=5,column=1,padx=2,pady=2)
        
        self.item_one_lbl = Label(self.entry_frame,text="Cost of one :",font=('arial',15) ,bg="lightgrey")
        self.item_one_lbl.grid(row=6,column=0,padx=2,pady=2)
         
        self.item_one_ent = Entry(self.entry_frame,bd=5,textvariable=cone,font=('arial',15) ,bg="lightgrey")
        self.item_one_ent.grid(row=6,column=1,padx=2,pady=2)
        
        #================== funtion ========================
        
        def default_bill():
            self.bill_txt.insert(END,"\t\t\tKrishna hotel & gust house")
            self.bill_txt.insert(END,"\n\t\t\tDwarikadhish temple opposite,Dwarika")
            self.bill_txt.insert(END,"\n\t\t\t\t       PIN Coad :- 361335")
            self.bill_txt.insert(END,"\n\t\t\t\t       Contact - +9510991141")
            self.bill_txt.insert(END,"\n=================================================================================")
            self.bill_txt.insert(END,f"\n   Bill Number {bill_no_tk.get()}")
        
        def genbill():
            if cust_nm.get() == "" or (cust_cot.get() == "" or len(cust_cot.get()) !=10):
                messagebox.showerror("Error!","please enter all the fields correctly.",parent=self.win)
            else:
                self.bill_txt.insert(END,f"\n Customer Name : {cust_nm.get()}")
                self.bill_txt.insert(END,f"\n Customer Contact : {cust_cot.get()}")
                self.bill_txt.insert(END,f"\n Date : {date_pr.get()}")
                self.bill_txt.insert(END,f"\n=================================================================================")
                self.bill_txt.insert(END,"\nProduct Name\t\t      Quantity      \t\t per cost\t\t      total")
                self.bill_txt.insert(END,f"\n=================================================================================")
            
                self.add_btn.config(state="normal")
                self.total_btn.config(state="normal")
        
        def clear_func():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("") 
        
        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)
            default_bill()
            
        def add_func():
            if item_pur.get() == "" or item_qty.get() == "":
                messagebox.showerror("Error!","please enter all the fields correctly.",parent=self.win)
            else:
                qty = int(item_qty.get())
                cones = int(cone.get())
                total = qty * cones
                total_list.append(total)
                self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t      {item_qty.get()}\t\t       Rs. {cone.get()}\t\t       Rs. {total}")
              
        def total_func():
            for item in total_list:
                self.grd_total = self.grd_total + item
            self.bill_txt.insert(END,f"\n=================================================================================")
            self.bill_txt.insert(END,f"\t\t\t\t            Grand total : {self.grd_total}")
            self.bill_txt.insert(END,f"\n=================================================================================")
            self.save_btn.config(state="normal")
            
                   
        def save_func():
            user_choice = messagebox.askyesno("confirm",f"do you want to save the bill {bill_no_tk.get}",parent=self.win)
            if user_choice > 0:
                self.bill_content = self.bill_txt.get("1.0",END)
                try:
                    con = open(f"{sys.path[0]}/bill_data/+str{bill_no_tk.get()}+","w")
                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {e}",parent=self.win)
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("success!",f"Bill {bill_no_tk.get()} has been saved successfully!",parent=self.win)
            else:
                return
   
        #================= button =================
        
        self.button_frame = LabelFrame(self.entry_frame,bd=5,text="Options",bg="lightgrey",font=("Arial",25))
        self.button_frame.place(x=20,y=280,width=392,height=300)
        
        self.add_btn = Button(self.button_frame,bd=2,text="add",font=('arial',12),width=11,height=2,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)
        
        self.generate_btn = Button(self.button_frame,bd=2,text="Generate",font=('arial',11),width=11,height=2,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)
        
        self.clear_btn = Button(self.button_frame,bd=2,text="Clear",font=('arial',11),width=11,height=2,command=clear_func)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)
        
        self.total_btn = Button(self.button_frame,bd=2,text="Total",font=('arial',11),width=11,height=2,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)
        
        self.reset_btn = Button(self.button_frame,bd=2,text="Reset",font=('arial',11),width=11,height=2,command=reset_func)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)
        
        self.save_btn = Button(self.button_frame,bd=2,text="Save",font=('arial',11),width=11,height=2,command=save_func)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)
        
        # self.print_btn = Button(self.button_frame,bd=2,text="Print",font=('arial',11),width=10,height=3)
        # self.print_btn.grid(row=2,column=0,padx=4,pady=2)
        
        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")
        
        #==========================================
        
        #============= calculater frame ===========
        
        self.calc_frame = Frame(self.win,bd=8,background="lightgrey",relief=GROOVE)
        self.calc_frame.place(x=570,y=110,width=605,height=295)
        
        self.num_ent = Entry(self.calc_frame,bd=15,background="lightgrey",textvariable=calc_var,font=('arial',15),width=50,justify='right')
        self.num_ent.grid(row=0,column=0,columnspan=11)
        
        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                if calc_var.get().isdigit():
                    value = int(calc_var.get())
                else:
                    try:
                        value = eval(self.num_ent.get())
                    except:
                        print("error")
                calc_var.set(value)
                self.num_ent.update()
            elif text == "C":
                pass
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()
                

        self.btn7 = Button(self.calc_frame,bg="lightgrey",text="7",bd=8,width=11,height=1,font=('arial',15))
        self.btn7.grid(row=1,column=0,padx=2,pady=2)
        self.btn7.bind("<Button-1>",press_btn)
               
        self.btn8 = Button(self.calc_frame,bg="lightgrey",text="8",bd=8,width=11,height=1,font=('arial',15))
        self.btn8.grid(row=1,column=1,padx=2,pady=2)
        self.btn8.bind("<Button-1>",press_btn)
        
        self.btn9 = Button(self.calc_frame,bg="lightgrey",text="9",bd=8,width=11,height=1,font=('arial',15))
        self.btn9.grid(row=1,column=2,padx=2,pady=2)
        self.btn9.bind("<Button-1>",press_btn)
        
        self.btnadd = Button(self.calc_frame,bg="lightgrey",text="+",bd=8,width=11,height=1,font=('arial',15))
        self.btnadd.grid(row=1,column=3,padx=2,pady=2)
        self.btnadd.bind("<Button-1>",press_btn)
        
        self.btn4 = Button(self.calc_frame,bg="lightgrey",text="4",bd=8,width=11,height=1,font=('arial',15))
        self.btn4.grid(row=2,column=0,padx=2,pady=2)
        self.btn4.bind("<Button-1>",press_btn)
               
        self.btn5 = Button(self.calc_frame,bg="lightgrey",text="5",bd=8,width=11,height=1,font=('arial',15))
        self.btn5.grid(row=2,column=1,padx=2,pady=2)
        self.btn5.bind("<Button-1>",press_btn)
        
        self.btn6 = Button(self.calc_frame,bg="lightgrey",text="6",bd=8,width=11,height=1,font=('arial',15))
        self.btn6.grid(row=2,column=2,padx=2,pady=2)
        self.btn6.bind("<Button-1>",press_btn)
        
        self.btnsubs = Button(self.calc_frame,bg="lightgrey",text="-",bd=8,width=11,height=1,font=('arial',15))
        self.btnsubs.grid(row=2,column=3,padx=2,pady=2)
        self.btnsubs.bind("<Button-1>",press_btn)
        
        self.btn1 = Button(self.calc_frame,bg="lightgrey",text="1",bd=8,width=11,height=1,font=('arial',15))
        self.btn1.grid(row=3,column=0,padx=2,pady=2)
        self.btn1.bind("<Button-1>",press_btn)
               
        self.btn2 = Button(self.calc_frame,bg="lightgrey",text="2",bd=8,width=11,height=1,font=('arial',15))
        self.btn2.grid(row=3,column=1,padx=2,pady=2)
        self.btn2.bind("<Button-1>",press_btn)
        
        self.btn3 = Button(self.calc_frame,bg="lightgrey",text="3",bd=8,width=11,height=1,font=('arial',15))
        self.btn3.grid(row=3,column=2,padx=2,pady=2)
        self.btn3.bind("<Button-1>",press_btn)
        
        self.btnmult = Button(self.calc_frame,bg="lightgrey",text="*",bd=8,width=11,height=1,font=('arial',15))
        self.btnmult.grid(row=3,column=3,padx=2,pady=2)
        self.btnmult.bind("<Button-1>",press_btn)
        
        self.btn0 = Button(self.calc_frame,bg="lightgrey",text="0",bd=8,width=11,height=1,font=('arial',15))
        self.btn0.grid(row=4,column=0,padx=2,pady=2)
        self.btn0.bind("<Button-1>",press_btn)
               
        self.btnpoint = Button(self.calc_frame,bg="lightgrey",text=".",bd=8,width=11,height=1,font=('arial',15))
        self.btnpoint.grid(row=4,column=1,padx=2,pady=2)
        self.btnpoint.bind("<Button-1>",press_btn)
        
        self.btn_eql = Button(self.calc_frame,bg="lightgrey",text="=",bd=8,width=11,height=1,font=('arial',15))
        self.btn_eql.grid(row=4,column=2,padx=2,pady=2)
        self.btn_eql.bind("<Button-1>",press_btn)
        
        self.btndiv = Button(self.calc_frame,bg="lightgrey",text="/",bd=8,width=11,height=1,font=('arial',15))
        self.btndiv.grid(row=4,column=3,padx=2,pady=2)
        self.btndiv.bind("<Button-1>",press_btn)
        
        #==========================================
        
        #============ Bill Area ==================
        
        self.bill_frame = LabelFrame(self.win,text="Bill Area",font=("arial",18),background="lightgrey",bd=8,relief=GROOVE)
        self.bill_frame.place(x=570,y=420,width=700,height=320)
        
        self.y_scroll = Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt = Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)
        
       
        default_bill()
        
        
        
        
        #==========================================
        
        
if __name__ == "__main__":
    main()