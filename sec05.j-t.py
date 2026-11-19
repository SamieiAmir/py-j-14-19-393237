





#wallet = 500000
#total_buy = 0
#
#cart_product1 = ""
#cart_count1 = 0
#
#cart_product2 = ""
#cart_count2 = 0
#
#cart_product3 = ""
#cart_count3 = 0
#
#while True:
#
#    print("\n========== SHOP ==========")
#    print("1. Show Products")
#    print("2. Buy Product")
#    print("3. Show Cart")
#    print("4. Show Wallet")
#    print("5. Exit")
#
#    choice = input("Enter your choice: ")
#
#    match choice:
#
#        case "1":
#            print("\n--- Products ---")
#            print("1. Phone - 150000")
#            print("2. Mouse - 50000")
#            print("3. Keyboard - 80000")
#            print("4. Headphone - 100000")
#            print("5. Flash - 40000")
#
#        case "2":
#            product = input("Enter product name: ")
#            count = int(input("Enter quantity: "))
#
#            if count > 0:
#
#                if product == "phone":
#                    price = 150000 * count
#
#                elif product == "mouse":
#                    price = 50000 * count
#
#                elif product == "keyboard":
#                    price = 80000 * count
#
#                elif product == "headphone":
#                    price = 100000 * count
#
#                elif product == "flash":
#                    price = 40000 * count
#
#                else:
#                    price = 0
#                    print("Product not found!")
#
#                if price > 0:
#
#                    if wallet >= price:
#
#                        wallet = wallet - price
#                        total_buy = total_buy + price
#
#                        print("Purchase successful!")
#
#                        if cart_product1 == "" or cart_product1 == product:
#                            cart_product1 = product
#                            cart_count1 = cart_count1 + count
#
#                        elif cart_product2 == "" or cart_product2 == product:
#                            cart_product2 = product
#                            cart_count2 = cart_count2 + count
#
#                        elif cart_product3 == "" or cart_product3 == product:
#                            cart_product3 = product
#                            cart_count3 = cart_count3 + count
#
#                        else:
#                            print("Cart is full!")
#
#                    else:
#                        print("Not enough money!")
#
#            else:
#                print("Invalid quantity!")
#
#        case "3":
#            print("\n--- Shopping Cart ---")
#
#            if cart_product1 != "":
#                print(cart_product1, ":", cart_count1)
#
#            if cart_product2 != "":
#                print(cart_product2, ":", cart_count2)
#
#            if cart_product3 != "":
#                print(cart_product3, ":", cart_count3)
#
#            if cart_product1 == "" and cart_product2 == "" and cart_product3 == "":
#                print("Cart is empty!")
#
#        case "4":
#            print("Your wallet:", wallet)
#
#        case "5":
#            print("Total purchases:", total_buy)
#            print("Goodbye!")
#            break
#
#        case _:
#            print("Invalid choice!")
#
#
#
#
#
#balance = 5000000
#other_balance = 0
#
#while True:
#
#    print("\n========== ATM ==========")
#    print("1. Show Balance")
#    print("2. Deposit")
#    print("3. Withdraw")
#    print("4. Transfer Money")
#    print("5. Show Destination Balance")
#    print("6. Exit")
#
#    choice = input("Enter your choice: ")
#
#    match choice:
#
#        case "1":
#            print("Your balance:", balance, "Toman")
#
#        case "2":
#            amount = int(input("Enter deposit amount: "))
#
#            if amount > 0:
#                balance = balance + amount
#                print("Deposit successful!")
#                print("New balance:", balance)
#
#            else:
#                print("Invalid amount!")
#
#        case "3":
#            amount = int(input("Enter withdrawal amount: "))
#
#            if amount > 0:
#
#                if amount <= balance:
#                    balance = balance - amount
#                    print("Withdrawal successful!")
#                    print("New balance:", balance)
#
#                else:
#                    print("Not enough money!")
#
#            else:
#                print("Invalid amount!")
#
#        case "4":
#            account = input("Enter destination account: ")
#            amount = int(input("Enter transfer amount: "))
#
#            if amount > 0:
#
#                if amount <= balance:
#                    balance = balance - amount
#                    other_balance = other_balance + amount
#
#                    print("Transfer successful!")
#                    print("Destination account:", account)
#                    print("Transfer amount:", amount)
#                    print("New balance:", balance)
#
#                else:
#                    print("Not enough money!")
#
#            else:
#                print("Invalid amount!")
#
#        case "5":
#            print("Destination balance:", other_balance)
#
#        case "6":
#            print("Thank you for using ATM!")
#            break
#
#        case _:
#            print("Invalid choice!")
#
#
#
#
#
#
#score = 0
#last_score = 0
#played = False
#
#while True:
#
#    print("\n========== QUIZ GAME ==========")
#    print("1. Start Quiz")
#    print("2. Show Score")
#    print("3. Show Rank")
#    print("4. Exit")
#
#    choice = input("Enter your choice: ")
#
#    match choice:
#
#        case "1":
#
#            print("\n1. Geography")
#            print("2. History")
#
#            category = input("Choose a category: ")
#
#            score = 0
#
#            if category == "1":
#
#                print("\n--- Geography Quiz ---")
#
#                for i in range(1, 11):
#
#                    match i:
#
#                        case 1:
#                            print("\n1. What is the capital of France?")
#                            print("A. London  B. Paris  C. Rome  D. Berlin")
#                            correct = "B"
#
#                        case 2:
#                            print("\n2. Which is the largest ocean?")
#                            print("A. Atlantic  B. Indian  C. Pacific  D. Arctic")
#                            correct = "C"
#
#                        case 3:
#                            print("\n3. Which country has the most population?")
#                            print("A. India  B. Japan  C. Italy  D. Canada")
#                            correct = "A"
#
#                        case 4:
#                            print("\n4. What is the capital of Japan?")
#                            print("A. Beijing  B. Tokyo  C. Seoul  D. Bangkok")
#                            correct = "B"
#
#                        case 5:
#                            print("\n5. Which continent is Egypt in?")
#                            print("A. Europe  B. Asia  C. Africa  D. America")
#                            correct = "C"
#
#                        case 6:
#                            print("\n6. Which is the largest country?")
#                            print("A. Russia  B. Germany  C. France  D. Spain")
#                            correct = "A"
#
#                        case 7:
#                            print("\n7. What is the capital of Iran?")
#                            print("A. Shiraz  B. Tehran  C. Tabriz  D. Isfahan")
#                            correct = "B"
#
#                        case 8:
#                            print("\n8. Which river is the longest in Africa?")
#                            print("A. Nile  B. Amazon  C. Thames  D. Rhine")
#                            correct = "A"
#
#                        case 9:
#                            print("\n9. Which country is famous for pyramids?")
#                            print("A. Brazil  B. Egypt  C. China  D. Turkey")
#                            correct = "B"
#
#                        case 10:
#                            print("\n10. Which continent is Australia in?")
#                            print("A. Asia  B. Europe  C. Australia  D. Africa")
#                            correct = "C"
#
#                    answer = input("Your answer (A/B/C/D): ").upper()
#
#                    if answer == correct:
#                        print("Correct!")
#                        score = score + 10
#                    else:
#                        print("Wrong answer!")
#
#            elif category == "2":
#
#                print("\n--- History Quiz ---")
#
#                for i in range(1, 11):
#
#                    match i:
#
#                        case 1:
#                            print("\n1. Who was the first president of the USA?")
#                            print("A. Lincoln  B. Washington  C. Obama  D. Trump")
#                            correct = "B"
#
#                        case 2:
#                            print("\n2. In which year did World War II end?")
#                            print("A. 1940  B. 1942  C. 1945  D. 1950")
#                            correct = "C"
#
#                        case 3:
#                            print("\n3. Who built the pyramids of Egypt?")
#                            print("A. Romans  B. Ancient Egyptians  C. Greeks  D. Persians")
#                            correct = "B"
#
#                        case 4:
#                            print("\n4. Which civilization built Persepolis?")
#                            print("A. Achaemenid  B. Roman  C. Greek  D. Ottoman")
#                            correct = "A"
#
#                        case 5:
#                            print("\n5. Who was the first man on the Moon?")
#                            print("A. Yuri Gagarin  B. Neil Armstrong  C. Einstein  D. Newton")
#                            correct = "B"
#
#                        case 6:
#                            print("\n6. In which year did World War I begin?")
#                            print("A. 1914  B. 1918  C. 1939  D. 1945")
#                            correct = "A"
#
#                        case 7:
#                            print("\n7. Who was the founder of the Mongol Empire?")
#                            print("A. Alexander  B. Genghis Khan  C. Caesar  D. Napoleon")
#                            correct = "B"
#
#                        case 8:
#                            print("\n8. Which ancient city was famous for its hanging gardens?")
#                            print("A. Athens  B. Babylon  C. Rome  D. Paris")
#                            correct = "B"
#
#                        case 9:
#                            print("\n9. Who discovered penicillin?")
#                            print("A. Newton  B. Fleming  C. Darwin  D. Galileo")
#                            correct = "B"
#
#                        case 10:
#                            print("\n10. Which empire was ruled by Cyrus the Great?")
#                            print("A. Roman  B. Achaemenid  C. Ottoman  D. Mongol")
#                            correct = "B"
#
#                    answer = input("Your answer (A/B/C/D): ").upper()
#
#                    if answer == correct:
#                        print("Correct!")
#                        score = score + 10
#                    else:
#                        print("Wrong answer!")
#
#            else:
#                print("Invalid category!")
#                continue
#
#            last_score = score
#            played = True
#
#            print("\n========== QUIZ RESULT ==========")
#            print("Your final score:", score, "/ 100")
#
#        case "2":
#
#            if played:
#                print("Your score:", last_score, "/ 100")
#            else:
#                print("You haven't played yet!")
#
#        case "3":
#
#            if played:
#
#                if last_score >= 90:
#                    print("Your rank: Excellent!")
#
#                elif last_score >= 70:
#                    print("Your rank: Very Good!")
#
#                elif last_score >= 50:
#                    print("Your rank: Good!")
#
#                elif last_score >= 30:
#                    print("Your rank: Average!")
#
#                else:
#                    print("Your rank: Beginner!")
#
#            else:
#                print("You haven't played yet!")
#
#        case "4":
#            print("Thank you for playing!")
#            break
#
#        case _:
#            print("Invalid choice!")
#
#
#
#
#
#total = 0
#months = 0
#registered = False
#
#while True:
#
#    print("\n========== ELECTRICITY SYSTEM ==========")
#    print("1. Register Electricity Consumption")
#    print("2. Calculate Cost")
#    print("3. Show Consumption Status")
#    print("4. Exit")
#
#    choice = input("Enter your choice: ")
#
#    match choice:
#
#        case "1":
#
#            months = int(input("Enter number of months: "))
#
#            total = 0
#
#            for i in range(1, months + 1):
#
#                consumption = float(input("Enter consumption of month: "))
#
#                if consumption >= 0:
#                    total = total + consumption
#                else:
#                    print("Invalid consumption!")
#                    total = total + 0
#
#            registered = True
#
#            print("Registration completed!")
#            print("Total consumption:", total)
#
#        case "2":
#
#            if registered:
#
#                if total < 100:
#                    cost = total * 500
#
#                elif total <= 300:
#                    cost = total * 1000
#
#                else:
#                    cost = total * 1500
#
#                print("Total consumption:", total)
#                print("Electricity cost:", cost, "Toman")
#
#            else:
#                print("Please register consumption first!")
#
#        case "3":
#
#            if registered:
#
#                print("Total consumption:", total)
#
#                if total < 100:
#                    print("Consumption status: Low")
#
#                elif total <= 300:
#                    print("Consumption status: Normal")
#
#                else:
#                    print("Consumption status: High")
#
#            else:
#                print("Please register consumption first!")
#
#        case "4":
#            print("Thank you!")
#            break
#
#        case _:
#            print("Invalid choice!")
#
#
#
#
#normal_price = 100000
#vip_price = 200000
#
#total_price = 0
#total_tickets = 0
#discount = 0
#
#while True:
#
#    print("\n========== CINEMA ==========")
#    print("1. Buy Normal Ticket")
#    print("2. Buy VIP Ticket")
#    print("3. Calculate Discount")
#    print("4. Show Invoice")
#    print("5. Exit")
#
#    choice = input("Enter your choice: ")
#
#    match choice:
#
#        case "1":
#            count = int(input("Enter ticket quantity: "))
#
#            if count > 0:
#                price = normal_price * count
#                total_price = total_price + price
#                total_tickets = total_tickets + count
#
#                print("Normal ticket purchased!")
#                print("Price:", price)
#
#            else:
#                print("Invalid quantity!")
#
#        case "2":
#            count = int(input("Enter ticket quantity: "))
#
#            if count > 0:
#                price = vip_price * count
#                total_price = total_price + price
#                total_tickets = total_tickets + count
#
#                print("VIP ticket purchased!")
#                print("Price:", price)
#
#            else:
#                print("Invalid quantity!")
#
#        case "3":
#
#            if total_tickets > 5:
#                discount = total_price * 15 / 100
#                print("You got 15% discount!")
#                print("Discount:", discount)
#
#            else:
#                discount = 0
#                print("No discount!")
#
#            final_price = total_price - discount
#            print("Final price:", final_price)
#
#        case "4":
#
#            if total_tickets > 0:
#
#                if total_tickets > 5:
#                    discount = total_price * 15 / 100
#                else:
#                    discount = 0
#
#                final_price = total_price - discount
#
#                print("\n========== INVOICE ==========")
#                print("Total tickets:", total_tickets)
#                print("Total price:", total_price)
#                print("Discount:", discount)
#                print("Final price:", final_price)
#                print("=============================")
#
#            else:
#                print("You haven't purchased any tickets!")
#
#        case "5":
#            print("Thank you for using Cinema!")
#            break
#
#        case _:
#            print("Invalid choice!")
#
#
#
#
#score = 0
#last_score = 0
#played = False
#
#while True:
#
#    print("\n========== DRIVING TEST ==========")
#    print("1. Start Exam")
#    print("2. Show Result")
#    print("3. Exit")
#
#    choice = input("Enter your choice: ")
#
#    match choice:
#
#        case "1":
#
#            score = 0
#
#            print("\n========== EXAM QUESTIONS ==========")
#
#            for i in range(1, 11):
#
#                match i:
#
#                    case 1:
#                        print("\n1. What does a red traffic light mean?")
#                        print("A. Go")
#                        print("B. Stop")
#                        print("C. Turn right")
#                        print("D. Speed up")
#                        correct = "B"
#
#                    case 2:
#                        print("\n2. What should you do before changing lanes?")
#                        print("A. Use the mirror and signal")
#                        print("B. Speed up")
#                        print("C. Stop suddenly")
#                        print("D. Honk")
#                        correct = "A"
#
#                    case 3:
#                        print("\n3. What does a yellow traffic light mean?")
#                        print("A. Drive faster")
#                        print("B. Stop if safe")
#                        print("C. Park")
#                        print("D. Turn left")
#                        correct = "B"
#
#                    case 4:
#                        print("\n4. What is the purpose of a seat belt?")
#                        print("A. Save fuel")
#                        print("B. Increase speed")
#                        print("C. Protect passengers")
#                        print("D. Improve visibility")
#                        correct = "C"
#
#                    case 5:
#                        print("\n5. What should you do at a STOP sign?")
#                        print("A. Slow down only")
#                        print("B. Stop completely")
#                        print("C. Speed up")
#                        print("D. Ignore it")
#                        correct = "B"
#
#                    case 6:
#                        print("\n6. What should you do when an ambulance approaches with siren?")
#                        print("A. Give way safely")
#                        print("B. Race with it")
#                        print("C. Block the road")
#                        print("D. Ignore it")
#                        correct = "A"
#
#                    case 7:
#                        print("\n7. What is the safe action in heavy rain?")
#                        print("A. Increase speed")
#                        print("B. Keep distance and slow down")
#                        print("C. Turn off headlights")
#                        print("D. Drive close to others")
#                        correct = "B"
#
#                    case 8:
#                        print("\n8. What should you do before reversing?")
#                        print("A. Check around the vehicle")
#                        print("B. Close your eyes")
#                        print("C. Speed up")
#                        print("D. Honk continuously")
#                        correct = "A"
#
#                    case 9:
#                        print("\n9. What does a pedestrian crossing sign indicate?")
#                        print("A. Parking area")
#                        print("B. Pedestrian crossing")
#                        print("C. Fuel station")
#                        print("D. Highway")
#                        correct = "B"
#
#                    case 10:
#                        print("\n10. What should you do when approaching a school zone?")
#                        print("A. Drive faster")
#                        print("B. Slow down and watch for children")
#                        print("C. Overtake everyone")
#                        print("D. Ignore the signs")
#                        correct = "B"
#
#                answer = input("Enter your answer (A/B/C/D): ").upper()
#
#                if answer == correct:
#                    print("Correct answer!")
#                    score = score + 2
#
#                else:
#                    print("Wrong answer!")
#
#            last_score = score
#            played = True
#
#            print("\n========== EXAM FINISHED ==========")
#            print("Your score:", score, "/ 20")
#
#            if score >= 14:
#                print("Congratulations! You passed!")
#            else:
#                print("Sorry! You failed!")
#
#        case "2":
#
#            if played:
#
#                print("\n========== EXAM RESULT ==========")
#                print("Your score:", last_score, "/ 20")
#
#                if last_score >= 14:
#                    print("Status: PASSED")
#                else:
#                    print("Status: FAILED")
#
#            else:
#                print("You haven't taken the exam yet!")
#
#        case "3":
#            print("Thank you!")
#            break
#
#        case _:
#            print("Invalid choice!")
#
#
#
#
#
#score = 0
#last_score = 0
#played = False
#
#while True:
#    print("\n===== EMPLOYMENT EXAM =====")
#    print("1. Start Exam")
#    print("2. Show Result")
#    print("3. Restart")
#    print("4. Exit")
#
#    choice = input("Choose an option: ")
#
#    match choice:
#
#        case "1":
#            score = 0
#            played = True
#
#            for i in range(1, 16):
#                print("\nQuestion", i)
#
#                match i:
#                    case 1:
#                        print("What is the capital of Iran?")
#                        answer = input("Answer: ").lower()
#                        correct = "tehran"
#
#                    case 2:
#                        print("How many days are in a week?")
#                        answer = input("Answer: ").lower()
#                        correct = "7"
#
#                    case 3:
#                        print("What is 10 * 5?")
#                        answer = input("Answer: ").lower()
#                        correct = "50"
#
#                    case 4:
#                        print("Which language is used for web pages?")
#                        answer = input("Answer: ").lower()
#                        correct = "html"
#
#                    case 5:
#                        print("What is the opposite of hot?")
#                        answer = input("Answer: ").lower()
#                        correct = "cold"
#
#                    case 6:
#                        print("How many months are in a year?")
#                        answer = input("Answer: ").lower()
#                        correct = "12"
#
#                    case 7:
#                        print("What is 100 / 10?")
#                        answer = input("Answer: ").lower()
#                        correct = "10"
#
#                    case 8:
#                        print("Which planet do we live on?")
#                        answer = input("Answer: ").lower()
#                        correct = "earth"
#
#                    case 9:
#                        print("What is the color of the sky on a clear day?")
#                        answer = input("Answer: ").lower()
#                        correct = "blue"
#
#                    case 10:
#                        print("What is 9 * 9?")
#                        answer = input("Answer: ").lower()
#                        correct = "81"
#
#                    case 11:
#                        print("Which device is used to type?")
#                        answer = input("Answer: ").lower()
#                        correct = "keyboard"
#
#                    case 12:
#                        print("How many hours are in a day?")
#                        answer = input("Answer: ").lower()
#                        correct = "24"
#
#                    case 13:
#                        print("What is the capital of France?")
#                        answer = input("Answer: ").lower()
#                        correct = "paris"
#
#                    case 14:
#                        print("What is 15 + 15?")
#                        answer = input("Answer: ").lower()
#                        correct = "30"
#
#                    case 15:
#                        print("Which animal is known as the king of the jungle?")
#                        answer = input("Answer: ").lower()
#                        correct = "lion"
#
#                if answer == correct:
#                    print("Correct! +2 points")
#                    score += 2
#                else:
#                    print("Wrong! -1 point")
#                    score -= 1
#
#            last_score = score
#            print("\nExam finished!")
#
#        case "2":
#            if played == True:
#                print("Your Score:", last_score)
#
#                if last_score > 20:
#                    print("Result: Accepted")
#                elif last_score >= 15:
#                    print("Result: Needs Review")
#                else:
#                    print("Result: Rejected")
#            else:
#                print("You have not taken the exam yet.")
#
#        case "3":
#            score = 0
#            last_score = 0
#            played = False
#            print("Exam restarted successfully!")
#
#        case "4":
#            print("Goodbye!")
#            break
#
#        case _:
#            print("Invalid option!")
#
#
#
#
#
#stock = 0
#total_produced = 0
#total_sold = 0
#total_income = 0
#total_cost = 0
#
#while True:
#    print("\n========== FACTORY SYSTEM ==========")
#    print("1. Produce Product")
#    print("2. Sell Product")
#    print("3. Check Inventory")
#    print("4. Calculate Income")
#    print("5. Calculate Production Cost")
#    print("6. Daily Report")
#    print("7. Exit")
#
#    choice = input("Choose an option: ")
#
#    match choice:
#
#        case "1":
#            amount = int(input("How many products to produce? "))
#
#            if amount > 0:
#                stock += amount
#                total_produced += amount
#                total_cost += amount * 50000
#                print("Products produced successfully!")
#            else:
#                print("Invalid amount!")
#
#        case "2":
#            amount = int(input("How many products to sell? "))
#
#            if amount <= 0:
#                print("Invalid amount!")
#            elif amount > stock:
#                print("Not enough products in stock!")
#            else:
#                stock -= amount
#                total_sold += amount
#                total_income += amount * 80000
#                print("Products sold successfully!")
#
#        case "3":
#            print("Current Stock:", stock)
#
#        case "4":
#            print("Total Income:", total_income, "Toman")
#
#        case "5":
#            print("Total Production Cost:", total_cost, "Toman")
#
#        case "6":
#            print("\n===== DAILY REPORT =====")
#
#            for day in range(1, 8):
#                print("Day", day)
#                print("Total Produced:", total_produced)
#                print("Total Sold:", total_sold)
#                print("Current Stock:", stock)
#
#            profit = total_income - total_cost
#
#            print("\nTotal Income:", total_income)
#            print("Total Cost:", total_cost)
#            print("Profit/Loss:", profit)
#
#            if profit > 0:
#                print("Factory is profitable.")
#            elif profit < 0:
#                print("Factory has a loss.")
#            else:
#                print("Factory has no profit or loss.")
#
#        case "7":
#            print("Goodbye!")
#            break
#
#        case _:
#            print("Invalid option!")
#
#
#
#
#
#
#current_floor = 0
#total_moves = 0
#
#while True:
#    print("\n========== ELEVATOR SYSTEM ==========")
#    print("1. Select Floor")
#    print("2. Show Current Floor")
#    print("3. Return to Floor Zero")
#    print("4. Exit")
#
#    choice = input("Choose an option: ")
#
#    match choice:
#
#        case "1":
#            destination = int(input("Enter destination floor (0-10): "))
#
#            if destination < 0 or destination > 10:
#                print("Invalid floor!")
#
#            elif destination > current_floor:
#                for floor in range(current_floor + 1, destination + 1):
#                    print("Moving up to floor:", floor)
#                    total_moves += 1
#
#                current_floor = destination
#                print("You reached floor", current_floor)
#
#            elif destination < current_floor:
#                for floor in range(current_floor - 1, destination - 1, -1):
#                    print("Moving down to floor:", floor)
#                    total_moves += 1
#
#                current_floor = destination
#                print("You reached floor", current_floor)
#
#            else:
#                print("You are already on this floor.")
#
#        case "2":
#            print("Current Floor:", current_floor)
#
#        case "3":
#            if current_floor > 0:
#                for floor in range(current_floor - 1, -1, -1):
#                    print("Moving down to floor:", floor)
#                    total_moves += 1
#
#                current_floor = 0
#                print("Elevator returned to floor zero.")
#            else:
#                print("Elevator is already on floor zero.")
#
#        case "4":
#            print("Total Elevator Moves:", total_moves)
#            print("Goodbye!")
#            break
#
#        case _:
#            print("Invalid option!")
#
#
#
#
#