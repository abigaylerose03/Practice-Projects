def christmasTree():
	rows = input("Enter range of rows:")
	for i in range(rows):
		print ' ' * (rows - i - 1) + "*" * (2*i+1)
	print "Merry Christmas!!!"


christmasTree()