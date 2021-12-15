# DATE PICKER
# import tkinter  as tk 
# from tkcalendar import DateEntry
# window = tk.Tk()
# window.geometry("340x220")  

cal=DateEntry(window,selectmode='day')
cal.grid(row=1,column=1,padx=15)

# window.mainloop()

import tkinter as tk
from tkcalendar import Calendar

class MyCalendar(Calendar):
    def __init__(self, master, **kw):
        Calendar.__init__(self, master, **kw)

        for row in self._calendar:
            for label in row:
                label['anchor'] = "nw"



root = tk.Tk()
cal = MyCalendar(root, showweeknumbers=False)
cal.pack(fill='both', expand=True)
root.geometry("700x400")
root.mainloop()