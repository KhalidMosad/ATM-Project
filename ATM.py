import tkinter
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import *
import sys
global Password_Entry
global img



def AccountNoChecker():
    global ACCOUNT_NUM
    ACCOUNT_NUM = AccountNo_Entry.get()
    Locked_Accounts_File = open("ATM_Locked_Accounts.txt","r")
    blocked_Accounts_List = list()
    for Line in Locked_Accounts_File:
        blocked_Accounts_List.append(Line.rstrip("\n"))
    if ACCOUNT_NUM in blocked_Accounts_List :
        if ACCOUNT_NUM=="":
            tkinter.messagebox.showwarning("Error","Enter Account Number")
        else:
        	tkinter.messagebox.showwarning("LOCKED ACCOUNT" , "THIS ACCOUNT IS LOCKED!, PLEASE GO TO THE BRANCH.")





    else:

        try:
            file=open("ATM_Database.txt" , 'r')

        except:
            file=open("ATM_Database.txt" , 'r')
        finally:
            global mydict
            mydict=dict()
            for line in file:
                ID = line[0 : line.find(" :")]
                Name = line[ line.find('@')+1 : line.find('@@') ]
                Password = line[ line.find("$")+1 : line.find('$@') ]
                Balance = line[ line.find('%')+1 : line.find('%@') ]
                mydict[ID]={ "Name" : Name , "Password" : Password , "Balance" : Balance}
        file.close()
        global Account_Index
        file=open("ATM_Database.txt" , 'r')
        List_of_lines = list()
        List_of_lines = file.readlines()
        file.close()
        i=0
        for line in List_of_lines:
            List_of_lines[i] = line[ 0:line.find(" :") ]
            i+=1

        if str(ACCOUNT_NUM) in mydict.keys():
            Account_Index = List_of_lines.index(ACCOUNT_NUM)
            Creat_Password_Window()
        else:

            tkinter.messagebox.showerror("ERROR" , "ACCOUNT NUMBER NOT FOUND")
            Creat_AccountNo_Window()
            return 0

def Creat_AccountNo_Window():
    Clear_WIDGETSALL()
    Creat_Label("Enter Your Account Number",5,1)
    global ATM_Window
    global AccountNo_Entry
    global test
    global label1
    global photo
    #phote=PhotoImage(file="C:\Users\Khaled\Desktop\Final_Project/refill_cash.png")
    #label1 = tkinter.Label( ATM_Window , image=phote )
   # label1.pack(x=0,y=0,relwidth=1, relheight=1)

    AccountNo_Entry=tkinter.Entry(ATM_Window , width=45 ,show="")
    AccountNo_Entry.grid(row= 5 , column= 3)
    AccountNo_Button=tkinter.Button(ATM_Window , text="Enter" ,width=10 , height=1, command = AccountNoChecker)
    AccountNo_Button.grid(row= 7 , column= 3)

	#ATM_Window.creat_image(40,40,anchor=NW, image=img)


def Creat_Password_Window():
    Clear_WIDGETSALL()
    Creat_Label("Enter Your Password",5,1)
    global ATM_Window
    global Password_Entry
    Password_Entry=tkinter.Entry(ATM_Window ,width=45 , show="*")
    Password_Entry.grid(row= 5 , column= 3)
    Password_Button=tkinter.Button(ATM_Window , text="Enter" ,width=10 , height=1, command = Password_Validation)
    Password_Button.grid(row= 7 , column= 3)
    BACK_Button = tkinter.Button(ATM_Window , text="Change Account Number " ,width=20 , height=2, command=Creat_AccountNo_Window)
    BACK_Button.grid(row=15 , column=1)
