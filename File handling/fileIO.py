
f=open("E:\Practice\Python\Basic Python\File handling\demo.txt","a")
f.write("\nThis is additional line.")
f.close()

f=open("E:\Practice\Python\Basic Python\File handling\demo.txt","r")
data=f.read()
print("Read\n",data)
print(type(data))
f.close()
