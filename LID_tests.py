import whois
from ansimarkup import ansiprint as print
import LID_sequence_matcher as LseqMatch
#require pip install whois
def LIDwhois(domain):
	_domain = whois.whois(domain)
	_text = _domain.text
	_creation = _domain.creation_date
	_expiration = _domain.expiration_date
	_domain = _domain.domain_name


	return(_domain,_creation,_expiration,_text)

def country(text):
	info= text.split("country:")[1].split("\n")[0]
	return(info)

def testWhois(originalDomain, domainToTest):
	grade = 0

	originalDomainName, originalDomainText, originalDomainCreation, originalDomainExpiration = LIDwhois(originalDomain)
	originalDomainCountry = country(originalDomainText)
	testDomainName, testDomainText, testDomainCreation, testDomainExpiration = LIDwhois(domainToTest)
	testDomainCountry = country(testDomainText)

	if testDomainName != originalDomainName:
		grade = grade+1

		if testDomainCountry != originalDomainCountry:
			grade=grade+1

		if testDomainCreation != originalDomainCreation:
			grade=grade+1

		if testDomainExpiration != originalDomainExpiration:
			grade=grade+1

	else:
		return grade

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


def doTests(urlToTest):

	originalDomain, ratio = testInScope(urlToTest)
	if ratio >= 0.7:

		print("<green>LID_tests.py > DEBUG : " + urlToTest + " in scope</green>")
		print("LID_tests.py > DEBUG : Beginning buzzword testing")
		buzzwordGrade = testBuzzword(urlToTest)
		print("<bold>LID_tests.py > DEBUG : " + urlToTest + " graded " + str(buzzwordGrade) + " in buzzword testing</bold>")
		print("LID_tests.py > DEBUG : Beginning whois testing")
		whoisGrade = testWhois(originalDomain, urlToTest)
		print("<bold>LID_tests.py > DEBUG : " + urlToTest + " graded " + str(whoisGrade) + "</bold>")

	else:
		print("<red>LID_tests.py > DEBUG : " + urlToTest + " not in scope</red>")
		return
