with open('input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

count = 0

#part 1
#for line in data:
#  line = line.split(',')
#  p1 = line[0].split('-')
#  p2 = line[1].split('-')
#  if(int(p1[0]) <= int(p2[0])):
#    if(int(p1[1]) >= int(p2[1])):
#      count += 1
#      print(p1,p2)
#      continue
#  if(int(p2[0]) <= int(p1[0])):
#    if(int(p2[1]) >= int(p1[1])):
#      count += 1
#      print(p1,p2)
#print(count)

for line in data:
  line = line.split(',')
  p1 = line[0].split('-')
  p2 = line[1].split('-')
  if(int(p1[0]) <= int(p2[0])):
    if(int(p2[0]) <= int(p1[1])):
      count+=1
      print(p1,p2)
      continue
  if(int(p2[0]) <= int(p1[0])):
    if(int(p1[0]) <= int(p2[1])):
      count+=1
      print(p1,p2)
print(count)
