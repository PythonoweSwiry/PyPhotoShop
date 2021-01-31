import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from tkinter import LAST, ROUND
from PIL import ImageTk, Image
from random import randint
import os

filepath = None

#Klasa pierwszego, powitalnego okna
class FirstWindow:
    def __init__(self,first_gui):
        #Ustawienia okna
        self.first_gui = first_gui
        # self.first_gui.geometry("500x300")
        first_gui.title("PyPhotoshop v1.0.0")
        # Dodanie ikony w lewym gornym rogu
        first_gui.wm_iconbitmap(bitmap = r"images\camera.ico")
        self.widget()

    def widget(self):
        #Frame dla canvasa i progressbara
        ProgressFrame = tk.Frame(self.first_gui)
        ProgressFrame.pack()

        canvas = tk.Canvas(ProgressFrame, width = 735, height = 560) #Canvas dla zdjecia w tle
        image = ImageTk.PhotoImage(file = r"images\win1_background.png")
        canvas.create_image(0, 0, image = image, anchor= tk.NW)
        canvas.pack()

        #Progressbar na dole okna
        Progress = ttk.Progressbar(ProgressFrame, orient = tk.HORIZONTAL, length = 500, mode = "determinate")
        Progress.place(x = 100, y = 500)

        #Funkcja do działania progressbaru
        def bar():
            import time
            for i in range(0,100,1):
                Progress["value"] = i
                ProgressFrame.update_idletasks()
                time.sleep(0.02)
            self.NewWindow()
        bar()

    #Komenda do zmieny okna
    def NewWindow(self):
        self.first_gui.destroy() #Usunięcie pierwszego ona
        self.input_gui = tk.Tk() #Stworzenie drugiego okna
        self.app = InputWindow(self.input_gui) #Wywołanie drugiego ona? Nie do końca wiem bo musiałem się wspomóc stackoverflow

