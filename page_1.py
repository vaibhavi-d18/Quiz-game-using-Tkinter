from tkinter import *

ws = Tk()
ws.geometry('800x450')
ws.resizable(0,0)
ws.title('PythonQuiz')

def nextPage():
    ws.destroy()
    import quiz_game

text = Label(ws,text="Welcome to the quiz game",font=("Comic sans MS", 24, "bold"),bg="#45458B",fg="white" )
text.pack(fill=X)

img1 = PhotoImage(file="C:/Users/HP/Downloads/quizimage.png")
labelimage = Label(
    ws,
    image = img1,
    background = "#ffffff",
)

labelimage.pack(pady=(50))

Rules = Label(ws,
text="Read the following instructions carefully:\nThis quiz contains 10 questions\nFor every question select correct option and click next\nAfter all questions are completed result will be displayed",
   width=50,font=("aerial", 14), bg="#999DA0",foreground="black",
        )
Rules.pack(pady=(3))

start=Button(
    ws,
    text="Start Quiz",
    fg="white",bg="#45458B",
    command=nextPage,
    height=1,
    width=10,
    font=("Calibra",15,"bold")
)
start.pack(pady=(20))

ws.mainloop()
