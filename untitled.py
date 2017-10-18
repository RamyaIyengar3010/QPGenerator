import Separate_file as sf
from random import randrange, choice
def generateQP(file, delim):
	fobj = open(file)
	questions_list, marks_list = sf.separate(fobj, delim)

	paperFile = []
	sum_marks = 0

	while sum_marks <= 100:
		section_num = randrange(len(questions_list))
		#print section_num, type(section_num)
		try:
			question = choice(questions_list[section_num])
		except IndexError:
			section_numb = 0 if section_numb is len(questions_list) -1 else section_num + 1
		#print question, type(question)
		sum_marks += marks_list[section_num][1]
		if sum_marks > 100:
			sum_marks -= marks_list[section_num][1]
			break

		paperFile.append(question)

		for i in range(len(questions_list[section_num])):
			if questions_list[section_num][i] is question:
				questions_list[section_num].pop(i)
				break

	print paperFile
	print sum_marks

	'''while sum_marks < 100:
		remain_marks = 100 - sum_marks
		for i in marks_list:
			if remain_marks % i[1] == 0:
				 print questions_list[i[0]]
				 question = choice(questions_list[i[0]])
				 paperFile.append(question)
				 for n in range(len(questions_list[i[0]])):
					if questions_list[i[0]][n] is question:
						questions_list[i[0]].pop(n)
						break
	'''

generateQP("QB1.txt", ['\n', '\r\n'])