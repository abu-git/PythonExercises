"""
The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will 
result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

	rgb(255, 255, 255) # returns FFFFFF
	rgb(255, 255, 300) # returns FFFFFF
	rgb(0,0,0) # returns 000000
	rgb(148, 0, 211) # returns 9400D3
"""

def rgb(r, g, b):
	if(r < 0):
		r = 0
	if(g < 0):
		g = 0
	if(b < 0):
		b = 0
	if(r > 255):
		r = 255
	if(g > 255):
		g = 255
	if(b > 255):
		b = 255
	the_r = hex(r)
	the_g = hex(g)
	the_b = hex(b)
	if(len(the_r) < 4):
		the_r = '0' + the_r[2:]
	if(len(the_r) == 4):
		the_r = the_r[2:]
	if(len(the_g) < 4):
		the_g = '0' + the_g[2:]
	if(len(the_g) == 4):
		the_g = the_g[2:]
	if(len(the_b) < 4):
		the_b = '0' + the_b[2:]
	if(len(the_b) == 4):
		the_b = the_b[2:]
	return the_r.upper() + the_g.upper() + the_b.upper()


print(rgb(0,0,0))
print(rgb(1,2,3))
print(rgb(255, 255, 255))
print(rgb(148, 0, 211))
print(rgb(254, 253, 252))
print(rgb(-20, 275, 125))