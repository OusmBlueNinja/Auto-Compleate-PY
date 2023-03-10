import json, msvcrt, sys, os

def __load_words():
    with open("common.json", "r") as f:
        return json.load(f)

def __autocomplete(prefix, words):
    counter = 0
    result = []
    for word in words:
        if word.startswith(prefix):
            result.append(word)
            counter += 1
        if counter == 10:
            break
    return result

  
def __getChar():
  char = msvcrt.getch()
  if char == b'\x3f':
    print("[EXIT] Closing Program")
    sys.exit()
  char2 = char
  return char2

def __clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  

words = __load_words()
prefix = ""
options = True
__clear()

  
def getWord(incompleteWord: str):
    return __autocomplete(str(incompleteWord), words)
    
    
      
            
    
      
