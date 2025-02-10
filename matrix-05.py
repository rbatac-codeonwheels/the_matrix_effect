import curses
import random

def matrix_effect(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    while True:
        x = random.randint(0, 20)
        y = random.randint(0, 20)

        stdscr.clear()
        try:
            stdscr.addstr(x, y, random.choice("01"), curses.color_pair(1))
        except curses.error:
            x = random.randint(0, 20)
            y = random.randint(0, 20)

        stdscr.refresh()

        key = stdscr.getch()
        if key != -1 and key == ord("q"):
            break

curses.wrapper(matrix_effect)