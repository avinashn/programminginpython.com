#This is a python program to decode and encode a caesar-cypher, given its key.

#Function to encrypt a given string.
def encrypt(k):                                                                         
    n,i=0,0
    l="abcdefghijklmnopqrstuvwxyz"
    l=list(l)
    b=[]
    a=input("enter text to be encrypted: ")
    a=list(a)
    while(n<len(a)):
        if a[n].lower() in l:
            if a[n].isupper():
                i=l.index(a[n].lower())
                i=(i+k)%26
                b.append(l[i].upper())
                n+=1
            else:
                i=l.index(a[n])
                i=(i+k)%26
                b.append(l[i])
                n+=1
        else:
            if(a[n]==' '):
                b.append(' ')
                n+=1
    print("The encrypted text is: ","".join(b))

#Function to decrypt an encrypted string.
def decrypt(k):                          
    n,i=0,0 
    l="abcdefghijklmnopqrstuvwxyz"
    l=list(l)
    b=[]
    a=input("Enter cipher to be decrypted: ")
    a=list(a)
    while(n<len(a)):
        if a[n].lower() in l:
            if a[n].isupper():
                i=l.index(a[n].lower())
                i=(i-k)%26
                b.append(l[i].upper())
                n+=1
            else:
                i=l.index(a[n])
                i=(i-k)%26
                b.append(l[i])
                n+=1
        else:
            if(a[n]==' '):
                b.append(' ')
                n+=1
    print("Cipher after decryption is: ","".join(b))

    
#Main
opt=int(input("1.encrypt   2.decrypt   0.exit"))
while(opt!=0):
    if(opt==1):
        n=int(input("enter key"))
        encrypt(n)
    elif(opt==2):
        n=int(input("enter key"))
        decrypt(n)
    else:
        print("enter valid option")
    opt=int(input("1.encrypt 2.decrypt 0.exit"))