x = 0
def Password_Validation():
    global ACCOUNT_NUM
    global Password_Entry
    global ATM_Window
    global x
    # print(mydict[ACCOUNT_NUM]["Password"])
    if x < 3:

        Received_Password = str(Password_Entry.get())
        if Received_Password == mydict[ACCOUNT_NUM]["Password"]:
            x=-1
            Options_Window()

        else:

            if 2 == x:
                Locked_Accounts_File = open("ATM_Locked_Accounts.txt" , "a")
                Locked_Accounts_File.write(str(ACCOUNT_NUM)+"\n")
                tkinter.messagebox.showwarning("LOCKED ACCOUNT", "YOUR ACCOUNT HAS BEEN LOCKED!!")
                x=-1
                Creat_AccountNo_Window()
            else:
                tkinter.messagebox.showerror("ERORR MESSAGE", "INCORRECT PASSWORD")
                Creat_Password_Window()

				#Password_Entry.delete(0,'end')
        x+=1

def Options_Window():
    Clear_WIDGETSALL()

    Cash_Withdraw_Button=tkinter.Button(ATM_Window , text="Cash Withdraw" ,width=20 , height=2, command = WITHDRAW_MONEY)
    Cash_Withdraw_Button.grid(row=1 , column=1)

    Balance_Inquiry_Button=tkinter.Button(ATM_Window , text="Balance Inquiry" ,width=20 , height=2, command = Balance_Inquiry)
    Balance_Inquiry_Button.grid(row=2 , column=2)

    Password_Change_Button=tkinter.Button(ATM_Window , text="Password Change" ,width=20 , height=2, command = CHANGING_PASSWORD)
    Password_Change_Button.grid(row=3 , column=3)

    Fawry_Service_Button=tkinter.Button(ATM_Window , text="Fawry Service" ,width=20 , height=2, command = Fawry_Service_Window)
    Fawry_Service_Button.grid(row=4 , column=4)

    Exit_Button=tkinter.Button(ATM_Window , text="Exit" ,width=20 , height=2, command = Exit_Function)
    Exit_Button.grid(row=10 , column=3)

    BACK_Button = tkinter.Button(ATM_Window , text="Go TO Another Account Number" ,width=25 , height=2, command=Creat_AccountNo_Window)
    BACK_Button.grid(row=10 , column=1)


#with direct using of exit .exe application give an error
def Exit_Function():
    sys.exit(0)

def Fawry_Service_Window():
    Clear_WIDGETSALL()
    Vodafone_Button = tkinter.Button(ATM_Window , text="Vodafone_Recharge" ,width=20 , height=2, command=Vodafone_Recharge_Window)
    Vodafone_Button.grid(row=2 , column=4)

    Orange_Button = tkinter.Button(ATM_Window , text="Orange Recharge" ,width=20 , height=2, command=Orange_Recharge_Window)
    Orange_Button.grid(row=2 , column=7)

	#BACK_Button = tkinter.Button(ATM_Window , text="Back" ,width=20 , height=2, command=Options_Window)
    #BACK_Button.grid(row=5 , column=7)

    Etisalat_Button = tkinter.Button(ATM_Window , text="Etisalat Recharge" ,width=20 , height=2, command=Etisalat_Recharge_Window)
    Etisalat_Button.grid(row=4 , column=4)

    We_Button = tkinter.Button(ATM_Window , text="We_Recharge" ,width=20 , height=2, command=We_Recharge_Window)
    We_Button.grid(row=4 , column=7)
    BACK_Button = tkinter.Button(ATM_Window , text="Back" ,width=20 , height=2, command=Options_Window)
    BACK_Button.grid(row=6 , column=7)



	#Back_Button = tkinter.Button(ATM_Window , text="Back" ,width=20 , height=2, command=Options_Window)
    #Back_Button.grid(row=5 , column=5)

def Vodafone_Recharge_Window():
    Clear_WIDGETSALL()

    Label_1 = tkinter.Label( ATM_Window , text="Please Enter the Number" )
    Label_1.grid(row=5 , column=2)

    global Vodafone_No
    Vodafone_No = tkinter.Entry(ATM_Window,width=40)
    Vodafone_No.grid(row=5 , column=4)

    Label_2 = tkinter.Label( ATM_Window , text="Please Enter Amount of Money" )
    Label_2.grid(row=7 , column=2)

    global Vodafone_Money
    Vodafone_Money = tkinter.Entry(ATM_Window,width=40)
    Vodafone_Money.grid(row=7 , column=4)

    Button = tkinter.Button(ATM_Window , text="Enter" ,width=7 , height=2, command=Vodafone_Recharge)
    Button.grid(row=9 , column=4)

    BACK_Button = tkinter.Button(ATM_Window , text="Back" ,width=20 , height=2, command=Options_Window)
    BACK_Button.grid(row=9 , column=7)

