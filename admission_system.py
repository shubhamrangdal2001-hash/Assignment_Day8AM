# admission_system.py
# Part A: Student Admission Decision System

def get_entrance_score():
    while True:
        try:
            score = float(input("Enter entrance score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_gpa():
    while True:
        try:
            gpa = float(input("Enter GPA (0-10): "))
            if 0 <= gpa <= 10:
                return gpa
            else:
                print("GPA must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_recommendation():
    while True:
        rec = input("Do you have a recommendation letter? (yes/no): ").strip().lower()
        if rec in ['yes', 'no']:
            return rec
        else:
            print("Please enter 'yes' or 'no'.")

def get_category():
    while True:
        cat = input("Enter category (general/obc/sc_st): ").strip().lower()
        if cat in ['general', 'obc', 'sc_st']:
            return cat
        else:
            print("Please enter one of: general, obc, sc_st")

def get_extracurricular():
    while True:
        try:
            score = float(input("Enter extracurricular score (0-10): "))
            if 0 <= score <= 10:
                return score
            else:
                print("Score must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def evaluate_admission():
    print("\n===== University Admission System =====\n")

    # collect inputs
    entrance_score = get_entrance_score()
    gpa = get_gpa()
    recommendation = get_recommendation()
    category = get_category()
    extra_score = get_extracurricular()

    print("\n--- Processing ---")

    # merit rule: auto-admit with scholarship if score >= 95
    if entrance_score >= 95:
        print(f"\nResult: ADMITTED (Scholarship)")
        print(f"Reason: Entrance score {entrance_score} >= 95 qualifies for automatic scholarship admission.")
        return

    # calculate bonus points
    bonus = 0
    bonus_details = []

    if recommendation == 'yes':
        bonus += 5
        bonus_details.append("+5 (recommendation)")

    if extra_score > 8:
        bonus += 3
        bonus_details.append("+3 (extracurricular)")

    effective_score = entrance_score + bonus

    if bonus_details:
        print(f"Bonus Applied: {' '.join(bonus_details)}")
    else:
        print("Bonus Applied: None")

    print(f"Effective Score: {effective_score}")

    # category-wise minimum cutoffs
    cutoffs = {
        'general': 75,
        'obc': 65,
        'sc_st': 55
    }

    min_score = cutoffs[category]

    # check GPA first
    if gpa < 7.0:
        print(f"\nResult: REJECTED")
        print(f"Reason: GPA {gpa} is below the minimum required GPA of 7.0")
        return

    # check entrance score against cutoff
    if effective_score >= min_score:
        print(f"\nResult: ADMITTED (Regular)")
        print(f"Reason: Meets {category.upper()} cutoff ({effective_score} >= {min_score}) and GPA requirement ({gpa} >= 7.0)")
    elif effective_score >= min_score - 10:
        # waitlist: within 10 points of cutoff
        print(f"\nResult: WAITLISTED")
        print(f"Reason: Effective score {effective_score} is close but below {category.upper()} cutoff of {min_score}.")
    else:
        print(f"\nResult: REJECTED")
        print(f"Reason: Effective score {effective_score} does not meet {category.upper()} cutoff of {min_score}.")

evaluate_admission()
