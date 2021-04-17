import time
from pynput import keyboard
from collections import deque
import pyperclip  as pc




k1 = keyboard.Controller()
flag=0
session_selector = 0
is_pressed = False



# try: 
# 	with open("data.txt","r") as f:
# 		all_sessions = f.read.split(chr(1000))
# except:
all_sessions=[]


def copy_paste():
	flag = 1 
	k1.press(keyboard.Key.ctrl)
	k1.press('c')
	k1.release('c')
	k1.release(keyboard.Key.ctrl)
	time.sleep(0.1)
	data =  pc.paste()
	print(data)
	try:
		with open("data.txt","a") as f:
			f.write(data+chr(1000))
			# f.write("\n")
	except:
		f = open("data.txt","r+")
		f.write(data+chr(1000))
		f.close()


def paste_stuff():
	
	if flag == 0:
		try:
			with open("data.txt","r") as f:
				data =  f.read().split(chr(1000))
				pc.copy(data)
				# print(data)

		except:
			print("nothing in clipboard")
	else:
		if session_selector != 1:
			pc.copy(all_sessions[-1])
		else:
			session_selector=0

	k1.press(keyboard.Key.ctrl)
	k1.press('v')
	k1.release('v')
	k1.release(keyboard.Key.ctrl)



def Print_all_session():
	if flag == 0:
		try:
			with open("data.txt","r") as f:
				data =  f.read().split(chr(1000))
				all_sessions = data
				for i in range(len(all_sessions)):
					print("session_id {} -- {}".format((i+1),all_sessions[i]))

		except:
			print("nothing in clipboard")
	else:
		for i in range(len(all_sessions)):
			print("session_id {} -- {}".format((i+1),all_sessions[i]))

j=deque([])



def select_session(session_id):
	session_selector = 1
	print(session_id)
	try:
		with open("data.txt","r") as f:
				data =  f.read().split(chr(1000))
				all_sessions = data
		print(all_sessions)
		pc.copy(all_sessions[session_id])
	except:
		print("Enter a valid session_id")


def clear_clipboard():
	try:
		with open("data.txt","w") as f:
				data =  f.write("")
		print("clipboard cleared")



c1 = ['Press(key=Key.alt)', "Press(key='s')", "Release(key='s')"]
c2 = ['Press(key=Key.alt)', "Press(key='x')", "Release(key='x')"]
c3 = ['Press(key=Key.alt)', "Press(key='f')", "Release(key='f')"]
c4 = ['Press(key=Key.alt)', "Press(key='f')", "Release(key='f')"]
checker = ['Press(key=Key.alt)', "Press(key='x')", "Release(key='x')",
"Press(key='s')", "Release(key='s')","Press(key='f')", "Release(key='f')"]
check_2 =["Press(key='0')", "Release(key='0')", "Press(key='1')", "Release(key='1')", 
"Press(key='2')", "Release(key='2')", "Press(key='3')", "Release(key='3')", 
"Press(key='4')", "Release(key='4')", "Press(key='5')", "Release(key='5')", 
"Press(key='6')", "Release(key='6')", "Press(key='7')", "Release(key='7')",
 "Press(key='8')", "Release(key='8')", "Press(key='9')", "Release(key='9')"]

checker.extend(check_2)

# The event listener will be running in this block

with keyboard.Events() as events:

	for event in events:
		# print(event)
		
		if str(event) == 'Release(key=Key.alt)':

			is_pressed = False
			j=deque([])

		if is_pressed:
			j.append('Press(key=Key.alt)')
			is_pressed=False

		if str(event) in checker :
			j.append(str(event))
		# print(j)

		if len(j)>0 and j[0]!='Press(key=Key.alt)':
			j=deque([])

		if len(j)==3 and j[1].split("'")[1].isdigit():
			print(j)
			select_session(int(j[1].split("'")[1]))


		if event.key == keyboard.Key.esc:
			break
		
		if len(j)==3:

			if list(j)==c1:

				copy_paste()
				is_pressed = True
				j=deque([])


			elif list(j)==c2:
			
				paste_stuff()
				j=deque([])

			elif list(j)==c3:

				Print_all_session()
				j = deque([])

			elif list(j)==c4:
				clear_clipboard()

			else:
				j=deque([])





