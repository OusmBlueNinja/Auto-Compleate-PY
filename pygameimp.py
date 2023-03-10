import pygame
import json, msvcrt, sys, os

def load_words():
    with open("words_dictionary.json", "r") as f:
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
    sys.exit()
  char2 = char
  return char2

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  

words = load_words()
prefix = ""
options = True
  
    

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Create a Pygame window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the font for the text input box
font = pygame.font.SysFont(None, 32)

# Set the position and size of the text input box
input_box = pygame.Rect(100, 100, 200, 32)

# Set the default text and color for the text input box
text = ""
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive

# Create a Pygame clock
clock = pygame.time.Clock()
backspace = False

# Main Pygame loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle the active state of the text input box
            if input_box.collidepoint(event.pos):
                color = color_active
            else:
                color = color_inactive
        if event.type == pygame.KEYDOWN:
            # If the text input box is active, add characters to the text string
            if color == color_active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    backspace = True
                else:
                    backspace = False
                    text += event.unicode
    prefix = text
    
      
    
    suggestions = autocomplete(str(prefix), words)
    
    if len(suggestions) == 1:
      
      if backspace: 
        pass
        
        
      else:
        text = suggestions[0]
      options = False
    else:
      
      options = True

    # Clear the screen
    window.fill((255, 255, 255))

    # Render the text input box
    pygame.draw.rect(window, color, input_box, 2)
    text_surface = font.render(text, True, (0, 0, 0))
    try:
      print(suggestions)
      text_surface2 = font.render(suggestions[0], True, (211, 211, 211))
      
    except:
      pass
    window.blit(text_surface2, (input_box.x + 5, input_box.y + 5))
    window.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)
