from tkinter import *
from tkinter import messagebox


def ComputePayment():
    List.delete(0, END)
    rate = rateTxt.get()
    years = yearTxt.get()
    amount = amtTxt.get()

    monthlyrate = float(rate)/12.0
    months = int(years) * 12
    payment = float(amount) * ((monthlyrate * (1+monthlyrate) **
                                months) / ((1 + monthlyrate) ** months - 1))

    balance = float(amount)
    total_interest = 0
    List.insert(END, "Month Payment Principal Interest Balance")
    for month in range(months):
        interest = balance * monthlyrate
        principal = payment - interest
        balance = balance - principal
        total_interest += interest
        List.insert(END, "{payment} {principal} {interest} {balance}".format(
            month=month + 1, payment=payment, principal=principal, interest=interest, balance=balance))

    e4.configure(state='normal')
    e4.delete(0, END)
    e4.insert(0, total_interest)
    e4.configure(state='readonly')

    e5.configure(state='normal')
    e5.delete(0, END)
    e5.insert(0, payment)
    e5.configure(state='readonly')


def Clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    List.delete(0, END)

    e4.configure(state='normal')
    e4.delete(0, END)
    e4.configure(state='readonly')

    e5.configure(state='normal')
    e5.delete(0, END)
    e5.configure(state='readonly')


def Exit():
    if messagebox.askokcancel("Quit", "Are you sure you'd like to quit?"):
        window.destroy()


window = Tk()

yearLabel = Label(window, text="Years")
yearLabel.grid(row=0, column=0)

AmountLabel = Label(window, text="Amount")
AmountLabel.grid(row=1, column=0)

rateLabel = Label(window, text="Rate")
rateLabel.grid(row=2, column=0)

paymentLabel = Label(window, text="Payment")
paymentLabel.grid(row=0, column=2)

totalInterestLabel = Label(window, text="Total Interest Paid")
totalInterestLabel.grid(row=1, column=2)

yearTxt = StringVar()
e1 = Entry(window, textvariable=yearTxt)
e1.grid(row=0, column=1)

amtTxt = StringVar()
e2 = Entry(window, textvariable=amtTxt)
e2.grid(row=1, column=1)

rateTxt = StringVar()
e3 = Entry(window, textvariable=rateTxt)
e3.grid(row=2, column=1)

paymentOutputTxt = StringVar()
e4 = Entry(window, textvariable=paymentOutputTxt, state ='readonly')
e4.grid(row=1, column=3)

totalInterestOutput = StringVar()
e5 = Entry(window, textvariable=totalInterestOutput, state='readonly')
e5.grid(row=0, column=3)

List = Listbox(window, height=10, width=90)
List.grid(row=3, column=0, rowspan=4, columnspan=4)
sb1 = Scrollbar(window)
sb1.grid(row=3, column=3, rowspan=4, sticky=N+S+E)
List.configure(yscrollcommand=sb1.set)
sb1.configure(command=List.yview)

b1 = Button(window, text="Compute", width=20, height=1, command=ComputePayment)
b1.grid(row=3, column=4)
b2 = Button(window, text="Clear", width=20, height=1, command=Clear)
b2.grid(row=4, column=4)
b3 = Button(window, text="Exit", width=20, height=1, command=Exit)
b3.grid(row=5, column=4)

window.mainloop()
