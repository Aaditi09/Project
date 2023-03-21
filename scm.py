#pip install tkinter
import tkinter as tk 
from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk
#GUI
root = tk.Tk()
 
root.title("Currency converter:ALGORITHM UNLOCK")
 
Tops = Frame(root, bg = '#0A0A0A', pady=4, width=2500, height=2000, relief="ridge")
Tops.grid(row=0, column=0)
 
headlabel = tk.Label(Tops, font=('pink', 15, 'bold'), text='                         Welcome to Real Time Currency Converter',
                    bg='#0A0A0A', fg='pink')
headlabel.grid(row=1, column=0, sticky=W)
headlabel = tk.Label(Tops, font=('yellow', 15, 'bold'), text='                                    Team Algorithm Unlock',bg='#0A0A0A', fg='yellow')
headlabel.grid(row=2, column=0, sticky=W)


 
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
 
variable1.set("currency")
variable2.set("currency")
#image


#Function To For Real Time Currency Conversion
 
def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()
 
    from_currency = variable1.get()
    to_currency = variable2.get()
 
    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")
 
    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency form menu.")
 
    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))
 
#clearing all the data entered by the user
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)
 
 
CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR","NEP"]
 
root.configure(background='#0A0A0A')
root.geometry("700x400")
 
Label_1 = Label(root, font=('yellow', 27, 'bold'), text="", padx=2, pady=2, bg="#0A0A0A", fg="yellow")
Label_1.grid(row=1, column=0, sticky=W)
 
label1 = tk.Label(root, font=('light blue', 15, 'bold'), text="\t    Amount  :  ", bg="#0A0A0A", fg="light blue")
label1.grid(row=2, column=0, sticky=W)
 
label1 = tk.Label(root, font=('light blue', 15, 'bold'), text="\t    From Currency  :  ", bg="#0A0A0A", fg="light blue")
label1.grid(row=3, column=0, sticky=W)
 
label1 = tk.Label(root, font=('light blue', 15, 'bold'), text="\t    To Currency  :  ", bg="#0A0A0A", fg="light blue")
label1.grid(row=4, column=0, sticky=W)
 
label1 = tk.Label(root, font=('light blue', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#0A0A0A", fg="light blue")
label1.grid(row=8, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#0A0A0A", fg="black")
Label_1.grid(row=5, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#0A0A0A", fg="black")
Label_1.grid(row=7, column=0, sticky=W)
 
FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)
 
FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)
 
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)
 
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="light blue", fg="black",
                 command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="black",
                 command=clear_all)
Label_9.grid(row=10, column=0)
 
 
root.mainloop()