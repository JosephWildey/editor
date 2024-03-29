# editor

This is a simple editor I wrote in Python with Tkinter. It's pretty barebones in terms of functionality, but aside from most of the typical stuff word editors have it includes the following:

- Word count
- Word frequency

It uses regex to pull words out of the content. It might still overcount, I have not tested it thoroughly. It also breaks formatting at the moment when a file is opened. However, it will now count hyphenated words as one word. I have plans to expand this project, but school has a way of getting in the way and being super stressful.


![editor2](https://user-images.githubusercontent.com/19524084/113521255-4c0c2800-9566-11eb-9f1e-1fab421be472.png)

# Future plans
I've got a kanban board set up to keep myself on track, but I'll share some of my ideas. 

- Improve the GUI (make the popup scrollable. Eventually consider overhauling layout)
- Improve the architecture (improve efficiency, code readability, code maintability, and possibly change some behaviors)
- Implement typical office tools into the word editor directly (e.g. launch independent calculator from menubar w/ option to insert equations or results into textbox. Not limited to a calculator.)
- cloud synchronization (made for school projects after all)
- improve analysis output (make it prettier, easier to read, etc)
- email functionality (no guarantees on GMail implementation)

# Run down/code review
You can find a rundown and review of the code written on my website, if you want more information about the project or how I'm approaching things: https://joewildey.com/2021/04/12/python-word-editor-pt1/
