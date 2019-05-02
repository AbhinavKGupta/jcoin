from writer import *
import pandas as pd

def sender_request(per,rcv,amt,dat,i,crm):
    lcsv=pd.read_csv("request.txt")
    lsat=lcsv[['row','date']]
    llll=len(lsat)
    
    stline=str(llll)+','+str(per)+','+str(rcv)+','+str(amt)+','+str(dat)+','+str(i)+','+str("0")+'\n'
    f_write("request.txt",stline)
    