#Klasa drugiego okna, z wyborem sciezki pliku
class InputWindow:
    def __init__(self, input_gui):#Ustawienia okna
        self.input_gui = input_gui
        input_gui.wm_iconbitmap(bitmap = r"images\camera.ico")
        input_gui.title("PyPhotoshop v1.0.0")
        input_gui.config(bg ="#252526")
        input_gui.geometry("600x400")
        self.widget()

    def widget(self):#Funkcje z wszytkimi widgetami w oknie
        self.btnState = False #Status przycisku Theme_Button

        def Theme(): #Funkcja do zmiany motywu (Troche dlugie ale sposob z ttk i style nie chcial ze mna wspolpracowac)
            if self.btnState:
                Theme_Button.config(image = night, activebackground="#252526", bg = "#252526")
                NameLabel.config(bg = "#252526", fg = "#eeeee8")
                self.input_gui.config(bg ="#252526")
                InputLabel.config(bg = "#252526", fg = "#eeeee8")
                InputFrame.config(bg = "#252526")
                self.Option_Button_Local.config(bg = "#3f3f40", fg = "#eeeee8")
                self.Option_Button_Cloud.config(bg = "#3f3f40", fg = "#eeeee8")
                self.Option_Button_New.config(bg = "#3f3f40", fg = "#eeeee8")
                self.btnState = False
            else:
                Theme_Button.config(image = day, activebackground="#eeeee8", bg = "#eeeee8")
                NameLabel.configure(bg = "#eeeee8", fg = "#252526")
                self.input_gui.config(bg ="#eeeee8")
                InputLabel.config(bg = "#eeeee8", fg = "#252526")
                InputFrame.config(bg = "#eeeee8")
                self.Option_Button_Local.config(bg = "#d6d6d2", fg = "#252526")
                self.Option_Button_Cloud.config(bg = "#d6d6d2", fg = "#252526")
                self.Option_Button_New.config(bg = "#d6d6d2", fg = "#252526")
                self.btnState = True

        #Funkcje do lekkiej zmiany koloru tła przyciskow podczas najechania kursorem
        def button_hover_local(e):
            self.Option_Button_Local["bg"] = "#5f5f63" if self.btnState else "#b3b3af"

        def button_hover_cloud(e):
            self.Option_Button_Cloud["bg"] = "#5f5f63" if self.btnState else "#b3b3af"

        def button_hover_new(e):
            self.Option_Button_New["bg"] = "#5f5f63" if self.btnState else "#b3b3af"

        def button_hover_leave_local(e):
            self.Option_Button_Local["bg"] = "#d6d6d2" if self.btnState else "#3f3f40"

        def button_hover_leave_cloud(e):
            self.Option_Button_Cloud["bg"] = "#d6d6d2" if self.btnState else "#3f3f40"

        def button_hover_leave_new(e):
            self.Option_Button_New["bg"] = "#d6d6d2" if self.btnState else "#3f3f40"

        with open(r"save\save.txt", "r") as f:
            self.save = [line.strip() for line in f]

        #Obrazy przycisku Theme_Button
        day = tk.PhotoImage(file = r"images\on.png")
        night = tk.PhotoImage(file = r"images\off.png")

        #Przycisk ThemeButton do zmiany motywu
        Theme_Button = tk.Button(self.input_gui, image = night, command = Theme, activebackground="#252526", borderwidth=0, bg = "#252526", cursor="hand2")
        Theme_Button.grid(row = 0, column = 1)

        #Logo aplikacji
        NameLabel = tk.Label(self.input_gui, text = "PyPhotoshop 2020", font = ("Arial 35 "), bg = "#252526", fg = "#eeeee8")
        NameLabel.grid(row = 0, column = 0, padx = 20, pady = 20)

        InputLabel = tk.Label(self.input_gui, text = "Rozpocznij", font = ("Arial 15 "), bg = "#252526", fg = "#eeeee8")
        InputLabel.grid(row = 1, column = 0, padx = (200,50), pady = 8)

        InputFrame = tk.Frame(self.input_gui, bg = "#252526")
        InputFrame.grid(row = 2, column = 0, padx = (200,50))

        #funkcja do wczytania obrazu Input Window - zapamietanie sciezki do wybranego obrazu
        def SelectImageInputWindow():
            global filepath
            types = [("png", "*.png"), ("jpg", "*.jpg"), ("jpeg", "*.jpeg"), ("wszystkie", ["*.jpeg", "*.jpg", "*.png"])]
            filepath = filedialog.askopenfilename( title='Wczytaj obraz', filetypes=types )
            self.NewWindow()

        #Wczytanie obrazow dla przyciskow do wyboru sciezki
        self.local_disc, self.cloud, self.new = tk.PhotoImage(file = r"images\local_disc.png"), tk.PhotoImage(file = r"images\cloud.png"), tk.PhotoImage(file = r"images\new.png")

        self.Option_Button_Local = tk.Button(InputFrame, bg = "#3f3f40", fg = "#eeeee8", text = "Wczytaj plik z dysku lokalnego", command = SelectImageInputWindow, image = self.local_disc, compound = tk.LEFT, width = 200, height = 50, font = "Arial 9 bold", relief = tk.FLAT, borderwidth=0, cursor="hand2")

        self.Option_Button_Cloud = tk.Button(InputFrame, bg = "#3f3f40", fg = "#eeeee8", text = "Wczytaj plik z chmury\nw trakcie realizacji", command = self.NewWindow, image = self.cloud, compound = tk.LEFT, width = 200, height = 50, font = "Arial 9 bold", relief = tk.FLAT, borderwidth=0, cursor="hand2")
        self.Option_Button_Cloud.config(state='disabled')

        self.Option_Button_New = tk.Button(InputFrame, bg = "#3f3f40", fg = "#eeeee8", text = "Nowy", command = self.NewWindow, image = self.new, compound = tk.LEFT, width = 200, height = 50, font = "Arial 9 bold", relief = tk.FLAT, borderwidth=0, cursor="hand2")

        self.Option_Button_Local.pack(pady = 5)
        self.Option_Button_Cloud.pack(pady = 5)
        self.Option_Button_New.pack(pady = 5)

        #Wywołanie funkcji podswietlania przyciskow
        self.Option_Button_Local.bind("<Enter>", button_hover_local)
        self.Option_Button_Cloud.bind("<Enter>", button_hover_cloud)
        self.Option_Button_New.bind("<Enter>", button_hover_new)
        self.Option_Button_Local.bind("<Leave>", button_hover_leave_local)
        self.Option_Button_Cloud.bind("<Leave>", button_hover_leave_cloud)
        self.Option_Button_New.bind("<Leave>", button_hover_leave_new)

    def NewWindow(self):
        self.input_gui.destroy() #Usunięcie pierwszego ona
        self.second_gui = tk.Tk() #Stworzenie drugiego okna
        self.app = SecondWindow(self.second_gui) #Wywołanie drugiego ona? Nie do końca wiem bo musiałem się wspomóc stackoverflow