def Vodafone_Recharge():

    Number = Vodafone_No.get()
    Money = Vodafone_Money.get()
    if str(Number)[0:3] == "010" and len(str(Number)) >=10 and len(str(Number)) <=11:
        if int(Money) > 0:
            file = open("ATM_Database.txt" , "r")
            List_of_lines = list()
            List_of_lines = file.readlines()
            file.close()
            Line_to_Edit = List_of_lines [Account_Index]
            Reminder = int( mydict[ACCOUNT_NUM]["Balance"] ) - int(Money)
            Line_to_Edit = Line_to_Edit.replace( mydict[ACCOUNT_NUM]["Balance"] , str(Reminder) )
            List_of_lines[Account_Index] = Line_to_Edit
            file = open("ATM_Database.txt" , "w" )
            file.writelines( List_of_lines )
            file.close()
            tkinter.messagebox.showinfo("Congratulations" , "Successfully Recharege Your Number:  "+ Number+ "\n Amount: "+ Money)
            Creat_AccountNo_Window()
        else:
            tkinter.messagebox.showerror("ERROR" , "Please Enter Valid Amount of Money")
            Vodafone_Recharge_Window()

    else:
        tkinter.messagebox.showerror("ERROR" , "Please Enter a Valid Number")
        Vodafone_Recharge_Window()

def We_Recharge_Window():
    Clear_WIDGETSALL()

    Label_1 = tkinter.Label( ATM_Window , text="Please Enter the Number" )
    Label_1.grid(row=5 , column=2)

    global We_No
    We_No = tkinter.Entry(ATM_Window,width=40)
    We_No.grid(row=5 , column=4)

    Label_2 = tkinter.Label( ATM_Window , text="Please Enter Amount of Money" )
    Label_2.grid(row=7 , column=2)

    global We_Money
    We_Money = tkinter.Entry(ATM_Window,width=40)
    We_Money.grid(row=7 , column=4)

    Button = tkinter.Button(ATM_Window , text="Enter" ,width=7 , height=2, command=We_Recharge)
    Button.grid(row=9 , column=4)
    BACK_Button = tkinter.Button(ATM_Window , text="Back" ,width=20 , height=2, command=Options_Window)
    BACK_Button.grid(row=9 , column=7)

def We_Recharge():

    Number = We_No.get()
    Money = We_Money.get()
    print(Number)
    print(str(Number)[:3])
    if str(Number)[0:3] == "015" and len(str(Number)) >=10 and len(str(Number)) <=11:
        if int(Money) > 0:
            file = open("ATM_Database.txt" , "r")
            List_of_lines = list()
            List_of_lines = file.readlines()
            file.close()
            Line_to_Edit = List_of_lines [Account_Index]
            Reminder = int( mydict[ACCOUNT_NUM]["Balance"] ) - int(Money)
            Line_to_Edit = Line_to_Edit.replace( mydict[ACCOUNT_NUM]["Balance"] , str(Reminder) )
            List_of_lines[Account_Index] = Line_to_Edit
            file = open("ATM_Database.txt" , "w" )
            file.writelines( List_of_lines )
            file.close()
            tkinter.messagebox.showinfo("Congratulations" , "Successfully Recharege Your Number:  "+ Number+ "\n Amount: "+ Money)
            Creat_AccountNo_Window()
        else:
            tkinter.messagebox.showerror("ERROR" , "Please Enter Valid Amount of Money")
            We_Recharge_Window()

    else:
        tkinter.messagebox.showerror("ERROR" , "Please Enter a Valid Number")
        Vodafone_Recharge_Window()



