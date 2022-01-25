from tkinter import *
from tkinter import simpledialog
import drawing_window
import cargame


class MainMenu:

    def __init__(self):
        self.root = Tk()
        self.root.title("Main Menu")
        self.root.geometry("1280x720")
        bg = PhotoImage(file=r"image.png")

        my_label = Label(self.root, image=bg)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Font1 = ("Comic Sans MS", 20, "bold")
        self.Font2 = ("Avenir Next LT Pro", 20, "bold")
        self.Font2i = ("Avenir Next LT Pro", 17, "bold")
        self.Font3 = ("Montserrat", 40, "bold")
        self.Font4 = ("Montserrat", 20) 


        self.mainlabel = Label(self.root, text="SELF DRIVING CAR SIMULATION", font = self.Font3, fg="#2e2d2d", bg = "#e4e4e4", padx = 150, pady = 20 )
        self.mainlabel.pack(pady=50, padx =50)


        self.button_ManualMode = Button(self.root, text="Manual Mode", command = self.Manual,fg ="#5fcca6", bg = "#2e2d2d", font=self.Font2)
        self.button_AIMode = Button(self.root, text="AI Mode", command =self.AI,fg ="#5fcca6", bg = "#2e2d2d", font=self.Font2 )
        self.button_PaintMode = Button(self.root, text="Paint Mode", command=self.PaintMode, fg ="#5fcca6", bg = "#2e2d2d", font=self.Font2, padx=170)
        self.button_Quit = Button(self.root, text = "Quit", command=self.root.destroy, fg ="#2e2d2d", bg = "#e4e4e4", font=self.Font2i,)


        self.button_ManualMode.pack(pady = 1, padx =133, side=LEFT)
        self.button_AIMode.pack(pady = 0, padx =133, side=LEFT )
        self.button_PaintMode.pack(pady = 0, padx =133, side=LEFT)
        self.button_Quit.place(x=620, y=650)


        self.root.mainloop()
    

    def Manual(self):
            self.picktrack()
            self.root.destroy()
            cargame.Race(self.trackname, "Manual")

    def AI(self):
            self.picktrack()
            self.root.destroy()
            cargame.Race(self.trackname, "AI")
            
    def PaintMode(self):
            self.root.destroy()
            drawing_window.Paint()
        
    def picktrack(self):
            self.trackname = simpledialog.askstring("Track Select", "Please enter a track name for the car to drive on \n(without any extensions)") + '.png'
            

if __name__ == '__main__':
    MainMenu()
        

        
