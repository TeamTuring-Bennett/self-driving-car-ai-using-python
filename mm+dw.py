from tkinter import *
from logging import root
from tkinter import messagebox
import PIL as pog
from PIL import Image
from PIL import ImageTk


root = Tk()
root.title("Main Menu")
root.geometry("1280x720")
bg = PhotoImage(file=r"image.png")


my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


class Paint(object):

    DEFAULT_TRACK_SIZE = 75
    DEFAULT_COLOR = '#2e2d2d'
    BG_COLOR = 'white'

    def __init__(self):
        self.points = []
        self.root = Tk(screenName='track creator', className='track creator')

        self.track_button = Button(self.root, text='Draw Track', command=self.use_track)
        self.track_button.grid(row=0, column=0, pady=5)

        self.start_button = Button(self.root, text='Place Starting Line', command=self.use_start)
        self.start_button.grid(row=0, column=1)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=2)

        self.choose_size_button = Scale(self.root, from_=60, to=90, orient=HORIZONTAL)
        self.choose_size_button.set(75)
        self.choose_size_button.grid(row=1, column=0, columnspan=2, pady=2)

        self.save_button = Button(self.root, text='Save Track', command=self.export)
        self.save_button.grid(row=0, column=14)

        self.sos_button = Button(self.root, text='Start Over', command=self.start_over)
        self.sos_button.grid(row=3, column=14)

        self.c = Canvas(self.root, bg='#5fcca6', width=1280, height=720)
        self.c.grid(row=2, columnspan=15)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.start = False
        self.start_made = False
        self.active_button = self.track_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.c.bind('<ButtonPress-1>', self.setStart)

    def use_track(self):
        self.activate_button(self.track_button)                     

    def use_start(self):
        self.activate_button(self.start_button, start_mode=True)

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def export(self):
        self.activate_button(self.save_button)
        if self.start_made:
            self.c.create_line(self.points[-1], self.points[0], width=self.line_width, fill='#2e2d2d', capstyle=ROUND, smooth=TRUE, splinesteps=36)
            #self.c.create_line(self.points[-1], self.points[0], dash=1, width=2, fill='#e4e4e4')
            #self.c.create_line(self.points, dash=1, width=2, fill='#e4e4e4')
        else:
            messagebox.showwarning('Could not export track', ' A starting line has not been made. Please make a starting line then retry saving.')
            self.use_track()

    def activate_button(self, some_button, eraser_mode=False, start_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode
        self.start = start_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = '#5fcca6' if self.eraser_on else self.color
        if self.old_x and self.old_y and self.start == False:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
    
    def setStart(self, event):
        self.line_width = self.choose_size_button.get()
        if self.start and self.start_made == False:
            paint_color = '#f5d21f'
            self.c.create_rectangle(event.x, event.y, event.x+13, event.y + self.line_width, 
                                    fill=paint_color, outline=paint_color)
            self.start_made = True
        

    def reset(self, event):
        self.old_x, self.old_y = None, None
        self.points.append((event.x, event.y))

    def start_over(self):
        self.root.destroy()
        Paint()


def Manual():
    Paint()

def AI():
    Paint()

def PaintMode():
    Paint()
  

Font1 = ("Comic Sans MS", 20, "bold")
Font2 = ("Avenir Next LT Pro", 20, "bold")
Font2i = ("Avenir Next LT Pro", 17, "bold")
Font3 = ("Montserrat", 40, "bold")
Font4 = ("Montserrat", 20) 


mainlabel = Label(root, text="SELF DRIVING AI CAR", font = Font3, fg="#2e2d2d", bg = "#e4e4e4", padx = 150, pady = 20 )
mainlabel.pack(pady=50, padx =50)


button_ManualMode = Button(root, text="Manual Mode", command = Manual,fg ="#5fcca6", bg = "#2e2d2d", font=Font2)
button_AIMode = Button(root, text="AI Mode", command =AI,fg ="#5fcca6", bg = "#2e2d2d", font=Font2 )
button_PaintMode = Button(root, text="Paint Mode", command=PaintMode, fg ="#5fcca6", bg = "#2e2d2d", font=Font2, padx=170)
button_Quit = Button(root, text = "Quit", command=root.destroy, fg ="#2e2d2d", bg = "#e4e4e4", font=Font2i,)


button_ManualMode.pack(pady = 1, padx =133, side=LEFT)
button_AIMode.pack(pady = 0, padx =133, side=LEFT )
button_PaintMode.pack(pady = 0, padx =133, side=LEFT)
button_Quit.place(x=620, y=650)


root.mainloop()
