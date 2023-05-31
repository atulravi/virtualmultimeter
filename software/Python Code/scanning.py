import serial
import time
import pyglet
from tkinter import *
pyglet.font.add_file('DSEG7Modern-Bold.ttf')


print('''    Virtual Voltmeter - Makes your voltmeter readings appear on stream with python
    Copyright (C) 2023  Atul Ravi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.''')
x = str(input("Enter COM port as text EG: (COM3).If entered wrong, restart the application. Type here:"))
x.upper()

root = Tk(className='VIRTUAL MULTIMETER ESCcrasci')
root.configure(background='#00FFFF')
root.iconbitmap("logo.ico")

ser = serial.Serial(x, 9800, timeout=1)
time.sleep(2)
while (True):
    line = ser.readline()   
    if line:
        stringa = line.decode()  
        w = Label(root, text=stringa  , font=("DSEG7 Modern-Bold",55) , fg="red" , bg="#00FFFF")
        w.pack()
        root.update()
        w.destroy()
        

ser.close()
root.mainloop()
