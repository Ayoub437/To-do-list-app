from tkinter import *
from tkinter import ttk


class todo:
    def __init__(self, root):  # root ist ein Objekt.
        # Hier setze ich die Geometrie meiner Applikation ein.
        self.root = root
        self.root.title("To-do-list")  # Hier spezifiziere ich den Titel.
        self.root.geometry(
            "650x410+300+150"
        )  # width and height of the window. 650 ist die Breite. 410 ist die Höhe. 300+150 sind die Positionswerte.

        # Hier erstelle ich mein Label. Ich benutze das label-widget in tkinter. Hier schreibe ich mein UI mit html.
        self.label = Label(
            self.root,
            text="To-Do-List-App",
            font="ariel, 25 bold",
            width=10,
            bd=5,
            bg="orange",
            fg="black",
        )  # "fg" steht füt Foreground/Vordergrund.
        self.label.pack(
            side="top", fill=BOTH
        )  # fill=BOTH sorgt dafür, dass der Navbar rechts und links getroffen wird. side="top" -> Navbar ist oben.
        # pack -> verpacken.
        self.label2 = Label(
            self.root,
            text="Add Task",
            font="ariel, 15 bold",
            width=10,
            bd=5,
            bg="orange",
            fg="black",
        )  # bd=1 -> ist die Größe des orangenen Backgrounds.
        self.label2.place(
            x=40, y=54
        )  # place -> ist ein gui management. # place(x=80, y=54) -> Höhe und Breite.

        self.label3 = Label(
            self.root,
            text="Tasks",
            font="ariel, 18 bold",
            width=10,
            bd=5,
            bg="orange",
            fg="black",
        )
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(
            self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold"
        )
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2,
                         width=30, font="ariel, 10 bold")
        self.text.place(
            x=20, y=120
        )  # Label ist ein Text der nicht clickable ist = Etikett.

        # =======================Add task==========================#
        # Hier kommen meine Funktionalitäten.

        # Hier möchte ich die Inhalte von "Add Task" auf dem "Listbox" also "Task" rüberbringen.
        # Ich bekomme also den Inhalt von der Listbox und dann füge ich das in meiner Listbox ein.

    def add(self):
        content = self.text.get(
            1.0, END
        )  # (1.0, END) -> 1.0 ist der Index gemeint. D.h. der Textinhalt vom Anfang bis zum Ende.
        self.main_text.insert(END, content)

        # main_text -> ist die Variable für die Listbox.
        with open(  # with -> ist ein Statement und gut mit Umgang von Dateien.
            "data.txt", "a"
        ) as file:  # Hier öffne ich eine Datei und speichere die Daten aus meinem Text Box. "a" steht für append = anhängen.
            file.write(content)
        self.text.delete(1.0, END)

    def delete(self):
        delete_index = self.main_text.curselection()
        look = self.main_text.get(delete_index)
        with open("data.txt", "r+") as f:  # "r+" für read.
            new_f = f.readlines()

            # Zeile: 46-52 -> Diese Zeile löscht es in meinem Text-Datei. Das ist eine Variable um jede Zeile zu lesen. Hier lese ich jede Zeile in meinem txt.Datei.
            f.seek(0)
            for line in new_f:
                item = str(look)
                if item not in line:
                    f.write(line)
            f.truncate()  # f.truncate() call should be outside the for loop. Otherwise, you might end up truncating the file multiple times unnecessarily.a
            # Das löscht den Inhalt in meiner Listbox.
            self.main_text.delete(delete_index)

        with open("data.txt", "r") as file:
            read = file.readlines()
            for i in read:
                ready = (
                    i.split()
                )  # split() -> ist eine Funktion. Jede Zeile wird auf eine seperate Zeile in meiner Listbox gebracht.
                self.main_text.insert(END, ready)
            file.close()

        # Buttons für deleting und adding.
        self.button = Button(
            self.root,
            text="Add",
            font="sarif, 20 bold italic",
            width=10,
            bd=5,
            bg="orange",
            fg="black",
            command=add,
        )  # command=add -> läuft.
        self.button.place(x=30, y=180)

        self.button2 = Button(
            self.root,
            text="Delete",
            font="sarif, 20 bold italic",
            width=10,
            bd=5,
            bg="orange",
            fg="black",
            command=delete,
        )
        self.button2.place(x=30, y=280)


def main():  # That function runs my main window.
    root = Tk()
    ui = todo(root)
    root.mainloop()


if __name__ == "__main__":  # Through that my windows run.
    main()

# Quelle des Codes: https://www.youtube.com/watch?v=mmpVsw8aXi4
