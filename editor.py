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

#open an askdialog box to explore and open files
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/home", title = "Select a file",
						filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))


	f = open(filename, "r")
	Lines = f.readlines()
	filename.close()
	text_box.delete(1.0, tk.END)
	text_box.insert(1.0,Lines)

#open an askdialog box to save files
def saveFiles():
	savedFile = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
	if savedFile is None:
		return

	text2save = str(text_box.get(1.0,tk.END))
	savedFile.write(text2save)
	savedFile.close()

#defines a menubar object
menubar = tk.Menu(window)

#defines a menubar object and adds options for user interaction
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New", command=text_box.delete("1.0","end"))
filemenu.add_command(label="Open", command=browseFiles)
filemenu.add_command(label="Save", command=saveFiles)
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
		userText = re.findall(r"[a-zA-Z-']+", text_box.get("1.0","end"))

	#output the word count into the word count label
	output = "Word count: {}".format(len(userText))

	#display the output in the word count label
	wordCountLabel['text'] = output

#function that launches the popup with the word frequency stuff
#takes in text as a message
def popupmsg(msg):
	#define popup object and label
	popup = tk.Tk()
	popup.wm_title("Word Frequency")
	label = tk.Label(popup, text=msg)
	label.pack()

	#add popup to the main loop, so it'll launch when triggered
	popup.mainloop()

#function that handles all the calculations and stuff
def text_analysis():

	#array to stick the text into for easy handling later on
	userText = []

	#again, make sure there is something in the text box
	if len(text_box.get("1.0", "end")) > 1:
		#using regex to get all the words again, including hyphenated ones
		userText = re.findall(r"[a-zA-Z-']+", text_box.get("1.0", "end").upper())

	#defining a variable to a counter object for the usertext array
	uniqueWords = Counter(userText)

	#three more arrays to handle and organize output into a readable fashion
	outputWord = []
	outputCount = []
	outputFrequency = []

	#get the entire length of the text in the textbox
	length = len(userText)

	#loop through the uniquewords array and examine each word
	for word in uniqueWords:
		
		#if the word is unique add it to the output word array, add it to the output count, and store the words frequency
		if word not in outputWord:
			outputWord.append(word)
			outputCount.append(uniqueWords.get(word))
			outputFrequency.append(uniqueWords.get(word)/length)

	#defines the endpoint of the unique words array for prettier code later on
	endpoint = len(uniqueWords)

	#defines output for prettier code later on
	output = ""

	#loop through all three arrays outputting stats for each individual unique word
	for i in range(endpoint):
		
		#print to screen
		output += "Word: {}\t Count: {}\t Frequency: {}\t \n".format(outputWord[i],outputCount[i],outputFrequency[i])

	#displays all the info in the popup
	popupmsg(output)

#creates another category of buttons on the menubar for analytical tools
analysisMenu = tk.Menu(menubar)
analysisMenu.add_command(label="Get word count", command = get_word_count)
analysisMenu.add_command(label="Get word frequency", command = text_analysis)

#organizes them in a cascading manner
menubar.add_cascade(label="Analyze", menu=analysisMenu)

#displays a popup that shares helpful information
def popup_help():
	showinfo("Help", "Click on analysis to get word count or word frequency.")

#gives my name
def popup_about():
	showinfo("About", "Created by Joe Wildey.")

#defines a help category on the menubar
helpMenu = tk.Menu(menubar)
helpMenu.add_command(label="Help", command = popup_help)
helpMenu.add_command(label="About", command = popup_about)

#organizes all the help stuff in a cascading manner
menubar.add_cascade(label="Help", menu=helpMenu)

#add the menu to the window
window.config(menu=menubar)

#display the window
window.mainloop()
