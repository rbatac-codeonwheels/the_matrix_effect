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
    column_states = [[] for _ in range(sw)]

    while True:
        # x = random.randint(0, sh - 1)
        # y = random.randint(0, sw - 1)

        stdscr.clear()
        for i in range(sw):
            char = random.choice("01")

            column_states[i].insert(0, (char, 1))

            if len(column_states[i]) > 10:
                column_states[i].pop()

            for j, (c, color) in enumerate(column_states[i]):
                try:
                    if 0 <= columns[i] < sh:
                        stdscr.addstr(columns[i] + j, i, c, curses.color_pair(color))
                except curses.error:
                    columns[i] = random.randint(1, sh - 2)
                    stdscr.addstr(columns[i], i, c, curses.color_pair(color))

            if columns[i] > sh or random.random() > 0.975:
                columns[i] = 0
            else:
                columns[i] += 1
                
        # stdscr.refresh()
        time.sleep(0.05)

        key = stdscr.getch()
        if key != -1 and key == ord("q"):
            break

curses.wrapper(matrix_effect)