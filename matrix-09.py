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
    columns = [random.randint(0, sh - 1) for _ in range(sw)]

    while True:
        # x = random.randint(0, sh - 1)
        # y = random.randint(0, sw - 1)

        stdscr.clear()
        for i in range(sw):
            char = random.choice("01")

            try:
                if 0 <= columns[i] < sh:
                    stdscr.addstr(columns[i], i, char, curses.color_pair(1))
            except curses.error:
                columns[i] = random.randint(0, sh - 1)
                stdscr.addstr(columns[i], i, char, curses.color_pair(1))

            if columns[i] > sh:
                columns[i] = 0
            else:
                columns[i] += 1
                
        # stdscr.refresh()
        time.sleep(0.05)

        key = stdscr.getch()
        if key != -1 and key == ord("q"):
            break

curses.wrapper(matrix_effect)