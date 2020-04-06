"""Gränssnitt för att testa layoutalgoritmer.

TDDE44 laboration 5

LayoutTester tillhandahåller ett gränssnitt och en Frame som kvadratiska
tkinter.Label-instanser ska layoutas i. En layout-funktion som sköter layouten
av tkinter.Label-instanserna skickas som argument när en LayoutTester skapas.

Layout-funktionen (argumentet layout_func till LayoutTester()) tar fem argument:

squares      -- Lista som innehåller tkinter.Label-objekt
frame_height -- Höjden (int) på fönstret som fyrkanterna ska
                layoutas i.
frame_width  -- Bredden (int) på den Frame som fyrkanterna ska
                layoutas i.
"""

from random import choice, randint
from tkinter.font import Font, NORMAL, BOLD, ITALIC, ROMAN
from tkinter import Button, Checkbutton, Frame, Label, LabelFrame, OptionMenu
from tkinter import Scale, Tk, IntVar, StringVar, BooleanVar
from tkinter import N, E, W, S
from tkinter import BOTH, HORIZONTAL, LEFT, RIGHT, TOP, BOTTOM, X, Y
from colorsys import hsv_to_rgb

# globala variabler för minsta och största kvadratsstorlek
MIN_SQUARE_SIZE = randint(25, 40)
MAX_SQUARE_SIZE = randint(80, 100)
NUMBER_OF_SIZES = randint(3, 6)
SIZE_STEP = (MAX_SQUARE_SIZE - MIN_SQUARE_SIZE) // (NUMBER_OF_SIZES-1)
MAX_NUM_SQUARES = 250

