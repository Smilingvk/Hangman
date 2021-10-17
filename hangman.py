
from math import trunc
import os 
import random 

IMAGES = ['''  +---+
  |   |
      |  ♥ ♥ ♥ ♥ ♥ ♥ ♥
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |  ♥ ♥ ♥ ♥ ♥ ♥ 
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
  |   |  ♥ ♥ ♥ ♥ ♥
      |
      |
=========''', '''  +---+
  |   |
  O   |  ♥ ♥ ♥ ♥
 /|   |
      |
      |
=========''', '''  +---+
  |   |
  O   |  ♥ ♥ ♥
 /|\  |
      |
      |
=========''', '''  +---+
  |   |
  O   |  ♥ ♥
 /|\  |
 /    |
      |
=========''', '''  +---+
  |   |
  O   |  ♥
 /|\  |
 / \  |
      |
=========''']

hangman_title = """ 
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

 WELCOME TO MY GAME !
 ingresa el numero 1 para jugar: 
 o haz ctrl c para salir :p 

"""

lost = """

 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝

"""
win = """ 

██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝

"""
def normalize(s): 
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

def read_data(filepath = "./data.txt"):
    words= []
    with open(filepath, "r", encoding="utf-8") as f :
        for line in f :
           words.append(line.strip().upper())
    return words

def display_board(chosen_word_list_underscores, tries):
        print(IMAGES[tries])
        print(" ")
        print(chosen_word_list_underscores)
        print("..................................")

def run():
    data = read_data(filepath = "./data.txt")
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = [" _ "] * len(chosen_word_list)
    letter_index_dict = {}
    for idx ,letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
             letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    tries = 0
    
    
          
    while True:
      os.system("cls")
      display_board(chosen_word_list_underscores, tries)

      for element in chosen_word_list_underscores:
          print(element + " ", end="")
      print("\n")

      try:
        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), input("Solo puedes ingresar letras :p!, presiona enter para continuar")
        assert len(letter) == 1, input("Solo puedes ingresar una letra!, presiona enter para continuar ")
      except AssertionError as e :
        print(e)
        continue
           
      if letter in chosen_word_list:
          for idx in letter_index_dict[letter]:
            chosen_word_list_underscores[idx] = letter
      
      if " _ " not in chosen_word_list_underscores:
        os.system("cls")
        print(win)
        print("¡Felicitaciones! Lo lograste. La palabra era: ", chosen_word)
        break
      
      else:
        tries += 1
        if tries == 7 :
            os.system("cls")
            print(lost)
            print("La palabra correcta era {}" .format(chosen_word))
            break
      

     
while True:
  try:
    opcion = input(hangman_title)
    if int(opcion) == 1:
      run()
    else: input("Debes ingresar el número 1 para jugar. Presiona la tecla Enter para reintentar.")
    assert len(str(opcion)) == 1, input("¡No puedes ingresar varias letras o números!, Presiona la tecla Enter para reintentar.")
  except AssertionError as a:
        print(a) 
  except ValueError:
        input("No se aceptan letras, ingresa el número 1 para jugar. Presiona la tecla Enter para reintentar.")   
        
    
if __name__ == "__main__":
  run()
  

