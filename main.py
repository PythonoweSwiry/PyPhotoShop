import tkinter as tk

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

        self.ButtonList = ["Wklej", "Wytnij", "Kopiuj", "Zaznacz", "Zmień rozmiar", "Obróć", "Pędziel", "Kształty", "Wypełnienie", "Kolory", "Edytuj kolory"]

        #Tworzenie glownych przyciskow
        for bb in self.ButtonList:
            if bb == "Kształty" or bb == "Kolory":
                self.ShapesList = ["Koło", "Prostokąt", "Dupa"]
                self.ColorList = ["Czerwony", "Zielony", "Niebieski"]
                self.BarListbox = tk.Listbox(self.second_gui)
                self.BarListbox.insert(1, self.ShapesList if bb == "Kształty" else self.ColorList)
                self.BarListbox.pack()
            else:
                self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3)
                self.BarButton.pack(side = tk.LEFT, padx = 3)

        #Stworzenie i ustawienie canvasa
        self.canvas = tk.Canvas(second_gui, width = 855, height = 500, bg = "red")
        self.canvas.pack()
        
### Nie jestem pewien co to jest bo jak już pisałem musaiłem się wpomóc stackiem ale prawdopodobnie w tym miejscu aplikacja startuje 
def main():
    root = tk.Tk()
    app = FirstWindow(root)
    root.mainloop()
###

###Wywołuje funkcje main ale po co i jak to działa to nie wiem, jak to usunąłem to program nie chciał ruszyć 
if __name__ == '__main__':
    main()
###

