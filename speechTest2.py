import pyttsx3

def announce(words):
    speech = pyttsx3.init()
    rate = speech.getProperty('rate')
    speech.setProperty('rate', 175)
    speech.say(words)
    speech.runAndWait()

word = input("What should I say?  ")

announce(word)

print(word)
