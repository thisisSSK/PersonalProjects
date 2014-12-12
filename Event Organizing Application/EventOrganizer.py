__author__ = 'thisisSSK'
"""
create a program that will allow you to enter events organizable by hour.
There must be menu options of some form, and you must be able to easily
edit, add, and delete events without directly changing the source code.
"""

from Tkinter import *

class EventOrganizer(Frame):

    def __init__(self, master ):


        Frame.__init__(self,master)

        entryframe = Frame(root)
        entryframe.pack()

        # Event title entry box
        Label(entryframe, text="Event ").grid(row = 0, column = 0, sticky=W)
        self.nameVar = StringVar()
        name = Entry(entryframe, textvariable=self.nameVar)
        name.grid(row=0, column=1, sticky = W)

        # Time entry Box
        Label(entryframe, text = "Time").grid(row=1, column =0, sticky = W)
        self.timeVar = StringVar()
        time = Entry(entryframe, textvariable=self.timeVar)
        time.grid(row=1,column=1, sticky=W)

        # Box of events
        eventframe = Frame(root)
        eventframe.pack()
        #   Scrollable listbox
        print "MAKING BOX"
        scroll = Scrollbar(eventframe, orient = VERTICAL)
        self.box = Listbox(eventframe, yscrollcommand=scroll.set, height = 6)
        # scroll configures y axis of box
        scroll.config (command = self.box.yview())
        # just organizing so scroll is on the right, and fill to adjust heigh/width to that of parent window
        scroll.pack(side=RIGHT, fill=Y)
        self.box.pack(side=LEFT, fill = BOTH, expand = 1)
        print self.box


        # Buttons
        buttonframe = Frame(root)
        buttonframe.pack()
        add = Button (buttonframe, text = " Add Event ", command = self.addEntry)
        edit = Button(buttonframe, text = " Edit Event ", command = self.editEntry)
        delete = Button (buttonframe, text = " Delete ", command = self.deleteEntry)
        ####sort = Button (buttonframe, text = " Sort Entries", command = self.sortEntrys())
        #   organizing buttons
        add.pack(side = LEFT) ; edit.pack(side = LEFT)
        delete.pack(side = LEFT);
        ####sort.pack(side = LEFT)


    def addEntry(self):
        # add current entry into the dictionary of events and also inserts title of event into the listbox widget

        self.box.insert(END, (self.timeVar.get() + ' - ' + self.nameVar.get()))
        print "Event Added!"

    def editEntry(self):
        # only edits the first item selected
        if bool(self.box.curselection()):
            index = self.box.curselection()[0]


            # deletes current entry in the listbox and adds the updated one
            self.box.delete(index)
            self.box.insert(index, [self.timeVar.get(), self.nameVar.get()])

    def deleteEntry(self):
        # get selected line
        index = self.box.curselection()[0]
        print index
        print type(self.box.get(index))
        self.box.delete(index)


root = Tk()

EventOrganizer(root)

root.mainloop()

