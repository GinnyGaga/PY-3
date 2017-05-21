from sys import argv # 导入这个脚本需要用到的功能模块引入脚本

script,input_file=argv #定义参数变量和参数

def print_all(f):  #定义函数名print_all、函数参数f
	print (f.read()) #读取该定义好的文件f

def rewind(f):  #再次定义另一个函数名rewind、函数参数还是一样f
	f.seek(0) #读取定义好的文件的初始位置

def print_a_line(line_count,f):  #定义函数名print_a_line,
                                 # 函数参数line_count和f。
	print (line_count,f.readline()) #f.readline()从文件中读取一					行,如果f.readline()返回一个空					字符串，则文件的结尾已经到达.

current_file=open(input_file) #打开上面定义的input—file，赋值给变量				current_file.

print("First let's print the whole file:\n")

print_all(current_file) #读取文件

print ("Now let's rewind,kind of like a tape.")

rewind(current_file)#从初始位置开始读取

print("Let's print three lines:")

current_line = 1 
print_a_line(current_line,current_file)  #调用函数print_a_line,重新				定义函数参数名，并把1赋 值给函数参数名

current_line = current_line+1 #继续调用，在上一次调用的基础上再+1,				同时打印文件对应位置的内容
print_a_line(current_line,current_file)

current_line = current_line+1  #继续调用，+1,打印
print_a_line(current_line,current_file)
