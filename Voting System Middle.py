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

dir = "D:/" #"D:/Work, creations, projects and stuff/Coding/VOTING SYSTEM/Middle Section/RESULT/"
file = "!Middle_Voting_Result"

#POSTS & HOUSES
post_list = [
    {"post": "PRESIDENT", "candidates": [None, "Nikita Chattri", "Kashvi Siotia"], "votes": [None, 0, 0]},
    {"post": "PRIME MINISTER", "candidates": [None, "Pranjal Lohia", "Dristi Lepcha", "Ryan Roy"], "votes": [None, 0, 0, 0]},
    {"post": "CULTURAL SECRETARY", "candidates": [None, "Manvi Agarwal", "Pratistha Gurung", "Aadya Agarwal"], "votes": [None, 0, 0, 0]},
    {"post": "EDUCATION MINISTER HEAD", "candidates": [None, "Dishita Arya", "Tseten Tempo", "Nirvaan Agarwal"], "votes": [None, 0, 0, 0]},
    {"post": "SPORTS MINISTER", "candidates": [None, "Grisha Bhattarai", "Keenara Pradhan"], "votes": [None, 0, 0]},
    {"post": "SPEAKER", "candidates": [None, "Nirja Upreti", "Ishaanvi Prasad", "Saanvi Mukherjee"], "votes": [None, 0, 0, 0]},
    {"post": "IT MINISTER", "candidates": [None, "Aarav Raj Pradhan", "Darsh Jajodia"], "votes": [None, 0, 0]},
    {"post": "ENVIRONMENT MINISTER HEAD", "candidates": [None, "Rasi Agarwal", "Mahima Pradhan"], "votes": [None, 0, 0]},
    {"post": "DEPUTY ENVIRONMENT MINISTER", "candidates": [None, "Vrithi Chettri", "Ryan Goyal", "Aradhya Singh", "Jessica Yolmo", "Abhimanyu Jairam", "Manasvi Bansal", "Garvit Singh", "Koustov Ghosh"], "votes": [None, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"post": "FILM AND MEDIA HEAD", "candidates": [None, "Nysha Saran", "Aradhya Dhamala"], "votes": [None, 0, 0]},
    {"post": "EVENT MANAGER HEAD", "candidates": [None, "Anusha Mandal", "Dichen Sherpa", "Hardiya Garg"], "votes": [None, 0, 0, 0]},
    {"post": "DEPUTY EVENT MANAGER", "candidates": [None, "Aarav Mittal", "Banalata Das", "Vibhu Goyal", "Kavya Sahi", "Arya Hang Rai", "Dripta Das", "Hanok Jeremath Tsaacs Bhutia", "Archisha Ranjan", "Swarit Gupta"], "votes": [None, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"post": "RADHAKRISHNAN CAPTAIN", "candidates": [None, "Ruben Chettri", "Taseefa Noor Kalam"], "votes": [None, 0, 0, 0, 0, 0]},
    {"post": "TAGORE CAPTAIN", "candidates": [None, "Anunay Evan Basumata", "Divyansh Agarwal"], "votes": [None, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"post": "TERESA CAPTAIN", "candidates": [None, "Rishab Gamj", "Md.Sheroz Afzal"], "votes": [None, 0, 0]},
    {"post": "VIVEKANANDA CAPTAIN", "candidates": [None, "Dithya Siotia", "Sarada Pandey"], "votes": [None, 0, 0]}
]

house_list = [None,  "RADHAKRISHNAN", "TAGORE", "TERESA", "VIVEKANANDA"]
house_list_colorised = [None,  "\033[91mRADHAKRISHNAN\033[m", "\033[92mTAGORE\033[m", "\033[96mTERESA\033[m", "\033[93mVIVEKANANDA\033[m"]


while True:
    #flushing next inputs (for windows only)
    sys.stdout.flush()
    while msvcrt.kbhit():
        msvcrt.getch()
    
    print("\n \n")
    print_r("\033[1m =====THE VOTING GAMES BEGINS===== \033[0m \n \n \n")
    #HOUSE SELECTION
    print("\033[1m CHOOSE YOUR HOUSE : \033[0m")
    for i in range(1, 5):
        print(f"{i}) {house_list_colorised[i]}")
    print()
    while True:
        try:
            hn = int(input("Enter House Number (1-4): "))
        except ValueError:
            print_r("\nPlease enter a Valid value from 1 to 4")
            continue
        if hn not in [1,2,3,4]:
            print_r("\nPlease enter a Valid value from 1 to 4")
            continue
        else:
            break
    house = house_list[hn]
    print()
    print(f"House Selected: {house_list_colorised[hn]}\n \n")

    #SELECT TO VOTE
    for d in post_list :
        post = d["post"]
        #check house
        if (post.split()[0]) not in house_list or (post.split()[0]) == house:
            #Print candidate list
            print_y(f"\033[1m CHOOSE {post}: \033[0m")
            for i in range(1, len(d["candidates"])):
                print(f"{i}) {d['candidates'][i]}")
            print()
            #Number of options list generate
            nc=[]
            for i in range(1, len(d["candidates"])):
                nc.append(i)
            # Choose candidate
            while True:
                try:
                    s = int(input(f"Enter Candidate Number (1-{len(d['candidates'])-1}): "))
                except ValueError:
                    print_r(f"\nPlease enter a Valid value from 1 to {len(d['candidates'])-1} ")
                    continue
                if s not in (nc):
                    print_r(f"\nPlease enter a Valid value from 1 to {len(d['candidates'])-1} ")
                    continue
                else:
                    break 
                #TODO can create csv update system here to directly update csv by checking if it matches and when it does it adds to it
            print()
            d["votes"][s] += 1
            with open(f"{dir}{post}.csv", "w+") as f:
                fw=csv.writer(f)
                fw.writerow(['CANDIDATE', 'VOTE'])
                for i in range(1, len(d["candidates"])):
                    fw.writerow([d["candidates"][i], d["votes"][i]])
            print()
    # Clearing the Screen
    print()
    print_p ("\033[1m ===== THANK YOU FOR VOTING. ENJOY DEMOCRACY. :] ===== \033[0m")
    print("\n \n")
    time.sleep(3.6)
    os.system('cls')

    #FILE GENERATION

    #txt
    with open(f"{dir}{file}.txt", "w") as f:
        for d in post_list:
            f.write(d["post"] + ":\n")
            for i in range(1, len(d["candidates"])):
                f.write(str(i) + ")" + d["candidates"][i] + ":" + str(d["votes"][i]) + "\n")
            f.write("\n")

    #csv
    with open(f"{dir}{file}.csv", "w") as f:
        fw=csv.writer(f)
        fw.writerow(['POST', 'CANDIDATE', 'VOTE'])
        for d in post_list:
            fw.writerow([d["post"]])
            for i in range(1, len(d["candidates"])):
                fw.writerow(['', d["candidates"][i], d["votes"][i]])
            fw.writerow([])