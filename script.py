def calculate(hourlyDollars):
  numHoursDaily = 4
  numDaysPerWeek = 2
  numWeeksPerPaycheck = 2
  taxPercent = .079

  grossPay = hourlyDollars * numHoursDaily * numDaysPerWeek * numWeeksPerPaycheck
  afterTax = grossPay - (grossPay * taxPercent)

  print("--------------")
  print("_$", hourlyDollars, "hr, working", numHoursDaily, "hours day, ", numDaysPerWeek, "days a week")
  print("$ after 1 paycheck", afterTax)
  print("$ after 2 months", afterTax * 4)
  print("$ after 6 months", afterTax * 12)
  print("$ after 1 year ", afterTax * 24)
  print("--------------")

hourlyPayOptions =  [13, 15, 16, 17, 18, 19, 20]

for i in hourlyPayOptions:
  calculate(i)