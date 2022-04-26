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
    print("Would you like to answer some riddles? (Yes/No): ")
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
        print(3)
        time.sleep(1)
        print("\n")
        print(2)
        time.sleep(1)
        print("\n")
        print(1)
        time.sleep(1)
        print("\n")
        print("\n")
        print("\n")
        correct.clear()
        openingTitle()
        riddleGameStart()
        score = len(correct)
        rating(score)
    if answer.lower() == 'yes':
        print(""" +-+-+-+-+ +-+-+-+-+-+ +-+-+ +-+-+-+
 |Y|a|y|,| |l|e|t|'|s| |d|o| |i|t|!|
 +-+-+-+-+ +-+-+-+-+-+ +-+-+ +-+-+-+""")
        print("\n")
        print(3)
        time.sleep(1)
        print("\n")
        print(2)
        time.sleep(1)
        print("\n")
        print(1)
        time.sleep(1)
        print("\n")
        print("\n")
        print("\n")
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
        riddle_four = 4
        riddle_five = 5
        riddle_six = 6
        riddle_seven = 7
        riddle_eight = 8
        riddle_nine = 9
        riddle_ten = 10

        riddle_number = random.randint(1, 10)

        if riddle_number == 1:
            print(""" +-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+
 |W|h|a|t| |h|a|s| |m|a|n|y| |t|e|e|t|h|,| |b|u|t| |c|a|n|n|o|t| |b|i|t|e|?|
 +-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+""")
            print("\n")
            riddle_one_answer = input()
            print("\n")
            if riddle_one_answer.lower() == "a comb" or riddle_one_answer.lower() == "comb":
                correct.append("yes")
                print("\nCorrect!\n")
            else:
                print("\Sorry, the answer is A Comb.\n")
        if riddle_number == 2:
            print(""" +-+-+-+-+ +-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+
 |W|h|a|t| |h|a|s| |o|n|e| |e|y|e|,| |b|u|t| |c|a|n|t| |s|e|e|?|
 +-+-+-+-+ +-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+""")
            print("\n")
            riddle_two_answer = input()
            print("\n")
            if riddle_two_answer.lower() == "a needle" or riddle_two_answer.lower() == "sewing needle" or riddle_two_answer.lower() == "a sewing needle" or riddle_two_answer.lower() == "needle":
                correct.append("yes")
                print("\nCorrect!\n")
            else:
                print("\nSorry, the correct answer is a needle.\n")
        if riddle_number == 3:
            print(""" +-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+ 
 |W|h|a|t| |c|a|n| |t|r|a|v|e|l| |a|l|l| |a|r|o|u|n|d| |t|h|e| |w|o|r|l|d| 
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+ 
 |w|i|t|h|o|u|t| |l|e|a|v|i|n|g| |i|t|s| |c|o|r|n|e|r|?|                   
 +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+                   """)
            print("\n")
            riddle_three_answer = input()
            print("\n")
            if riddle_three_answer.lower() == "a stamp" or riddle_three_answer.lower() == "stamp":
                correct.append("yes")
                print("\nCorrect!\n")
            else:
                print("\nSorry, the correct answer is a Stamp.\n")
        if riddle_number == 4:
            print(""" +-+-+-+-+ +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+          
 |W|h|a|t| |r|u|n|s|,| |b|u|t| |n|e|v|e|r| |w|a|l|k|s|.|          
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+          
 |M|u|r|m|u|r|s|,| |b|u|t| |n|e|v|e|r| |t|a|l|k|s|.|              
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+        
 |H|a|s| |a| |b|e|d|,| |b|u|t| |n|e|v|e|r| |s|l|e|e|p|s|.|        
 +-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+
 |A|n|d| |h|a|s| |a| |m|o|u|t|h|,| |b|u|t| |n|e|v|e|r| |e|a|t|s|?|
 +-+-+-+ +-+-+-+ +-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+""")
            print("\n")
            riddle_four_answer = input()
            print("\n")
            if riddle_four_answer.lower() == "a river" or riddle_four_answer.lower() == "river":
                correct.append("yes")
                print("\nCorrect!\n")
            else:
                print("\nSorry, the correct answer is a river.\n")
        if riddle_number == 5:
            print(""" +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+     
 |P|o|o|r| |p|e|o|p|l|e| |h|a|v|e| |i|t|.|     
 +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+     
 |R|i|c|h| |p|e|o|p|l|e| |n|e|e|d| |i|t|.|     
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
 |I|f| |y|o|u| |e|a|t| |i|t| |y|o|u| |d|i|e|.| 
 +-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+ 
 |W|h|a|t| |i|s| |i|t|?|                       
 +-+-+-+-+ +-+-+ +-+-+-+                       """)
            print("\n")
            riddle_five_answer = input()
            print("\n")
            if riddle_five_answer.lower() == "nothing":
                correct.append("yes")
                print("\nCorrect!\n")
            else:
                print("\nSorry, the correct answer is nothing.\n")        
        if riddle_number == 6:
            print(""" +-+ +-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+ +-+-+ +-+-+-+-+-+-+-+     
 |I| |h|a|v|e| |c|i|t|i|e|s|,| |b|u|t| |n|o| |h|o|u|s|e|s|.|     
 +-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+ 
 |I| |h|a|v|e| |m|o|u|n|t|a|i|n|s|,| |b|u|t| |n|o| |t|r|e|e|s|.| 
 +-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+ 
 |I| |h|a|v|e| |w|a|t|e|r|,| |b|u|t| |n|o| |f|i|s|h|.|           
 +-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+ +-+-+ +-+-+-+-+-+           
 |W|h|a|t| |a|m| |I|?|                                           
 +-+-+-+-+ +-+-+ +-+-+                                           """)
            print("\n")
            riddle_six_answer = input()
            print("\n")
            if riddle_six_answer.lower() == "a map" or riddle_six_answer.lower() == "map":
                correct.append("yes")
                print("\nCorrect!\n")
            else:
                print("\nSorry, the correct answer is a map.\n")
        if riddle_number == 7:
            print(""" +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+ +-+-+ +-+-+-+-+-+ +-+-+-+-+ 
 |S|p|e|l|l|e|d| |f|o|r|w|a|r|d|s| |I|m| |w|h|a|t| |y|o|u| |d|o| |e|v|e|r|y| |d|a|y|,| 
 +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
 |s|p|e|l|l|e|d| |b|a|c|k|w|a|r|d| |I|m| |s|o|m|e|t|h|i|n|g| |y|o|u| |h|a|t|e|.|       
 +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+       
 |W|h|a|t| |a|m| |I|?|                                                                 
 +-+-+-+-+ +-+-+ +-+-+                                                                 """)
            print("\n")
            riddle_seven_answer = input()
            print("\n")
            if riddle_seven_answer.lower() == "live":
                correct.append("yes")
                print("\nCorrect!\n")
            else:
                print("\nSorry, the correct answer is live.\n")
        if riddle_number == 8:
            print(""" +-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+ +-+-+-+-+ +-+-+ +-+-+-+                   
 |T|h|e| |p|e|r|s|o|n| |w|h|o| |m|a|k|e|s| |i|t| |h|a|s| |n|o| |n|e|e|d| |o|f| |i|t|;|                   
 +-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                   
 |t|h|e| |p|e|r|s|o|n| |w|h|o| |b|u|y|s| |i|t| |h|a|s| |n|o| |u|s|e| |f|o|r| |i|t|.|                     
 +-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+ 
 |T|h|e| |p|e|r|s|o|n| |w|h|o| |u|s|e|s| |i|t| |c|a|n| |n|e|i|t|h|e|r| |s|e|e| |n|o|r| |f|e|e|l| |i|t|.| 
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+ 
 |W|h|a|t| |i|s| |i|t|?|                                                                                 
 +-+-+-+-+ +-+-+ +-+-+-+                                                                                 """)
            print("\n")
            riddle_eight_answer = input()
            print("\n")
            if riddle_eight_answer.lower() == "a coffin" or riddle_eight_answer.lower() == "coffin":
                correct.append("yes")
                print("\nCorrect!\n")
            else:
                print("\nSorry, the correct answer is a coffin.\n")
        if riddle_number == 9:
            print(""" +-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+ 
 |I| |h|a|v|e| |b|r|a|n|c|h|e|s|,| |b|u|t| |n|o| |f|r|u|i|t|,| |t|r|u|n|k|,| |o|r| |l|e|a|v|e|s|.| 
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+ 
 |W|h|a|t| |a|m| |I|?|                                                                             
 +-+-+-+-+ +-+-+ +-+-+                                                                             """)
            print("\n")
            riddle_nine_answer = input()
            print("\n")
            if riddle_nine_answer.lower() == "a bank" or riddle_nine_answer.lower() == "bank":
                correct.append("yes")
                print("\nCorrect!\n")
            else:
                print("\nSorry, the correct answer is a bank.\n")
        if riddle_number == 10:
            print(""" +-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+
 |W|h|a|t| |b|e|l|o|n|g|s| |t|o| |y|o|u|,| |b|u|t| |e|v|e|r|y|o|n|e| |e|l|s|e| |u|s|e|s| |i|t|?|
 +-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+""")
            print("\n")
            riddle_ten_answer = input()
            print("\n")
            if riddle_ten_answer.lower() == "a name" or riddle_ten_answer.lower() == "your name" or riddle_ten_answer.lower() == "name":
                correct.append("yes")
                print("\nCorrect!\n")
            else:
                print("\nSorry, the correct answer is a name.\n")
        #if riddle_number == :
         #  print("\n")
          #  riddle__answer = input()
         #   print("\n")
          #  if riddle__answer.lower() == "":
         #       correct.append("yes")
          #      print("\nCorrect!\n")
         #   else:
           #     print("\nWrong!\n")
openingTitle()
riddleGameStart()
score = len(correct)
rating(score)
