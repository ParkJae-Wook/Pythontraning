import tkinter as tk
from tkinter import messagebox
import time

def timer():
    
    
    try:
        end = int(entry.get())
    except ValueError:
        messagebox.showerror("입력오류","숫자를 입력해주세요.")
        return
  
    for i in range(end, 0, -1):
        label.config(text=str(i), font=("Helvetica", 30))
        window.update()
        time.sleep(1)
    label.config(text="타이머 종료!", font=("Helvetica", 24))
    messagebox.showinfo("알림","타이머 종료!")
    


window = tk.Tk()
window.title("Timer")
window.geometry("300x200")
    
label = tk.Label(window, text="타이머 프로그램입니다.", font=("Helvetica", 18))
label.pack()

entry = tk.Entry(window)
entry.pack()
    
button = tk.Button(window, text="타이머 시작", command=timer)
button.pack()
    
window.mainloop()
    