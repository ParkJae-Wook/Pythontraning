import random,tkinter as tk
from tkinter import messagebox


class RunGame:
    
    def start_game(self):
        self.mynum = 0
        self.com_num = random.randint(1, 100)
        self.guess_num = 0
        self.turn = 0
        self.min = 1
        self.max = 100
        self.label = tk.Label(window, text="컴퓨터가 맞출 숫자를 입력하세요.", font=("Arial", 13),width=30)
        self.label.grid(row=0, column=0, columnspan=4,sticky='news')
        
        self.up_button = tk.Button(window, text='UP!', font=("Arial", 15),width=3, bg="lightgray", fg="black")
        self.up_button.grid(row=5, column=0,columnspan=2,sticky ='news' , padx=2, pady=2)
        self.down_button = tk.Button(window, text='DOWN!', font=("Arial", 15),width=3, bg="lightgray", fg="black")
        self.down_button.grid(row=5, column=2,columnspan=2,sticky ='news' , padx=2, pady=2)
        self.start_button = tk.Button(window, text='다시 시작', font=("Arial", 15),width=3, bg="lightgray", fg="black",command=self.start_game)
        self.start_button.grid(row=6, column=0,columnspan=4,sticky ='news' , padx=2, pady=2)
        
        self.mynum_label = tk.Label(window, text="0", font=("Arial", 20),anchor="center",width=10,fg="red")
        self.mynum_label.grid(row=1, column=0,columnspan=4,sticky='news')
        #내가 입력한 숫자 라벨

        self.com_num_label = tk.Label(window, text="0", font=("Arial", 20),anchor="center",width=7,fg="blue")
        self.com_num_label.grid(row=2, column=2,columnspan=2,sticky='news')
        self.com_label = tk.Label(window, text=" ", font=("Arial", 10),width=7,fg="blue")
        self.com_label.grid(row=3, column=2,columnspan=2,sticky='news')
        #컴퓨터가 제시하는 숫자

        self.input_num_label = tk.Label(window, text="0", font=("Arial", 20),anchor="center",width=7)
        self.input_num_label.grid(row=2, column=0,columnspan=2,sticky='news')
        self.input_label = tk.Label(window, text=" ", font=("Arial", 20),width=7)
        self.input_label.grid(row=3, column=0,columnspan=2,sticky='news')
        #내가 입력할 숫자와 결과

        self.entry = tk.Entry(window, font=("Arial", 15),width=3)
        self.entry.grid(row=4, column=1,columnspan=2,sticky='news')
        self.entry.bind("<Return>", self.on_enter)
        self.up_button.bind("<Button-1>", self.on_click)
        self.down_button.bind("<Button-1>", self.on_click)
        self.entry.delete(0, "end")
        self.entry.focus()
   
    def __init__(self):
        self.mynum = 0
        self.com_num = 0
        self.guess_num = 0
        self.turn = 0
        self.min = 1
        self.max = 100
    
    def check_guess(self):
        if self.guess_num < self.com_num:
            self.input_label.config(text="UP!")
        elif self.guess_num > self.com_num:
            self.input_label.config(text="DOWN!")    
        else:
            messagebox.showinfo("알림", "정답입니다!")
            return
                      
        self.com_guess = random.randint(self.min, self.max)
        self.com_num_label.config(text=str(self.com_guess))
        if self.com_guess == self.mynum:
            messagebox.showinfo("알림", "컴퓨터가 정답을 맞췄습니다!")
            return
        self.com_label.config(text="UP or DOWN?")

    def on_enter(self,event):
        if self.mynum == 0:
            try:
                self.mynum=int(self.entry.get())
            except ValueError:
                messagebox.showinfo("알림", "숫자를 입력해주세요.")
                self.entry.delete(0, "end")
                self.entry.focus()
                return
            self.mynum_label.config(text=self.entry.get())
            self.label.config(text="컴퓨터가 맞춰야 할 숫자")
            self.input_num_label.config(text="뭐게?")
            self.entry.delete(0, "end")
            self.entry.focus()
            return
        elif self.turn == 1:
            messagebox.showinfo("알림", "UP! 또는 DOWN! 버튼을 눌러주세요.") #컴퓨터 턴일때 숫자를 입력하면 오류 출력
            return
        else:
            try:
                self.guess_num=int(self.entry.get())
            except ValueError:
                messagebox.showinfo("알림", "숫자를 입력해주세요.")
                self.entry.delete(0, "end")
                self.entry.focus()
                return
            self.input_num_label.config(text=self.entry.get())
            self.check_guess()
            self.turn=1
            self.entry.delete(0, "end")
            self.entry.focus()

    def on_click(self,event):
        text = event.widget.cget("text")
        if self.mynum == 0:
            messagebox.showinfo("알림", "컴퓨터가 맞출 숫자를 입력해주세요.")
            return   
        elif self.turn == 0:
            messagebox.showinfo("알림", "당신 차례입니다. 숫자를 입력해주세요.")
            self.up_button.config(state="normal")
            self.down_button.config(state="normal")
            return
        elif text == "UP!" and self.com_guess < self.mynum:
            self.com_label.config(text="UP!")
            self.min=int(self.com_num_label.cget("text"))
            self.turn=0            
        elif text == "DOWN!" and self.com_guess > self.mynum:
            self.com_label.config(text="DOWN!")
            self.max=int(self.com_num_label.cget("text"))
            self.turn=0
        else:
            messagebox.showinfo("알림", "잘못된 입력입니다.")
            self.up_button.config(state="normal")
            self.down_button.config(state="normal")
            return
        

window = tk.Tk()
window.title("숫자 맞추기 게임!")
window.geometry("275x250+800+350")
window.resizable(0, 0)
#창 생성

label3 = tk.Label(window, text="", font=("Arial", 13),width=30)
label3.grid(row=0, column=0,columnspan=4,sticky='news')
label3 = tk.Label(window, text="", font=("Arial", 13),width=30)
label3.grid(row=1, column=0,columnspan=4,sticky='news')
label3 = tk.Label(window, text="", font=("Arial", 13),width=30)
label3.grid(row=2, column=0,columnspan=4,sticky='news')
label1 = tk.Label(window, text="1부터 100 사이의 숫자를 맞춰보세요.", font=("Arial", 13),width=30)
label1.grid(row=3, column=0,columnspan=4,sticky='news')
#게임 설명 라벨


start_button1 = tk.Button(window, text='시작', font=("Arial", 15),width=3, bg="lightgray", fg="black",command=RunGame().start_game)
start_button1.grid(row=6, column=1,columnspan=2,sticky ='news' , padx=2, pady=2)
#시작버튼

run_game = RunGame()

window.mainloop()