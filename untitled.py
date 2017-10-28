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
			if questions_list[section_num] is None:
				questions_list.pop(section_num)
				marks_list.pop(section_num)
			else:
				question = choice(questions_list[section_num])
		except IndexError:
			section_num = 0 if section_num is len(questions_list) -1 else section_num + 1
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

	while sum_marks < 100:
		remain_marks = 100 - sum_marks
		for i in reversed(marks_list):
			try:
				if questions_list[i[0]] is None:
					questions_list.pop(i[0])
					marks_list.pop(i[0])
				else:
					if remain_marks % i[1] == 0:
						 #print questions_list[i[0]]
						 question = choice(questions_list[i[0]])
						 paperFile.append(question)
						 sum_marks += i[1]
						 for n in range(len(questions_list[i[0]])):
							if questions_list[i[0]][n] is question:
								questions_list[i[0]].pop(n)
								break
			except IndexError:
				pass
	

generateQP("QB1.txt", ['\n', '\r\n'])