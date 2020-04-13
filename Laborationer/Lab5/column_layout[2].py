#!/usr/bin/env python3
"""Laboration 5 -- TDDE44

Exempel på slumpmässig layout-funktion. Layout-funktionen skickas som
argument när en instans av lab5.LayoutTester skapas.
"""

import lab5
import random
import math

"""Denna funktion används för att placera ut kvadraterna i y-led"""
def plot_squares(squares, square_size, xpos, square_marginal):
    ypos = square_marginal
    for square in squares:
        square.place(x=xpos, y=ypos)
        ypos += square_size + square_marginal

"""Denna funktion räknar ut hur många kvadrater (med mellanrum)
det får plats i y-led"""
def number_of_squares_generator(square_size, frame_width, frame_height, square_marginal):
    x_max = math.floor(frame_width / (square_marginal + square_size))
    y_max = math.floor(frame_height / (square_marginal + square_size))
    max = [x_max, y_max]
    return max

"""list_chopper används för att dela upp squares i listor som är lika
långa som antalet kvadrater det får plats i y-led"""
def list_chopper(squares, number_of_squares):
    i = 0
    chopped_list = []
    if number_of_squares[1] > len(squares):
        pass
    while i < len(squares):
        chopped_list.append(list(squares[i:i + number_of_squares[1]]))
        i += number_of_squares[1]
        if i + number_of_squares[1] > len(squares):
            chopped_list.append(squares[i:])
            return chopped_list

"""Huvudfunktionen som kallar på de tidigare funktionerna för
att placera ut kvadraterna"""
def column_layout(squares, frame_height, frame_width):
    square_size = squares[0].winfo_width()
    square_marginal = square_size / 4
    number_of_squares = number_of_squares_generator(square_size,
                                                    frame_width,
                                                    frame_height,
                                                    square_marginal)
    xpos = square_marginal
    if list_chopper(squares, number_of_squares):
        plot_squares(squares, square_size, x_pos, square_marginal)
    for chopped_list in list_chopper(squares, number_of_squares):
        if xpos + square_size < frame_width:
            plot_squares(chopped_list, square_size, xpos, square_marginal)
            xpos += square_size + square_marginal


if __name__ == "__main__":
    layout_tester = lab5.LayoutTester(column_layout)
