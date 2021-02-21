#!/usr/bin/python
import tkinter as tk
from tkinter.messagebox import showinfo
import re
from collections import Counter

window = tk.Tk()

text_box = tk.Text()

text_box.pack()

label = tk.Label(text="Stats")

wordCountLabel = tk.Label()

label.pack()

wordCountLabel.pack()

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)
filemenu.add_command(label="New", command=text_box.delete("1.0","end"))
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Quit",command=window.quit)

menubar.add_cascade(label="File", menu=filemenu)

def get_word_count():

	userText = []

	if len(text_box.get("1.0","end")) > 1:
		userText = re.findall(r"[a-zA-Z]+", text_box.get("1.0","end"))

	output = "Word count: {}".format(len(userText))

	wordCountLabel['text'] = output

def popupmsg(msg):
	popup = tk.Tk()
	popup.wm_title("Word Frequency")
	label = tk.Label(popup, text=msg)
	label.pack()

	popup.mainloop()

def text_analysis():

	userText = []

	if len(text_box.get("1.0", "end")) > 1:
		userText = re.findall(r"[a-zA-Z]+", text_box.get("1.0", "end").upper())

	uniqueWords = Counter(userText)

	outputWord = []
	outputCount = []
	outputFrequency = []

	length = len(userText)

	for word in uniqueWords:
		if word not in outputWord:
			outputWord.append(word)
			outputCount.append(uniqueWords.get(word))
			outputFrequency.append(uniqueWords.get(word)/length)

	endpoint = len(uniqueWords)

	output = ""

	for i in range(endpoint):
		output += "Word: {}\t Count: {}\t Frequency: {}\t \n".format(outputWord[i],outputCount[i],outputFrequency[i])

	popupmsg(output)

analysisMenu = tk.Menu(menubar)
analysisMenu.add_command(label="Get word count", command = get_word_count)
analysisMenu.add_command(label="Get word frequency", command = text_analysis)

menubar.add_cascade(label="Analyze", menu=analysisMenu)

def popup_help():
	showinfo("Help", "Click on analysis to get word count or word frequency.")

def popup_about():
	showinfo("About", "Created by Joe Wildey.")

helpMenu = tk.Menu(menubar)
helpMenu.add_command(label="Help", command = popup_help)
helpMenu.add_command(label="About", command = popup_about)

menubar.add_cascade(label="Help", menu=helpMenu)

window.config(menu=menubar)

window.mainloop()
