def validate_email(email):
    if re.match(reg, email):
        print(f"Email '{email}' is valid.")
        return True
    else:
        print(f"Email '{email}' is invalid.")
        return False

def get_department(email):
    if email_validity==True:
        print(f"Email department code: {re.match(reg, email).group(1)}")
    else:
        print("None")

def categorize_emails(email_list):
    categorized_emails = {}
    for email in email_list:
        if re.match(reg, email)!=None:
            department=re.match(reg, email).group(1)
            if department in categorized_emails:
                categorized_emails[department].append(email)
            else:
                categorized_emails[department]=[email]
    print(categorized_emails)
        

#main program
import re
reg='^[a-zA-Z]{1}[a-z]+@(hr|it|fin|mkt|ops)\.company\.com$'
email=input("Enter an email address: ")
email_list=["jdoe@hr.company.com", "elade@fin.company.com", "dprobst@ops.company.com", "anour@it.company.com", "mmunk@mkt.company.com", "nbisp@it.company.com", "jhfhjfhhfr"]
email_validity=validate_email(email)
get_department(email)
categorize_emails(email_list)