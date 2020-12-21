import tkinter as tk
#eehhhh


#Klasa pierwszego, powitalnego okna
class FirstWindow:
    def __init__(self, first_gui):
        #Ustawienia okna
        self.first_gui = first_gui
        self.first_gui.geometry("500x300")
        self.first_gui.title("PyPhotoshop v1.0.0")
        # W first_gui działa dodanie ikony okna a w second_gui już nie
        # self.first_gui.wm_iconbitmap(bitmap = "camera.ico")

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
        self.second_gui.geometry("804x589")
        self.second_gui.title("PyPhotoshop v1.0.0")
        # W first_gui działa dodanie ikony okna a w second_gui już nie
        # self.second_gui.wm_iconbitmap(bitmap = "camera.ico")

        #Stworzenie i ustawienie frame dla widgetow (TopBarFrame dla przycisku plik i opcje na samej górze, BarFrame dla 10 przycisków poniżej)
        self.WidgetTopBarFrame = tk.Frame(self.second_gui)
        self.WidgetTopBarFrame.place(x = 0, y = 0)

        self.WidgetBarFrame = tk.Frame(self.second_gui)
        self.WidgetBarFrame.place(x = 0, y = 30)
        
        #Ustawienie pozycji 10 przycisków
        def SetBarGrid(ButtonList):
            for Button in ButtonList:
                Button.pack(side = tk.LEFT)

        def SetTopBarGrid(ButtonTopList):
            ### Wersja robocza, potem to zmienie
            # self.x1, self.y1 = 0, 0
            # for Button in ButtonTopList:
            #     Button.grid(row = self.x1, column = self.y1)
            #     self.y1 += 1
            ###
            #Ustawienie przycisków plik i opcje 
            for Button in ButtonTopList:
                Button.pack(side = tk.LEFT)


        self.AllTopBarButton = [] #Lista do której dodaje przyciski plik i opcje, potrzebne do ustawienia pozycji

        #Tworzenie przycisków plik i opcje
        for tb in range(2):
            self.TopBarButton = tk.Button(self.WidgetTopBarFrame)
            self.TopBarButton.config(text = "Plik" if tb == 1 else "Opcje")
            self.AllTopBarButton.append(self.TopBarButton)

        self.AllBarButton = [] ##Lista do której dodaje 10 przycisków, potrzebne do ustawienia pozycji

        #Tworzenie 10 przycisków (funkcyjnych? Wiadomo o co chodzi :) )
        for bb in range(10):
            self.BarButton = tk.Button(self.WidgetBarFrame, text = "Opcja" + str(bb), width = 10, height = 3)
            self.AllBarButton.append(self.BarButton)

        SetBarGrid(self.AllBarButton) #Wywołanie komendy ustawenia przycisków
        SetTopBarGrid(self.AllTopBarButton) #Wywołanie komendy ustawenia przycisków

        #Stworzenie i ustawienie canvasa
        self.canvas = tk.Canvas(second_gui, width = 800, height = 500, bg = "red")
        self.canvas.place(x = 0, y = 85)


        
        
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

