from tkinter import *
from functools import partial

colors = {
    0:"#ab91ff", 1:"#d0a176", 2:"#ecce86", 3:"#ecff91", 4:"#fff991", 5:"#92ff9f", 6:"#f991ff", 7:"#91dfff",
    8:"#d2ff91", 9:"#b8ff91"
}

buttonsPos = {
    "H":[1, 1, colors[0]], "He":[1, 18, colors[7]],

    "Li":[2, 1,  colors[1]], "Be":[2, 2, colors[2]], "B":[2, 13, colors[5]], "C":[2, 14, colors[0]], "N":[2, 15, colors[0]],
    "O":[2, 16, colors[0]], "F":[2, 17, colors[6]], "Ne":[2, 18, colors[7]],

    "Na":[3, 1, colors[1]], "Mg":[3, 2, colors[2]], "Al":[3, 13, colors[4]], "Si":[3, 14, colors[5]], "P":[3, 15, colors[0]],
    "S":[3, 16, colors[0]], "Cl":[3, 17, colors[6]], "Ar":[3, 18, colors[7]],

    "K":[4, 1, colors[1]], "Ca":[4, 2, colors[2]], "Sc":[4, 3, colors[3]], "Ti":[4, 4, colors[3]], "V":[4, 5, colors[3]],
    "Cr":[4, 6, colors[3]], "Mn":[4, 7, colors[3]], "Fe":[4, 8, colors[3]], "Co":[4, 9, colors[3]], "Ni":[4, 10, colors[3]],
    "Cu":[4, 11, colors[3]], "Zn":[4, 12, colors[3]], "Ga":[4, 13, colors[4]], "Ge":[4, 14, colors[5]], "As":[4, 15, colors[5]],
    "Se":[4, 16, colors[0]], "Br":[4, 17, colors[6]], "Kr":[4, 18, colors[7]],

    "Rb":[5, 1, colors[1]], "Sr":[5, 2, colors[2]], "Y":[5, 3, colors[3]], "Zr":[5, 4, colors[3]], "Nb":[5, 5, colors[3]],
    "Mo":[5, 6, colors[3]], "Tc":[5, 7, colors[3]], "Ru":[5, 8, colors[3]], "Rh":[5, 9, colors[3]], "Pd":[5, 10, colors[3]],
    "Ag":[5, 11, colors[3]], "Cd":[5, 12, colors[3]], "In":[5, 13, colors[4]], "Sn":[5, 14, colors[4]], "Sb":[5, 15, colors[5]],
    "Te":[5, 16, colors[5]], "I":[5, 17, colors[6]], "Xe":[5, 18, colors[7]],

    "Cs":[6, 1, colors[1]], "Ba":[6, 2, colors[2]], "Lu":[6, 3, colors[3]], "Hf":[6, 4, colors[3]], "Ta":[6, 5, colors[3]],
    "W":[6, 6, colors[3]], "Re":[6, 7, colors[3]], "Os":[6, 8, colors[3]], "Ir":[6, 9, colors[3]], "Pt":[6, 10, colors[3]],
    "Au":[6, 11, colors[3]], "Hg":[6, 12, colors[3]], "Tl":[6, 13, colors[4]], "Pb":[6, 14, colors[4]], "Bi":[6, 15, colors[4]],
    "Po":[6, 16, colors[5]], "At":[6, 17, colors[6]], "Rn":[6, 18, colors[7]],

    "Fr":[7, 1, colors[1]], "Ra":[7, 2, colors[2]], "Lr":[7, 3, colors[3]], "Rf":[7, 4, colors[3]], "Db":[7, 5, colors[3]],
    "Sg":[7, 6, colors[3]], "Bh":[7, 7, colors[3]], "Hs":[7, 8, colors[3]], "Mt":[7, 9, colors[3]], "Ds":[7, 10, colors[3]],
    "Rg":[7, 11, colors[3]], "Cn":[7, 12, colors[3]], "Nh":[7, 13, colors[4]], "Fl":[7, 14, colors[4]], "Mc":[7, 15, colors[4]],
    "Lv":[7, 16, colors[4]], "Ts":[7, 17, colors[6]], "Og":[7, 18, colors[7]],

    "La":[8, 4, colors[8]], "Ce":[8, 5, colors[8]], "Pr":[8, 6, colors[8]], "Nd":[8, 7, colors[8]], "Pm":[8, 8, colors[8]],
    "Sm":[8, 9, colors[8]], "Eu":[8, 10, colors[8]], "Gd":[8, 11, colors[8]], "Tb":[8, 12, colors[8]], "Dy":[8, 13, colors[8]],
    "Ho":[8, 14, colors[8]], "Er":[8, 15, colors[8]], "Tm":[8, 16, colors[8]], "Yb":[8, 17, colors[8]],

    "Ac":[9, 4, colors[9]], "Th":[9, 5, colors[9]], "Pa":[9, 6, colors[9]], "U":[9, 7, colors[9]], "Np":[9, 8, colors[9]],
    "Pu":[9, 9, colors[9]], "Am":[9, 10, colors[9]], "Cm":[9, 11, colors[9]], "Bk":[9, 12, colors[9]], "Cf":[9, 13, colors[9]],
    "Es":[9, 14, colors[9]], "Fm":[9, 15, colors[9]], "Md":[9, 16, colors[9]], "No":[9, 17, colors[9]]
}

