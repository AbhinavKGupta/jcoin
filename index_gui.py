from tkinter import *
import pandas as pd
from users import *
from nakamoto import *
from datetime import *
from random import *

from pathlib import Path

class page:
    def __init__(self,root):
 
        self.f=Frame(root,height=450,width=700)
        self.f.propagate(0)
        self.f.pack()
        self.createlogin()

    def login(self):
        self.l1=Label(text='enter public key :')
        self.l2=Label(text='enter private key:')

        self.e1=Entry(self.f,width=25,fg='blue',bg='yellow',font=('arial',15))
        self.e2=Entry(self.f,width=25,fg='blue',bg='yellow',show='@')
        self.e2.bind("<Return>",self.check)

        self.l1.place(x=50,y=100)
        self.e1.place(x=200,y=100)
        self.l2.place(x=50,y=150)
        self.e2.place(x=200,y=150)

    def check(self,event):
        self.str1=self.e1.get()
        self.str2=self.e2.get()
        
        print(self.str1)
        csv=pd.read_csv("account.txt")
        data=csv[["uname","pass"]]
        i=0
        l=len(data['uname'])
        while i<l:
            if data['uname'][i]==self.str1 and data['pass'][i]==self.str2:
                self.valid()
                break
            else:
                i+=1
        if i==l:
            self.ll=Label(text='incorrect credentials')
            self.ll.place(x=80,y=200)
        print("login clicked")
    def valid(self):
        if str(self.str1)!="satoshi":
            self.usr=user(self.str1)
        else:
            self.usr=naka()
        print("welcoming..")
        #quit()

    def newcheck(self):
        self.p1=str(self.c2.get())
        self.p2=str(self.c3.get())
        self.nuu=str(self.newun) 
        print(self.p1,self.p2)
        if str(self.p1)!=str(self.p2):
            self.lm=Label(text='password mismatch')
            self.lm.place(x=100,y=270)
            return
        stn="amt,ggt,date,prs,unq\n50,0,"+str(datetime.now())+"satoshi,0\n"
        obn=open(self.newun+'.txt',"a+")
        obn.write(stn)
        obn.close()
        self.usr=user(self.newun)
        ptl=Path("account.txt").is_file()
        if ptl==False:
            obb=open("account.txt","a+")
            st="uname,pass\n"
            obb.write(st)
            obb.close()
            ok=open("request.txt","a+")
            ok.write("row,sender,reciever,amount,date,unq,confirm\n")
            ok.close()
            oo=open("request1.txt","a+")
            oo.write("row")
            oo.close()
        obb=open("account.txt","a+")
        sto=self.newun+","+self.p1+"\n"
        obb.write(sto)
        obb.close()
        return 1
        
        
        
        
        
       

    def create(self):
        #self.root2=Tk()
        #self.f2=Frame(self.root2,height=350,width=750)
        print("creatong account")
        tags=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.newun=''
        j=0
        num=0
        while j<5:
            v=randint(0,1)
            if v==1 and num <=2:
                z=randint(0,len(tags)-1)
                self.newun+=tags[z]
            else:
                z=randint(0,9)
                self.newun+=str(z)
                num+=1
            j+=1
               
        self.m1=Label(self.f,text='your public key      :')
        self.m2=Label(self.f,text='enter private key    :')
        self.m3=Label(self.f,text='re-enter private key :')

        self.c1=Label(self.f,text=self.newun,width=25,fg='blue',bg='yellow',font=('arial',15))
        self.c2=Entry(self.f,width=25,fg='blue',bg='yellow',show='@')
        self.c3=Entry(self.f,width=25,fg='blue',bg='yellow',show='@')
        self.b9=Button(self.f,text="get in",width=10,height=3,command=lambda: self.newcheck())

        self.m1.place(x=50,y=100)
        self.c1.place(x=200,y=100)
        self.m2.place(x=50,y=150)
        self.c2.place(x=200,y=150)
        self.m3.place(x=50,y=200)
        self.c3.place(x=200,y=200)
        self.b9.place(x=250,y=250)



    def createlogin(self):
        self.b1=Button(self.f,text="log me in",width=10,height=3,command=lambda: self.login())
        self.b2=Button(self.f,text="create account",width=10,height=3,command=lambda: self.create())

        self.b1.pack()
        self.b2.pack()






root=Tk()
obj=page(root)

root.mainloop()
