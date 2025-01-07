from tkinter import *
from tkinter import filedialog,messagebox
import tkinter.ttk as ttk,os
from PIL import Image

def add_files():
    files =filedialog.askopenfilenames(title="이미지 파일을 선택하세요",filetypes=(("JPG파일","*.jpg"),("PNG 파일","*.png"),("BMP 파일","*.bmp"))\
                                        ,initialdir="C:/자바학습/SampleProject/images")
    for file in files:
        image_list.insert(END,file)
def del_files():
    for index in reversed(image_list.curselection()):
        image_list.delete(index)
def find_directory():
    folder = filedialog.askdirectory(title="저장경로를 설정해주세요",initialdir="C:/Python/Mygit/Pythontraning")
    if folder =='':
        return
    path_entry.delete(0,END)
    path_entry.insert(0,folder)
def start_mer():
    try:
        selected_width = width_combobox.get()
        selected_term = term_combobox.get()
        if selected_term=="좁게":
            selected_term=30
        elif selected_term=="보통":
            selected_term=60
        elif selected_term=="넓게":
            selected_term = 90
        else :
            selected_term = 0
        selected_format = format_combobox.get().lower()
        
        images = [Image.open(x) for x in image_list.get(0,END)]
        if selected_width =="원본유지":
            selected_width = -1
        else :
            selected_width = int(selected_width)
        image_sizes = []
        if selected_term>-1:
            image_sizes = [(int(selected_width),int(selected_width*x.size[1]/x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0],x.size[1]) for x in images]
        
        widths ,heights= zip(*(image_sizes))
        
        max_width, total_height = max(widths), sum(heights)+(selected_term*(len(images)-1))
        
        result_image = Image.new("RGB",(max_width,int(total_height)),(255,255,255))
        y_offset = 0
        for idx,img in enumerate(images):
            if selected_width>-1:
                img = img.resize(image_sizes[idx])
            result_image.paste(img,(0,y_offset))
            y_offset+=(img.size[1]+selected_term)
            
            progress = (idx+1)/len(images)*100
            p_var.set(progress)
            mer_progress.update()
        file_name = "merimage."+selected_format    
        save_path = os.path.join(path_entry.get(),file_name)
        result_image.save(save_path)
        messagebox.showinfo("알림","작업이 완료 되었습니다.")
    except Exception as err :
        messagebox.showerror("에러",err)
    
root = Tk()
root.title("Image Merger")
root.resizable(0,0)

control_frame = Frame(root)
control_frame.pack(fill="x",padx=5,pady=5)

add_btn = Button(control_frame,text="파일추가",padx=5,pady=5,width=12,command=add_files)
add_btn.pack(side="left",padx=5,pady=5)

del_btn = Button(control_frame,text="선택 삭제",padx=5,pady=5,width=12,command=del_files)
del_btn.pack(side="right",padx=5,pady=5)

list_frame=Frame(root)
list_frame.pack(fill="both",expand=True,padx=5,pady=5)

list_scroll = Scrollbar(list_frame)
image_list = Listbox(list_frame,height=20,selectmode="extended",yscrollcommand=list_scroll.set)
image_list.pack(side="left",fill="both",expand=True)
list_scroll.pack(side="right",fill="y")
list_scroll.config(command=image_list.yview)

path_label = LabelFrame(root,text="저장경로")
path_label.pack(fill="x",padx=5,pady=5)

path_entry = Entry(path_label)
path_entry.pack(side="left",fill="x",expand=True,padx=5,pady=5,ipady=5)

find_btn = Button(path_label,text="찾아보기",padx=5,pady=5,width=10,command=find_directory)
find_btn.pack(side="right",padx=5,pady=5)

option_label = LabelFrame(root,text="옵션")
option_label.pack(fill="x",padx=5,pady=5)

width_label = Label(option_label,text="가로넓이",width=10)
width_label.pack(side="left",padx=5,pady=10)

widths = ["원본유지","1024","800","640"]
width_combobox = ttk.Combobox(option_label,state="readonly",width=12,values=widths)
width_combobox.pack(side="left",padx=5,pady=10)
width_combobox.current(0)

term_label = Label(option_label,text="간격",width=10)
term_label.pack(side="left",padx=5,pady=10)

terms = ["없음","좁게","보통","넓게"]
term_combobox = ttk.Combobox(option_label,state="readonly",width=10,values=terms)
term_combobox.pack(side="left",padx=5,pady=10)
term_combobox.current(0)

format_label = Label(option_label,text="포맷",width=10)
format_label.pack(side="left",padx=5,pady=10)

formats = ["PNG","JPG","BMP"]
format_combobox = ttk.Combobox(option_label,state="readonly",width=10,values=formats)
format_combobox.pack(side="left",padx=5,pady=10)
format_combobox.current(0)

progress_label = LabelFrame(root,text="진행상황")
progress_label.pack(fill="x",padx=5,pady=5)

p_var = DoubleVar()
mer_progress = ttk.Progressbar(progress_label,maximum=100,variable=p_var)
mer_progress.pack(fill="x",padx=5,pady=10)

start_frame = Frame(root)
start_frame.pack(fill="x",padx=5,pady=5)

close_btn = Button(start_frame,text="닫기",padx=5,pady=5,width=12,command=root.quit)
close_btn.pack(side="right",padx=5,pady=5)

start_btn = Button(start_frame,text="시작",padx=5,pady=5,width=12,command=start_mer)
start_btn.pack(side="right",padx=5,pady=5)


root.mainloop()