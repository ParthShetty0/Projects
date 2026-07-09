#Architecture of the KBC questionaire
def ask_question(question, options, correct_answer, winnings):
    print(question)
    print("Options:", options)
    
    user_input = input("Please select the correct option: ")
    if user_input == correct_answer:
        print(f"Correct! The {correct_answer} is the longest river in the world.")
        print("You have won : ", winnings)
        return winnings
            
        
    else:
        print(f"Incorrect. Try again!")
        return 0

"""I tried looping the question everytime if user inputs incorrect option.
Help would be appreciated. :)"""


        # for option in options :
        #     if option == correct_answer:
        #         break
             
            # else:
            #     print(question)
            #     print("Options:", options)
    
            #     user_input = input("Please select the correct option: ")
            #     if user_input == correct_answer:
            #         print(f"Correct! The {correct_answer} is the longest river in the world.")
            #         break
            #     else:
            #         print(f"Incorrect. Try again!")        

total_bank = 0    

#Questions - General Knowledge 
Q1 = "Which is the longest river in the world?"
Options = ["Nile", "Amazon", "Yangtze", "Mississippi"]
q1_prize = ask_question(Q1, Options, "Nile", 1000)
total_bank += q1_prize

Q2 = "What is the capital of Australia?"
Options2 = ["Sydney", "Melbourne", "Canberra", "Perth"]
q2_prize = ask_question(Q2, Options2, "Canberra", 2000)
total_bank += q2_prize

Q3 = "Who painted the Mona Lisa?"
Options3 = ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"]
q3_prize = ask_question(Q3, Options3, "Leonardo da Vinci", 3000)
total_bank += q3_prize

Q4 = "Which planet is known as the Red Planet?"
Options4 = ["Venus", "Mars", "Jupiter", "Saturn"]
q4_prize = ask_question(Q4, Options4, "Mars", 4000)
total_bank += q4_prize

Q5 = "What is the hardest natural substance on Earth?"
Options5 = ["Gold", "Iron", "Diamond", "Platinum"]
q5_prize = ask_question(Q5, Options5, "Diamond", 5000)
total_bank += q5_prize

Q6 = "Which is the largest ocean on Earth?"
Options6 = ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"]
q6_prize = ask_question(Q6, Options6, "Pacific Ocean", 6000)
total_bank += q6_prize

Q7 = "Which is the smallest country in the world by land area?"
Options7 = ["Monaco", "Vatican City", "San Marino", "Liechtenstein"]
q7_prize = ask_question(Q7, Options7, "Vatican City", 7000)
total_bank += q7_prize

Q8 = "What is the chemical symbol for Gold?"
Options8 = ["Au", "Ag", "Gd", "Go"]
q8_prize = ask_question(Q8, Options8, "Au", 8000)
total_bank += q8_prize

Q9 = "Who wrote the play 'Hamlet'?"
Options9 = ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"]
q9_prize = ask_question(Q9, Options9, "William Shakespeare", 9000)
total_bank += q9_prize

Q10 = "What is the fastest land animal?"
Options10 = ["Lion", "Cheetah", "Horse", "Greyhound"]
q10_prize = ask_question(Q10, Options10, "Cheetah", 10000)
total_bank += q10_prize

print(f"\n Game over, You have won:", total_bank)

