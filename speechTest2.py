import pyttsx3

def announce(words):
    speech = pyttsx3.init()
    speech.say("one two three"+ words)
    speech.runAndWait()

word = input("What should I say?  ")

announce(word)

print(word)