def Orange_Recharge_Window():
    Clear_WIDGETSALL()

    Label_1 = tkinter.Label( ATM_Window , text="Please Enter the Number" )
    Label_1.grid(row=5 , column=2)

    global Orange_No
    Orange_No = tkinter.Entry(ATM_Window,width=40)
    Orange_No.grid(row=5 , column=4)

    Label_2 = tkinter.Label( ATM_Window , text="Please Enter Amount of Money" )
    Label_2.grid(row=7 , column=2)

    global Orange_Money
    Orange_Money = tkinter.Entry(ATM_Window,width=40)
    Orange_Money.grid(row=7 , column=4)

    Button = tkinter.Button(ATM_Window , text="Enter" ,width=7 , height=2, command=Orange_Recharge)
    Button.grid(row=9 , column=4)
    BACK_Button = tkinter.Button(ATM_Window , text="Back" ,width=20 , height=2, command=Options_Window)
    BACK_Button.grid(row=9 , column=7)

def Orange_Recharge():

    Number = Orange_No.get()
    Money = Orange_Money.get()
    print(Number)
    print(str(Number)[:3])
    if str(Number)[0:3] == "012" and len(str(Number)) >=10 and len(str(Number)) <=11:
        if int(Money) > 0:
            file = open("ATM_Database.txt" , "r")
            List_of_lines = list()
            List_of_lines = file.readlines()
            file.close()
            Line_to_Edit = List_of_lines [Account_Index]
            Reminder = int( mydict[ACCOUNT_NUM]["Balance"] ) - int(Money)
            Line_to_Edit = Line_to_Edit.replace( mydict[ACCOUNT_NUM]["Balance"] , str(Reminder) )
            List_of_lines[Account_Index] = Line_to_Edit
            file = open( "ATM_Database.txt" , "w" )
            file.writelines( List_of_lines )
            file.close()
            tkinter.messagebox.showinfo("Congratulations" , "Successfully Recharege Your Number:  "+ Number+ "\n Amount: "+ Money)
            Creat_AccountNo_Window()
        else:
            tkinter.messagebox.showerror("ERROR" , "Please Enter Valid Amount of Money")
            Vodafone_Recharge_Window()

    else:
        tkinter.messagebox.showerror("ERROR" , "Please Enter a Valid Number")
        Vodafone_Recharge_Window()


def Etisalat_Recharge_Window():
    Clear_WIDGETSALL()

    Label_1 = tkinter.Label( ATM_Window , text="Please Enter the Number" )
    Label_1.grid(row=5 , column=2)

    global Etisalat_No
    Etisalat_No = tkinter.Entry(ATM_Window,width=40)
    Etisalat_No.grid(row=5 , column=4)

    Label_2 = tkinter.Label( ATM_Window , text="Please Enter Amount of Money" )
    Label_2.grid(row=7 , column=2)

    global Etisalat_Money
    Etisalat_Money = tkinter.Entry(ATM_Window,width=40)
    Etisalat_Money.grid(row=7 , column=4)

    Button = tkinter.Button(ATM_Window , text="Enter" ,width=7 , height=2, command=Etisalat_Recharge)
    Button.grid(row=9 , column=4)
    BACK_Button = tkinter.Button(ATM_Window , text="Back" ,width=20 , height=2, command=Options_Window)
    BACK_Button.grid(row=9 , column=7)

def Etisalat_Recharge():

    Number = Etisalat_No.get()
    Money = Etisalat_Money.get()
    print(Number)
    print(str(Number)[:3])
    if str(Number)[0:3] == "011" and len(str(Number)) >=10 and len(str(Number)) <=11:
        if int(Money) > 0:
            file = open("ATM_Database.txt" , "r")
            List_of_lines = list()
            List_of_lines = file.readlines()
            file.close()
            Line_to_Edit = List_of_lines [Account_Index]
            Reminder = int( mydict[ACCOUNT_NUM]["Balance"] ) - int(Money)
            Line_to_Edit = Line_to_Edit.replace( mydict[ACCOUNT_NUM]["Balance"] , str(Reminder) )
            List_of_lines[Account_Index] = Line_to_Edit
            file = open( "ATM_Database.txt" , "w" )
            file.writelines( List_of_lines )
            file.close()
            tkinter.messagebox.showinfo("Congratulations" , "Successfully Recharege Your Number:  "+ Number+ "\n Amount: "+ Money)
            Creat_AccountNo_Window()
        else:
            tkinter.messagebox.showerror("ERROR" , "Please Enter Valid Amount of Money")
            Vodafone_Recharge_Window()

    else:
        tkinter.messagebox.showerror("ERROR" , "Please Enter a Valid Number")
        Vodafone_Recharge_Window()

