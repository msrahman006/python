import random

def selected_word():
  words=['Take','fake','lake','joke']
  word = words[random.randint(0,len(words)-1)]
  return word