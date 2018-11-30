import certstream
import LID_tests as Ltests

def retrieveOneDomain_callback(message, context):

    if message['message_type'] == "heartbeat":
        return

    if message['message_type'] == "certificate_update":
        allDomains = message['data']['leaf_cert']['all_domains']

        if len(allDomains) == 0:
            print("LID_event_retrieval.py > WARNING : No domain in message", file=sys.stderr)
            return

        targetDomain = allDomains[0]
        print("LID_event_retrieval.py > Retrieved " + targetDomain)
        Ltests.doTests(targetDomain)

def connectFireHose(requestedType):

    if requestedType == "single_domain":
        certstream.listen_for_events(retrieveOneDomain_callback,"wss://certstream.calidog.io")
    else:
        print("LID_event_retrieval.py > ERROR : Incorrect type specified", file=sys.stderr)
        raise(ValueError)
