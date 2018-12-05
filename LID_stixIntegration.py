from stix2 import MemoryStore, Indicator
import datetime

mem = MemoryStore()

def writeStix(shadyUrl, score):

    # a mettre dans ta callback
    indicator = Indicator(
        name="Malicious site (phishing)",
        labels=["malicious-activity"],
        pattern="[url:value = \'" + shadyUrl + "\']",
        created="{}".format(datetime.datetime.now().date()),
        valid_from="{}".format(datetime.datetime.now().date()),
        description="Possible malicious site detected by LID-TP1 with a score of "+ str(score)+ ", shady url : "+ shadyUrl
    )
    mem.add(indicator)
    mem.save_to_file("./database/{}.json".format(datetime.datetime.now().date()))  # end of the function, if the site is a phishing site (score > 0) -> write in STIXv2.0 file
