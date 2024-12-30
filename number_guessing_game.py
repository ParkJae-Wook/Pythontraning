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
        up_button.config(state="normal")
        down_button.config(state="normal")
    
    def check_guess(self):
        if self.guess_num < self.com_num:
            input_label.config(text="UP!")
        elif self.guess_num > self.com_num:
            input_label.config(text="DOWN!")    
        else:
            messagebox.showinfo("알림", "정답입니다!")
            return
                      
        self.com_guess = random.randint(self.min, self.max)
        com_num_label.config(text=str(self.com_guess))
        if self.com_guess == self.mynum:
            messagebox.showinfo("알림", "컴퓨터가 정답을 맞췄습니다!")
            return
        com_label.config(text="UP or DOWN?")

    def on_enter(self,event):
        
        if label.cget("text") == "1부터 100 사이의 숫자를 맞춰보세요.":
            messagebox.showinfo("알림", "게임을 시작해주세요")
            return
        elif self.mynum == 0:
            try:
                self.mynum=int(entry.get())
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
        elif self.turn == 1:
            messagebox.showinfo("알림", "UP! 또는 DOWN! 버튼을 눌러주세요.") #컴퓨터 턴일때 숫자를 입력하면 오류 출력
            return
        else:
            try:
                self.guess_num=int(entry.get())
            except ValueError:
                messagebox.showinfo("알림", "숫자를 입력해주세요.")
                entry.delete(0, "end")
                entry.focus()
                return
            input_num_label.config(text=entry.get())
            self.check_guess()
            self.turn=1
            entry.delete(0, "end")
            entry.focus()

    def on_click(self,event):
        text = event.widget.cget("text")
        if text == "시작" or text == "다시 시작":
            self.start_game()
        elif label.cget("text") == "1부터 100 사이의 숫자를 맞춰보세요.":
            messagebox.showinfo("알림", "게임을 시작해주세요")
            return
        elif self.mynum == 0:
            messagebox.showinfo("알림", "컴퓨터가 맞출 숫자를 입력해주세요.")
            return   
        elif self.turn == 0:
            messagebox.showinfo("알림", "당신 차례입니다. 숫자를 입력해주세요.")
            up_button.config(state="normal")
            down_button.config(state="normal")
            return
        elif text == "UP!" and self.com_guess < self.mynum:
            com_label.config(text="UP!")
            self.min=int(com_num_label.cget("text"))
            self.turn=0            
        elif text == "DOWN!" and self.com_guess > self.mynum:
            com_label.config(text="DOWN!")
            self.max=int(com_num_label.cget("text"))
            self.turn=0
        else:
            messagebox.showinfo("알림", "잘못된 입력입니다.")
            up_button.config(state="normal")
            down_button.config(state="normal")
            return
        

    


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

#입력칸


up_button = tk.Button(window, text='UP!', font=("Arial", 15),width=3, bg="lightgray", fg="black")
up_button.grid(row=5, column=0,columnspan=2,sticky ='news' , padx=2, pady=2)

down_button = tk.Button(window, text='DOWN!', font=("Arial", 15),width=3, bg="lightgray", fg="black")
down_button.grid(row=5, column=2,columnspan=2,sticky ='news' , padx=2, pady=2)

start_button = tk.Button(window, text='시작', font=("Arial", 15),width=3, bg="lightgray", fg="black")
start_button.grid(row=6, column=0,columnspan=4,sticky ='news' , padx=2, pady=2)

#버튼들

run_game = RunGame()
entry.bind("<Return>", run_game.on_enter)
up_button.bind("<Button-1>", run_game.on_click)
down_button.bind("<Button-1>", run_game.on_click)
start_button.bind("<Button-1>", run_game.on_click)
window.mainloop()