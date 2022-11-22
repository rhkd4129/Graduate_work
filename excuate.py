from tkinter import *
import tkinter
import os
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from image_preprocessing import cvt_image_save
from tkinter_1 import Clear,mainWindow,GOClick


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException
from urllib.error import HTTPError,URLError
import time
import urllib.request
import os
import socket
import googletrans




### GUI 실행 #####

main = Tk()
mainWindow()
main.mainloop()