import random,tkinter as tk
from tkinter import messagebox


class RunGame:
    
    def start_game(self):
        label.config(text="컴퓨터가 맞출 숫자를 입력하세요.")
        mynum_label.config(text="0")
        com_num_label.config(text="0")
        input_num_label.config(text="0")
        input_label.config(text=" ")
        com_label.config(text=" ")
        self.mynum = 0
        self.com_num = random.randint(1, 100)
        self.guess_num = 0
        self.turn = 0
        self.min = 1
        self.max = 100
        entry.delete(0, "end")
        entry.focus()
        start_button.config(text="다시 시작")
    def __init__(self):
        self.mynum = 0
        self.com_num = 0
        self.guess_num = 0
        self.turn = 0
        self.min = 1
        self.max = 100        
    def set_mynum(self,num):
        self.mynum = num
    def set_comnum(self,num):
        self.com_num = num
    def set_guessnum(self,num):
        self.guess_num = num
    def set_turn(self,num):
        self.turn = num
    def set_min(self,num):
        self.min = num
    def set_max(self,num):
        self.max = num
    def get_mynum(self):
        return self.mynum
    def get_comnum(self):
        return self.com_num
    def get_guessnum(self):
        return self.guess_num
    def get_turn(self):
        return self.turn
    def get_min(self): 
        return self.min
    def get_max(self):
        return self.max
    
def check_guess():
    com_num = int(run_game.get_comnum)
    n = int(run_game.get_guessnum)
    mn = int(run_game.get_mynum)
    if n < com_num:
        input_label.config(text="UP!")
    elif n > com_num:
        input_label.config(text="DOWN!")    
    else:
        messagebox.showinfo("알림", "정답입니다!")
        return
                      
    com_guess = random.randint(run_game.get_min, run_game.get_max)
    com_num_label.config(text=str(com_guess))
    if com_guess == mn:
        messagebox.showinfo("알림", "컴퓨터가 정답을 맞췄습니다!")
        return
    com_label.config(text="UP or DOWN?")

def on_enter(event):
    
    if label.cget("text") == "1부터 100 사이의 숫자를 맞춰보세요.":
        messagebox.showinfo("알림", "게임을 시작해주세요")
        return
    elif mynum_label.cget("text") == "0":
        try:
            run_game.set_mynum(int(entry.get()))
        except ValueError:
            messagebox.showinfo("알림", "숫자를 입력해주세요.")
            entry.delete(0, "end")
            entry.focus()
            return
        mynum_label.config(text=entry.get())
        label.config(text="컴퓨터가 맞춰야 할 숫자")
        input_num_label.config(text="뭐게?")
        entry.delete(0, "end")
        entry.focus()
        return
    elif run_game.get_turn() :
        messagebox.showinfo("알림", "UP! 또는 DOWN! 버튼을 눌러주세요.")
        return
    else:
        try:
            run_game.set_guessnum(int(entry.get()))
        except ValueError:
            messagebox.showinfo("알림", "숫자를 입력해주세요.")
            entry.delete(0, "end")
            entry.focus()
            return
        input_num_label.config(text=entry.get())
        check_guess()
        run_game.set_turn(1)
        entry.delete(0, "end")
        entry.focus()

def on_click(event):
    text = event.widget.cget("text")
    if text == "UP!":
        if int(com_num_label.cget("text")) < int(mynum_label.cget("text")):
            com_label.config(text="UP!")
            run_game.set_max(int(com_num_label.cget("text")))
            run_game.set_turn(0)
        else:
            messagebox.showinfo("알림", "잘못된 입력입니다.")
            return
    elif text == "DOWN!":
        if int(com_num_label.cget("text")) > int(mynum_label.cget("text")):
            com_label.config(text="DOWN!")
            run_game.set_min(int(com_num_label.cget("text")))
            run_game.set_turn(0)
        else:
            messagebox.showinfo("알림", "잘못된 입력입니다.")
            return
    elif text == "시작" or text == "다시 시작":
        run_game.start_game()
    else:
        print("Error")
        

    


window = tk.Tk()
window.title("숫자 맞추기 게임!")
window.geometry("280x250")
window.resizable(0, 0)
#창 생성

label = tk.Label(window, text="1부터 100 사이의 숫자를 맞춰보세요.", font=("Arial", 13),width=30)
label.grid(row=0, column=0, columnspan=4,sticky='news')
#게임 설명 라벨

mynum_label = tk.Label(window, text="my0", font=("Arial", 20),anchor="center",width=10,fg="red")
mynum_label.grid(row=1, column=0,columnspan=4,sticky='news')
#내가 입력한 숫자 라벨

com_num_label = tk.Label(window, text="0", font=("Arial", 20),anchor="center",width=7,fg="blue")
com_num_label.grid(row=2, column=2,columnspan=2,sticky='news')
com_label = tk.Label(window, text="com", font=("Arial", 10),width=7,fg="blue")
com_label.grid(row=3, column=2,columnspan=2,sticky='news')
#컴퓨터가 제시하는 숫자

input_num_label = tk.Label(window, text="0", font=("Arial", 20),anchor="center",width=7)
input_num_label.grid(row=2, column=0,columnspan=2,sticky='news')
input_label = tk.Label(window, text="com", font=("Arial", 20),width=7)
input_label.grid(row=3, column=0,columnspan=2,sticky='news')
#내가 입력할 숫자와 결과

entry = tk.Entry(window, font=("Arial", 15),width=3)
entry.grid(row=4, column=1,columnspan=2,sticky='news')
entry.bind("<Return>", on_enter)
#입력칸


up_button = tk.Button(window, text='UP!', font=("Arial", 15),width=3, bg="lightgray", fg="black")
up_button.grid(row=5, column=0,columnspan=2,sticky ='news' , padx=2, pady=2)
up_button.bind("<Button-1>", on_click)
down_button = tk.Button(window, text='DOWN!', font=("Arial", 15),width=3, bg="lightgray", fg="black")
down_button.grid(row=5, column=2,columnspan=2,sticky ='news' , padx=2, pady=2)
down_button.bind("<Button-1>", on_click)
start_button = tk.Button(window, text='시작', font=("Arial", 15),width=3, bg="lightgray", fg="black")
start_button.grid(row=6, column=0,columnspan=4,sticky ='news' , padx=2, pady=2)
start_button.bind("<Button-1>", on_click)
#버튼들

run_game = RunGame()

window.mainloop()