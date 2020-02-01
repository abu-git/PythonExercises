"""
Write a function that when given a URL as a string, parses out just the domain name and returns it 
as a string. 

For example:

	domain_name("http://github.com/carbonfive/raygun") == "github" 
	domain_name("http://www.zombie-bites.com") == "zombie-bites"
	domain_name("https://www.cnet.com") == "cnet"
"""

def domain_name(url):
	striped = ""
	if(url[0:4] == "www."):
		striped = url[4:]
	elif(url[0:7] == "http://"):
		if(url[0:11] == "http://www."):
			striped = url[11:]
		else:
			striped = url[7:]
	elif(url[0:8] == "https://"):
		if(url[0:12] == "https://www."):
			striped = url[12:]
		else:
			striped = url[8:]
	else:
		striped = url[:]
	the_dot = striped.find(".")
	return striped[:the_dot]


print(domain_name("http://google.com"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("http://www.cnet.com"))