#Klasa drugiego okna "Głównego"
class SecondWindow:
    def __init__(self, second_gui,):
        #Ustawenia okna
        self.second_gui = second_gui
        self.second_gui.config(bg ="#252526")
        # self.second_gui.geometry("804x589")
        self.second_gui.title("PyPhotoshop v1.0.0")
        # Dodanie ikony w lewym gornym rogu
        self.second_gui.wm_iconbitmap(bitmap = r"images\camera.ico")
        # Dodanie obiektu przechowującego obraz
        self.img = tk.PhotoImage()
        self.widget()

    def widget(self):
        #Funkcje do lewego górnego menu tj. wybór zdjęcia, zapis płótna
        def SelectImageFromInWindow(number): #Funkcja do wczytania obrazu z poziomu inputwindow
            self.pilImage = Image.open(number)
            self.TkImage = ImageTk.PhotoImage( image = self.pilImage )
            self.canvas.create_image(0, 0, anchor="nw" , image = self.TkImage )
            self.canvas.pack()

        #argument domyslny na None, wykorzystamy gdy odwolamy sie tu do zmiennej globalnej filepath (ustawiana jest, gdy wybor obrazu w InputWindow)
        def SelectImage( path=None ):
            if path:
                self.filename = path
            else:
                self.types = [("png", "*.png"), ("jpg", "*.jpg"), ("jpeg", "*.jpeg"), ("wszystkie", ["*.jpeg", "*.jpg", "*.png"])]
                self.filename = filedialog.askopenfilename( title='Wczytaj obraz', filetypes=self.types )
            width, height = self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()
            self.pilImage = Image.open( self.filename )
            if self.pilImage.width > width:
                self.pilImage = self.pilImage.resize( (width, int(self.pilImage.height/self.pilImage.width * width)), Image.ANTIALIAS )
            if self.pilImage.height > height:
                self.pilImage = self.pilImage.resize( (int(self.pilImage.width/self.pilImage.height * height), height), Image.ANTIALIAS )
            self.TkImage = ImageTk.PhotoImage( image = self.pilImage )
            self.canvas.create_image(0, 0, anchor="nw" , image = self.TkImage )
            self.canvas.pack()

        # Wymagania systemowe:
        # 1. instalacja ghostscript dla waszej wersji systemu:       https://www.ghostscript.com/download/gsdnld.html
        # 2. dodanie do ścieżki linijki (tutaj w zależnosci jaką wersję gs macie pobraną):       C:\Program Files\gs\gs9.53.3\bin\
        def SaveCanvas():
            width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
            self.filename = filedialog.asksaveasfilename( title = "Zapisz jako", filetypes = [(".png", "*.png")])
            with open(r"save\save.txt", "a") as f:
                f.write("\n")
                f.write(self.filename)
            self.canvas.postscript( file = self.filename + ".eps" )
            self.img_before = Image.open( self.filename + ".eps" )
            self.img_after = self.img_before.convert( "RGBA" )
            self.img_after = self.img_after.resize( (width, height), Image.ANTIALIAS )
            self.img_after.save( self.filename + ".png", lossless = True)
            self.img_before.close()
            os.remove( self.filename + ".eps" )

        def NewCanvas():
            prompt = messagebox.askyesno(title = "Potwierdź", message = "Przed wyjściem zapisać zmiany?")   #zwraca True False
            if prompt == True:
                SaveCanvas()
            self.canvas.delete("all")

        def TopMenuBar(self):
            # Menu bar (Przycisku na samej górze)
            self.MenuBar = tk.Menu(self.second_gui)#Tworze miejsce do menu bar (Nie trzeba lokalizować bo jest tylko jedna możliwośc lokalizacji)

            self.FileOpctions = tk.Menu(self.MenuBar, tearoff = False) #Tworze menu opcji dla pierwszego przycisku
            self.MenuBar.add_cascade(label = "Opcje", menu = self.FileOpctions)

            self.FileOpctions.add_command(label="Nowy", command=NewCanvas ) #Opcja 1
            self.FileOpctions.add_command(label="Zapisz", command=SaveCanvas ) #Opcja 2
            self.FileOpctions.add_command(label="Wczytaj", command=SelectImage ) #Opcja 3

            self.FileOpctions.add_separator() #Linia oddzielajaca
            self.FileOpctions.add_command(label="Wyjdz", command=self.second_gui.destroy) #Opcja 4

            self.ZoomOpctions = tk.Menu(self.MenuBar, tearoff = False) #Tworze menu opcji dla drugiego przycisku

            self.ZoomOpctions.add_command(label="Przybliż", command=lambda: print("Przybliżono")) #Opcja 1
            self.ZoomOpctions.add_command(label="Oddal", command=lambda: print("Oddalono")) #Opcja 2
            self.ZoomOpctions.add_command(label="Pełen obraz", command=lambda: print("Pełen obraz")) #Opcja 3

            # self.ThemeOpctions = tk.Menu(self.MenuBar, tearoff = False)

            # self.FileOpctions.add_cascade(label = "Ciemny", menu = self.FileOpctions, command = Theme)

            self.MenuBar.add_cascade(label = "Widok", menu = self.ZoomOpctions) #Tworze drugi przycisk i dodaje to co ma wykonać
            # self.MenuBar.add_cascade(label = "Motyw", menu = self.Theme) #Tworze trzeci przycisk i dodaje to co ma wykonać

            self.second_gui.config(menu=self.MenuBar) #Podlaczenie calego menubar do drugiego okna


        TopMenuBar(self) #Wywołuje funkcje odpowiedzialna za MenuBar

        #Stworzenie i ustawienie frame dla widgetow

        self.WidgetBarFrame = tk.Frame(self.second_gui, bg ="#252526")
        self.WidgetBarFrame.pack(pady = 8)

        self.ButtonList = ["Motyw","Wytnij", "Zaznacz", "Zmień rozmiar", "Obróć", "Pędzel","Gumka", "Rozmiar_Pisaka",
                            "Spray", "Edytuj kolory","Kolorowa linia","Kosmos line","Usuń wszystko","Kształty" ]
        self.ColorList = ["white", "yellow", "green", "orange", "blue", "red", "grey80", "violet", "grey", "black"]


        self.ListColorButton = [] #Lista potrzebna do ustawenia pozycji colorbutton
        self.SchapesList = [] #Lista potrzebna do ustawienia pozycji ShapesButton
        self.Button_Theme_List = []

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

        self.btnState = False

        def Theme(): #Funkcja do zmiany motywu (Troche dlugie ale sposob z ttk i style nie chcial ze mna wspolpracowac)
            if self.btnState:
                self.Theme_Button.config(image = self.night, activebackground="#252526", bg = "#252526")
                self.second_gui.config(bg ="#252526")
                self.WidgetBarFrame.config(bg ="#252526")
                self.ListboxFrame.config(bg ="#252526")
                self.ColorFrame.config(bg ="#252526")
                self.SchapesFrame.config(bg ="#252526")
                self.canvas.config(bg ="#3f3f40")
                for button in self.SchapesList:
                    button.config(bg = "#3f3f40", fg = "#eeeee8")
                for button in self.Button_Theme_List:
                    button.config(bg = "#3f3f40", fg = "#eeeee8")
                self.btnState = False
            else:
                self.Theme_Button.config(image = self.day, activebackground="#eeeee8", bg = "#eeeee8")
                self.second_gui.config(bg ="#eeeee8")
                self.WidgetBarFrame.config(bg ="#eeeee8")
                self.ListboxFrame.config(bg ="#eeeee8")
                self.ColorFrame.config(bg ="#eeeee8")
                self.SchapesFrame.config(bg ="#eeeee8")
                self.canvas.config(bg ="#d6d6d2")
                for button in self.SchapesList:
                    button.config(bg = "#d6d6d2", fg = "#252526")
                for button in self.Button_Theme_List:
                    button.config(bg = "#d6d6d2", fg = "#252526")
                self.btnState = True

        #Frame dla list boxa żeby wszytko było w jednej lini
        self.ListboxFrame = tk.Frame(self.WidgetBarFrame, bg ="#252526")
        self.ListboxFrame.pack(side = tk.RIGHT, padx = 3)

        #Frame dla colorbuttons żeby wszytko było w jednej lini
        self.ColorFrame = tk.Frame(self.WidgetBarFrame, bg ="#252526")
        self.ColorFrame.pack(side = tk.RIGHT, padx = 3)

        #Frame dla schapesbuttons żeby wszytko było w jednej lini
        self.SchapesFrame = tk.Frame(self.WidgetBarFrame, bg ="#252526")
        self.SchapesFrame.pack(side = tk.RIGHT, padx = 3)

        self.imglist = [ImageTk.PhotoImage(Image.open(r"images\Prosta.png")), ImageTk.PhotoImage(Image.open(r"images\Krzywa.png")),
        ImageTk.PhotoImage(Image.open(r"images\Elipsa.png")), ImageTk.PhotoImage(Image.open(r"images\Prostokąt.png")),
        ImageTk.PhotoImage(Image.open(r"images\Serce.png")), ImageTk.PhotoImage(Image.open(r"images\Gwiazda.png"))]
        #Lista icon na schapebuttons

        #Tworzenie glownych przyciskow
        def AddButtonBar():
            for bb in self.ButtonList:
                if bb == "Motyw":
                    self.day = tk.PhotoImage(file = r"images\on.png")
                    self.night = tk.PhotoImage(file = r"images\off.png")
                    self.Theme_Button = tk.Button(self.WidgetBarFrame, image = self.night, activebackground="#252526", borderwidth=0, bg = "#252526", cursor="hand2", command = Theme)
                    self.Theme_Button.pack(side = tk.LEFT, padx = 10)
                elif bb == "Kształty":
                    # for img in self.imglist:
                    self.SchapesButton, self.SchapesButton2, self.SchapesButton3, self.SchapesButton4, self.SchapesButton5, self.SchapesButton6 = [tk.Button(self.SchapesFrame, image = img, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")for img in self.imglist]
                    self.SchapesButton.config(command= lambda: self.use_figure(option=2))
                    self.SchapesButton3.config(command= lambda: self.use_figure(option=0))
                    self.SchapesButton4.config(command= lambda: self.use_figure(option=1))
                    self.SchapesList.append(self.SchapesButton)
                    self.SchapesList.append(self.SchapesButton2)
                    self.SchapesList.append(self.SchapesButton3)
                    self.SchapesList.append(self.SchapesButton4)
                    self.SchapesList.append(self.SchapesButton5)
                    self.SchapesList.append(self.SchapesButton6)

                elif bb == "Zaznacz":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.autodraw, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)
                elif bb == "Wytnij":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.cut_rect, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)

                elif bb == "Pędzel":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.use_pen, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)

                elif bb == "Spray":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.use_spray, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)

                elif bb == "Kolorowa linia":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.use_color_line, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)

                elif bb == "Kosmos line":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.use_cosmos, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)

                elif bb == "Usuń wszystko":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.use_clean, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)

                elif bb == "Gumka":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.use_rubber, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)

                elif bb == "Rozmiar_Pisaka":
                    self.BarButtonSize = tk.Spinbox(self.WidgetBarFrame, from_=1, to=10,text = str(bb), width = 7, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButtonSize.pack(side = tk.LEFT, padx = 3, pady = 1)
                    self.Button_Theme_List.append(self.BarButtonSize)

                elif bb == "Edytuj kolory":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.use_color, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)

                else:
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)
            
            self.ColorButton1, self.ColorButton2, self.ColorButton3, self.ColorButton4, self.ColorButton5, self.ColorButton6, self.ColorButton7, self.ColorButton8, self.ColorButton9, self.ColorButton10 = [tk.Button(self.ColorFrame, background=col, cursor="hand2") for col in self.ColorList]
            self.ColorButton = [self.ColorButton1, self.ColorButton2, self.ColorButton3, self.ColorButton4, self.ColorButton5, self.ColorButton6, self.ColorButton7, self.ColorButton8, self.ColorButton9, self.ColorButton10]
            self.ColorButton1.config(command= lambda: self.modify_color(1) ) 
            self.ColorButton2.config(command= lambda: self.modify_color(2) ) 
            self.ColorButton3.config(command= lambda: self.modify_color(3) ) 
            self.ColorButton4.config(command= lambda: self.modify_color(4) )
            self.ColorButton5.config(command= lambda: self.modify_color(5) ) 
            self.ColorButton6.config(command= lambda: self.modify_color(6) )
            self.ColorButton7.config(command= lambda: self.modify_color(7) ) 
            self.ColorButton8.config(command= lambda: self.modify_color(8) )
            self.ColorButton9.config(command= lambda: self.modify_color(9) ) 
            self.ColorButton10.config(command= lambda: self.modify_color(10) )
            [self.ListColorButton.append(ColorButton) for ColorButton in self.ColorButton ]

        AddButtonBar() #Wywołanie funkcji do tworzenia przycisków
        SetColorGrid() #Wywołanie funkcji do pozycjonowania colorbuttons
        SetShapesGrid() #Wywołanie funkcji do pozycjonowania shapebuttons

        #Stworzenie i ustawienie canvasa

        self.canvas = tk.Canvas(self.second_gui, width = 855, height = 500, bg = "#252526")
        self.canvas.pack()
        if filepath:
            SelectImage(filepath)

    #FUNKCJA RYSOWANIA - POCZATEK - aktywacja przycisku ,,Pędzel"

    DEFAULT_PEN_SIZE = 5.0 #Tutaj można wstawić wybór grubości pisaka
    DEFAULT_COLOR = 'black' #Póżniej bd można wstawić tutaj wybór kolorów
    DEFAULT_BACKGROUND_COLOR = 'white'

    #do zmiany koloru pisaka i figur za pomocą przycisków
    def modify_color(self, opt):
        color = self.ColorButton[opt-1].cget('background')   #pobieram kolor tła przycisku
        self.DEFAULT_COLOR = color
        self.color = color


    def setup(self):
        self.old_x, self.old_y = None, None #definicja poczatkowa wspolrzednych
        self.line_width = self.BarButtonSize.get()
        self.color = self.DEFAULT_COLOR #definicja koloru pisaka
        self.background_color = self.DEFAULT_BACKGROUND_COLOR #definicja koloru tła
        self.active_button = self.BarButton
        self.canvas.bind('<B1-Motion>', self.paint) #wybór klawisza myszy <B1-Motion>, <B2-Motion>, <B3-Motion> i wywołanie funkcji PAINT
