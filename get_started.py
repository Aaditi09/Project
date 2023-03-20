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
 
headlabel = tk.Label(Tops, font=('pink', 15, 'bold'), text=' Welcome to Real Time Currency Converter',
                    bg='#0A0A0A', fg='pink')
headlabel.grid(row=1, column=0, sticky=W)
headlabel = tk.Label(Tops, font=('yellow', 15, 'bold'), text='Team Algorithm Unlock',bg='#0A0A0A', fg='yellow')
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
