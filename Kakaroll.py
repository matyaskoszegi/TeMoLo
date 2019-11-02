# App von Mátyás Kőszegi, entwickelt für DLL Modul 3

from tkinter import *
from tkinter import messagebox
import random

main = Tk()
main.title("Reihenfolge der Satzglieder - App von Mátyás Kőszegi")
main.geometry('800x600')

text = Label(main, text="Bilden Sie Sätze. Achten Sie auf die Reihenfolge der Elemente.", font = ('Garamond', 20))
text.place(x=40,y=30)
text2 = Label(main, text="Ich möchte", font = ('Garamond', 18))
text2.place(x=10, y=200)

Temporal = Entry(main)
Temporal.place(x=150,y=210)
Modal = Entry(main)
Modal.place(x=350,y=210)
Lokal = Entry(main)
Lokal.place(x=550,y=210)

text3 = Label(main, text="fahren.", font = ('Garamond', 18))
text3.place(x=700,y=200)

ZeitListe=['am Montag','morgen','jeden Abend','um 15 Uhr','heute','in zwei Wochen','in der Früh','am Wochenende','einmal pro Tag','nie','oft','manchmal','jedes Jahr','im Jahr 2025','in der Nacht']
ModalListe=['sehr schnell','mit Mama','ohne dich','mit dem Zug','mit dir','zu Fuß','mit meiner Familie','langsam','ruhig']
OrtListe=['nach London','ans Meer','zum Bäcker','auf eine Insel','in die Stadt','nach Deutschland','nach Hause','zum Park','in die Schweiz','zur Uni','in die Alpen','in den Wald']

Zeit = Label(main, text=random.choice(ZeitListe), font = ('Garamond', 18))
Zeit.place(x=150,y=480)
Methode = Label(main, text=random.choice(ModalListe), font = ('Garamond', 18))
Methode.place(x=350, y=480)
Ort = Label(main, text=random.choice(OrtListe), font = ('Garamond', 18))
Ort.place(x=550, y=480)

def NeueWoerter():
    Zeit.configure(text=random.choice(ZeitListe), font = ('Garamond', 18))
    Zeit.place(x=550, y=480)
    Methode.configure(text=random.choice(ModalListe), font=('Garamond', 18))
    Methode.place(x=350, y=480)
    Ort.configure(text=random.choice(OrtListe), font=('Garamond', 18))
    Ort.place(x=150, y=480)

def Loeschen():
    Zeit.place_forget()
    Methode.place_forget()
    Ort.place_forget()

def Ueber():
    if Temporal.get() in ZeitListe and Modal.get() in ModalListe and Lokal.get() in OrtListe:
        messagebox.showinfo("Antwort","Richtig!")
    else:
        messagebox.showinfo("Antwort", "Leider falsch.")

def Beenden():
    main.destroy()

button = Button(main, text='Überprüfen', width=25, command=Ueber)
button.place(x=300,y=300)

button2 = Button(main, text='Wörter löschen', width=25, command=Loeschen)
button2.place(x=300,y=340),

button3 = Button(main, text='Neue Wörter', width=25, command=NeueWoerter)
button3.place(x=300,y=380)

button4 = Button(main, text='Beenden', width =25, command=Beenden)
button4.place(x=300, y=420)


main.mainloop()
