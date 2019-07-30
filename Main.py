################ Made by: RKAISSI YOUSSEF    ###############
import random as r
numbers=[1,2,3,4,5,6,7,8,9,0]
lettersL=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersU=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
Symbols=['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?']

list=[1,2,3,4]
pw=[]
while len(pw)<=15:
    c=r.choice(list)
    if c==1:
        pick=r.choice(numbers)
        pw.append(pick)
    elif c==2:
        pick=r.choice(lettersL)
        pw.append(pick)
    elif c==3:
        pick=r.choice(lettersU)
        pw.append(pick)

    else:
        pick=r.choice(Symbols)
        pw.append(pick)

pws="".join(str(e) for e in pw)
webs=input("What is the web site ?\n")
username=input("Enter the username or the email :\n")   
f=open("[PATH]"+str(webs)+".txt","w")
f.write(username)     
f.write(":")
f.write(pws)   
f.close()   


