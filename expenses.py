expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = sum(expenses)
print('Total expenses: ' + str(total) + ' dollars', sep='')

expenses_self = []
total_self = 0
num_expenses = int(input('How many expenses do you have?\n'))
for i in range(num_expenses):
    expenses_self.append(float(input('Enter expense ' + str(i + 1) + ':')))
total_self = sum(expenses_self)
print('Total expenses: ' + str(total_self) + ' dollars', sep='')
