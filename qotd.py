import socket
import os
import curses
import time

from _thread import *
from random import randint


def threaded_client(connection):
	f = open('quote.txt','r')
	count = 0
	value = randint(0,33)

	for x in f:
		if count == value:
			connection.send(str.encode(x))
			break
		else:
			count +=1
	x = ""
	connection.close()


def main(stdscr):

	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	s = socket.socket()
	host = ''
	port = 17
	Tcount = 0
	h,w = stdscr.getmaxyx()
	x = w//2
	y = h//2

	try:
		s.bind((host,port))
	except socket.error as e:
		print(str(e))
	time.sleep(1)

	stdscr.clear()
	s.listen(5)
	wai = "Waiting for connection . . ."
	stdscr.addstr(y,x - len(wai)//2,wai)
	stdscr.refresh()
	stdscr.clear()

	welcome = 'Welcome to Quote of The Day Server'
	sum = 'qotd server will sent a quote everytime client ask for connection'
	con = 'Connection IP                    ID                    Thread Number'


	stdscr.addstr(5,x - len(welcome)//2,welcome)
	stdscr.addstr(6,x - len(sum)//2,sum)
	stdscr.addstr(10,x - len(con)//2,con)

	while True:
		client, add = s.accept()
		start_new_thread(threaded_client,(client,))
		Tcount += 1
		dis_con = add[0] + "                   " + str(add[1]) + "                         " + str(Tcount)
		stdscr.addstr(12+Tcount,x - len(con)//2,dis_con)

		stdscr.refresh()

	s.close()
curses.wrapper(main)


















