#Architecture of the KBC questionaire
def ask_question(question, options, correct_answer):
    print(question)
    print("Options:", options)
    
    user_input = input("Please select the correct option: ")
    if user_input == correct_answer:
        print(f"Correct! The {correct_answer} is the longest river in the world.")
         
    else:
        print(f"Incorrect. Try again!")

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

#Questions - General Knowledge 
Q1 = "Which is the longest river in the world?"
Options = ["Nile", "Amazon", "Yangtze", "Mississippi"]
ask_question(Q1, Options, "Nile")

Q2 = "What is the capital of Australia?"
Options2 = ["Sydney", "Melbourne", "Canberra", "Perth"]
ask_question(Q2, Options2, "Canberra")

Q3 = "Who painted the Mona Lisa?"
Options3 = ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"]
ask_question(Q3, Options3, "Leonardo da Vinci")

Q4 = "Which planet is known as the Red Planet?"
Options4 = ["Venus", "Mars", "Jupiter", "Saturn"]
ask_question(Q4, Options4, "Mars")

Q5 = "What is the hardest natural substance on Earth?"
Options5 = ["Gold", "Iron", "Diamond", "Platinum"]
ask_question(Q5, Options5, "Diamond")


Q6 = "Which is the largest ocean on Earth?"
Options6 = ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"]
ask_question(Q6, Options6, "Pacific Ocean")

Q7 = "Which is the smallest country in the world by land area?"
Options7 = ["Monaco", "Vatican City", "San Marino", "Liechtenstein"]
ask_question(Q7, Options7, "Vatican City")


Q8 = "What is the chemical symbol for Gold?"
Options8 = ["Au", "Ag", "Gd", "Go"]
ask_question(Q8, Options8, "Au")

Q9 = "Who wrote the play 'Hamlet'?"
Options9 = ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"]
ask_question(Q9, Options9, "William Shakespeare")

Q10 = "What is the fastest land animal?"
Options10 = ["Lion", "Cheetah", "Horse", "Greyhound"]
ask_question(Q10, Options10, "Cheetah")

Q11 = "What is the capital of Japan?"
Options11 = ["Seoul", "Beijing", "Tokyo", "Kyoto"]
ask_question(Q11, Options11, "Tokyo")

Q12 = "Who is credited with inventing the telephone?"
Options12 = ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Albert Einstein"]
ask_question(Q12, Options12, "Alexander Graham Bell")

Q13 = "Which is the largest mammal in the world?"
Options13 = ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"]
ask_question(Q13, Options13, "Blue Whale")

Q14 = "What is the official currency of the United Kingdom?"
Options14 = ["Euro", "Dollar", "Pound Sterling", "Franc"]
ask_question(Q14, Options14, "Pound Sterling")

Q15 = "Which is the largest planet in our solar system?"
Options15 = ["Earth", "Saturn", "Jupiter", "Uranus"]
ask_question(Q15, Options15, "Jupiter")

Q16 = "What is the chemical symbol for Iron?"
Options16 = ["Ir", "Fe", "In", "I"]
ask_question(Q16, Options16, "Fe")

Q17 = "Mount Everest is located in which mountain range?"
Options17 = ["Andes", "Rockies", "Alps", "Himalayas"]
ask_question(Q17, Options17, "Himalayas")

Q18 = "Who discovered penicillin?"
Options18 = ["Marie Curie", "Louis Pasteur", "Alexander Fleming", "Rosalind Franklin"]
ask_question(Q18, Options18, "Alexander Fleming")

Q19 = "Which continent has the highest number of countries?"
Options19 = ["Asia", "Europe", "Africa", "South America"]
ask_question(Q19, Options19, "Africa")

Q20 = "Who was the first person to walk on the moon?"
Options20 = ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"]
ask_question(Q20, Options20, "Neil Armstrong")

Q21 = "What is the capital of Canada?"
Options21 = ["Toronto", "Vancouver", "Ottawa", "Montreal"]
ask_question(Q21, Options21, "Ottawa")

Q22 = "What is the tallest mountain in the world above sea level?"
Options22 = ["K2", "Mount Kilimanjaro", "Mount Everest", "Mount Fuji"]
ask_question(Q22, Options22, "Mount Everest")

Q23 = "Which is the longest bone in the human body?"
Options23 = ["Femur", "Tibia", "Fibula", "Humerus"]
ask_question(Q23, Options23, "Femur")

Q24 = "Who painted 'The Starry Night'?"
Options24 = ["Vincent van Gogh", "Claude Monet", "Edvard Munch", "Salvador Dali"]
ask_question(Q24, Options24, "Vincent van Gogh")

Q25 = "What gas do plants absorb from the atmosphere during photosynthesis?"
Options25 = ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"]
ask_question(Q25, Options25, "Carbon Dioxide")

