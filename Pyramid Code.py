message_file = open("message.txt", "r")

def decode(message_file):
  lines = message_file.read().split("\n")

  edits = []
  
  for line in lines:
      edits.append(line.split(" "))
    

  edits.sort(key=lambda x: int(x[0]))
  print(edits)
  
  for edit in edits:
      del edit[0]
  
  rows = 0
  
  elements = []

  while len(edits) > 0:
    elements.append(edits.pop(0))
    rows+=1

    del edits[0:rows]

    message = " ".join(element[0] for element in elements)
    message.strip()
 
  return message

print(decode(message_file))

message_file.close()
