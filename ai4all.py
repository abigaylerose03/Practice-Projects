# Your code here
d = dict()
count = 0
fave_fast_food = input("Fave fast food restaurant: ")

for i in range(1, 11):
  if fave_fast_food in d:
      d[fave_fast_food] += 1
  else:
      d[fave_fast_food] = 1
  count+= 1
  fave_fast_food = input("Fave fast food restaurant: ")

for k,v in d.items():
    print('Fast Food Resturants that are ' + k + ": " + str(v))

maximum = max(d, key=d.get)  # Just use 'min' instead of 'max' for minimum.
print("The fast food restaurant " + maximum + " has this many votes:", d[maximum])