import pandas as pd
from pathlib import Path
import datetime as dt
from linsertor import *

def sentwa(per,rcv,amt):
    wf=per+'.txt'    
    csv=pd.read_csv(per+'.txt')
    nw=str(dt.datetime.now())
    data=csv[['amt','ggt','date']]
    i=len(data)
    print(i)
    sts=str(amt)+',1,'+str(nw)+','+str(rcv)+','+str(i)+'\n'
    wobj=open(wf,"a+")
    wobj.write(sts)

    sender_request(per,rcv,amt,nw,i,0)
    wobj.close()
    

#sentwa("satoshi","bx123",101)