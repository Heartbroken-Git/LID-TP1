import whois
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
