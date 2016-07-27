Words = ["poem", "poetry"]


def isValid(text):
    return bool(re.search(r'\bpoem\b', text, re.IGNORECASE))


def handle(text, mic, profile):
    messages = ["It's 42, you idiot.",
                "It's 42. How many times do I have to tell you?"]

    message = random.choice(messages)

    mic.say(message)


mic.say("would you like to hear another")

