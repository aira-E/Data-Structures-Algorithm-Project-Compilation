from tkinter import *
root = Tk()
root.title("Sweet’s Candy Shop")
var = StringVar()

#Pera Counter
global inserted_money
inserted_money = 0

#---------------------------------------------- BUTTON FUNCTIONS----------------------------------------------
#Reset Button Func
def reset_button ():
    costarea.delete(1.0,END)
    output.delete(1.0,END)
    change.delete(1.0,END)
    moneydisplay.delete(0,100)
    b1["state"] = "normal"
    b2["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"
    b5["state"] = "disabled"

#Candy Button Func
def candy_button():
    costarea.insert("1.0", "candy \ncosts 50 cents")
    b2["state"] = "disable"
    b3["state"] = "disable"
    b4["state"] = "disable"
    b5["state"] = "normal"

#Chips Button Func
def chips_button():
    costarea.insert("1.0", "chips \ncosts 50 cents")
    b1["state"] = "disable"
    b3["state"] = "disable"
    b4["state"] = "disable"
    b5["state"] = "normal"

#Gums Button Func
def gums_button():
    costarea.insert("1.0", "gums \ncosts 50 cents")
    b1["state"] = "disable"
    b2["state"] = "disable"
    b4["state"] = "disable"
    b5["state"] = "normal"

#Cookes Button Func
def cookies_button():
    costarea.insert("1.0", "cookies \ncosts 50 cents")
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
    b5["state"] = "normal"

#Naglagay ng pera ang user
def pushmoney_button():
    try:
        output.delete(1.0,END)
        change.delete(1.0,END)
        moneyin = moneydisplay.get()

        #Naglagay ng sobra o saktong pera ang user
        if float(moneyin) >= 50:
            if float(moneyin) > 50: #Naglagay ng sobra ang user
                sukli = float(moneyin) - 50
                change.insert("1.0",(f"change: {sukli}")) #nagsukli
            #Di na maglalabas ng change kapag sakto ang pera
            output.insert("2.0", "\n\n Enjoy your \n product!", ) #naibigay ang product

        #Naglagay ng kulang na pera ang user
        elif float(moneyin) < 50:
            global inserted_money
            inserted_money += float(moneyin) #I-dagdag ang kulang na pera

            #Nagdagdag ng kulang na pera ang user
            if inserted_money < 50:
                kulang = 50 - inserted_money
                change.insert("1.0",(f"please add: {kulang}")) #nagabiso kung ilang ang kulang

            #Nagdagdag ng sobra o saktong kulang na pera ang user
            elif inserted_money >= 50 :
                sukli = inserted_money - 50
                change.insert("1.0",(f"change: {sukli}"))
                output.insert("2.0", "\n\n Enjoy your \n product!", )
                inserted_money = 0 #nakuha na ang pera

        moneydisplay.delete(0,100) #na-delete ang hulugan ng pera
    except:
            output.insert("2.0","Error")

        #moneyin = pera na hinuhulog
        #moneydisplay = doon tinatype yung pera
#---------------------------------------------- INTERFACE ----------------------------------------------
f1 = Frame(relief= RAISED, bd = 20, bg= "#EF3F78") 
f1.grid(row=1, column=0, padx= 10, pady=10)

f2 = Frame(f1,relief= FLAT, bd = 10, bg = "#73CFC4")
f2.grid (row=1, column=0, padx= 10, pady=10)

f3 = Frame(f2,relief= FLAT, bd = 10, bg = "#5EA6A4")
f3.grid (row=0, column=2, padx= 5, pady=5, rowspan=3)

root = Label(f1, text= "SWEET'S CANDY SHOP", font = "arial 18 bold",
            height= 2, width = 70, bg = "#FFEC94", bd = 10, fg = "PURPLE", relief= RIDGE)
root.grid (row=0, column=0, columnspan=3)


#Cost
costarea = Text(f2, width= 18, height= 2, bd = 10, bg = "#222223", font = "arial 15 bold", fg = "white")
costarea.grid(row=2, column=1, padx=10, pady=10)

#Input Money
money = Label (f3, text= "Input your money here",bg= "#ACC1FF", fg = "#222223", width= 20, font= "arial 15 bold", relief= SUNKEN)
money.grid (row=0, column=0,padx = 10, pady= 10)
moneydisplay = Entry(f3, width= 18, bd= 7, font= "arial 15 bold", justify= "center", textvariable=int)
moneydisplay.grid(row = 1, column=0,padx=10, pady=10)

#Change
change = Text(f3, width= 18, height= 2, bd = 10, bg = "#222223", font = "arial 15 bold", fg = "white")
change.grid(row=3, column=0, padx=10, pady=10)

#Candy Output
output = Text(f1, width= 15, height= 11, bd = 10, bg = "#222223", font = "arial 15 bold", fg = "white")
output.grid(row=1, column=1, padx=10, pady=10)

#---------------------------------------------- BUTTONS ----------------------------------------------
#CandyButton
b1 = Button(f2, width= 18, text = "Candy", font= "Arial 15 bold", bd = 10, bg = "#B0E57C", fg= "black", relief= GROOVE , command= candy_button)
b1.grid(row = 0 , column = 0, padx = 10, pady= 10)
#ChipsButton
b2 = Button(f2, width= 18, text = "Chips", font= "Arial 15 bold", bd = 10, bg = "#B0E57C", fg= "black", relief= GROOVE , command= chips_button)
b2.grid(row = 1 , column = 0, padx = 10, pady= 10)
#GumsButton
b3 = Button(f2, width= 18, text = "Gums", font= "Arial 15 bold", bd = 10, bg = "#B0E57C", fg= "black", relief= GROOVE , command= gums_button)
b3.grid(row = 0, column = 1, padx = 10, pady= 10)
#CookiesButton
b4 = Button(f2, width= 18, text = "Cookies", font= "Arial 15 bold", bd = 10, bg = "#B0E57C", fg= "black", relief= GROOVE , command= cookies_button)
b4.grid(row = 1, column = 1, padx = 10, pady= 10)
#ResetButton
b5 = Button(f2, width= 18, text = "Reset", font= "Arial 15 bold", bd = 10, bg = "#ED1C24", fg= "white", relief= GROOVE , command= reset_button)
b5.grid(row = 2, column = 0, padx = 10, pady= 10)
#PushMoneyButton
b5 = Button(f3, width= 18, text = "Push Money",state= "disabled", font= "Arial 15 bold", bd = 10, bg = "#ED1C24", fg= "white", relief= GROOVE, command= pushmoney_button)
b5.grid(row = 2, column = 0, padx = 10, pady= 10)
root.mainloop()