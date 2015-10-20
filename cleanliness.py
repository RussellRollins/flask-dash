import random

clean_messages = [
  "The dishes are clean!",
  "The dishes are spotless, ya' jackass.",
  "They can't get cleaner than this.",
  "Those dishes are pretty damn clean.",
  "You should probably empty it, you lazy bum (they're clean)"
]

dirty_messages = [
  "The dishes are filthy.",
  "Dishes dirty, maybe run the dishwasher?",
  "Those dishes are pretty damn dirty.",
  "THEY AREN'T!",
  "Not clean, not clean at all."
]

def message(is_clean):
  if is_clean:
    return select_rand_message(clean_messages)
  else:
    return select_rand_message(dirty_messages)

def select_rand_message(message_array):
  return message_array[random.randrange(0,len(clean_messages),1)] 
