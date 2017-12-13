nama=str(input("Masukan Nama : " ))
asal=str(input("Masukan Asal : " ))
tanggal=str(input("Tanggal Lahir : " ))

file = open("data.txt","a+")
result= file.write("Nama Saya Adalah %s\n"%(nama))
print (result)

file = open("data.txt","a+")
result= file.write("Saya Berasal Dari %s\n"%(asal))
print (result)

file = open("data.txt","a+")
result= file.write("Saya Lahir Pada tanggal %s\n"%(tanggal))
print (result)

file = open("data.txt","r")
for data in file :
	print (data)
	
