import curses

stdscr = curses.initscr()

stdscr.clear()
stdscr.addstr(0, 0, "Green Text")
stdscr.addstr(1, 0, "Yellow Text")
stdscr.refresh()

stdscr.getch()
curses.endwin()