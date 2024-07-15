 # this program helps users manage their fianances by tracking income, expenses, and saving goals.
 # while utilizing various data structures, file input/output and conditional statements.
 
from sys import argv
script, data_file = argv

print("Please note that everything you type in should be in Naira.")

info = {
        "income" : float(input("please, type in how much you earn in a month?: ")),
        "saving_goals" : float(input("please, type saving goal?: ")),
        "house_rent" : float(input("How much did you spend on rent.?: ")),
        "food" : float(input("How much did you spend on food.?: ")),
        "transport" : float(input("How much did you spend on transportation?: ")),
        "health" : float(input("How much did you spend on your health related activities(in Naira)?: ")),
        "personal_care" : float(input("How much did you spend on your personal care,\ne.g haircut, gym, beauty products, etc.: ")),
        "education" : float(input("How much did you spend on your education?: ")),
        "clothing" : float(input("How much did you spend on clothing?: "))
        }




first_value = list(info.values())[0] # singles out the first value of the dictionary "info"
income = first_value
second_value = list(info.values())[1] # singles out the secondvalue of the dictionary "info"
saving_goals = second_value



def expenses(info):
    expenses_sum = sum(list(info.values())[2:]) # excludes the first value of the dictionary item(income)
     
    return expenses_sum
    
exp_sum = expenses(info)

def expenses_percent(exp_sum,income):
    expen_percent = (exp_sum / income) * 100
    return expen_percent
    
expense = expenses_percent(exp_sum,income)

def alert(exp_sum, income, saving_goals):
    if exp_sum > income:
        print("Wow expenses akaria income!")
        print(f"you have spent {expense:.2f}% of your income")
    elif exp_sum < income:
        print("It seems like you still have some money to save")
        print(f"you have spent {expense:.2f}% of your income")
        print(f"your saving goal for the month is {saving_goals}")
        if (((income-exp_sum)/income)*100) < ((saving_goals/income)*100):
            print("you didn't your target")
            print("try your best next month")
            print(f"you have spent {expense:.2f}% of your income")
        elif (((income-exp_sum)/income)*100) > ((saving_goals/income)*100):
            print("you have met your target for the month")
            print(f"you have spent {expense:.2f}% of your income")
    else:
        print("You are fiancially stressed")
        print(f"you have spent {expense:.2f}% of your income")
        
alert(exp_sum, income, saving_goals)

def create_and_write(data_file, dict):
    open_file = open(data_file, 'w+')
    for key, value in dict.items():
            open_file.write(f"{key}:{value}\n")
        
cw_file = create_and_write(data_file, info)


def print_file(data_file):
    open_file = open(data_file, 'r')
    read_file = open_file.read()
    print("This are the content of the newly created file\n",read_file)
    
print_file(data_file)

    
