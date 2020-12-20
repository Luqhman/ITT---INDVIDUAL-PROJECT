import socket
import os
import curses
import time
import sys


def chose_button(stdscr, row_idx,):
	menu = ["Try another quote", "Exit"]
	h,w = stdscr.getmaxyx()
	for idx, row in enumerate(menu):
		x = w//2 - len(row)//2
		y = h//2 - len(menu)//2 + idx + 8
		if idx == row_idx:
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(y,x,row)
			stdscr.attroff(curses.color_pair(1))
		else:
			stdscr.addstr(y,x,row)
	stdscr.refresh()


def main(stdscr):
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)


	host = '192.168.43.100'
	port = 17
	h,w = stdscr.getmaxyx()
	x = w//2
	y = h//2
	cur_row_idx = 0

	wel= "Welcome to Quote of the day application"

	print('waiting for connection')

	while True:

		stdscr.clear()
		cSock = socket.socket()
		chose_button(stdscr,cur_row_idx)
		stdscr.addstr(10,x - len(wel)//2,wel)
		try:
			cSock.connect((host,port))
		except socket.error as e:
			print(str(e))

		res = cSock.recv(1024)
		res2 = res.decode('utf-8')
		stdscr.addstr(y,x - len(res2)//2,res2)

		cSock.close()


		while True:

			key = stdscr.getch()
			if key == curses.KEY_UP and cur_row_idx == 1:
				cur_row_idx -= 1
			elif key == curses.KEY_DOWN and cur_row_idx == 0:
				cur_row_idx += 1
			elif key == curses.KEY_ENTER or key in [10,13]:
				if cur_row_idx == 0:
					break
				else:
					sys.exit()
			chose_button(stdscr,cur_row_idx)

		stdscr.refresh()

curses.wrapper(main)






