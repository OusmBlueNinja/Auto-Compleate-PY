import json, msvcrt, sys, os

def load_words():
    with open("common.json", "r") as f:
        return json.load(f)

def autocomplete(prefix, words):
    counter = 0
    result = []
    for word in words:
        if word.startswith(prefix):
            result.append(word)
            counter += 1
        if counter == 10:
            break
    return result

  
def getChar():
  char = msvcrt.getch()
  if char == b'\x3f':
    print("[EXIT] Closing Program")
    sys.exit()
  char2 = char
  return char2

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  

words = load_words()
prefix = ""
options = True
clear()
print("Press [ ? ] to exit \n")
while True:
  
    char = getChar()
    if char != b'\b':
      if options:
        prefix += str(char)[2]
    else: 
      prefix = prefix[:-1]
      
    if not prefix == "":
      suggestions = autocomplete(str(prefix), words)
    
    if len(suggestions) == 1:
      if char != b'\b':
        prefix = suggestions[0]
      options = False
    else:
      
      options = True
      
            
    clear()
    print("Press [ ? ] to exit")
    print()
    print(prefix)
    try:
      print(suggestions[0])
    except:
      print("No Words Found")
      
