import random


def higher_lower_game():

    people_data = {
        'person1': {
            'name': 'John Doe',
            'occupation': 'Software Engineer',
            'age': 30,
            'followers_on_instagram': 10000,
            'country': 'United States',
        },
        'person2': {
            'name': 'Jane Smith',
            'occupation': 'Graphic Designer',
            'age': 28,
            'followers_on_instagram': 8000,
            'country': 'Canada',
        },
        'person3': {
            'name': 'Alex Johnson',
            'occupation': 'Marketing Specialist',
            'age': 35,
            'followers_on_instagram': 12000,
            'country': 'United Kingdom',
        },
        'person4': {
            'name': 'Emily Davis',
            'occupation': 'Doctor',
            'age': 32,
            'followers_on_instagram': 15000,
            'country': 'Australia',
        },
        'person5': {
            'name': 'Michael Brown',
            'occupation': 'Entrepreneur',
            'age': 40,
            'followers_on_instagram': 20000,
            'country': 'India',
        },
        'person6': {
            'name': 'Megan White',
            'occupation': 'Fitness Trainer',
            'age': 27,
            'followers_on_instagram': 9000,
            'country': 'Brazil',
        },
        'person7': {
            'name': 'David Lee',
            'occupation': 'Journalist',
            'age': 33,
            'followers_on_instagram': 11000,
            'country': 'South Africa',
        },
        'person8': {
            'name': 'Sophia Martinez',
            'occupation': 'Chef',
            'age': 31,
            'followers_on_instagram': 13000,
            'country': 'Mexico',
        },
        'person9': {
            'name': 'Chris Taylor',
            'occupation': 'Artist',
            'age': 29,
            'followers_on_instagram': 9500,
            'country': 'Germany',
        },
        'person10': {
            'name': 'Olivia Harris',
            'occupation': 'Lawyer',
            'age': 36,
            'followers_on_instagram': 18000,
            'country': 'France',
        },
    }

    # Select two random people for the game
    person_keys = random.sample(list(people_data.keys()), 2)
    person1, person2 = people_data[person_keys[0]], people_data[person_keys[1]]

    print(f"Compare the number of Instagram followers between {person1['name']} and {person2['name']}")

    # Get user input for their guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Check the user's guess and compare the followers
    if user_guess == 'A':
        correct_answer = person1['followers_on_instagram'] > person2['followers_on_instagram']
    elif user_guess == 'B':
        correct_answer = person2['followers_on_instagram'] > person1['followers_on_instagram']
    else:
        print("Invalid input. Please type 'A' or 'B'.")
        return

    # Provide feedback to the user
    print(f"{person1['name']} has {person1['followers_on_instagram']} followers.")
    print(f"{person2['name']} has {person2['followers_on_instagram']} followers.")

    if correct_answer:
        print("Congratulations! You guessed correctly.")
    else:
        print("Oops! Wrong guess. Better luck next time.")


higher_lower_game()
