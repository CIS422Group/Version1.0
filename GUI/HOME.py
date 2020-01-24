#Author: Lucas Hyatt


'''======================================Imports=========================================='''
import tkinter as tk
from tkinter import filedialog, Text
import tkinter.ttk as ttk
import tkinter.font
import os
import GUI
import sys

# Needed for importing files a level up
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from objects import Student, classQueue


'''======================================Functions=========================================='''

def switch_view():
    GUI.testScreenUpdate()

studentQueue = classQueue()

def inputFile(delimiter = "    "):
    filepath = filedialog.askopenfilename(initialdir="./..", title="Select File")

    try:
        with open(filepath, "r") as f:
            next(f)     # skip first line of roster file (comments)
            for i, line in enumerate(f):
                elements = line.strip().split(delimiter)

                try:
                    fname = str(elements[0])
                    lname = str(elements[1])
                    uoID = int(elements[2])
                    email = str(elements[3])
                    phonetic = str(elements[4])
                    reveal = bool(elements[5])

                    if len(elements) >= 9:
                        numCalled = int(elements[6])
                        numFlags = int(elements[7])
                        dates = list("".join(elements[8:]).replace("[", "").replace("]", "").split())
                        # TODO: parse, sort dates
                    else:
                        numCalled = 0
                        numFlags = 0
                        dates = []

                    # Create Student object, Insert into Queue
                    studentQueue.enqueue(Student(fname, lname, uoID, email, phonetic, reveal, numCalled, numFlags, dates))

                except (ValueError, IndexError):
                    print("Line {i} of roster file is formatted incorrectly")
                    # quit()
                    # TODO: flash errors to GUI

    except FileNotFoundError:
        print("File Does not exist")
        # quit()
        # TODO: flash errors to GUI

    studentQueue.printQ()
    writeLogFile()
    writeSummaryPerformanceFile()

def writeSummaryPerformanceFile():

    filepath = "SummaryPerformanceFile.txt"
    header = "Summary Performance File for the Cold-Call-Assist program. Number-of-Times-Called    Student-Flag    First-Name    Last-Name    UO-ID    Email    Phonetic-Spelling    Reveal-Code    List-of-Dates\n"

    try:
        with open(filepath, "w") as f:
            f.write(header)

            for student in studentQueue.queue:
                line = student.summaryPerformance()
                f.write(line)

                # TODO: clean up column justification?
                # f.write(f"{student.numCalled}\t{student.flag}\t{student.fname}\t{student.lname}\t{student.uoID}\t{student.email}\t{student.phonetic}\t{student.reveal}\t{student.dates}\n")

    except FileNotFoundError:
        print("File Does not exist")
        # quit()
        # TODO: flash errors to GUI

def writeLogFile(delimiter="    "):

    if len(studentQueue.queue) == 0:
        print("No data to log")
        # TODO: flash errors to GUI
    

    # TODO: decide on if log file overrides roster or is seperate
    # The following line depend on if the file is being written in place or written to a new file
    #
    # filepath = filedialog.askopenfilename(initialdir="./..", title="Select File")
    #  -- or --
    # try:
    #     with open(filepath, "r") as f:
    #         header = f.readline()
    #
    # except FileNotFoundError:
    #     print("File Does not exist")
    #     # quit()
    #     # TODO: flash errors to GUI

    filepath = "log.txt"
    header = "TEMP COMMENT HEADER\n"

    try:
        # Overwrite roster file, but preserve the first line
        with open(filepath, "w") as f:
            f.write(header)

            for student in studentQueue.queue:
                line = "{student.fname}{delimiter}{student.lname}{delimiter}{student.uoID}{delimiter}{student.email}{delimiter}{student.phonetic}{delimiter}{student.reveal}{delimiter}{student.numCalled}{delimiter}{student.numFlags}{delimiter}{student.dates}\n"
                f.write(line)

    except FileNotFoundError:
        print("File Does not exist")
        # quit()
        # TODO: flash errors to GUI

def export():
    #GUI.ErrorBox('Log Error', "Log Error", "This function needs to be implemented").display()
    pass

def exitProgram():
    root.destroy()

'''======================================GUI=========================================='''

'''
Color Scheme:

red = #ff0443
blue = #0486ff
yellow = #ffde04
'''

root = tk.Tk() #Establishes structure for app window
root.resizable(False, False)
root.title("Cold Call System")
root.attributes("-topmost", True)   # open window in front


pane = tk.Frame(root, bg = '#0486ff', bd=30)
pane.pack(fill = tk.BOTH, expand = True)

button_font = tkinter.font.Font(family="Helvetica",size=20,weight="bold")

#Progress bar will show how many student out of the roster have been chosen.
progress = ttk.Progressbar(pane, orient=tk.HORIZONTAL, length=496)
progress['value'] = 25
progress.pack(side=tk.BOTTOM)

user_view = tk.Button(pane, pady=8, text="User View", command=switch_view)
user_view.pack(side=tk.LEFT) 
user_view['font'] = button_font
user_view.update()

input_roster = tk.Button(pane, pady=8, text="Input Roster", command=inputFile)
input_roster.pack(side=tk.LEFT)
input_roster['font'] = button_font
input_roster.update()

export_calls = tk.Button(pane, pady=8, text="Export to Log", command=export)
export_calls.pack(side=tk.LEFT) 
export_calls['font'] = button_font
export_calls.update()

exit_menu = tk.Button(pane, pady=8, text="Quit", command=exitProgram)
exit_menu.pack(side=tk.LEFT) 
exit_menu['font'] = button_font
exit_menu.update()

# Main Loop
root.attributes("-topmost", False)  # allow window to go behind other windows
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














