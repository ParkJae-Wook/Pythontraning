import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(view_label.cget("text"))
            view_label.config(text=str(result))
        except Exception as e:
            view_label.config(text="Error")
    elif text == "AC":
        view_label.config(text="0")
    elif text == "CE":
        view_label.config(text=view_label.cget("text")[:-1])
    else:
        if view_label.cget("text") == "0":
            view_label.config(text=text)
        else:
            view_label.config(text=view_label.cget("text") + text)

window = tk.Tk()
window.title("Calculator")
window.geometry("280x330")
window.resizable(0, 0)
bottons = [
    'AC', '^', '%', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    'CE', '0', '.', '='
]
view_label = tk.Label(window, text="0", anchor="se", font=("Arial", 20), width=17,height=3,bg="lightgray", fg="black")
view_label.grid(row = 0, column = 0,sticky='nwes',rowspan=3, columnspan = 4)
buttons_frame = tk.Frame(window)
buttons_frame.grid(row=4, column=0, columnspan=4)

for i,button in enumerate(bottons, start=0):
    button = tk.Button(window, text=button, font=("Arial", 15),width=4,height=1, bg="gray", fg="black")
    button.grid(row=(i//4)+4, column=i%4,sticky ='news' , padx=2, pady=2)
    button.bind("<Button-1>", on_click)    

window.mainloop()