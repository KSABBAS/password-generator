from tkinter import *
import random
main=Tk()
main.geometry("300x370+20+20")
main.resizable(False,False)
main.title(r"KS password creator")
main.config(background='#b0fc38')
# main.iconbitmap('password_generator_icon.ico')

symbols=Label(main,text="symbols",font=("family","13"),bg="#b0fc38",fg="purple")
symbols.place(x=10,y=30)
symbolsentry=Entry(main,font=("family","13"),width=20)
symbolsentry.place(x=90,y=30)

numbers=Label(main,text="numbers",font=("family","13"),bg="#b0fc38",fg="purple")
numbers.place(x=10,y=105)
numbersentry=Entry(main,font=("family","13"),width=20)
numbersentry.place(x=90,y=105)

letters=Label(main,text="letters",font=("family","13"),bg="#b0fc38",fg="purple")
letters.place(x=10,y=180)
lettersentry=Entry(main,font=("family","13"),width=20)
lettersentry.place(x=90,y=180)

c_numbs=Label(main,text="c_numbs",font=("family","13"),bg="#b0fc38",fg="purple")
c_numbs.place(x=10,y=255)
c_numbsentry=Entry(main,font=("family","13"),width=20)
c_numbsentry.place(x=90,y=255)
# def creat():
#     c()
# creat_button=Button(main,text="creat",relief="flat",command=creat)
# creat_button.place(x=240,y=320)
# def c():
#     global p
#     output=Tk()
#     output.geometry("200x100+350+20")
#     output.resizable(False,False)
#     output.title("KS password creator output")
#     output.config(background='#b0fc38')
#     output.iconbitmap('password_generator_icon.ico')
    

#     symbols=list(symbolsentry.get())
    
#     numbers=list(numbersentry.get())
    
#     letters=list(lettersentry.get())
    
#     c_numbs=c_numbsentry.get()
   
#     c_numbs=int(float(c_numbs))

 
#     symbols=symbols + letters+numbers

#     symbols=''.join(symbols)
#     paord=[]
    
    
#     while c_numbs >0:
#         t=random.choice(symbols)
#         paord.append(t)
#         c_numbs-=1
#     password=''.join(paord)
#     pas=Label(output,text=password,font=("family","15"))
#     pas.place(x=10,y=20)
#     output.mainloop()
main.mainloop()
