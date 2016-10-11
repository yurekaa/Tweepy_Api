#--------------------------------------------------------------------------#
#                             Created/Credited by                          #
#                             Kibeom Alex Hong                             #
#--------------------------------------------------------------------------#

# This code parses your list of IDs into different groups in text file
# by the length of IDs.

#--------------------------------------------------------------------------#



ids = open("smithsonian_ids.txt","r")
# select your IDs text file created from "get_followers_ids.py"


# ** VERY IMPORTANT : Last line of the text file should have blank line with no text.




#--------------------------------------------------------------------------#

content = ids.readlines()

ids.close()



one_file = open("one.txt","w")
# numbers that are length of 1

two_file = open("two.txt","w")
# numbers that are length of 2

three_file = open("three.txt","w")
# numbers that are length of 3

four_file = open("four.txt","w")
# numbers that are length of 4

five_file = open("five.txt","w")
# numbers that are length of 5

six_file = open("six.txt","w")
# numbers that are length of 6

seven_file = open("seven.txt","w")
# numbers that are length of 7

eight_file = open("eight.txt","w")
# numbers that are length of 8

nine_file = open("nine.txt","w")
# numbers that are length of 9

ten_file = open("ten.txt","w")
# numbers that are length of 10


one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
ten = []



for item in content:

    if len(str(item)) == 2:
        one.append(item)
        #one
    elif len(str(item)) == 3:
        two.append(item)
        #two
    elif len(str(item)) == 4:
        three.append(item)
        #three
    elif len(str(item)) == 5:
        four.append(item)
        #four
    elif len(str(item)) == 6:
        five.append(item)
        #five
    elif len(str(item)) == 7:
        six.append(item)
        #six
    elif len(str(item)) == 8:
        seven.append(item)
        #seven
    elif len(str(item)) == 9:
        eight.append(item)
        #eight
    elif len(str(item)) == 10:
        nine.append(item)
        #nine
    elif len(str(item)) == 11:
        ten.append(item)
        #ten



for i in one:
    one_file.write(str(i))        
for i in two:
    two_file.write(str(i))
for i in three:
    three_file.write(str(i))
for i in four:
    four_file.write(str(i))
for i in five:
    five_file.write(str(i))
for i in six:
    six_file.write(str(i))
for i in seven:
    seven_file.write(str(i))
for i in eight:
    eight_file.write(str(i))
for i in nine:
    nine_file.write(str(i))
for i in ten:
    ten_file.write(str(i))

one_file.close()
two_file.close()
three_file.close()
four_file.close()
five_file.close()
six_file.close()
seven_file.close()
eight_file.close()
nine_file.close()
ten_file.close()



print "done"

#----------------------------------------------------------------------------------------------#
#                                                                                       1      


import textwrap

one_id = open("one.txt","r")

one_content = one_id.read()

one_id.close()



one_content = str(one_content).replace("\n",",")


one_content = '\n'.join(textwrap.wrap(one_content, 200)) # 1


one_final = open("one.txt","w")
one_final.write(one_content)
one_final.close()


one_new = open("one.txt","r")
one_content_new = one_new.readlines()


one_final = open("one.txt","w")


for i in one_content_new[0:-1]:
    new = i[:-2]
    one_final.write(new + "\n")

for i in one_content_new[-1:]:
    one_final.write(i[:-1])

one_final.close()

print "1 Done"

#----------------------------------------------------------------------------------------------#
#                                                                                       2      

import textwrap

two_id = open("two.txt","r")

two_content = two_id.read()

two_id.close()



two_content = str(two_content).replace("\n",",")


two_content = '\n'.join(textwrap.wrap(two_content, 300)) # 2


two_final = open("two.txt","w")
two_final.write(two_content)
two_final.close()


two_new = open("two.txt","r")
two_content_new = two_new.readlines()


two_final = open("two.txt","w")


for i in two_content_new[0:-1]:
    new = i[:-2]
    two_final.write(new + "\n")

for i in two_content_new[-1:]:
    two_final.write(i[:-1])

two_final.close()

print "2 Done"


#----------------------------------------------------------------------------------------------#
#                                                                                       3      


import textwrap

three_id = open("three.txt","r")

three_content = three_id.read()

three_id.close()



three_content = str(three_content).replace("\n",",")


three_content = '\n'.join(textwrap.wrap(three_content, 400)) # 3


three_final = open("three.txt","w")
three_final.write(three_content)
three_final.close()


three_new = open("three.txt","r")
three_content_new = three_new.readlines()


three_final = open("three.txt","w")


for i in three_content_new[0:-1]:
    new = i[:-2]
    three_final.write(new + "\n")

for i in three_content_new[-1:]:
    three_final.write(i[:-1])

three_final.close()

print "3 Done"

#----------------------------------------------------------------------------------------------#
#                                                                                       4      


import textwrap

four_id = open("four.txt","r")

four_content = four_id.read()

four_id.close()



four_content = str(four_content).replace("\n",",")


four_content = '\n'.join(textwrap.wrap(four_content, 500)) # 4


four_final = open("four.txt","w")
four_final.write(four_content)
four_final.close()


four_new = open("four.txt","r")
four_content_new = four_new.readlines()


four_final = open("four.txt","w")


for i in four_content_new[0:-1]:
    new = i[:-2]
    four_final.write(new + "\n")

for i in four_content_new[-1:]:
    four_final.write(i[:-1])

four_final.close()

print "4 Done"

#----------------------------------------------------------------------------------------------#
#                                                                                       5      


import textwrap

five_id = open("five.txt","r")

five_content = five_id.read()

five_id.close()



five_content = str(five_content).replace("\n",",")


five_content = '\n'.join(textwrap.wrap(five_content, 600)) # 5


