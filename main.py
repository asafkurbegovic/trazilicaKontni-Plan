import pandas as panda
import tkinter

kontniPlan = panda.read_csv('C:/Users/asafk/PycharmProjects/Trazilica/KontniPlan.csv')
df= panda.DataFrame(kontniPlan)
df = df[['Konto', 'Naziv']]


gui = tkinter.Tk()
gui.geometry('500x500')
gui.title('Trazilica za kontni paln - MILAGROS')

tkinter.Label(gui, text = 'Unesite naziv konta - (mala slova)').pack()

entry = tkinter.Entry(gui)
entry.pack()



resutlLable = tkinter.Label(gui)

def getEntry():
    text = entry.get()
    resutlLable.config(text=(df[df['Naziv'].str.lower().str.contains(text)]))


tkinter.Button(gui, text= 'TRAZI', width=15, command=getEntry ).pack()

gui.bind('<Return>', (lambda event:getEntry()))
resutlLable.pack()



gui.mainloop()