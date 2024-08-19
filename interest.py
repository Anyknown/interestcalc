def calculate_interest(principal, rate, years):
    interest_values = []
    for i in range(years):
        interest = principal * rate * i
        interest_values.append(interest)
    
    return interest_values

def write_to_file(file_name, interest_values):
    with open(file_name, 'w') as file:
        for interest in interest_values:
            file.write(str(interest) + '\n')

principal = 1000
rate = 0.05
years = 10
interest_values = calculate_interest(principal, rate, years)
write_to_file('.github/workflows/interest_values.txt', interest_values)
