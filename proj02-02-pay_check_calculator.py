print("Hello! this calculator is intended to drive you mad, due to how much \"Uncle Sam\" Takes from you")

hours_worked = int(input("Please enter yours hours: "))
hourly_rate = float(input("Please enter your hourly rate: "))
tax_rate = int(input("Please enter your federal and or state tax. If you dont know, please enter 18%: "))
print("\n")

gross_pay = round(hours_worked * hourly_rate, 2)
tax_amount = round(gross_pay * (tax_rate / 10), 2)
take_home_pay = round(gross_pay - tax_amount, 2)

print(f"Your gross pay is ${gross_pay}")
print(f"Tax rate {tax_rate}%")
print(f"Uncle Sam took this ${tax_amount}, from your paycheck")
print(f"Your take home is: ${take_home_pay}")


print(f"Your: ${gross_pay}")
print(f"Your: {tax_rate}%")
print(f"Your: ${tax_amount}")
print(f"Your: ${take_home_pay}","\n")
print("Goodbye, you poor thing")
