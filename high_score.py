# High Scores

scores = []

choice = None

while choice != "0":
    print(
        """
        High Scores
        
        0 - Exit
        1 - Show Scores
        2 - Add a Score
        3 - Remove a Score
        4 - Sort Scores
        """
    )

    choice = input("Choice: ")
    print()

    # Exit
    if choice == "0":
        print("Good-bye.")
    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)
    elif choice == "2":
        score = int(input("What score did you get? "))
        scores.append(score)
    elif choice == "3":
        score = int(input("What score do you want to remove? "))
        if score in scores:
            scores.remove(score)
            print("The score has been removed.")
        else:
            print("The score doesn't exist in the records.")
    elif choice == "4":
        scores.sort(reverse=True)
