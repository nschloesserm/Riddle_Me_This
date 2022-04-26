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
    print("\nWould you like to answer some riddles? (Yes/No): \n")
    answer = input()

    if answer.lower() == 'no':
        print("\nSorry, maybe next time!\n")
        time.sleep(2)
        openingTitle()
        riddleGameStart()
    if answer.lower() == 'yes':
        print("\nYay!\n")
        riddleGame()
    else:
        print("\nPlease type Yes or No\n")
        riddleGameStart()

def rating(score):
    print("Congradulations, you have answered",score,"correctly")
    print("\nWould you like to play again? (Yes/No): \n")
    answer = input()

    if answer.lower() == 'no':
        print("\nSorry, maybe next time!\n")
        time.sleep(3)
        openingTitle()
        riddleGameStart()
    if answer.lower() == 'yes':
        print("\nYay!\n")
        openingTitle()
        riddleGame()
        score = len(correct)
        rating(score)
    else:
        print("\nPlease type Yes or No\n")
        riddleGameStart()

def riddleGame():
    for riddles_needed in range(int("3")):
        riddle_one = 1
        riddle_two = 2
        riddle_three = 3

        riddle_number = random.randint(1, 3)

        if riddle_number == 1:
            print("\nWhat has many teeth, but cannot bite?\n")
            riddle_one_answer = input()
            if riddle_one_answer.lower() == "a comb" or riddle_one_answer.lower() == "comb":
                correct.append("yes")
                print("\ncorrect!\n")
            else:
                print("\nworng!\n")
        if riddle_number == 2:
            print("\nriddletwo?\n")
            riddle_two_answer = input()
            if riddle_two_answer == "b":
                correct.append("yes")
                print("\ncorrect!\n")
            else:
                print("\nworng!\n")
        if riddle_number == 3:
            print("\nriddlethree?\n")
            riddle_three_answer = input()
            if riddle_three_answer == "c":
                correct.append("yes")
                print("\ncorrect!\n")
            else:
                print("\nworng!\n")

openingTitle()
riddleGameStart()
score = len(correct)
rating(score)