class LayoutTester(object):
    """Gränssnitt för testning av layoutfunktioner."""

    def __init__(self, layout_func, debug=False):
        """Skapa GUI och förbereder tkinter.Labels som ska layoutas.

        layout_func -- Funktionen som ska placera kvadraterna, se
                       modulbeskrivning ovan.
        """
        self.layout_func = layout_func
        self.debug = debug

        # storleksalternativ
        self.size_options = [size for size in range(MIN_SQUARE_SIZE,
                                                    MAX_SQUARE_SIZE+1,
                                                    SIZE_STEP)] + ["random"]

        # lista för kvadraterna
        self.squares = []

        # skapa gränssnittet och kör igång mainloop
        self.ui_xpadding = 4
        self.ui_ypadding = 4
        self.init_ui()
        # slumpa fram fönsterstorlek
        w_size = "{}x{}".format(705 + randint(0, 300),
                                250 + randint(0, 500))
        self.root.geometry(w_size)

        self.root.mainloop()


    def init_ui(self):
        """Skapa gränssnittet och kör igång mainloop."""
        self.root = Tk()
        self.root.title("Laboration 5")
        # root.resizable(width=False, height=False)

        # Tk-variabler till kvadratsstorlek, antal kvadrater, start_left och
        # start_top.
        self.size_value = StringVar()
        self.size_value.set(self.size_options[0])
        self.number_of_squares = IntVar()
        self.start_left = BooleanVar()
        self.start_left.set(True)
        self.start_top = BooleanVar()
        self.start_top.set(True)

        # Frame att lägga kvadraterna i
        self.square_frame = Frame(self.root,
                                  #height=self.squares_frame_height,
                                  #width=self.squares_frame_width,
                                  bg="#eef")
        if self.debug:
            self.square_frame.bind("<Configure>", self.frame_changed)
        self.square_frame.pack(side=TOP, expand=1, fill=BOTH,
                               padx=self.ui_xpadding, pady=self.ui_ypadding)

        # Frame med inställningar
        self.controll_panel = LabelFrame(self.root, text="Inställningar")
        self.init_controll_panel()
        self.controll_panel.pack(fill=BOTH,
                                 padx=self.ui_xpadding, pady=self.ui_ypadding)

        # Informationstext
        infotext = "Kom ihåg att ändra fönstrets storlek när du testar! " + \
                   "Se även utskrifterna i terminalen."
        self.instructions = Label(self.root, text=infotext)
        self.instructions.pack(anchor=W)


    def init_controll_panel(self):
        """Skapa kontrollpanel för inställningar."""
        self.create_size_panel()
        self.create_num_squares_panel()
        #self.create_start_pos_panel()
        self.create_run_quit_panel()

    def create_size_panel(self):
        """Skapa OptionMenu för storlek på kvadraterna."""
        size_panel = Frame(self.controll_panel)
        Label(size_panel, text="Kvadratsstorlek").pack(side=LEFT)
        OptionMenu(size_panel, self.size_value,
                   *self.size_options).pack(side=LEFT)
        size_panel.pack(side=LEFT,
                        padx=self.ui_xpadding, pady=self.ui_ypadding)

    def create_num_squares_panel(self):
        """Skapa kontroller för att välja antal kvadrater som skapas."""
        num_squares_panel = Frame(self.controll_panel)
        Label(num_squares_panel, text="Antal kvadrater").pack(side=LEFT,
                                                              anchor=S)
        Scale(num_squares_panel, variable=self.number_of_squares,
              from_=4, to=MAX_NUM_SQUARES, orient=HORIZONTAL).pack(side=LEFT,
                                                                   anchor=N)
        num_squares_panel.pack(side=LEFT, anchor=N,
                               padx=self.ui_xpadding, pady=self.ui_ypadding)

    def create_start_pos_panel(self):
        """Skapa kontroller för att välja var layouten börjar."""
        start_panel = Frame(self.controll_panel)
        Checkbutton(start_panel, text="Börja från vänster", justify=LEFT,
                    variable=self.start_left,
                    onvalue=True, offvalue=False).pack(fill=X, anchor=N)
        Checkbutton(start_panel, text="Börja uppifrån",
                    variable=self.start_top, justify=LEFT,
                    onvalue=True, offvalue=False).pack(fill=X, anchor=N)
        start_panel.pack(side=LEFT, anchor=N,
                         padx=self.ui_xpadding, pady=self.ui_ypadding)

    def create_run_quit_panel(self):
        """Skapa knappar för att köra layout och avsluta programmet."""
        button_panel = Frame(self.controll_panel)
        Button(button_panel, text="Kör layoutfunktion",
               command=self.run_layout).pack(fill=X)
        Button(button_panel, text="Avsluta",
               command=self.root.quit).pack(fill=X)
        button_panel.pack(side=RIGHT, anchor=N,
                          padx=self.ui_xpadding, pady=self.ui_ypadding)

    def create_squares(self):
        """Skapa tkinter.Label objekt som sparas i LayoutTester-instansen.

        Antalet kvadrater som ska skapas, samt kvadraternas storlek hämtas från
        gränssnittet.
        """
        number_of_squares = self.number_of_squares.get()
        size = self.size_value.get()
        square_counter = 0
        hue_step = 1 / number_of_squares
        hue_value = 0

        # Skapa kvadrater och lägg dem i listan self.squares
        while square_counter < number_of_squares:
            # konververa hsv-färg till rgb-trippel (heltal 0-255)
            rgb = [int(val * 255) for val in hsv_to_rgb(hue_value, 0.75, 0.70)]
            # konvertera rgb-trippel till sträng
            bg_color ="#{:x}{:x}{:x}".format(rgb[0], rgb[1], rgb[2])

            # textfärg
            fg_color = "#fff"

            # sätt storleken på kvadraten
            if size != "random":
                square_size = int(size)
            else:
                square_size = choice(self.size_options[:-1])
            # sätt storleken på texten baserat på kvadratstorleken
            font_size = int(square_size * 0.6)

            # skapa kvadraten
            square = Label(self.square_frame, fg=fg_color, bg=bg_color,
                           font=Font(family="Verdana",
                                     weight=NORMAL,
                                     size=font_size),
                           text=str(square_counter + 1))
            # spara den i listan med kvadrater
            self.squares.append(square)

            # göm kvadraten utanför det synliga området och ställ in
            # dess storlek
            square.place(x=-square_size, y=-square_size,
                         height=square_size, width=square_size)

            # gå vidare till nästa kvadrat och färg
            square_counter += 1
            hue_value += hue_step

        # uppdatera geometri-info för alla widgets (ser till att de vet hur
        # stora de är)
        square.update_idletasks()

    def clear_squares(self):
        """Ta bort existerande kvadrater."""
        for square in self.squares:
            square.destroy()
        del self.squares[:]

    def frame_changed(self, event):
        if event.widget == self.square_frame or event.widget == self.root:
            print("Resize. root: {}x{}, square_frame: {}x{}".format(
                    self.root.winfo_width(), self.root.winfo_height(),
                    self.square_frame.winfo_width(),
                    self.square_frame.winfo_height()))

    def run_layout(self):
        """Skapa nya kvadrater och kör layoutfunktionen."""
        # ta bort gamla kvadrater
        self.clear_squares()

        # skapa nya kvadrater
        self.create_squares()

        # placera ut kvadraterna
        print("Running '{0}(<squares>, {1}, {2})'..."
              .format(self.layout_func.__name__,
                      self.square_frame.winfo_height(),
                      self.square_frame.winfo_width()))
        self.layout_func(self.squares,
                         self.square_frame.winfo_height(),
                         self.square_frame.winfo_width())
