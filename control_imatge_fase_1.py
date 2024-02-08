from tkinter import *
import cv2 as cv

from PIL import Image
from PIL import ImageTk





def takeVideoButtonClick ():
    global cap
    global window, id
    _, frame = cap.read()
    frame = cv.resize(frame, (360, 240))
    cv.imshow("video", frame)
    cv.waitKey(1)
    id = window.after(10, takeVideoButtonClick)

def stopVideoButtonClick ():
    global takingVideo
    global window, id
    window.after_cancel(id)
    cv.destroyWindow ('video')


def takePictureButtonClick ():
    global cap
    _, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    image = Image.fromarray(frame)
    max_size = (400, 300)
    image.thumbnail(max_size)
    picturePanel.image = ImageTk.PhotoImage(image)
    picturePanel.create_image(0, 0, anchor=NW, image=picturePanel.image)


window = Tk()
window.geometry("400x400")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

cap = cv.VideoCapture(0)


takeVideoButton = Button(window, text="Toma video", bg='red', fg="white",command=takeVideoButtonClick)
takeVideoButton.grid(row=0, column=0, padx=5, pady=5, sticky=N + S + E + W)

stopVideoButton = Button(window, text="Stop videon", bg='red', fg="white",command=stopVideoButtonClick)
stopVideoButton.grid(row=0, column=1, padx=5, pady=5, sticky=N + S + E + W)


takePictureButton = Button(window, text="Toma foto", bg='red', fg="white",command=takePictureButtonClick)
takePictureButton.grid(row=1,column=0, columnspan = 2, padx=5, pady=5, sticky=N + S + E + W)
picturePanel = Canvas(window)
picturePanel.grid(row=2,column =0, columnspan = 2, sticky=N + S + E + W)


window.mainloop()


