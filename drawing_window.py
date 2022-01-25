from fileinput import filename
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from mainmenu import *
from PIL import ImageGrab
import os


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

        self.menu_button = Button(self.root, text='Back to Menu', command=self.menu)
        self.menu_button.grid(row=3, column=0)
        
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
            #implement these two after fixing autocomplete bugs.
            #self.c.create_line(self.points[-1], self.points[0], dash=1, width=2, fill='#e4e4e4')
            #self.c.create_line(self.points, dash=1, width=2, fill='#e4e4e4')

            savename = simpledialog.askstring('Save track as PNG', 'Please pick a name for the track.')
            if savename == None or savename == '':
                messagebox.showerror('Could not export track', 'Invalid name!')
                self.use_track()
            else:
                x=self.root.winfo_rootx()+self.c.winfo_x()
                y=self.root.winfo_rooty()+self.c.winfo_y()
                x1=x+1280
                y1=y+720
                filepath = '.\\tracks'
                filename = savename + '.png'
                completepath = os.path.join(filepath, filename)
                ImageGrab.grab().crop((x,y,x1,y1)).save(completepath)
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
        if self.eraser_on:
            try:
                self.points.remove((event.x, event.y))
            except:
                pass
        else:
            self.points.append((event.x, event.y))
    
    def setStart(self, event):
        self.line_width = self.choose_size_button.get()
        if self.start and self.start_made == False:
            paint_color = '#f5d21f'
            self.c.create_rectangle(event.x, event.y, event.x+13, event.y + self.line_width, 
                                    fill=paint_color, outline=paint_color)
            self.start_made = True
        

    def reset(self, event):
        self.old_x, self.old_y = None, None
        
        

    def start_over(self):
        self.root.destroy()
        Paint()

    def menu(self):
        self.root.destroy()
        MainMenu()



    