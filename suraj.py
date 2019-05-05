import tkinter
import subprocess
import cv2
import PIL.Image, PIL.ImageTk
import time, os
from PIL import ImageTk, Image
tk= tkinter.Tk()
tk.title("Automatic Number Plate Recognization")
class App:
    def __init__(self, window, window_title, video_source, images='images'):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.images=images

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)

        
        #make a directory name data if it is not present
        self.dir_path=os.path.exists(self.images)

        
        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot=tkinter.Button(window, text="Capture Image", bg="DarkGoldenrod1", activebackground="MediumPurple1", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        
        ret, frame = self.vid.get_frame()
        name ='/home/nineleaps/helmet/yolov3-Helmet-Detection/test/' + "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpeg"
        print ('Creating...' + name)             
        
        if ret:
            cv2.imwrite(name, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()        

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)



class gui:
	def __init__():
		print
		"start"


	def run_program():
		print
		"Below is the output from the shell script in terminal"
		subprocess.call('./start.sh ', shell=True)

	def imagee():
		subprocess.call('./input.sh', shell=True)

	def out():
		subprocess.call('./output.sh', shell=True)

	def report():
		subprocess.call('./report.sh', shell=True)

	def quit():

		tk.destroy()

	E = tkinter.Button(tk, text="Exit", bg="DarkGoldenrod1",width=50, activebackground="MediumPurple1", command=quit)
	# e = ImageTk.PhotoImage(file="/home/nineleaps/alpr-unconstrained/interface/but/ee.png")
	# E.config(image=e)
	E.pack(side='bottom')

	#D = tkinter.Button(tk, text="Report", bg="DarkGoldenrod1",width=50, activebackground="MediumPurple1", command=report)
	# d = ImageTk.PhotoImage(file="/home/nineleaps/alpr-unconstrained/interface/but/dd.png")
	# D.config(image=d)
	#D.pack(side='bottom')

	C = tkinter.Button(tk, text="Output Images", bg="DarkGoldenrod1",width=50,  activebackground="MediumPurple1", command=out)
	# c = ImageTk.PhotoImage(file="/home/nineleaps/alpr-unconstrained/interface/but/cc.png")
	# C.config(image=c)
	C.pack(side='bottom')

	B = tkinter.Button(tk, text="Run Program", bg="DarkGoldenrod1", width=50,activebackground="MediumPurple1",
					   command=run_program)
	# b = ImageTk.PhotoImage(file="/home/nineleaps/alpr-unconstrained/interface/but/bb.png")
	# B.config(image=b)
	B.pack(side='bottom')

	A = tkinter.Button(tk, text="Input image",bg="DarkGoldenrod1", width=50 ,activebackground="MediumPurple1", command=imagee)
	# a = ImageTk.PhotoImage(file="/home/nineleaps/alpr-unconstrained/interface/but/aa.png")
	#A.config(image=a)
	A.pack(side='bottom')










class MyVideoCapture:
    def __init__(self, video_source):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        self.dir_path=os.path.exists('test')
        try:
            if not self.dir_path:
                os.makedirs('test')
        except OSError:
            print ('Error: Creating directory of data')

        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()

            if ret:
                # Return a boolean success flag and the current frame converted to GRAY
                return (ret,frame)
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Create a window and pass it to the Application object
App(tk,"Real Time Helmet Detection","http://192.168.1.105:4747/mjpegfeed?640x480")
