data = {
    "H":["Hidrógeno", "1.00794", "1", "1312.0", "2.20", "+1\n-1", "1s"+u"\u00b9"],
    "Li":["Litio", "6.941", "3", "520.2", "0.98", "+1\n-1", "1s"+u"\u00b2"+" 2s"+u"\u00b9"],
    "Be":["Berilio", "9.012182", "4", "899.5", "1.57", "+2", "1s"+u"\u00b2"+" 2s"+u"\u00b2"],
    "Na":["Sodio", "22.98976", "11", "495.8", "0.93", "+1\n-1", "[Ne] 3s"+u"\u00b9"],
    "Mg":["Magnesio", "24.3050", "12", "737.7", "1.31", "+2\n+1", "[Ne] 3s"+u"\u00b2"],
    "K":["Potasio", "29.0913", "19", "418.8", "0.82", "+1", "[Ar] 4s"+u"\u00b9"],
    "Ca":["Calcio", "40.078", "20", "589.8", "1.00", "+2", "[Ar] 4s"+u"\u00b2"],
    "Rb":["Rubidio", "85.4678", "37", "403.0", "0.82", "+1", "[Kr] 5s"+u"\u00b9"]
}

DEFAULT_BOLD = ("Helvetica", "15", "bold")
MAIN_BOLD = ("Helvetica", "30", "bold")
ATOMIC_BOLD = ("Helvetica", "17", "bold")
FULLNAME_BOLD = ("Helvetica", "10", "bold")

