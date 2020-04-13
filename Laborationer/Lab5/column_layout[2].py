#!/usr/bin/env python3
import lab5
import random
import math


def random_layout(squares, frame_height, frame_width):
    """Placera ut kvadrater uppifrån och ned så länge det finns plats i ramen.
    """
    xpos = 0
    ypos = 0
    # loopa genom rutor i listan
    for square in squares:
        square_size = square.winfo_width()
        max_squares_x = math.floor(frame_width / square_size)
        max_squares_y = math.floor(frame_height / square_size)
        x_marginal = (frame_width % square_size) / (max_squares_x - 1)
        y_marginal = (frame_height % square_size) / (max_squares_y - 1)
        # sätt in en kvadrat om det finns plats i y-led
        if ypos + square_size <= frame_height:
            square.place(x=xpos, y=ypos)
            ypos += square_size + y_marginal
        else:
            # annars, öka x-led, börja om i y-led, sätt in en kvadrat,
            # öka y-led
            if xpos + square_size <= frame_width:
                xpos += square_size + x_marginal
                ypos = 0
                square.place(x=xpos, y=ypos)
                ypos += square_size + y_marginal


if __name__ == "__main__":
    layout_tester = lab5.LayoutTester(random_layout)
