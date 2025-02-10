import curses

def matrix_effect(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.addstr(0, 0, "Green Text", curses.color_pair(1))
    stdscr.addstr(1, 0, "Yellow Text", curses.color_pair(2))
    stdscr.refresh()

    stdscr.getch()

curses.wrapper(matrix_effect)