#         self.canvas.bind("<Button-1>", self.paint)
        #widget.bind(event, handler) the "handler" function is called with an event object. describing the event.
        self.canvas.bind('<ButtonRelease-1>', self.reset)#wyór klawisza myszy<ButtonRelease-1>, <ButtonRelease-2>, and <ButtonRelease-3>.

    def use_pen(self):
        self.canvas.unbind("<Button-1>")    #potrzebne po zaznaczaniu
        self.setup()
        self.activate_button(self.BarButton)

    def use_rubber(self):
        self.setup() #wykonywaie funkcji
        self.activate_button(self.BarButton, eraser_mode=True)

    def use_spray(self):
        self.setup() #wykonywaie funkcji
        self.activate_button(self.BarButton, spray_mode=True)
        self.eraser_on = False

    def use_cosmos(self):
        self.setup() #wykonywaie funkcji
        self.activate_button(self.BarButton, cosmos_mode=True)
        self.eraser_on = False

    def use_color_line(self):
        self.setup() #wykonywaie funkcji
        self.activate_button(self.BarButton, flower_mode=True)
        self.eraser_on = False

    def use_color(self): #wczytane kolorów i zmiana kolory pisaka
        self.setup() #wykonywaie funkcji
        self.color = colorchooser.askcolor(color=self.color)[1]

    def activate_button(self, some_button, eraser_mode=False, draw_mode=False, spray_mode = False, flower_mode = False, cosmos_mode = False ):
        self.active_button.config(relief=tk.RAISED) #relief - styl widżetu (FLAT, RAISED, SUNKEN, GROOVE, RIDGE)
        some_button.config(relief=tk.SUNKEN) #definicja pozostalych przyciskow
        self.active_button = some_button
        self.eraser_on = eraser_mode
        self.draw_on = draw_mode
        self.spray_on = spray_mode
        self.flower_line_on = flower_mode
        self.cosmos_on = cosmos_mode

    def paint(self, event): #rysowanie linii
        self.line_width = self.BarButtonSize.get()
        self.canvas.config(cursor="pencil")
        if self.eraser_on and self.btnState:
            paint_color = "#d6d6d2"  #definicja koloru przy jasnym motywne tła
        elif self.eraser_on and  not self.btnState:
            paint_color = "#252526"
        else:
            paint_color = self.color
        if self.old_x and self.old_y:
            if self.spray_on:
                self.toolsThickness = 2
                multiplier = 8
                xrand = randint(-self.toolsThickness * multiplier,
                                 +self.toolsThickness * multiplier)
                yrand = randint(-self.toolsThickness * multiplier,
                                 +self.toolsThickness * multiplier)

                self.canvas.create_oval(event.x + xrand, event.y + yrand,
                                        event.x + xrand + self.toolsThickness, event.y + yrand + self.toolsThickness,
                                        fill=paint_color, outline = paint_color, width=self.line_width)
            elif self.cosmos_on:
                self.toolsThickness = 4
                multiplier = 6
                xrand = randint(-self.toolsThickness * multiplier,
                                 +self.toolsThickness * multiplier)
                yrand = randint(-self.toolsThickness * multiplier,
                                 +self.toolsThickness * multiplier)
                tk_rgb = "#%02x%02x%02x" % (randint(5,255), randint(10,150), randint(13,255))
                self.canvas.create_oval(event.x + xrand, event.y + yrand,
                                        event.x + self.toolsThickness, event.y + self.toolsThickness,
                                        fill=tk_rgb, outline = tk_rgb, width=self.line_width)

            elif self.flower_line_on:
                tk_rgb = "#%02x%02x%02x" % (randint(140,255), randint(20,225), randint(5,255))

                self.canvas.create_line(self.old_x , self.old_y,
                                        event.x, event.y,
                                         width=self.line_width, fill = tk_rgb)
            else:
                self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,width=self.line_width,
                                   fill=paint_color, capstyle=ROUND, smooth = True)

        #ROUND - zokraglone brzegi, SMOOTT - true - spine false - łamana
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None
##FUNKCJA RYSOWANIA - koniec

    def use_figure(self, option):
        #self.canvas.unbind("<Button-1>")      
        #self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')
        self.opt = option
        self.shapes = [self.canvas.create_oval, self.canvas.create_rectangle, self.canvas.create_line]
        self.shape = self.shapes[option]
        self.canvas.bind('<Button-1>', self.start_draw)
        self.canvas.bind('<B1-Motion>',   self.end_draw)
    def start_draw(self, event):
        self.start_figure = event
        self.drawn = None
    def end_draw(self, event):
        self.canvas = event.widget
        if self.drawn: self.canvas.delete(self.drawn)
        tk_rgb = self.DEFAULT_COLOR              #  "#%02x%02x%02x" % (randint(5,255), randint(10,150), randint(13,255))
        objectId = self.shape(self.start_figure.x, self.start_figure.y, event.x, event.y, width=4)
        if self.opt == 2:
            self.canvas.itemconfig(objectId, fill=tk_rgb)
        else:
            self.canvas.itemconfig(objectId, outline=tk_rgb)
        self.drawn = objectId

    def use_clean(self):
        self.canvas.delete('all')