New_Password_1=""
New_Password_2=""
def CHANGING_PASSWORD():
    Clear_WIDGETSALL()
    Label = tkinter.Label( ATM_Window , text="Please Enter the Password" )
    Label.grid(row=5 , column=2)

    global New_Password_Entry_1
    New_Password_Entry_1 = tkinter.Entry(ATM_Window,width=40)
    New_Password_Entry_1.grid(row=5 , column=4)

    Label = tkinter.Label( ATM_Window , text="Please Re-Enter the Password" )
    Label.grid(row=7 , column=2)

    global New_Password_Entry_2
    New_Password_Entry_2 = tkinter.Entry(ATM_Window,width=40)
    New_Password_Entry_2.grid(row=7 , column=4)

    Button = tkinter.Button(ATM_Window , text="Enter" ,width=7 , height=2, command=CHECK_NEW_PASSWORD)
    Button.grid(row=9 , column=4)

    BACK_Button = tkinter.Button(ATM_Window , text="Back" ,width=20 , height=2, command=Options_Window)
    BACK_Button.grid(row=10 , column=2)


def CHECK_NEW_PASSWORD():
    New_Password_1 = int( New_Password_Entry_1.get() )
    New_Password_2 = int( New_Password_Entry_2.get() )

    if New_Password_1 == New_Password_2 :
        if len(str(New_Password_1)) != 4:
            tkinter.messagebox.showwarning("Length Error" , "Password Must Be 4 Digits!")
            CHANGING_PASSWORD()
        else:
            file = open("ATM_Database.txt" , "r")
            List_of_lines = list()
            List_of_lines = file.readlines()
            file.close()
            Line_to_Edit = List_of_lines [Account_Index]
            Line_to_Edit = Line_to_Edit.replace( mydict[ACCOUNT_NUM]["Password"] , str(New_Password_1) )
            List_of_lines[Account_Index] = Line_to_Edit
            file = open( "ATM_Database.txt" , "w" )
            file.writelines( List_of_lines )
            file.close()
            tkinter.messagebox.showinfo("Congratulations" , "Password Successfully Updated")
            Creat_AccountNo_Window()
    else:
        tkinter.messagebox.showerror("WRONG PASSWORD" , "Password Does Not Match")





def Balance_Inquiry():
    Clear_WIDGETSALL()
    Label = tkinter.Label( ATM_Window , text="Name: "+mydict[ACCOUNT_NUM]["Name"]+" \nBalance= "+mydict[ACCOUNT_NUM]["Balance"] )
    Label.grid(row=5 , column=2)

    Button = tkinter.Button(ATM_Window , text="OK" ,width=7 , height=2 , command=Creat_AccountNo_Window)
    Button.grid(row=7 , column=3)

    BACK_Button = tkinter.Button(ATM_Window , text="Back" ,width=20 , height=2, command=Options_Window)
    BACK_Button.grid(row=9 , column=2)


def WITHDRAW_MONEY():
    Clear_WIDGETSALL()

    Label=tkinter.Label(ATM_Window , text="Please Enter the Desired Amount" )
    Label.grid(row=5 , column=2)

    global Cash_Withdraw_Entry
    Cash_Withdraw_Entry=tkinter.Entry(ATM_Window,width=40)
    Cash_Withdraw_Entry.grid(row=5 , column=4)

    Enter_Button=tkinter.Button(ATM_Window , text="Enter" , height=2 , width=7, command = PRINT_OUT)
    Enter_Button.grid(row= 7, column=4)

    BACK_Button = tkinter.Button(ATM_Window , text="Back" ,width=20 , height=2, command=Options_Window)
    BACK_Button.grid(row=10 , column=2)


