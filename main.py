import tkinter as tk
from tkinter import colorchooser

#Klasa pierwszego, powitalnego okna
class FirstWindow:
    def __init__(self,first_gui):
        #Ustawienia okna
        self.first_gui = first_gui
        self.first_gui.geometry("500x300")
        self.first_gui.title("PyPhotoshop v1.0.0")
        # Dodanie ikony w lewym gornym rogu
        self.first_gui.wm_iconbitmap(bitmap = "camera.ico")

        #Stworzenie i ustawienie frame, label i button 
        self.HelloFrame = tk.Frame(self.first_gui)
        self.HelloFrame.pack(padx = 10, pady = 10)

        self.LabelHello = tk.Label(self.HelloFrame, text = "Witaj! Załącz plik do edycji", font = ("Arial", 20))
        self.LabelHello.grid(row = 1, column = 1, pady = 40)

        self.ButtonHello = tk.Button(self.HelloFrame, text = "Załącz", height = 3, width = 10, font = 10, command = self.NewWindow)
        self.ButtonHello.grid(row = 5, column = 1, pady = 40)

    #Komenda do zmieny okna
    def NewWindow(self):
            self.first_gui.destroy() #Usunięcie pierwszego ona
            self.second_gui = tk.Tk() #Stworzenie drugiego okna
            self.app = SecondWindow(self.second_gui) #Wywołanie drugiego ona? Nie do końca wiem bo musiałem się wspomóc stackoverflow
            self.second_gui.mainloop()

#Klasa drugiego okna "Głównego"
class SecondWindow:
    def __init__(self, second_gui):
        #Ustawenia okna
        self.second_gui = second_gui
        # self.second_gui.geometry("804x589")
        self.second_gui.title("PyPhotoshop v1.0.0")
        # Dodanie ikony w lewym gornym rogu
        self.second_gui.wm_iconbitmap(bitmap = "camera.ico")

        def TopMenuBar(self):
            # Menu bar (Przycisku na samej górze)
            self.MenuBar = tk.Menu(self.second_gui)#Tworze miejsce do menu bar (Nie trzeba lokalizować bo jest tylko jedna możliwośc lokalizacji)

            self.FileOpctions = tk.Menu(self.MenuBar, tearoff = False) #Tworze menu opcji dla pierwszego przycisku
            self.FileOpctions.add_command(label="Nowy", command=lambda: print("Nowy plik")) #Opcja 1
            self.FileOpctions.add_command(label="Zapisz", command=lambda: print("Zapisano")) #Opcja 2
            self.FileOpctions.add_command(label="Wczytaj", command=lambda: print("Wczytano")) #Opcja 3 
            self.FileOpctions.add_separator() #Linia oddzielajaca 
            self.FileOpctions.add_command(label="Wyjdz", command=self.second_gui.destroy) #Opcja 4

            self.ZoomOpctions = tk.Menu(self.MenuBar, tearoff = False) #Tworze menu opcji dla drugiego przycisku

            self.ZoomOpctions.add_command(label="Przybliż", command=lambda: print("Przybliżono")) #Opcja 1
            self.ZoomOpctions.add_command(label="Oddal", command=lambda: print("Oddalono")) #Opcja 2
            self.ZoomOpctions.add_command(label="Pełen obraz", command=lambda: print("Pełen obraz")) #Opcja 3

            self.MenuBar.add_cascade(label = "Opcje", menu = self.FileOpctions) #Tworze pierwszy przycisk i dodaje to co ma wykonać 
            self.MenuBar.add_cascade(label = "Widok", menu = self.ZoomOpctions) #Tworze drugi przycisk i dodaje to co ma wykonać 

            self.second_gui.config(menu=self.MenuBar) #Podlaczenie calego menubar do drugiego okna

        TopMenuBar(self) #Wywołuje funkcje odpowiedzialna za MenuBar

        #Stworzenie i ustawienie frame dla widgetow 

        self.WidgetBarFrame = tk.Frame(self.second_gui)
        self.WidgetBarFrame.pack()

###################### IN-PROGRESS (szukam sposobu zeby to ustawic podobnie jak jest w paincie)

        self.ButtonList = ["Wklej", "Wytnij", "Kopiuj", "Zaznacz", "Zmień rozmiar", "Obróć", "Pędziel", "Kształty", "Wypełnienie", "Edytuj kolory"]
        self.ColorList = ["black", "grey", "red", "orange", "yellow", "green", "blue", "violet", "white", "grey80"]

        def color(): #Aktywacja colorchosera
            self.my_color = colorchooser.askcolor()

        self.ListColorButton = [] #Lista potrzebna do ustawenia pozycji colorbutton

        def SetColorGrid(NewLine = 2): #Ustawienie pozycji colorbuttons
            self.row, self.col = 0,0
            for button in self.ListColorButton:
                button.grid(row = self.row, column = self.col)
                self.row += 1
                if self.row == NewLine:
                    self.col += 1
                    self.row = 0

        #Frame dla list boxa żeby wszytko było w jednej lini
        self.ListboxFrame = tk.Frame(self.WidgetBarFrame)
        self.ListboxFrame.pack(side = tk.RIGHT, padx = 3)

        #Frame dla colorbuttons żeby wszytko było w jednej lini
        self.ColorFrame = tk.Frame(self.WidgetBarFrame)
        self.ColorFrame.pack(side = tk.RIGHT, padx = 3)

        #Tworzenie glownych przyciskow
        def AddButtonBar():
            for bb in self.ButtonList:
                if bb == "Kształty":
                    self.ShapesList = ["Koło", "Prostokąt", "Dupa"]
                    self.BarListbox = tk.Listbox(self.ListboxFrame, height=3)
                    self.BarListbox.insert(1, self.ShapesList)
                    self.BarListbox.pack()
                else:
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3)
                    self.BarButton.pack(side = tk.LEFT, padx = 3)
                    self.BarButton.config(command = color if bb == "Edytuj kolory" else None)
            for col in self.ColorList:
                self.ColorButton = tk.Button(self.ColorFrame, background = col)
                self.ListColorButton.append(self.ColorButton)
        AddButtonBar() #Wywołanie funkcji do tworzenia przycisków 
        SetColorGrid() #Wywołanie funkcji do pozycjonowania colorbuttons

######################

        #Stworzenie i ustawienie canvasa
        self.canvas = tk.Canvas(second_gui, width = 855, height = 500, bg = "red")
        self.canvas.pack()
        
### Nie jestem pewien co to jest bo jak już pisałem musaiłem się wpomóc stackiem ale prawdopodobnie w tym miejscu aplikacja startuje 
if __name__ == '__main__':
    root = tk.Tk()
    app = FirstWindow(root)
    root.mainloop()
###