Q26 = "Who wrote the 'Harry Potter' book series?"
Options26 = ["J.R.R. Tolkien", "George R.R. Martin", "J.K. Rowling", "C.S. Lewis"]
ask_question(Q26, Options26, "J.K. Rowling")

Q27 = "What is the capital of Italy?"
Options27 = ["Venice", "Florence", "Milan", "Rome"]
ask_question(Q27, Options27, "Rome")

Q28 = "How many continents are there on Earth?"
Options28 = ["5", "6", "7", "8"]
ask_question(Q28, Options28, "7")

Q29 = "Which is the largest hot desert in the world?"
Options29 = ["Gobi", "Sahara", "Kalahari", "Mojave"]
ask_question(Q29, Options29, "Sahara")

Q30 = "Who was the first President of the United States?"
Options30 = ["Abraham Lincoln", "Thomas Jefferson", "John Adams", "George Washington"]
ask_question(Q30, Options30, "George Washington")

Q31 = "Which organ pumps blood throughout the human body?"
Options31 = ["Lungs", "Liver", "Brain", "Heart"]
ask_question(Q31, Options31, "Heart")

Q32 = "How many colors are typically seen in a rainbow?"
Options32 = ["5", "6", "7", "8"]
ask_question(Q32, Options32, "7")

Q33 = "Which metal is liquid at room temperature?"
Options33 = ["Zinc", "Mercury", "Lead", "Aluminum"]
ask_question(Q33, Options33, "Mercury")

Q34 = "Which country is known as the 'Land of the Rising Sun'?"
Options34 = ["China", "South Korea", "Thailand", "Japan"]
ask_question(Q34, Options34, "Japan")

Q35 = "What is the capital of Egypt?"
Options35 = ["Alexandria", "Cairo", "Giza", "Luxor"]
ask_question(Q35, Options35, "Cairo")

Q36 = "Which is the smallest planet in our solar system?"
Options36 = ["Venus", "Mars", "Mercury", "Neptune"]
ask_question(Q36, Options36, "Mercury")

Q37 = "Which is the largest internal organ in the human body?"
Options37 = ["Stomach", "Heart", "Liver", "Kidneys"]
ask_question(Q37, Options37, "Liver")

Q38 = "Who is the author of the dystopian novel '1984'?"
Options38 = ["Aldous Huxley", "George Orwell", "Ray Bradbury", "Margaret Atwood"]
ask_question(Q38, Options38, "George Orwell")

Q39 = "In which year did the Titanic sink?"
Options39 = ["1905", "1912", "1920", "1898"]
ask_question(Q39, Options39, "1912")

Q40 = "What is the scientific study of stars and the universe called?"
Options40 = ["Astrology", "Astronomy", "Cosmetology", "Meteorology"]
ask_question(Q40, Options40, "Astronomy")

Q41 = "What is the capital of France?"
Options41 = ["Lyon", "Marseille", "Paris", "Nice"]
ask_question(Q41, Options41, "Paris")

Q42 = "What is the chemical symbol for Silver?"
Options42 = ["Si", "Sv", "Ag", "Sl"]
ask_question(Q42, Options42, "Ag")

Q43 = "What is the highest uninterrupted waterfall in the world?"
Options43 = ["Niagara Falls", "Victoria Falls", "Angel Falls", "Iguazu Falls"]
ask_question(Q43, Options43, "Angel Falls")

Q44 = "What is the first element on the periodic table?"
Options44 = ["Helium", "Oxygen", "Lithium", "Hydrogen"]
ask_question(Q44, Options44, "Hydrogen")

Q45 = "What is the primary language spoken in Brazil?"
Options45 = ["Spanish", "Portuguese", "French", "English"]
ask_question(Q45, Options45, "Portuguese")

Q46 = "How many teeth does a typical adult human have?"
Options46 = ["28", "30", "32", "34"]
ask_question(Q46, Options46, "32")

Q47 = "What is the capital of Spain?"
Options47 = ["Barcelona", "Madrid", "Seville", "Valencia"]
ask_question(Q47, Options47, "Madrid")

Q48 = "Which is the largest species of bird in the world?"
Options48 = ["Emperor Penguin", "Albatross", "Emu", "Ostrich"]
ask_question(Q48, Options48, "Ostrich")

Q49 = "What is the boiling point of water at sea level in Celsius?"
Options49 = ["50", "90", "100", "120"]
ask_question(Q49, Options49, "100")

Q50 = "Which famous scientist developed the theory of relativity?"
Options50 = ["Isaac Newton", "Galileo Galilei", "Stephen Hawking", "Albert Einstein"]
ask_question(Q50, Options50, "Albert Einstein")

