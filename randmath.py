import random
import time
MAX_OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left_operand = random.randint(MIN_OPERAND,MAX_OPERAND)
    right_operand = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(MAX_OPERATORS)
    expr = str(left_operand) + " " + operator + " " + str(right_operand)
    answer = eval(expr)
    return expr,answer

wrong = 0
print("THE GAME HAS STARTED.....")
print("---------------------")
start_time = time.time()
for i in range(TOTAL_PROBLEMS):
    expr , answer = generate_problem()
    while True:
        guess = input("enter the answer for " + expr + " : ")
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()
total_time = end_time - start_time
print("total time taken is ",int(total_time)," second")
