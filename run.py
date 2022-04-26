import time
import random
correct = []
score = len(correct)

def openingTitle():
    print("""      _______    __     ________   ________   ___       _______  
     /"      \  |" \   |"      "\ |"      "\ |"  |     /"     "| 
    |:        | ||  |  (.  ___  :)(.  ___  :)||  |    (: ______) 
    |_____/   ) |:  |  |: \   ) |||: \   ) |||:  |     \/    |   
     //      /  |.  |  (| (___\ ||(| (___\ || \  |___  // ___)_  
    |:  __   \  /\  |\ |:       :)|:       :)( \_|:  \(:      "| 
    |__|  \___)(__\_|_)(________/ (________/  \_______)\_______) 
    |"  \    /"  | /"     "|                                     
     \   \  //   |(: ______)                                     
     /\\\  \/.    | \/    |                                       
    |: \.        | // ___)_                                      
    |.  \    /:  |(:      "|                                     
    |___|\__/|___|_\_______) __      ________   ___              
    ("     _   ")/" |  | "\ |" \    /"       ) |"  |             
     )__/  \\\__/(:  (__)  :)||  |  (:   \___/  ||  |             
        \\\_ /    \/      \/ |:  |   \___  \    |:  |             
        |.  |    //  __  \\\ |.  |    __/  \\\  _|  /              
        \:  |   (:  (  )  :)/\  |\  /" \   :)/ |_/ )             
         \__|    \__|  |__/(__\_|_)(_______/(_____/              
                                                                """)

def riddleGameStart():
    print(""" +-+-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
 |W|o|u|l|d| |y|o|u| |l|i|k|e| |t|o| |a|n|s|w|e|r| |s|o|m|e| |r|i|d|d|l|e|s|?| |(|Y|e|s|/|N|o|)|:|
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+""")
    print("\n")
    answer = input()
    print("\n")

    if answer.lower() == 'no':
        print(""" +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+
 |S|o|r|r|y|,| |m|a|y|b|e| |n|e|x|t| |t|i|m|e|!|
 +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+""")
        print("\n")
        time.sleep(2)
        openingTitle()
        riddleGameStart()
    if answer.lower() == 'yes':
        print(""" +-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+
 |Y|a|y|,| |l|e|t|'|s| |s|t|a|r|t|!|
 +-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+""")
        print("\n")
        riddleGame()
    else:
        print(""" +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+ +-+-+ +-+-+
 |P|l|e|a|s|e| |t|y|p|e| |Y|e|s| |o|r| |N|o|
 +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+ +-+-+ +-+-+""")
        print("\n")
        riddleGameStart()

def rating(score):
    print("\n")
    print("congratulations, you have answered",score,"correctly")
    print("\n")
    print(""" +-+-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
 |W|o|u|l|d| |y|o|u| |l|i|k|e| |t|r|y| |m|o|r|e| |r|i|d|d|l|e|s|?| |(|Y|e|s|/|N|o|)|:|
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+""")
    print("\n")
    answer = input()
    print("\n")

    if answer.lower() == 'no':
        print(""" +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+
 |S|o|r|r|y|,| |m|a|y|b|e| |n|e|x|t| |t|i|m|e|!|
 +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+""")
        print("\n")
        time.sleep(3)
        print("\n")
        print("\n")
        correct.clear()
        openingTitle()
        riddleGameStart()
    if answer.lower() == 'yes':
        print(""" +-+-+-+-+ +-+-+-+-+-+ +-+-+ +-+-+-+
 |Y|a|y|,| |l|e|t|'|s| |d|o| |i|t|!|
 +-+-+-+-+ +-+-+-+-+-+ +-+-+ +-+-+-+""")
        print("\n")
        time.sleep(3)
        openingTitle()
        riddleGame()
        score = len(correct)
        rating(score)
    else:
        print(""" +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+ +-+-+ +-+-+
 |P|l|e|a|s|e| |t|y|p|e| |Y|e|s| |o|r| |N|o|
 +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+ +-+-+ +-+-+""")
        print("\n")
        riddleGameStart()

def riddleGame():
    for riddles_needed in range(int("3")):
        riddle_one = 1
        riddle_two = 2
        riddle_three = 3

        riddle_number = random.randint(1, 3)

        if riddle_number == 1:
            print(""" +-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+
 |W|h|a|t| |h|a|s| |m|a|n|y| |t|e|e|t|h|,| |b|u|t| |c|a|n|n|o|t| |b|i|t|e|?|
 +-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+""")
            print("\n")
            riddle_one_answer = input()
            print("\n")
            if riddle_one_answer.lower() == "a comb" or riddle_one_answer.lower() == "comb":
                correct.append("yes")
                print("\ncorrect!\n")
            else:
                print("\nworng!\n")
        if riddle_number == 2:
            print("\nriddletwo?\n")
            print("\n")
            riddle_two_answer = input()
            print("\n")
            if riddle_two_answer == "b":
                correct.append("yes")
                print("\ncorrect!\n")
            else:
                print("\nworng!\n")
        if riddle_number == 3:
            print("\nriddlethree?\n")
            print("\n")
            riddle_three_answer = input()
            print("\n")
            if riddle_three_answer == "c":
                correct.append("yes")
                print("\ncorrect!\n")
            else:
                print("\nworng!\n")

openingTitle()
riddleGameStart()
score = len(correct)
rating(score)
