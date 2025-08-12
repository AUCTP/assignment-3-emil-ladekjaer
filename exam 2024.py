def sales_target(data):
    sales_score=[]
    for employee in data:
        sales_score.append(data[employee]["salesTarget"])
    return sales_score

def customer_satisfaction(data):
    satisfaction_score=[]
    for employee in data:
        satisfaction_score.append(data[employee]["customerSatisfaction"])
    return satisfaction_score

def attendance(data):
    attendance_score=[]
    for employee in data:
        attendance_score.append(data[employee]["attendance"])
    return attendance_score

def peer_feedback(data):
    feedback_score=[]
    for employee in data:
        feedback_score.append(data[employee]["peerFeedback"])
    return feedback_score

def evaluate_performance(salesscores, customersatisfaction, attendances, feedbacks):
    print("Employee performance evaluation:")
    overall_ratings = []
    for employee in range(len(data.keys())):
        sales=salesscores[employee]
        satisfaction=customersatisfaction[employee]
        attendance=attendances[employee]
        feedback=feedbacks[employee]
        print(f"Employee: {list(data.keys())[employee]}")
        if sales < 80:
            sales_rating = "Poor"
        elif 80 <= sales <= 100:
            sales_rating = "Average"
        elif 100 < sales <= 120:
            sales_rating = "Good"
        else:
            sales_rating = "Excellent"
        print(f"Sales Target Achievement: {sales_rating}")
        if satisfaction < 6:
            satisfaction_rating = "Poor"
        elif 6 <= satisfaction <= 7:
            satisfaction_rating = "Average"
        elif 8 <= satisfaction <= 9:
            satisfaction_rating = "Good"
        else:
            satisfaction_rating = "Excellent"
        print(f"Customer Satisfaction Score: {satisfaction_rating}")
        if attendance < 20:
            attendance_rating = "Poor"
        elif 20 <= attendance <= 24:
            attendance_rating = "Average"
        elif 25 <= attendance <= 27:
            attendance_rating = "Good"
        else:
            attendance_rating = "Excellent"
        print(f"Attendance Record: {attendance_rating}")
        if feedback < 4:
            feedback_rating = "Poor"
        elif 4 <= feedback <= 6:
            feedback_rating = "Average"
        elif 7 <= feedback <= 8:
            feedback_rating = "Good"
        else:
            feedback_rating = "Excellent"
        print(f"Peer Feedback Score: {feedback_rating}")
        ratings = [sales_rating, satisfaction_rating, attendance_rating, feedback_rating]
        if ratings.count("Excellent") == 4:
            overall_rating = "Outstanding"
        elif ratings.count("Poor") >= 2:
            overall_rating = "Needs Improvement"
        elif ratings.count("Good") + ratings.count("Excellent") >= 3:
            overall_rating = "Strong Performer"
        else:
            overall_rating = "Satisfactory"
        print(f"Overall Performance Rating: {overall_rating}\n")
        overall_ratings.append(overall_rating)
    return overall_ratings

def calculate_bonus(rating):
    print("Annual bonus calculation:")
    employee_names = list(data.keys())
    for employee in range(len(employee_names)):
        name= employee_names[employee]
        tenure=data[name]["yearsofservice"]
        if tenure<2:
            multiplier = 1
        elif 2 <= tenure <= 5:
            multiplier = 1.5
        else:
            multiplier = 2
        if rating[employee] == "Outstanding":
            bonus = 1000 * multiplier
        elif rating[employee] == "Strong Performer":
            bonus = 800 * multiplier
        elif rating[employee] == "Satisfactory":
            bonus = 500 * multiplier
        else:
            bonus = 200 * multiplier
        print(f"Employee: {list(data.keys())[employee]} will receive an annual bonus of ${bonus:.2f} based on their performance rating of {rating[employee]} and {tenure} years of service.\n")

###main program
data= {"Emil": {"salesTarget": 125, "customerSatisfaction": 10, "attendance": 28, "peerFeedback": 9, "yearsofservice": 3}, "Anna": {"salesTarget": 115, "customerSatisfaction": 8, "attendance": 26, "peerFeedback": 4, "yearsofservice": 1}, "Niko":{ "salesTarget": 75, "customerSatisfaction": 5, "attendance": 28, "peerFeedback": 9, "yearsofservice": 6}}
salesscores=sales_target(data)
customersatisfaction=customer_satisfaction(data)
attendances=attendance(data)
feedbacks=peer_feedback(data)
overall_ratings=evaluate_performance(salesscores, customersatisfaction, attendances, feedbacks)
calculate_bonus(overall_ratings)
