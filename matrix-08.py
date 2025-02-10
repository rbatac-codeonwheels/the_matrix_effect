import curses
import random
import time

def matrix_effect(stdscr):
    curses.curs_set(0)
    stdscr.timeout(100)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    sh, sw = stdscr.getmaxyx()

    while True:
        x = random.randint(0, sh - 1)
        y = random.randint(0, sw - 1)

        stdscr.clear()
        try:
            stdscr.addstr(x, y, random.choice("01"), curses.color_pair(1))
        except curses.error:
            x = random.randint(0, sh - 1)
            y = random.randint(0, sw - 1)

        # stdscr.refresh()
        time.sleep(0.05)

        key = stdscr.getch()
        if key != -1 and key == ord("q"):
            break

curses.wrapper(matrix_effect)