from tkinter import *
import pandas as pd
from users import *
from nakamoto import *
from datetime import *
from random import *

ok=[]
class page:
    def __init__(self,root):
    
        self.f=Frame(root,height=450,width=700)
        self.f.propagate(0)
        self.f.pack()
        self.b1=Button(self.f,text="new",width=10,height=3,command=lambda: self.login())
        self.b1.pack()
        
        self.login()
        self.corr=0


    def login(self):

        self.b1.pack()
        self.f['bg']="white"
	



        

        csv=pd.read_csv("account.csv")
        data=csv[["uname","pass"]]
        i=0
        l=len(data['uname'])
        nm=randint(0,l-1)
        while nm in ok:
            nm=randint(0,l-1)
        ok.append(nm)
        
        self.ltxt=Label(text=data['uname'][nm])
        self.ltxt.place(x=200,y=100)
        self.mystr=data['uname'][nm]

     
        self.e2=Entry(self.f,width=25,fg='blue',bg='yellow')
        self.e2.bind("<Return>",self.check)
        self.e2.place(x=200,y=150)

    def check(self,event):
       
        self.str2=self.e2.get()
        
        csv=pd.read_csv("account.csv")
        data=csv[["uname","pass"]]
        i=0
        l=len(data['uname'])
        while i<l:
            if data['uname'][i].lower()==self.mystr.lower() and data['pass'][i].lower()==self.str2.lower():
                break
            else:
                i+=1
        if i==l:
            self.ll=Label(text='incorrect')
            self.f['bg']="red"
            self.corr-=0.25
        else:
            self.ll=Label(text="  right  ")
            self.f['bg']="green"
            self.ltxt['text']=''
            self.corr+=1.0
        #self.ll.place(x=180,y=180)
  
        print("login clicked")


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
        obb=open("account.txt","a+")
        sto=self.newun+","+self.p1+"\n"
        obb.write(sto)
        return 1
        
        
        
        
        
       

    def create(self):
        #self.root2=Tk()
        #self.f2=Frame(self.root2,height=350,width=750)
        print("creatong account")







root=Tk()
obj=page(root)

root.mainloop()
