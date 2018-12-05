import whois
from ansimarkup import ansiprint as print
import LID_sequence_matcher as LseqMatch
#require pip install whois
def LIDwhois(domain):
	_domain = whois.whois(domain)
	_creation = _domain.creation_date
	_expiration = _domain.expiration_date
	_domain = _domain.domain_name


	return(_domain,_creation,_expiration)

def testBuzzword(urlToTest):

	grade = 0
	file = []

	with open("data/buzzword.txt", "r") as f:
		file = f.readlines()


	for line in file:
		lineArray = line.split(': ')
		for subdomain in urlToTest.split('.'):
			if subdomain == lineArray[0]:
				grade = grade + lineArray[1]

	return grade

def testInScope(urlToTest):

	maxRatio = 0
	maxProbableDomain = ''

	with open("data/trustlist.txt", "r") as file:
		for line in file:
			possibleRatio = LseqMatch.getResemblanceRatio(line, urlToTest)
			if maxRatio < possibleRatio:
				maxRatio = possibleRatio
				maxProbableDomain = line

	return maxProbableDomain, maxRatio

def testManyWeirdChar(urlToTest, weirdChar):

	nbChar = 0

	for char in urlToTest:
		if char == weirdChar:
			nbChar += 1

		if nbChar >= 3:
			return True

	return False

def finalGrading(resemblanceRatio, buzzwordGrade, hasManyHyphens, hasManyDots):
	finalGrade = 0

	finalGrade += (resemblanceRatio - 0.7) * 100

	finalGrade += buzzwordGrade

	if hasManyHyphens:
		finalGrade += 10

	if hasManyDots:
		finalGrade += 20

	return finalGrade

def doTests(urlToTest):

	originalDomain, ratio = testInScope(urlToTest)
	if ratio >= 0.7:

		print("<green>LID_tests.py > DEBUG : " + urlToTest + " in scope</green>")

		print("LID_tests.py > DEBUG : Beginning buzzword testing")
		buzzwordGrade = testBuzzword(urlToTest)
		print("<bold>LID_tests.py > DEBUG : " + urlToTest + " graded " + str(buzzwordGrade) + " in buzzword testing</bold>")

		print("LID_tests.py > DEBUG : Beginning hyphen testing")
		hyphenGrade = testManyWeirdChar(urlToTest, '-')
		print("<bold>LID_tests.py > DEBUG : " + urlToTest + " has many hyphens ? " + str(hyphenGrade) + "</bold>")

		print("LID_tests.py > DEBUG : Beginning dot testing")
		dotsGrade = testManyWeirdChar(urlToTest, '.')
		print("<bold>LID_tests.py > DEBUG : " + urlToTest + " has many dots ? " + str(dotsGrade) + "</bold>")

		finalGrade = finalGrading(ratio, buzzwordGrade, hyphenGrade, dotsGrade)
		print("<bold>LID_tests.py > DEBUG : "+ urlToTest+ "\'s final grade is "+ str(finalGrade) + "</bold>")

	else:
		# print("<red>LID_tests.py > DEBUG : " + urlToTest + " not in scope</red>")
		return
