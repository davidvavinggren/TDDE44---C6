#!/usr/bin/env python3
"""Laboration 5 -- TDDE44

Exempel på slumpmässig layout-funktion. Layout-funktionen skickas som
argument när en instans av lab5.LayoutTester skapas.
"""

# Läs denna fil för att se hur gränssnittet skapats.
import lab5
import random
import math


def random_layout(squares, frame_height, frame_width):
    """Placera ut fyrkanterna i listan squares slumpmässigt.

    Argument:
    squares      -- Lista som innehåller tkinter.Label-objekt
    frame_height -- Höjden (int) på den Fram som fyrkanterna ligger i
    frame_width  -- Bredden (int) på den Frame som fyrkanterna ligger i
    """
    xpos = 0
    ypos = 0
    for square in squares:
        square_size = square.winfo_width()
        max_squares_x = math.floor(frame_width / square_size)
        max_squares_y = math.floor(frame_height / square_size)
        x_marginal = (frame_width % square_size) / (max_squares_x - 1)
        y_marginal = (frame_height % square_size) / (max_squares_y - 1)
        if ypos + square_size <= frame_height:
            square.place(x=xpos, y=ypos)
            ypos += square_size + y_marginal
        else:
            if xpos + square_size <= frame_width:
                xpos += square_size + x_marginal
                ypos = 0
                square.place(x=xpos, y=ypos)
                ypos += square_size + y_marginal


if __name__ == "__main__":
    layout_tester = lab5.LayoutTester(random_layout)
