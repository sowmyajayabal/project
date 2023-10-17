"""def hello ():
    name="sowmi"
    print(f"hello {name}")
hello()

def hello ():
    name="sowmi"
    print("hello",name)
hello()

x=20
def fun():
    print(x)
fun()
print(x)


def fun():
   global x
   x=300
fun()
print(x)

import platform
x=platform.system()
print(x)

def greet (name):
    print(f"hello,{name}!")
    greet()

    def greeting(name):
        print("hello,"+name)
 def.greeting("sowmi")"""


#f = open("C:\\Users\\SightSpectrum\\Desktop\\New Text Document.txt", "r+")

#f.write("Good Morning")


#print(f.read())


f=open("C:\\Users\\SightSpectrum\\Desktop.txt","w")
print("name of the file",f.name)

print("mode of the file",f.mode)

print("file is close or not",f.closed)

f.close()
print("file is closed or not",f.closed)

f=open("sow.txt","r")
print(f.read())