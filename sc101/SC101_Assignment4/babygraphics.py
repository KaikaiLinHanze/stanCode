"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    gap = int((width-2*GRAPH_MARGIN_SIZE)/len(YEARS))
    # the gap between line
    x_coordinate = year_index * gap + GRAPH_MARGIN_SIZE
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    # upper line

    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # lower line

    for i in range(len(YEARS)):
        x_position = get_x_coordinate(width=CANVAS_WIDTH, year_index=i)
        canvas.create_line(x_position, 0, x_position, CANVAS_HEIGHT)
        # vertical line
        canvas.create_text(x_position+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW,
                           font="times 16")
        # add text


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        data = name_data[lookup_names[i]]
        x_position = []
        y_position = []
        for j in range(len(YEARS)):
            if str(YEARS[j]) not in data:
                data[str(YEARS[j])] = 0
            if int(data[str(YEARS[j])]) == 0:
                y_position.append(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
            else:
                y_position.append(GRAPH_MARGIN_SIZE + (int(data[str(YEARS[j])])/1000)*(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE))
            x_position.append(get_x_coordinate(width=CANVAS_WIDTH, year_index=j))
        for k in range(len(YEARS)):
            color_type = i % len(COLORS)
            if data[str(YEARS[k])] == 0:
                data[str(YEARS[k])] = "*"
            if k + 1 < len(YEARS):
                canvas.create_line(x_position[k], y_position[k], x_position[k+1], y_position[k+1],
                                   fill=COLORS[color_type])
                canvas.create_text(x_position[k] + TEXT_DX, y_position[k], text=lookup_names[i] +
                                    str(data[str(YEARS[k])]), anchor=tkinter.SW, font="times 16",
                                   fill=COLORS[color_type])
            else:
                canvas.create_text(x_position[k] + TEXT_DX, y_position[k], text=lookup_names[i] +
                                    str(data[str(YEARS[k])]), anchor=tkinter.SW, font="times 16",
                                   fill=COLORS[color_type])



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
