#PURPOSE: Get Student Details, theo and prac subject marks as input

import csv
import os
import time
import sys
import msvcrt

#COSMETICS
def print_y(msg): print(f"\033[93m{msg}\033[00m")      #YELLOW text
def print_g(msg): print(f"\033[92m{msg}\033[00m")      #GREEN text
def print_p(msg): print(f"\033[95m{msg}\033[00m")      #PURPLE text
def print_r(msg): print(f"\033[91m{msg}\033[00m")      #RED text
def print_b(msg): print(f"\033[96m{msg}\033[00m")      #BLUE text
def print_o(msg): print(f"\033[33m{msg}\033[00m")      #ORANGE text


cst, csp, mt, mp, pt, pp, ct, cp, et, ep = 0,0,0,0,0,0,0,0,0,0

d_name=["ID", "Name", "Class", "Section"] #for input loop
sub_name = ["CS", "Maths", "Physics", "Chemistry", "English"] #for input loop

sub_var=[cst, csp, mt, mp, pt, pp, ct, cp, et, ep]

fields=["ID", "Name", "Class", "Section", "CS Theory", "CS Practical", "Maths Theory", "Maths Practical", "Physics Theory", "Physics Practical", "Chemistry Theory", "Chemistry Practical", "English Theory", "English Practical"]

# CREATE FIELDS HEADERS
# f = open("records_dict.csv", 'a+')
# fw=csv.writer(f)
# fw.writerow(fields)
# f.close()

print()
print_y("----------------------------------------")
print_y("Welcome to Report Card Generator")
print_y("----------------------------------------")
print ("\n")

while True:
    #flushing next inputs (for windows only)
    sys.stdout.flush()
    while msvcrt.kbhit():
        msvcrt.getch()
    
    
    l_csv=[] #contains all field data
    ld=[] #contains details for report
    lm=[] # contains marks for report

    for i in d_name:
        inp=input(f"Enter {i}:")
        l_csv.append(inp)
        ld.append(inp)
    print()

    #for i,j,k in zip(sub_name, sub_var, sub_var[::2]):
    for i,j in zip(sub_name, sub_var):
        theo=int(input (f"Enter {i} Theory Marks:"))
        l_csv.append(theo)
        lm.append(theo)
        j=theo
        #print (j)
        prac=int(input (f"Enter {i} Practical Marks:"))
        l_csv.append(prac)
        lm.append(prac)
        k=prac
        #print(k)
        print()

    #print(l_csv, "\n")

    #print(sub_var , "\n")

    time.sleep(1) #DELAY BETWEEN INPUT AND REPORT

    print_y("------------REPORT------------\n")

    #DETAILS PRINT
    for i,j in zip(d_name, ld):
        print(f"{i}: {j}")
    print()

    #MARKS PRINT
    for i,j,k in zip(sub_name, lm, lm[::2]):
        print(f"{i} Theory: {j} Practical: {k}")
        print_p(f"{i} Total: {j+k}")
        print()

    #TOTAL & AVERAGE MARKS PRINT
    s=0
    for i in lm:
        s+=i
    total=s
    avg=s/(len(sub_name))
    print_b(f"TOTAL MARKS: {total}")
    print_b(f"AVERAGE MARKS: {avg}")
    print("\n\n")

    #CSV WRITE
    f = open("D:\Works & Skills\Coding\!School Projects\Report Card Generator/records_dict.csv", 'a+')
    fw=csv.writer(f)
    fw.writerow(l_csv)
    f.close()
    #CSV WRITE OVER

    time.sleep(1)

    c=input("\033[91mAdd another record? (y/n):\033[00m")
    print("\n")

    if c.lower()!="y":
        print_g("--------------")
        print_g("Thank You :]")
        print_g("--------------\n")
        time.sleep(1)
        break
