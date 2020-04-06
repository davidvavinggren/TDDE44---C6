#!/usr/bin/env python3
"""Laboration 5 -- TDDE44

Exempel på slumpmässig layout-funktion. Layout-funktionen skickas som
argument när en instans av lab5.LayoutTester skapas.
"""

# Läs denna fil för att se hur gränssnittet skapats.
import lab5
import random


def random_layout(squares, frame_height, frame_width):
    """Placera ut fyrkanterna i listan squares slumpmässigt.

    Argument:
    squares      -- Lista som innehåller tkinter.Label-objekt
    frame_height -- Höjden (int) på den Fram som fyrkanterna ligger i
    frame_width  -- Bredden (int) på den Frame som fyrkanterna ligger i
    """


    # Slumpa ut positioner för alla fyrkanter utan att de hamnar utanför framen
    for square in squares:
        square_size = square.winfo_width()
        square_margin = square_size / 10
        squares_placed_x = -1
        squares_placed_y = -1
        xpos = 0
        ypos = 0
        print (square_size)
        print (xpos + square_margin < frame_width)
        while xpos + square_margin < frame_width:
            squares_placed_x += 1
            xpos += ("""squares_placed_x *""" square_size + square_margin)

            while ypos + square_margin < frame_height:
                squares_placed_y += 1
                ypos += ("""squares_placed_y *""" square_size + square_margin)
                square.place(x=xpos, y=ypos)


if __name__ == "__main__":
    layout_tester = lab5.LayoutTester(random_layout)
