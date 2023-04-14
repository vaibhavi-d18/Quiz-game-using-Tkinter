from tkinter import *
from tkinter import messagebox as mb

class Quiz:
    def __init__(self):
        self.qno = 0
        self.disp_title()
        self.disp_ques()
        self.opt_sel = IntVar()
        self.opts = self.radio_buttons()
        self.disp_opt()
        self.buttons()
        self.total_size = len(question)
        self.correct = 0

    # display title function
    def disp_title(self):
        title = Label(
                ws,
                text="Python QUIZ",
                width=50,
                bg="#45458B",
                fg="white",
                font=("ariel", 20, "bold")
        )
        title.place(x=0, y=2)

    # display question function
    def disp_ques(self):
        qno = Label(
            ws,
            text=question[self.qno],
            width=60,
            font=('ariel', 16, 'bold'),
            anchor='w',
            wraplength=700,
            justify='center'
        )
        qno.place(x=70, y=100)
        
    # display option function
    def disp_opt(self):
        val = 0
        self.opt_sel.set(0)

        for option in options[self.qno]:
            self.opts[val]['text'] = option
            val += 1

    # radio button function
    def radio_buttons(self):
        q_list = []
        y_pos = 150

        while len(q_list) < 4:
            radio_btn = Radiobutton(
                ws,
                text=" ",
                variable=self.opt_sel,
                value=len(q_list) + 1,
                font=("ariel", 14)
            )
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list
    
    # check answer function
    def check_ans(self, qno):

        if self.opt_sel.get() == answer[qno]:
            return True
        
    # next and quit button
    def buttons(self):
        next_button = Button(
            ws,
            text="Next",
            command=self.next_btn,
            width=10,
            bg="#45458B",
            fg="white",
            font=("ariel", 16, "bold")
        )

        next_button.place(x=350, y=380)

        quit_button = Button(
            ws,
            text="Quit",
            command=ws.destroy,
            width=5,
            bg="black",
            fg="white",
            font=("ariel", 16, " bold")
        )
        quit_button.place(x=700, y=50)

    # next button function
    def next_btn(self):

        if self.check_ans(self.qno):
            self.correct += 1

        self.qno += 1

        if self.qno == self.total_size:
            self.disp_res()
            ws.destroy()
        else:
            self.disp_ques()
            self.disp_opt()
            
    # display result function
    def disp_res(self):
        
        correct = f"Correct: {self.correct}"
        wrong_count = self.total_size - self.correct
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.total_size * 100)
        result = f"Score: {score}%"

        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


ws = Tk()
ws.geometry("800x450")
ws.resizable(0,0)
ws.title("Python Quiz")


question = [
      "Q1. Who developed Python Programming Language?",
      "Q2. Which type of Programming does Python support?",
      "Q3. Which of the following functions can find version of python?",
      "Q4. What does pip stand for python?",
      "Q5. Which of the following functions is a built-in function in python?",
      "Q6. Which of these is the definition for packages in Python?",
      "Q7. In which language is Python written?",
      "Q8. Which of the following precedence order is correct in Python?",
      "Q9. What happens when '2' == 2 is executed?",
      "Q10. Which one of these is incorrect?"]
options = [
      ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
      ["object-oriented programming", "structured programming", " functional programming", "all of the mentioned"],
      ["sys.version(1)", "sys.version(0)", "sys.version()", "sys.version"],
      ["Pip Installs Python", "Pip Installs Packages", "Preferred Installer Program", " None of the mentioned"],
      ["factorial() ","print() ","seed() ","sqrt()"],
      ["A set of main modules ","A folder of python modules","A number of files containing Python definitions and statements ","A set of programs making use of Python modules"],
      ["C","PHP ","Java ","All of the above"],
      ["Parentheses, Exponential, Multiplication, Division, Addition, Subtraction",
        "Multiplication, Division, Addition, Subtraction, Parentheses, Exponential",
        "Division, Multiplication, Addition, Subtraction, Parentheses, Exponential",
        "Exponential, Parentheses, Multiplication, Division, Addition, Subtraction"],
      ["False","True","ValueError occurs","TypeError occurs"],
      [" float('nan')","float('inf')","float('12+34')","float('56'+'78')"]
    ]
answer = [3, 4, 4, 3, 2, 2, 1, 1, 1, 3]

quiz = Quiz()
ws.mainloop()
