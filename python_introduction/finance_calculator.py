monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print(f"(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))")