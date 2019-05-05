import tkinter
import subprocess
import cv2
import PIL.Image, PIL.ImageTk
import time, os
from PIL import ImageTk, Image
import csv

tk = tkinter.Tk()
tk.title("Automatic Number Plate Recognization")
tk.geometry("1280x720")

image = Image.open('bc3.jpg')
photo_image = ImageTk.PhotoImage(image)
label = tkinter.Label(tk, image=photo_image)
label.place(y=-600)

from tkinter import *
from tkinter import font

helv36 = font.Font( size=16)


class App:
	def __init__(self, window, window_title, video_source, images='test'):
		self.window = window
		self.window.title(window_title)
		self.video_source = video_source
		self.images = images
		self.vid = MyVideoCapture(self.video_source)
		self.canvas = tkinter.Canvas(window, width=self.vid.width, height=self.vid.height)
		self.canvas.place(x=50, y=50)
		self.canvas.config(bd=1, bg='navy',relief=RAISED)
		self.btn_snapshot = tkinter.Button(window, text="Capture Image", bg="lawn green",
										   activebackground="red", command=self.snapshot)
		self.btn_snapshot.place(x=750, y=55, width=500, height=50)
		self.btn_snapshot.config(bd=6, relief=RAISED, width=50, font=helv36)
		self.delay = 15
		self.update()
		self.window.mainloop()

	def snapshot(self):
		ret, frame = self.vid.get_frame()
		name = '/home/nineleaps/helmet/yolov3-Helmet-Detection/test/' + "helmet-" + time.strftime(
			"%d-%m-%Y-%H-%M-%S") + ".jpeg"
		print('Creating...' + name)
		if ret:
			cv2.imwrite(name, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

	def update(self):
		ret, frame = self.vid.get_frame()
		if ret:
			self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
			self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
		self.window.after(self.delay, self.update)

class gui:
	def __init__():
		print ("start")

	def execute():
		subprocess.call('./start.sh ', shell=True)

	def imagee():
		subprocess.call('./input.sh', shell=True)

	def out():
		subprocess.call('./output.sh', shell=True)

	def report():
		# subprocess.call('./report.sh', shell=True)
		with open("/tmp/output/results.csv") as file:
			reader = csv.reader(file)
			data = []
			rr=50
			cc=550
			for col in reader:
				data.append(col)
				label = tkinter.Label(tk,bd=4,relief=RAISED, width=170,bg="lawn green", height=2, text=col)
				label.place(x=rr, y=cc)
				cc +=30

	def quit():
		tk.destroy()

	E = tkinter.Button(tk, text="Exit", bg="lawn green", activebackground="red", command=quit)
	E.place(x=750, y=480, width=500, height=50)
	E.config(bd=6, relief=RAISED, width=50, font=helv36, )

	D = tkinter.Button(tk, text="Report", bg="lawn green", activebackground="red", command=report)
	D.place(x=750, y=395, width=500, height=50)
	D.config(bd=6, relief=RAISED, width=50, font=helv36, )

	C = tkinter.Button(tk, text="Output Images", bg="lawn green", activebackground="red", command=out)
	C.place(x=750, y=310, width=500, height=50)
	C.config(bd=6, relief=RAISED, width=50, font=helv36, )

	B = tkinter.Button(tk, text="Run Program", bg="lawn green", activebackground="red", command=execute)
	B.place(x=750, y=235, width=500, height=50)
	B.config(bd=6, relief=RAISED, width=50, font=helv36, )

	A = tkinter.Button(tk, text="Input image", bg="lawn green", activebackground="red", command=imagee)
	A.place(x=750, y=145, width=500, height=50)
	A.config(bd=6, relief=RAISED, width=50, font=helv36, )


class MyVideoCapture:
	def	__init__(self, video_source):
		# Open the video source
		self.vid = cv2.VideoCapture(video_source)
		self.dir_path = os.path.exists('test')
		try:
			if not self.dir_path:
				os.makedirs('test')
		except OSError:
			print('Error: Creating directory of data')

		if not self.vid.isOpened():
			raise ValueError("Unable to open video source", video_source)

		self.width = 640
		self.height = 480

	def get_frame(self):
		if self.vid.isOpened():
			ret, frame = self.vid.read()

			if ret:
				return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
			else:
				return (ret, None)
		else:
			return (ret, None)

	def __del__(self):
		if self.vid.isOpened():
			self.vid.release()



App(tk, "Automatic Number Plate Recognization", "http://192.168.1.105:4747/mjpegfeed?640x480")

