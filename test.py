list = [["orange", "vlees"], ["purple"], ["red"]]
list2 = [item for sublist in list for item in sublist]

print(list2)