###ZAZNACZANIE - początek
    # rysowanie prostokąta
    def draw(self, start, end, **kwargs):
        return self.canvas.create_rectangle(*(list(start)+list(end)), **kwargs)

    # rysowanie za pomocą przycisków myszy
    def autodraw(self):
        self.start = None
        self.item = None
        self.canvas.bind("<Button-1>", self.__update)
        self.canvas.bind("<B1-Motion>", self.__update)
        self.canvas.bind("<ButtonRelease-1>", self.__stop)

        self.rectopts = {"outline" : "black", "width" : 1, "dash" : [2,3]}

    # aktualizacja prosokąta - żeby na bieżąco widzieć zmianę
    def __update(self, event):
        if not self.start:
            self.start = [event.x, event.y]
            return

        if self.item is not None:
            self.canvas.delete(self.item)
        self.item = self.draw(self.start, (event.x, event.y), **self.rectopts)

    # oderwanie kursora od płótna - zmiana wydarzeń dołączonych do przycisków (teraz będzie można poruszyć prostokątem)
    def __stop(self, event):
        self.canvas.itemconfig(self.item, outline="blue", dash=(2,2), fill='')
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<Button-1>", self.__check)

    # sprawdzenie czy kliknięto na wnętrze prostokąta czy poza nim - jeśli wnętrze to będzie można ruszać prostokątem
    def __check(self, event):
        self.coords = self.canvas.coords(self.item)
        if not self.coords:
            self.canvas.unbind("<Button-1>")
            self.canvas.bind("<Button-1>", self.__update)
            return

        xlow = min(self.coords[0], self.coords[2])
        xhigh = max(self.coords[0], self.coords[2])
        ylow = min(self.coords[1], self.coords[3])
        yhigh = max(self.coords[1], self.coords[3])

        if (event.x < xlow or event.x > xhigh) or (event.y < ylow or event.y > yhigh):
            self.start = None
            self.canvas.delete(self.item)
            self.canvas.unbind("<Button-1>")
            self.canvas.bind("<Button-1>", self.__update)
            return
        else:
            self.initial = [event.x, event.y]
            self.canvas.unbind("<B1-Motion>")
            self.canvas.bind("<B1-Motion>", self.__move)
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.bind("<ButtonRelease-1>", self.__restart)
            return

    # poruszanie prostokątem
    def __move(self,event):
        diff_x, diff_y = event.x - self.initial[0], event.y - self.initial[1]
        self.canvas.move(self.item, diff_x, diff_y )
        self.initial = [event.x, event.y]

    # kliknięto poza prostokątem, zatem rysowanie nowego (czyli powrót do początkowych ustawień)
    def __restart(self, event):
        self.start = None
        self.canvas.unbind("<B1-Motion>")
        self.canvas.bind("<B1-Motion>", self.__update)
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<ButtonRelease-1>", self.__stop)
###ZAZNACZANIE - koniec

    def cut_rect(self):
        coords = self.canvas.coords(self.item)
        if self.btnState:
            self.draw([coords[0], coords[1]], [coords[2], coords[3]] , fill = "#d6d6d2", outline = "#d6d6d2")
        else:
            self.draw([coords[0], coords[1]], [coords[2], coords[3]], fill = "#252526", outline = "#252526")

### Aplikacja tutaj startuje
if __name__ == '__main__':
    root = tk.Tk()
    app = FirstWindow(root)
    root.mainloop()
###