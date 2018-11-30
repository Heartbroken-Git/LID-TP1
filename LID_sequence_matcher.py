from difflib import SequenceMatcher

def getResemblanceRatio(originalUrl, testedUrl):
    return SequenceMatcher(None, originalUrl, testedUrl).ratio()
