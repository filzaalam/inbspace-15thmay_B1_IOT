###############que 1
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
for num in numbers:
    if num%2==0:
        print(num)
    elif num==237:
        break
############################Que2
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color = color_list_1.difference(color_list_2)
print(color)

############################Que3

from string import ascii_lowercase
def check(s):
    return set(ascii_lowercase)-set(s.lower()) == set()
string = input('Enter the string: ')
if check(string)== True:
    print("pangram")
else:
    print("not pangram")

#############################Que4

num = int(input("Enter the number: "))
m = int( "%s" % num )
n = int( "%s%s" % (num,num) )
o = int( "%s%s%s" % (num,num,num) )
print (m+n+o)

###########################Que5

l =input('enter:')
res = []
res = l.split('#')
l1 = []
l2 = []
for i in list(res[0].split()):
    l1.append(int(i))
print(l1)
for i in list(res[1].split()):
    l2.append(int(i))
print(l2)
#############################Que6


v = input("Input some comma seprated word sequence : ")
words = [word for word in v.split(',')]
print(','.join(sorted(list(set(words)))))


##################################Que7
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
	

	
index = 0;
for i in d['Marks']:
    if i == max(d['Marks']):    
	break
    else:           
        index += 1
print(d['Student'][index])       


###############################Que8

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


#########################Que9

d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

subject = input() 

newData = {'Name': [], 'Subject': [], 'Ratings':[] }


subject_index_list = [index for index in range(len(d['Subject'])) if subject == d['Subject'][index]]


for i in subject_index_list:
    
    newData['Name'].append(d['Name'][i])
    newData['Subject'].append(d['Subject'][i])
    newData['Ratings'].append(d['Ratings'][i] )

print(newData)


##############################que10

def generator(n):
    list_of = range(1,n+1)
     for i in list_of:
         if i % 7 == 0:
             yield i
n = int(input('enter number: '))
print(list(generator(n)))



####################################que11
import math

x, y = 0, 0

while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)    

