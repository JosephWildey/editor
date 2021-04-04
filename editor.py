#imports
#!/usr/bin/python - code was written on Ubuntu 20.04 LTS
import tkinter as tk
from tkinter.messagebox import showinfo
import re
from collections import Counter

#defines the main window
window = tk.Tk()

#defines a text box object
text_box = tk.Text()

#displays textbox object to screen
text_box.pack()

#defining a label for the stats of the document
label = tk.Label(text="Stats")

#defining a label for the word count of the document
wordCountLabel = tk.Label()

#displays the stats label below the textbox
label.pack()

#displays the wordcount label below the stats label and window
wordCountLabel.pack()

#defines a menubar object
menubar = tk.Menu(window)

#defines a menubar object and adds options for user interaction
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New", command=text_box.delete("1.0","end"))
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Quit",command=window.quit)

#organizes the menubar's elements into a cascade
menubar.add_cascade(label="File", menu=filemenu)

#function for getting the word count for the document
#outputs the word count of the document into the wordcount label
def get_word_count():

	#store words into array to make retrieving the count easier later
	userText = []

	#ensure that there are words in the text box before trying to get anything
	if len(text_box.get("1.0","end")) > 1:
		
		#use regex to get each individual word and stick them into the array, hyphenated words are counted as one word
		userText = re.findall(r"[a-zA-Z-]+", text_box.get("1.0","end"))

	#output the word count into the word count label
	output = "Word count: {}".format(len(userText))

	#display the output in the word count label
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