five_final = open("five.txt","w")
five_final.write(five_content)
five_final.close()


five_new = open("five.txt","r")
five_content_new = five_new.readlines()


five_final = open("five.txt","w")


for i in five_content_new[0:-1]:
    new = i[:-2]
    five_final.write(new + "\n")

for i in five_content_new[-1:]:
    five_final.write(i[:-1])

five_final.close()

print "5 Done"

#----------------------------------------------------------------------------------------------#
#                                                                                       6      


import textwrap

six_id = open("six.txt","r")

six_content = six_id.read()

six_id.close()



six_content = str(six_content).replace("\n",",")


six_content = '\n'.join(textwrap.wrap(six_content, 700)) # 6


six_final = open("six.txt","w")
six_final.write(six_content)
six_final.close()


six_new = open("six.txt","r")
six_content_new = six_new.readlines()


six_final = open("six.txt","w")


for i in six_content_new[0:-1]:
    new = i[:-2]
    six_final.write(new + "\n")

for i in six_content_new[-1:]:
    six_final.write(i[:-1])

six_final.close()

print "6 Done"


#----------------------------------------------------------------------------------------------#
#                                                                                       7      


import textwrap

seven_id = open("seven.txt","r")

seven_content = seven_id.read()

seven_id.close()



seven_content = str(seven_content).replace("\n",",")


seven_content = '\n'.join(textwrap.wrap(seven_content, 800)) # 7


seven_final = open("seven.txt","w")
seven_final.write(seven_content)
seven_final.close()


seven_new = open("seven.txt","r")
seven_content_new = seven_new.readlines()


seven_final = open("seven.txt","w")


for i in seven_content_new[0:-1]:
    new = i[:-2]
    seven_final.write(new + "\n")

for i in seven_content_new[-1:]:
    seven_final.write(i[:-1])

seven_final.close()

print "7 Done"

#----------------------------------------------------------------------------------------------#
#                                                                                       8      

                                                                                

import textwrap

eight_id = open("eight.txt","r")

eight_content = eight_id.read()

eight_id.close()



eight_content = str(eight_content).replace("\n",",")


eight_content = '\n'.join(textwrap.wrap(eight_content, 900)) # 8


eight_final = open("eight.txt","w")
eight_final.write(eight_content)
eight_final.close()


eight_new = open("eight.txt","r")
eight_content_new = eight_new.readlines()


eight_final = open("eight.txt","w")


for i in eight_content_new[0:-1]:
    new = i[:-2]
    eight_final.write(new + "\n")

for i in eight_content_new[-1:]:
    eight_final.write(i[:-1])

eight_final.close()

print "8 Done"


#----------------------------------------------------------------------------------------------#
#                                                                                       9      


import textwrap

nine_id = open("nine.txt","r")

nine_content = nine_id.read()

nine_id.close()



nine_content = str(nine_content).replace("\n",",")


nine_content = '\n'.join(textwrap.wrap(nine_content, 1000)) # 9


nine_final = open("nine.txt","w")
nine_final.write(nine_content)
nine_final.close()


nine_new = open("nine.txt","r")
nine_content_new = nine_new.readlines()


nine_final = open("nine.txt","w")


for i in nine_content_new[0:-1]:
    new = i[:-2]
    nine_final.write(new + "\n")

for i in nine_content_new[-1:]:
    nine_final.write(i[:-1])

nine_final.close()

print "9 Done"


#----------------------------------------------------------------------------------------------#
#                                                                                       10     


import textwrap

ten_id = open("ten.txt","r")

ten_content = ten_id.read()

ten_id.close()



ten_content = str(ten_content).replace("\n",",")


ten_content = '\n'.join(textwrap.wrap(ten_content, 1100)) # 10


ten_final = open("ten.txt","w")
ten_final.write(ten_content)
ten_final.close()


ten_new = open("ten.txt","r")
ten_content_new = ten_new.readlines()


ten_final = open("ten.txt","w")


for i in ten_content_new[0:-1]:
    new = i[:-2]
    ten_final.write(new + "\n")

for i in ten_content_new[-1:]:
    ten_final.write(i[:-1])

ten_final.close()

print "10 Done"


#----------------------------------------------------------------------------------------------#


lines_one = open("one.txt", "r")
lines_one_content = lines_one.read()

lines_two = open("two.txt", "r")
lines_two_content = lines_two.read()

lines_three = open("three.txt", "r")
lines_three_content = lines_three.read()

lines_four = open("four.txt", "r")
lines_four_content = lines_four.read()

lines_five = open("five.txt", "r")
lines_five_content = lines_five.read()

lines_six = open("six.txt", "r")
lines_six_content = lines_six.read()

lines_seven = open("seven.txt", "r")
lines_seven_content = lines_seven.read()

lines_eight = open("eight.txt", "r")
lines_eight_content = lines_eight.read()

lines_nine = open("nine.txt", "r")
lines_nine_content = lines_nine.read()

lines_ten = open("ten.txt", "r")
lines_ten_content = lines_ten.read()

#----------------------------------------------------------------------------------------------#

final_ids = open("all_ids_by_100.txt", "w")


final_ids.write(lines_one_content + "\n")
final_ids.write(lines_two_content + "\n")
final_ids.write(lines_three_content + "\n")
final_ids.write(lines_four_content + "\n")
final_ids.write(lines_five_content + "\n")
final_ids.write(lines_six_content + "\n")
final_ids.write(lines_seven_content + "\n")
final_ids.write(lines_eight_content + "\n")
final_ids.write(lines_nine_content + "\n")
final_ids.write(lines_ten_content)


#----------------------------------------------------------------------------------------------#

final_ids.close()

print "All Done !"



# take the "all_ids_by_100.txt" file and use it at "list_of_bios.py"

# GO TO --> "list_of_bios.py"













