user_data= input("enter text to write to the file: ")
file1= open('out.txt',"w")
write_file= file1.write(user_data)

print("Data successfully written to output.txt")
file1.close()

user_data2=input("enter additional text to append:")
file1= open('out.txt',"a")

file1.write("\n")
write_file1 = file1.write(user_data2)
print(write_file1)

print("data successfully appended")


file1.close()

file1=open('out.txt','r')
read_file1=file1.read()
print("final content of output.txt is :")
print(read_file1)
file1.close()
