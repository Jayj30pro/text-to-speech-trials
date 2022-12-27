import pyttsx3

speech = pyttsx3.init()

word = input("What should I say?  ")


# words added to beginning are not said trying to find out why


speech.say(word)



speech.runAndWait()

print(word)
