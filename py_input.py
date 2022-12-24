import easygui as eg

'''def main():
    ans=eg.enterbox("Iuput the Java file name(include the extension):","Java Editor")
    k=ans
    p=k.split('.')
    x=p[0]
    if p[1]=="java":
        x+='.'+p[1]
    f=open("cmd_input.txt","w")
    f.write(x)
    f.close()'''



ans=eg.enterbox("Iuput the Java file name(include the extension):","Java Editor")
k=ans
p=k.split('.')
x=p[0]
if p[1]=="java":
    x+='.'+p[1]
f=open("cmd_input.txt","w")
f.write(x)
f.close()
