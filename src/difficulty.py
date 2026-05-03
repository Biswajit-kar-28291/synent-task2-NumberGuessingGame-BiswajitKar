def choose_difficulty():
    print("\nChosse Difficulty Level:")
    print("1. Easy -> 1 to 50 | 10 attempts")
    print("2. Medium -> 1 to 100 | 7 attempts")
    print("3. Hrad -> 1 to 200 | 5 attempts")

    while True:
        choice=input("Enter Your Choice (1/2/3): ")
        
        if choice == "1":
            return {
                "level":"Easy",
                "low":1,
                "high":50,
                "max_attempts":10
            }
        elif choice=="2":
            return {
                "level":"Medium",
                "low":1,
                "high":100,
                "max_attempts":7
            }
        elif choice=="2":
            return {
                "level":"Hard",
                "low":1,
                "high":200,
                "max_attempts":5
            }
        else:
            print("Invalid choice. Please enter 1, 2 or 3")