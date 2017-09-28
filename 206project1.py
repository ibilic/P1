import os
import filecmp
import csv
import operator
from operator import itemgetter
import collections
from datetime import datetime
from datetime import date


def getData(file):
	lst = list()
	dic = dict()
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)

		for files in reader:
			x = dict(files)
			lst.append(x)
			# lst.append(file)
	return (lst)


#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

	#Your code here:
	pass

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	# list_dic = getData(data)
	#Your code here:
	x = sorted(data, key = itemgetter(col))
	return (x[0]['First'] + ' ' + x[0]['Last'])
	pass

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	cnt = collections.Counter()
	print (len(data))

	for dic in data:
		cnt[dic['Class']] += 1
		tups = cnt.items()
		l = sorted(tups, key = itemgetter(1), reverse = True)

	return (l)




# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	#Your code here:
	d = dict()
	for list in a:
		spt = list["DOB"].split('/')
		if spt[1] not in d:
			d[spt[1]] = 1
		else:
			d[spt[1]] +=1
	sorted_d = sorted(d.items(), key = itemgetter(1), reverse=True)
	return (int(sorted_d[0][0]))


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	s = 0
	count = 0
	for line in a:
		x=line['DOB']
		dob = datetime.strptime(x, "%m/%d/%Y")
		date_today = datetime.today()
		age = date_today - dob
		s += age.days
		count += 1
	return (int((s/count)/365))

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: NoneFirst,Last,Email,Class,DOB

	with open(fileName, 'w') as f:
		writer = csv.DictWriter(f, delimiter = ',', fieldnames = ['First', 'Last','Email','Class', 'DOB'])
		x = sorted(a, key = itemgetter(col))
		for line in x:
			# writer.writerow({'First':(line['First'] + ','), 'Last':(line['Last'] + ','), 'Email':line['Email']})
			writer.writerow({'First':(line['First']), 'Last':(line['Last']), 'Email':line['Email']})


	#There is spacing between the columns, so it doesn't look exactly like the outfile.



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
