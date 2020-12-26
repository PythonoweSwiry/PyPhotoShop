import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

#Klasa pierwszego, powitalnego okna
class FirstWindow:
    def __init__(self,first_gui):
        #Ustawienia okna
        self.first_gui = first_gui
        # self.first_gui.geometry("500x300")
        self.first_gui.title("PyPhotoshop v1.0.0")
        # Dodanie ikony w lewym gornym rogu
        self.first_gui.wm_iconbitmap(bitmap = "camera.ico")

        #Frame dla canvasa i progressbara
        self.ProgressFrame = tk.Frame(self.first_gui)
        self.ProgressFrame.pack()

        self.canvas = tk.Canvas(self.ProgressFrame, width = 735, height = 560) #Canvas dla zdjecia w tle
        self.image = ImageTk.PhotoImage(file = "win1_background.png") 
        self.canvas.create_image(0, 0, image = self.image, anchor= tk.NW) 
        self.canvas.pack()

        #Progressbar na dole okna
        self.Progress = ttk.Progressbar(self.ProgressFrame, orient = tk.HORIZONTAL, length = 500, mode = "determinate")
        self.Progress.place(x = 100, y = 500)

        #Funkcja do działania progressbaru
        def bar(): 
            import time 
            for i in range(0,100,1):
                self.Progress["value"] = i
                self.ProgressFrame.update_idletasks()
                time.sleep(0.02)
            self.NewWindow()
        bar()

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
        # Dodanie obiektu przechowującego obraz
        self.img = tk.PhotoImage()

        #Funkcje do lewego górnego menu tj. wybór zdjęcia, zapis płótna
        def SelectImage():
            self.types = [("png", "*.png"), ("jpg", "*.jpg"), ("jpeg", "*.jpeg"), ("wszystkie", ["*.jpeg", "*.jpg", "*.png"])]
            self.filename = filedialog.askopenfilename( title='Wczytaj obraz', filetypes=self.types )
            self.img.config(file=self.filename)
            self.canvas.create_image(0, 0, anchor='nw', image=self.img )
            self.canvas.pack()

        def SaveCanvas():
            self.filename = filedialog.asksaveasfilename( title = "Zapisz jako",
                                 filetypes = [(".png", "*.png"), (".jpg","*.jpg")])   
            self.canvas.postscript(file = self.filename + ".ps")
            self.im = Image.open(self.filename + ".ps")
            self.im.save(self.filename + ".png", "png")    #tu dodam tez jpg

        def NewCanvas():
            prompt = messagebox.askyesno(title = "Potwierdź", message = "Zapisać zmiany?")   #zwraca True False
            if prompt == True:
                SaveCanvas()
            self.canvas.delete("all")
            self.canvas.config( bg = "red" )

        def TopMenuBar(self):
            # Menu bar (Przycisku na samej górze)
            self.MenuBar = tk.Menu(self.second_gui)#Tworze miejsce do menu bar (Nie trzeba lokalizować bo jest tylko jedna możliwośc lokalizacji)

            self.FileOpctions = tk.Menu(self.MenuBar, tearoff = False) #Tworze menu opcji dla pierwszego przycisku
            self.FileOpctions.add_command(label="Nowy", command=NewCanvas ) #Opcja 1
            self.FileOpctions.add_command(label="Zapisz", command=SaveCanvas ) #Opcja 2
            self.FileOpctions.add_command(label="Wczytaj", command=SelectImage ) #Opcja 3
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

        self.ButtonList = ["Wklej", "Wytnij", "Kopiuj", "Zaznacz", "Zmień rozmiar", "Obróć", "Pędzel", "Kształty", "Wypełnienie", "Edytuj kolory"]
        self.ColorList = ["white", "olive", "yellow", "green", "orange", "blue", "red", "grey80", "violet", "grey", "purple", "black", "pink", "brown"]
        def color(): #Aktywacja colorchosera
            self.my_color = colorchooser.askcolor()

        self.ListColorButton = [] #Lista potrzebna do ustawenia pozycji colorbutton
        self.SchapesList = [] #Lista potrzebna do ustawienia pozycji ShapesButton

        def SetColorGrid(NewLine = 2): #Ustawienie pozycji colorbuttons
            self.row, self.col = 0,0
            for button in self.ListColorButton:
                button.grid(row = self.row, column = self.col)
                self.row += 1
                if self.row == NewLine:
                    self.col += 1
                    self.row = 0

        def SetShapesGrid(NewLine = 2): #Ustawienie pozycji shapesbutton
            self.row, self.col = 0,0
            for SchapesButton in self.SchapesList:
                SchapesButton.grid(row = self.row, column = self.col, padx = 3, pady = 3)
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

        #Frame dla schapesbuttons żeby wszytko było w jednej lini
        self.SchapesFrame = tk.Frame(self.WidgetBarFrame)
        self.SchapesFrame.pack(side = tk.RIGHT, padx = 3)

        self.licznik = 0 # licznik do pętli, żeby wykonała sie tylko 4 razy
        self.imglist = [ImageTk.PhotoImage(Image.open("Prosta.png")), ImageTk.PhotoImage(Image.open("Krzywa.png")),
        ImageTk.PhotoImage(Image.open("Elipsa.png")), ImageTk.PhotoImage(Image.open("Prostokąt.png")),
        ImageTk.PhotoImage(Image.open("Serce.png")), ImageTk.PhotoImage(Image.open("Gwiazda.png"))]
        #Lista icon na schapebuttons

        #Tworzenie glownych przyciskow
        def AddButtonBar():
            for bb in self.ButtonList:
                if bb == "Kształty":
                    for Schapes in ["Prosta", "Krzywa", "Elipsa", "Prostokąt", "Serce", "Gwiazda"]:
                        for img in self.imglist:
                            self.SchapesButton = tk.Button(self.SchapesFrame, image = img)
                            self.SchapesList.append(self.SchapesButton)
                            self.licznik += 1
                        if self.licznik == 6:
                            break
                else:
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3)
                    self.BarButton.pack(side = tk.LEFT, padx = 3)
                    self.BarButton.config(command = color if bb == "Edytuj kolory" else None)
            for col in self.ColorList:
                self.ColorButton = tk.Button(self.ColorFrame, background = col)
                self.ListColorButton.append(self.ColorButton)
        AddButtonBar() #Wywołanie funkcji do tworzenia przycisków
        SetColorGrid() #Wywołanie funkcji do pozycjonowania colorbuttons
        SetShapesGrid() #Wywołanie funkcji do pozycjonowania shapebuttons
######################

        #Stworzenie i ustawienie canvasa
        self.canvas = tk.Canvas(second_gui, width = 855, height = 500, bg = "red")
        self.canvas.pack()

### Aplikacja tutaj startuje
if __name__ == '__main__':
    root = tk.Tk()
    app = FirstWindow(root)
    root.mainloop()
###