def PRINT_OUT():
    global ACCOUNT_NUM
    global Cash_Withdraw_Entry
    Entry = str(Cash_Withdraw_Entry.get())
    if int(Entry) % 100 == 0 :
        if Entry <= mydict[ACCOUNT_NUM]["Balance"]:
            if int(Entry)<=5000 :
                file = open("ATM_Database.txt" , "r")
                List_of_lines = list()
                List_of_lines = file.readlines()
                file.close()
                # print("Account index",Account_Index)
                Line_to_Edit = List_of_lines [Account_Index]
                Reminder = int( mydict[ACCOUNT_NUM]["Balance"] ) - int(Entry)
                # print(Reminder)
                Line_to_Edit = Line_to_Edit.replace( mydict[ACCOUNT_NUM]["Balance"] , str(Reminder) )
                # print(Line_to_Edit)
                # print(List_of_lines[Account_Index])
                List_of_lines[Account_Index] = Line_to_Edit
                file = open("ATM_Database.txt" , "w" )
                file.writelines( List_of_lines )
                file.close()
            else:
                tkinter.messagebox.showerror("Out of Range" , "maximum Allowed Value is 5000 L.E ")
                WITHDRAW_MONEY()
        else:
            tkinter.messagebox.showerror("No Sufficient Balance" , "Sorry You are so Poor!, You Do Not Have Enough Money")
            Creat_AccountNo_Window()


    else:
        tkinter.messagebox.showerror("Not Allowed Value" , "The Allowed Values are Multiple of 100L.E")
        WITHDRAW_MONEY()


    if Entry <= mydict[ACCOUNT_NUM]["Balance"] and int(Entry) % 100 == 0 and int(Entry)<=5000:
        tkinter.messagebox.showinfo("Thanks" , "Thank \n "+ mydict[ACCOUNT_NUM]["Name"] + " \n "+ "Amount "+ Entry +"\n" )
        Creat_AccountNo_Window()

    #the next two -instead of previous three lines- lines make an error and I do not why!
    #the error is program call the functions normally but exit immediately without execution
    # tkinter.messagebox.showinfo("Thanks" , "Thank You for Using Our Application")
    # Creat_AccountNo_Window()





ATM_Window=tkinter.Tk()                                 #Tk() function to creat main app window

def Creat_App_Window():
    global ATM_Window
    ATM_Window.title("ATM_APPLICATIOM")           #title for the application
    ATM_Window.geometry( "700x500+500+100" )                 #.geometry( "window width  x window height + position right + position down" )
    ATM_Window.resizable(width=False , height=False)          #.resizable is a function to control sizing option in application
    ATM_Window.configure(background="blue")              #.configure is a function to configure application window
    # ATM_Window.mainloop()       #mainloop() is a function put your code in infinite loop
    global FilePath
    #tkinter.messagebox.showinfo("Determine Workspace Path" , "Please Select Workspace Path Which Contain Database File")
    #FilePath = filedialog.askdirectory()
    ATM_Window.withdraw()
    ATM_Window.deiconify()

def Configure_grid_Window(Row_No , Row_Minsize , Column_No , Column_Minsize):
    global ATM_Window
    i=0
    while i<Row_No:
        ATM_Window.grid_rowconfigure(i,minsize=Row_Minsize)
        i+=1

    i=0
    while i<Column_No:
        ATM_Window.grid_columnconfigure(i,minsize=Column_Minsize)
        i+=1
def Creat_Button(Button_Name,Row_Position,Column_Position,function):
    global ATM_Window
    Button=tkinter.Button(ATM_Window , text=Button_Name,command=function)
    Button.grid(row= Row_Position , column= Column_Position)


def Creat_Label(Label_Name,Row_Position,Column_Position):
    global ATM_Window
    Label=tkinter.Label(ATM_Window ,width=30, text=Label_Name)
    Label.grid(row= Row_Position , column= Column_Position)


def Creat_Entry(Row_Position,Column_Position,Show_character=''):
    global ATM_Window
    Entry=tkinter.Entry(ATM_Window , show=Show_character)
    Entry.grid(row= Row_Position , column= Column_Position)

def Clear_WIDGETSALL():
    global ATM_Window
    Widget_List=ATM_Window.grid_slaves()
    for Widgwt in Widget_List:
        Widgwt.destroy()
