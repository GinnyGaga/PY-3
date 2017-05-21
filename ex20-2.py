from sys import argv #导入脚本需要用的功能模块
script,f=argv        #定义参数变量的参数名

def print_a_line(count_line,f):#定义函数名和函数参数
	print (count_line,f.readline()) #f.readline()从文件中读取一					行;如果f.readline()返回一个空					字符串，则文件的结尾已经到达

#def rewind(f):
#	f.seek(0)##读取定义好的文件的初始位置

current_file=open(f)
current_line=0
while current_line <= 2:
	current_line+=1
	print_a_line(current_line,current_file)

#current_line=1
#print_a_line(current_line,current_file)

#current_line=current_line+1
#print_a_line(current_line,current_file)

#current_line=current_line+1
#print_a_line(current_line,current_file)