class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.configure(bg="#ffffff")
        self.root.geometry("900x414")
        #self.root.iconbitmap("./icon.ico")
        self.root.title("Tabla periódica de los elementos")
        self.root.resizable(False, False)
        self.buttonsFrame = self.createFButtons()
        self.buttons = self.createButtons(self.buttonsFrame)
        self.c = Canvas(self.buttonsFrame, width=495, height=135, highlightthickness=0, bg="#ffffff")
        self.c.place(x=100, y=0)
        self.actualrec = self.c.create_rectangle(50, 20, 150, 120, fill="#ab91ff", width=2)
        self.actualtext = self.c.create_text(55, eval("(20+120)/2"), text="H", font=MAIN_BOLD, anchor=W)
        self.actualfulltext = self.c.create_text(55, eval("((20+120)/2)+25"), text="Hidrógeno", font=FULLNAME_BOLD, anchor=W)
        self.actualAmasstext = self.c.create_text(55, 30, text="1.00794", font=FULLNAME_BOLD, anchor=W)
        self.actualNmasstext = self.c.create_text(130, 35, text="1", font=ATOMIC_BOLD)
        self.actualiontext = self.c.create_text(55, 46, text="1312.0", anchor=W)
        self.actualelectrotext = self.c.create_text(95, 46, text="2.20", anchor=W)
        self.actualoxtext = self.c.create_text(133, 48, text="+1\n-1", anchor=NW)
        self.actualconftext = self.c.create_text(55, 110, text="1s"u"\u00b9", anchor=W)

        self.metalesalcalinos = self.c.create_rectangle(205, 10, 220, 25, fill="#d0a176")
        self.alcalinoterreos = self.c.create_rectangle(205, 30, 220, 45, fill="#ecce86")
        self.otrosmetales = self.c.create_rectangle(205, 50, 220, 65, fill="#fff991")
        self.metalesdetrans = self.c.create_rectangle(205, 70, 220, 85, fill="#ecff91")
        self.lantanidos = self.c.create_rectangle(205, 90, 220, 105, fill="#d2ff91")
        self.actinidos = self.c.create_rectangle(205, 110, 220, 125, fill="#b8ff91")

        self.metalesalcalinostext = self.c.create_text(225, 16, text="metales alcalinos", anchor=W)

        self.alcalinoterreostext = self.c.create_text(225, 36, text="alcalinotérreos", anchor=W)
        self.otrosmetalestext = self.c.create_text(225, 56, text="otros metales", anchor=W)
        self.metalesdetranstext = self.c.create_text(225, 76, text="metales de transición", anchor=W)
        self.lantanidostext = self.c.create_text(225, 96, text="lantánidos", anchor=W)
        self.actinidostext = self.c.create_text(225, 116, text="actínidos", anchor=W)

        self.metaloides = self.c.create_rectangle(360, 10, 375, 25, fill="#92ff9f")
        self.nometales = self.c.create_rectangle(360, 30, 375, 45, fill="#ab91ff")
        self.halogenos = self.c.create_rectangle(360, 50, 375, 65, fill="#f991ff")
        self.gasesnobles = self.c.create_rectangle(360, 70, 375, 85, fill="#91dfff")

        self.metaloidestext = self.c.create_text(380, 16, text="metaloides", anchor=W)
        self.nometalestext = self.c.create_text(380, 36, text="no metales", anchor=W)
        self.halogenostext = self.c.create_text(380, 56, text="halógenos", anchor=W)
        self.gasesnoblestext = self.c.create_text(380, 76, text="gases nobles", anchor=W)

    def do(self, color, text):
        self.c.itemconfig(self.actualrec, fill=color)
        self.c.itemconfig(self.actualtext, text=text)

        for k, v in data.items():
            if k == text:
                self.c.itemconfig(self.actualfulltext, text=v[0])
                self.c.itemconfig(self.actualAmasstext, text=v[1])
                self.c.itemconfig(self.actualNmasstext, text=v[2])
                self.c.itemconfig(self.actualiontext, text=v[3])
                self.c.itemconfig(self.actualelectrotext, text=v[4])
                self.c.itemconfig(self.actualoxtext, text=v[5])
                self.c.itemconfig(self.actualconftext, text=v[6])

    def createButtons(self, frame):
        bs = []
        for k,v in buttonsPos.items():
            b = Button(frame, command=partial(self.do, v[2], str(k)), text=str(k), font=DEFAULT_BOLD, height=1, width=3,
                       borderwidth=4, bg=v[2])
            b.grid(row=v[0], column=v[1], sticky=NSEW)
            bs.append(b)
        return bs

    def createFButtons(self):
        frame = Frame(self.root, bg="#ffffff")
        frame.pack(fill="both", expand="True")
        return frame

    def loop(self):
        self.root.mainloop()

if __name__ == "__main__":
    c = GUI()
    c.loop()
