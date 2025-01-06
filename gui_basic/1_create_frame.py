from tkinter import *
import tkinter.ttk as ttk,os
from tkinter import messagebox

root = Tk()
root.title("제목없음 - Windows 메모장") 
root.geometry("640x480+100+300") #가로 *세로 +창이 뜨는 위치 x좌표, +창이 뜨는 위치 y좌표
menu = Menu(root)
path = os.path.dirname(__file__)
file_name = path+"/mynote.txt"

def openfile():
    if os.path.isfile(file_name):
        with open(file_name,"r",encoding="euc-kr") as file:
            txt.delete("1.0",END)
            txt.insert(END,file.read())
    else:
        messagebox.showwarning("파일 없음","저장된 파일이 없습니다.")
def savefile():
    with open(file_name,"w") as file:
        file.write(txt.get("1.0",END))
file_menu = Menu(menu,tearoff=0)
file_menu.add_command(label="열기",command=openfile)
file_menu.add_command(label="저장",command=savefile)
file_menu.add_separator()
file_menu.add_command(label="끝내기",command=root.quit)

menu.add_cascade(label="퍄일",menu=file_menu)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)



txt = Text(root)
txt.pack(side="left",fill="both",expand=True)
scbar = Scrollbar(root,command=txt.yview)
scbar.pack(side="right",fill="y")
txt.config(yscrollcommand=scbar.set)


root.mainloop()