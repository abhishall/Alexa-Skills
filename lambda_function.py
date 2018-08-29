def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event, event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()
    
def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello! Namaste!"
    speechOutput =  "Hello , Welcome to Animal Groups. " \
                    "You can ask me what the group of an animal is collectively called. " \
                    "What's your favourite animal?.  "
    repromptText =  "You can say, for example , a group of dogs is . "
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }
    
def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using Animal Groups. " \
                    "Have a great day! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

  
def onIntent(event, session):
             
    intent = event['request']['intent']
    intentName = event['request']['intent']['name']
    if intentName == "askGroup":
        return animal_group(event, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")


def animal_group(event, session):
    
    cardTitle = event['request']['intent']['name']
    sessionAttributes = {}
    shouldEndSession = False
    speechOutput = ''
    if 'value' not in event['request']['intent']['slots']['animalname'] :
        speechOutput = "I'm not sure what animal you are saying. " \
                       "Please provide a valid animal name or say stop to close Animal Groups. " 
        repromptText = "I'm not sure what animal you are saying. " \
                       "Please provide a valid animal name or say stop to close Animal Groups. "
    
    
    elif event['request']['intent']['slots']['animalname']['name'] == 'animalname' :
        aname = event['request']['intent']['slots']['animalname']['value']
        cnt = 0
        for i in range(len(names)):
            if names[cnt].lower() == aname.lower() :
                speechOutput = "A group of " + aname + " is called " + groupname[cnt] +". " \
                               "You can ask me another animal's group name or say stop to close Animal Groups."
                
                repromptText = "You can ask me another animal's group name or say stop to close Animal Groups."
                break
            cnt = cnt + 1
        if len(speechOutput) == 0 :
            speechOutput = "I'm not sure what animal you are saying. " \
                        "Please try again."
            repromptText = "I'm not sure what animal you are saying. " \
                        "You can ask me another animal's group name"
    else:
         speechOutput = "I'm not sure what animal you are saying. " \
                        "Please try again."
         repromptText = "I'm not sure what animal you are saying. " \
                        "You can ask me another animal's group name"
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))


names = [
    "Zebras","Wolves","Whales","Weasles","Turtles","Turkeys","Toads","Tigers","Swans","Stingrays","Squirrels","Snakes","Skunk","Shark","Rhinoceroses","Ravens","Rats","Rabbits","Porcupines","Pigs","Parrots","Owls","Oxen","Otters","Mules","Monkeys","Moles","Lions","Leopards","Lemurs","Kangaroos","Jellyfish","Jaguars","Hyenas","Hippopotami","Gorillas","Giraffes","Geese","Frogs","Fox","Flamingos","Fish","Ferrets","Falcons","Elk","Elephants","Eagles","Donkeys","Dogs","Crows","Crocodiles","Cobras","Wild Cats","Cats","Camels","Buffalo","Bees","Bears","Bats","Badgers","Apes","Zebra","Wolf","Whale","Weasle","Turtle","Turkey","Toad","Tiger","Swan","Stingray","Squirrel","Snake","Rhinoceros","Raven","Rat","Rabbit","Porcupine","Pig","Parrot","Owl","Ox","Otter","Mule","Monkey","Mole","Lion","Leopard","Lemur","Kangaroo","Jaguar","Hyena","Hippopotamus","Gorilla","Giraffe","Goose","Frog","Flamingo","Ferret","Falcon","Elephant","Eagle","Donkey","Dog","Crow","Crocodile","Cobra","Wild Cat","Cat","Camel","Buffaloes","Bee","Bear","Bat","Badger","Ape"
    ]
    
groupname = [
    "a zeal","a pack","a pod, a school, or a gam","a colony, a gang or a pack","a bale or a nest","a gang or a rafter","a knot","an ambush or a streak","a bevy or a game (if in flight: a wedge)","a fever","a dray or a scurry","a nest","a stench","a shiver","a crash","an unkindness","a colony","a herd","a prickle","a drift or drove (younger pigs) or a sounder or a team (older pigs)","a pandemonium","a parliament","a team or a yoke","a family","a pack","a barrel or a troop","a labor","a pride","a leap","a conspiracy","a troop or a mob","a smack","a shadow","a cackle","a bloat","a band","a tower","a gaggle","an army","a charm","a stand","a school","a business","a cast","a gang or a herd","a parade","a convocation","a drove","a pack. Fun Fact: A group of Puppies is called a litter","a murder","a bask","a quiver","a destruction","a clowder or a glaring","a caravan","a gang or obstinacy","a swarm","a sloth or a sleuth","a colony or a camp","a cete","a shrewdness","a zeal","a pack","a pod, a school, or a gam","a colony, a gang or a pack","a bale or a nest","a gang or a rafter","a knot","an ambush or a streak","a bevy or a game (if in flight: a wedge)","a fever","a dray or a scurry","a nest","a crash","an unkindness","a colony","a herd","a prickle","a drift or drove (younger pigs) or a sounder or a team (older pigs)","a pandemonium","a parliament","a team or a yoke","a family","a pack","a barrel or a troop","a labor","a pride","a leap","a conspiracy","a troop or a mob","a shadow","a cackle","a bloat","a band","a tower","a gaggle","an army","a stand","a business","a cast","a parade","a convocation","a drove","a pack. Fun Fact: A group of Puppies is called a litter","a murder","a bask","a quiver","a destruction","a clowder or a glaring","a caravan","a gang or obstinacy","a swarm","a sloth or a sleuth","a colony or a camp","a cete","a shrewdness"
    ]