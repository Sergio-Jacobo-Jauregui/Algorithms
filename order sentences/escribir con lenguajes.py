import re

file = open('ingles.txt', 'r')
content = file.read()
file.close()

def order(text):
  sentences = text.split('\n')

  dicc = { }
  
  for i in sentences:
    search = re.search(r'\((.*?)\)', i) 
    word = search.group(1)
    try: dicc[word].append(i)
    except: dicc[word] = [i] 

  return dicc

ordered_sentences = order(content)

def imprimir_en_orden(dicc):
  text = ''
  for values in dicc.values():
    for undervalue in values:
      text += f'{undervalue}\n'
    text += '\n'
  return text

text = imprimir_en_orden(ordered_sentences)

# new_file_name = input('Que nombre le quieres poner?: ')
# file = open(f'{new_file_name}.txt', 'w')
file = open('ingles.txt', 'w')
file.write(str(text))
file.close()
