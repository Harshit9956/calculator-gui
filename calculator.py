from tkinter import*
win=Tk()
win.geometry('400x400')

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except:
                value='error'
        scvalue.set(value)
        screen.update()
    elif text=='c':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


scvalue=StringVar()
scvalue.set("")

screen=Entry(win,textvar=scvalue)
screen.pack(fill=BOTH)
f=Frame(win,bg="grey")

for i  in range(1,4):
    b=Button(f,text=str(i),font='calibri 12 bold')
    b.pack(side=LEFT)
    b.bind("<Button-1>",click)
f.pack(fill=BOTH,padx=20)
f=Frame(win,bg="grey")
for i  in range(4,7):
    b=Button(f,text=str(i),font='calibri 12 bold')
    b.pack(side=LEFT)
    b.bind("<Button-1>",click)
f.pack(fill=BOTH,padx=20)
f=Frame(win,bg="grey")
for i in range(7,10):
     b=Button(f,text=str(i),font='calibri 12 bold')
     b.pack(side=LEFT)
     b.bind("<Button-1>",click)
f.pack(fill=BOTH,padx=20,)
f=Frame(win,bg="grey")
lis=['0','*','+']
for i in lis:
    b=Button(f,text=str(i),font='calibri 12 bold')
    b.pack(side=LEFT)
    b.bind("<Button-1>",click)
f.pack(fill=BOTH,padx=20)
f=Frame(win,bg="grey")
lis=['-','/','%']
for i in lis:
    b=Button(f,text=str(i),font='calibri 12 bold')
    b.pack(side=LEFT)
    b.bind("<Button-1>",click)
f.pack(fill=BOTH,padx=20)
lis=['=','**','c']
for i in lis:
    b=Button(f,text=str(i),font='calibri 12 bold')
    b.pack(side=LEFT)
    b.bind("<Button-1>",click)
f.pack(fill=BOTH,padx=20)

win.mainloop()  