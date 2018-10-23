mealCost = input()
tipPercent = input()
taxPercent = input()

total = mealCost * (1 + tipPercent/100.0 + taxPercent/100.0)
total = round(total, 0)
print "The total meal cost is",
print "%.0f" % total,
print "dollars."