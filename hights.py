import math

input = open('input.txt', 'r')
output = open('output.txt', 'w')

max_square = 0      #var to save square
out_height = 0      #var to save height
h_last = 0          #pervios input height
rect_set = []       #set of rects as a "list of lists"

c = input.readline().rstrip()
while len(c) > 0:
    h = int(c)                      #current height
    if h > h_last:                  
        for rect in rect_set:
           rect[0] += 1             #add width to all rect_set
        rect_set.append([1,h])      #add new rect to rect_set
    elif h == h_last:               
        for rect in rect_set:
           rect[0] += 1             #just add width
    else:
        for i in range(len(rect_set)-1,-1,-1):  #check all rect in rect_set from last to first
            if rect_set[i][1] <= h:             #add width
               rect_set[i][0] +=1
            else:
               if rect_set[i][1] * rect_set[i][0] > max_square: #check for better square
                   max_square = rect_set[i][1] * rect_set[i][0] #set max square
                   out_height = rect_set[i][1]                  #set height
                   rect_set.pop(i)                              #delete rect from rect_set
    h_last = h
    c = input.readline().rstrip()

# check all rects in rect_set for better square
for i in range(len(rect_set)):
    if rect_set[i][1] * rect_set[i][0] > max_square:
        max_square = rect_set[i][1] * rect_set[i][0]
        out_height = rect_set[i][1]

# out
print(max_square, file=output)
print(out_height, file=output)
input.close()
output.close()