table_number= int(input("enter the number of your choice to print the multiplication table: "))

print("the multiplication table of: " , table_number)

for count in range(1,11):
    print(table_number, 'x', count, '=', table_number * count)