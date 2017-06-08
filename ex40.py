cities={'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'} #字典


cities['NY']='New York'#额外的字典
cities['OR']='Portland'

def find_city(t,s):#定义函数，函数变量

	if s in t:
		return t[s]
	else:
		return "Not found."
cities['_find']=find_city

while True:
	print("State?[ENTER to quit]",end=' ')
	s=input(">")
	if not s:break
	

	city_found=cities['_find'](cities,s)
	print (city_found)

del cities['CA']
print(cities)
