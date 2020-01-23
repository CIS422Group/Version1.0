import tkinter as tk
from tkinter import filedialog, Text
import tkinter.font
import os
import GUI

root = tk.Tk() #Establishes structure for app window
root.resizable(False, False)
root.title("Cold Call System")

'''
Color Scheme:

red = #ff0443
blue = #0486ff
yellow = #ffde04
'''
def switch_view():
    GUI.testScreenUpdate()


def inputFile():
	filename = filedialog.askopenfilename(initialdir="./..", title="Select File")

	#This is where we insert the rest of I/O

pane = tk.Frame(root, bg = '#0486ff', bd=30)
pane.pack(fill = tk.BOTH, expand = True)

# canvas = tk.Canvas(root, height = 500, width = 700, bg='#1FB7C9')
# canvas.pack()

# inputRoster = tk.Button(root, text="Input Roster", padx=10, pady=10, fg="#E74C3C", command=inputFile).place(relx=.3, rely=.1)
# # inputRoster.pack()

# userView = tk.Button(root, text="User View", padx=10, pady=10, fg="#E74C3C").place(relx=.5, rely=.1)
# # teacherView.pack()

button_font = tkinter.font.Font(family="Helvetica",size=36,weight="bold")

user_view = tk.Button(pane, text="User View", width=15, height=3, activeforeground='#7cff68', fg="#ff0443", command=switch_view)
user_view.pack() 
user_view['font'] = button_font

input_roster = tk.Button(pane, text="Input Roster", width=15, height=3, activeforeground='#7cff68', fg="#ff0443", command=inputFile)
input_roster.pack() 
input_roster['font'] = button_font

export_calls = tk.Button(pane, text="Export to Log", width=15, height=3, activeforeground='#7cff68', fg="#ff0443")
export_calls.pack() 
export_calls['font'] = button_font

exit_menu = tk.Button(pane, text="Quit", width=15, height=3, activeforeground='#7cff68', fg="#ff0443", command=quit)
exit_menu.pack() 
exit_menu['font'] = button_font

# Main Loop
root.mainloop()

'''
Sources: 
https://stackoverflow.com/questions/31128780/tkinter-how-to-make-a-button-center-itself
https://www.geeksforgeeks.org/python-pack-method-in-tkinter/
https://www.youtube.com/watch?v=u4ykDbciXa8&feature=youtu.be
https://www.youtube.com/watch?v=qC3FYdpJI5Y&feature=youtu.be
https://stackoverflow.com/questions/110923/how-do-i-close-a-tkinter-window
https://www.tutorialspoint.com/python/tk_place.htm
'''














