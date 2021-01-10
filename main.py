import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import os

#Klasa pierwszego, powitalnego okna
class FirstWindow:
    def __init__(self,first_gui):
        #Ustawienia okna
        self.first_gui = first_gui
        # self.first_gui.geometry("500x300")
        self.first_gui.title("PyPhotoshop v1.0.0")
        # Dodanie ikony w lewym gornym rogu
        self.first_gui.wm_iconbitmap(bitmap = r"images\camera.ico")
        self.widget()

    def widget(self):
        #Frame dla canvasa i progressbara
        self.ProgressFrame = tk.Frame(self.first_gui)
        self.ProgressFrame.pack()

        self.canvas = tk.Canvas(self.ProgressFrame, width = 735, height = 560) #Canvas dla zdjecia w tle
        self.image = ImageTk.PhotoImage(file = r"images\win1_background.png")
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
            self.input_gui = tk.Tk() #Stworzenie drugiego okna
            self.app = InputWindow(self.input_gui) #Wywołanie drugiego ona? Nie do końca wiem bo musiałem się wspomóc stackoverflow

#Klasa drugiego okna, z wyborem sciezki pliku
class InputWindow:
    def __init__(self, input_gui):#Ustawienia okna
        self.input_gui = input_gui
        self.input_gui.wm_iconbitmap(bitmap = r"images\camera.ico")
        self.input_gui.title("PyPhotoshop v1.0.0")
        self.input_gui.config(bg ="#252526")
        self.widget()

    def widget(self):#Funkcje z wszytkimi widgetami w oknie
        self.btnState = False #Status przycisku Theme_Button

        def Theme(): #Funkcja do zmiany motywu (Troche dlugie ale sposob z ttk i style nie chcial ze mna wspolpracowac)
            if self.btnState:
                self.Theme_Button.config(image = self.night, activebackground="#252526", bg = "#252526")
                self.NameLabel.config(bg = "#252526", fg = "#eeeee8")
                self.input_gui.config(bg ="#252526")
                self.InfoLabel.config(bg = "#252526", fg = "#eeeee8")
                self.InputLabel.config(bg = "#252526", fg = "#eeeee8")
                self.InputFrame.config(bg = "#252526")
                self.Option_Button_Local.config(bg = "#3f3f40", fg = "#eeeee8")
                self.Option_Button_Cloud.config(bg = "#3f3f40", fg = "#eeeee8")
                self.Option_Button_New.config(bg = "#3f3f40", fg = "#eeeee8")
                self.btnState = False
            else:
                self.Theme_Button.config(image = self.day, activebackground="#eeeee8", bg = "#eeeee8")
                self.NameLabel.configure(bg = "#eeeee8", fg = "#252526")
                self.input_gui.config(bg ="#eeeee8")
                self.InfoLabel.config(bg = "#eeeee8", fg = "#252526")
                self.InputLabel.config(bg = "#eeeee8", fg = "#252526")
                self.InputFrame.config(bg = "#eeeee8")
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
        self.day = tk.PhotoImage(file = r"images\on.png")
        self.night = tk.PhotoImage(file = r"images\off.png")

        #Przycisk ThemeButton do zmiany motywu
        self.Theme_Button = tk.Button(self.input_gui, image = self.night, command = Theme, activebackground="#252526", borderwidth=0, bg = "#252526", cursor="hand2")
        self.Theme_Button.grid(row = 0, column = 1)

        #Logo aplikacji
        self.NameLabel = tk.Label(self.input_gui, text = "PyPhotoshop 2020", font = ("Arial 35 "), bg = "#252526", fg = "#eeeee8")
        self.NameLabel.grid(row = 0, column = 0, padx = 20, pady = 20)

        #Na to mam pomysl ale musze to dopracowac
        self.InfoLabel = tk.Label(self.input_gui, text = "Otwórz ostatnio używane", font = ("Arial", 15), bg = "#252526", fg = "#eeeee8")
        self.InfoLabel.grid(row = 1, column = 0, pady = 8)

        self.LastSave = tk.Frame(self.input_gui, bg = "#252526")
        self.LastSave.grid(row = 2, column = 0, padx = 20)

        self.SaveButton1 = tk.Button(self.LastSave, bg = "#3f3f40", fg = "#eeeee8", text = "Ostatni", command = self.NewWindow, width = 30
        , height = 3, font = "Arial 9 bold", relief = tk.FLAT, borderwidth=0, cursor="hand2")

        self.SaveButton2 = tk.Button(self.LastSave, bg = "#3f3f40", fg = "#eeeee8", text = "Przeostatni", command = self.NewWindow, width = 30, height = 3, font = "Arial 9 bold", relief = tk.FLAT, borderwidth=0, cursor="hand2")

        self.SaveButton3 = tk.Button(self.LastSave, bg = "#3f3f40", fg = "#eeeee8", text = "Przedprzedostatni", command = self.NewWindow, width = 30, height = 3, font = "Arial 9 bold", relief = tk.FLAT, borderwidth=0, cursor="hand2")

        self.SaveButton1.pack(pady = 5)
        self.SaveButton2.pack(pady = 5)
        self.SaveButton3.pack(pady = 5)

        self.InputLabel = tk.Label(self.input_gui, text = "Rozpocznij", font = ("Arial 15 "), bg = "#252526", fg = "#eeeee8")
        self.InputLabel.grid(row = 1, column = 1, padx = 5, pady = 8)

        self.InputFrame = tk.Frame(self.input_gui, bg = "#252526")
        self.InputFrame.grid(row = 2, column = 1, padx = 20)

        #Wczytanie obrazow dla przyciskow do wyboru sciezki
        self.local_disc, self.cloud, self.new = tk.PhotoImage(file = r"images\local_disc.png"), tk.PhotoImage(file = r"images\cloud.png"), tk.PhotoImage(file = r"images\new.png")

        self.Option_Button_Local = tk.Button(self.InputFrame, bg = "#3f3f40", fg = "#eeeee8", text = "Wczytaj plik z dysku lokalnego", command = self.NewWindow, image = self.local_disc, compound = tk.LEFT, width = 200, height = 50, font = "Arial 9 bold", relief = tk.FLAT, borderwidth=0, cursor="hand2")

        self.Option_Button_Cloud = tk.Button(self.InputFrame, bg = "#3f3f40", fg = "#eeeee8", text = "Wczytaj plik z chmury", command = self.NewWindow, image = self.cloud, compound = tk.LEFT, width = 200, height = 50, font = "Arial 9 bold", relief = tk.FLAT, borderwidth=0, cursor="hand2")

        self.Option_Button_New = tk.Button(self.InputFrame, bg = "#3f3f40", fg = "#eeeee8", text = "Nowy", command = self.NewWindow, image = self.new, compound = tk.LEFT, width = 200, height = 50, font = "Arial 9 bold", relief = tk.FLAT, borderwidth=0, cursor="hand2")

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

        def SelectImage():
            width, height = self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()
            self.types = [("png", "*.png"), ("jpg", "*.jpg"), ("jpeg", "*.jpeg"), ("wszystkie", ["*.jpeg", "*.jpg", "*.png"])]
            self.filename = filedialog.askopenfilename( title='Wczytaj obraz', filetypes=self.types )
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
            self.canvas.config( bg = "red" )

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

        self.ButtonList = ["Motyw","Wklej", "Wytnij", "Kopiuj", "Zaznacz", "Zmień rozmiar", "Obróć", "Pędzel", "Gumka", "Kształty", "Wypełnienie", "Edytuj kolory"]
        self.ColorList = ["white", "olive", "yellow", "green", "orange", "blue", "red", "grey80", "violet", "grey", "purple", "black", "pink", "brown"]


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
                    self.SchapesList.append(self.SchapesButton)
                    self.SchapesList.append(self.SchapesButton2)
                    self.SchapesList.append(self.SchapesButton3)
                    self.SchapesList.append(self.SchapesButton4)
                    self.SchapesList.append(self.SchapesButton5)
                    self.SchapesList.append(self.SchapesButton6)
                elif bb == "Pędzel":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.use_pen, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)
                elif bb == "Gumka":
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, command = self.use_rubber, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.Button_Theme_List.append(self.BarButton)
                else:
                    self.BarButton = tk.Button(self.WidgetBarFrame, text = str(bb), width = 11, height = 3, bg = "#3f3f40", fg = "#eeeee8", activebackground="#3f3f40", borderwidth=0, cursor="hand2")
                    self.BarButton.pack(side = tk.LEFT, padx = 3, pady = 5)
                    self.BarButton.config(command = self.use_color if bb == "Edytuj kolory" else None)
                    self.Button_Theme_List.append(self.BarButton)
            for col in self.ColorList:
                self.ColorButton = tk.Button(self.ColorFrame, background = col, cursor="hand2")
                self.ListColorButton.append(self.ColorButton)

        AddButtonBar() #Wywołanie funkcji do tworzenia przycisków
        SetColorGrid() #Wywołanie funkcji do pozycjonowania colorbuttons
        SetShapesGrid() #Wywołanie funkcji do pozycjonowania shapebuttons

        #Stworzenie i ustawienie canvasa
        self.canvas = tk.Canvas(self.second_gui, width = 855, height = 500, bg = "#252526")
        self.canvas.pack()

        self.setup() #wykonywaie funkcji

    #FUNKCJA RYSOWANIA - POCZATEK - aktywacja przycisku ,,Pędzel"

    DEFAULT_PEN_SIZE = 5.0 #Tutaj można wstawić wybór grubości pisaka
    DEFAULT_COLOR = 'black' #Póżniej bd można wstawić tutaj wybór kolorów
    DEFAULT_BACKGROUND_COLOR = 'white'

    def setup(self):
        self.old_x, self.old_y = None, None #definicja poczatkowa wspolrzednych
        self.color = self.DEFAULT_COLOR #definicja koloru pisaka
        self.background_color = self.DEFAULT_BACKGROUND_COLOR #definicja koloru tła
        self.active_button = self.BarButton
        self.canvas.bind('<B1-Motion>', self.paint) #wybór klawisza myszy <B1-Motion>, <B2-Motion>, <B3-Motion> i wywołanie funkcji PAINT
        #widget.bind(event, handler) the "handler" function is called with an event object. describing the event.
        self.canvas.bind('<ButtonRelease-1>', self.reset)#wyór klawisza myszy<ButtonRelease-1>, <ButtonRelease-2>, and <ButtonRelease-3>.

    def use_pen(self):
        self.activate_button(self.BarButton)

    def use_rubber(self):
        self.activate_button(self.BarButton, eraser_mode=True)

    def use_color(self): #wczytane kolorów i zmiana kolory pisaka
        self.color = colorchooser.askcolor(color=self.color)[1]


    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=tk.RAISED) #relief - styl widżetu (FLAT, RAISED, SUNKEN, GROOVE, RIDGE)
        some_button.config(relief=tk.SUNKEN) #definicja pozostalych przyciskow
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event): #rysowanie linii
        self.canvas.config(cursor="pencil")
        if self.eraser_on and self.btnState:
            paint_color = "#d6d6d2"  #definicja koloru przy jasnym motywne tła
        elif self.eraser_on and  not self.btnState:
            paint_color = "#252526"
        else:
            paint_color = self.color
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                               fill=paint_color)
                               #ROUND - zokraglone brzegi, SMOOTT - true - spine false - łamana
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None
##FUNKCJA RYSOWANIA - koniec
### Aplikacja tutaj startuje
if __name__ == '__main__':
    root = tk.Tk()
    app = FirstWindow(root)
    root.mainloop()
###