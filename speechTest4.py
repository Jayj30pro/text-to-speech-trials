import pyttsx3

def announce(words):
    speech = pyttsx3.init()
    rate = speech.getProperty('rate')
    speech.setProperty('rate', 150)
    voice = speech.getProperty('voices')
    #speech.setProperty('voice', 'english+f1')
    #speech.setProperty('voice', 'english+f2')
    #speech.setProperty('voice', 'english+f3')
    speech.setProperty('voice', 'english+f4')
    #speech.setProperty('voice', 'english_rp+f3') #my preference
    #speech.setProperty('voice', 'english_rp+f4')

    speech.say("one two  "+ words)
    speech.runAndWait()

word = input("What should I say?  ")

announce(word)

print(word)

