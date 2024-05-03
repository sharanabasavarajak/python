rows = 5  # Adjust this value to change the diamond size (must be odd)

for i in range(1, rows + 1):
  print(" " * (rows - i), end="")  # Print leading spaces
  if i == 1:
      print("*")
  else:
      print("*" + " " * (i*2-3) + "*")  # Print top outline

for i in range(rows - 1, 0, -1):
  print(" " * (rows - i), end="")  # Print leading spaces
  if i == 1:
      print("*")
  else:
      print("*" + " " * (i*2-3) + "*")  # Print top outline
