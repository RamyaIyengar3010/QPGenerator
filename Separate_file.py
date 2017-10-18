#!/usr/bin/env python


def separate(fobj, delimiter):
	'''Given a file, with a set of sections separated by delimiters, place each delimiter in a separate sublist inside a list
	'''
	
	result = []
	marks_list =[]

	i=-1

	for line in fobj:
		if line not in delimiter:
			result[i].append(line)	
		else:
			result.append([])
			i += 1

	for i in range(len(result)):
		marks_list.append((i, int(result[i].pop(0)[0])))

	return result, marks_list

def main():
	file = raw_input("Enter file name: ")
	
	try:
		import sys
		fobj = open(file)
		
	except IOError as e:
		print 'No such file or directory found'
		sys.exit(1)

	delim = input("Enter section delimiter: ")
	rs, ms = separate(fobj, delim)
	print rs
	print ms

if __name__ == '__main__':
	main()