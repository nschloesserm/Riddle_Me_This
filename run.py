print("""  _______    __     ________   ________   ___       _______  
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

    if answer.lower() == 'no':
        print("Sorry, maybe next time!")
        riddleGameStart()
    if answer.lower() == 'yes':
        print("Yay!")
        riddleGame()  

import random

def riddleGame():
    for riddles_needed in range(int("3")):
        riddle_one = 1
        riddle_two = 2
        riddle_three = 3

        riddle_number = random.randint(1, 3)

        if riddle_number == 1:
            print("\nriddleone?\n")
            riddle_one_answer = input()
            if riddle_one_answer == "a":
                print("\ncorrect!\n")
            else:
                print("\nworng!\n")
        if riddle_number == 2:
            print("\nriddletwo?\n")
            riddle_two_answer = input()
            if riddle_two_answer == "b":
                print("\ncorrect!\n")
            else:
                print("\nworng!\n")
        if riddle_number == 3:
            print("\nriddlethree?\n")
            riddle_three_answer = input()
            if riddle_three_answer == "c":
                print("\ncorrect!\n")
            else:
                print("\nworng!\n")
    

riddleGameStart()

