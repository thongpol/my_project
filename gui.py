
from tkinterweb import HtmlFrame #import the HTML browser
try:
    import tkinter as tk
    import requests
    H = 600  # กำหนดค่าตัวแปรความสูงหน้าต่างโปรแกรม
    W = 800  # ตัวแปรความกว้าง

    root = tk.Tk()


    canvas = tk.Canvas(root, height=H, width=W)
    canvas.pack()
except ImportError:    


    frame = tk.Frame(root, dg='#80c1ff', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, 
    anchor='n')
    entry = tk.Entry(frame, font=('Courier', 18))
    entry.place(relwidth=0.65, relheiht=1)

    button = tk.Button(frame, text='ตกลง', font=40)
    button.place(relx=0.7, relwidth=0.3, relheight=1)
# except ImportError:    

    root.mainloop()
