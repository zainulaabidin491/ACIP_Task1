
 # Task 1 - Record the yield
cow_data = {}
for day in range(7):
    print(f"---- Day {day+1} ----")
    for milking in range(2):
        print(f"----Milking {milking+1} -----")
        while True:
            cow_id = input("Enter cow ID (3 digits): ")
            if len(cow_id) == 3 and cow_id.isdigit():
                break
            print("Invalid ID. Please enter a 3-digit ID.")

        yield1 = float(input("Enter yield (litres): "))
        while yield1 < 0:
            print("Yield cannot be negative. Please enter a valid yield.")
            yield1 = float(input("Enter yield (litres): "))

        if cow_id not in cow_data:
            cow_data[cow_id] = []
        cow_data[cow_id].append(yield1)

# Task 2 - Calculate the statistics
total_milk = sum(sum(yields) for yields in cow_data.values())
average_milk = total_milk / len(cow_data)
print(f"Total weekly milk: {total_milk:.1f} litres")
print(f"Average milk per cow: {average_milk:.1f} litres")

# Task 3 - Identify the most productive cow and cows with low volume
most_milk = max(cow_data, key=lambda x: sum(cow_data[x]))
low_milk_cows = [cow for cow, yields in cow_data.items() if sum(yields) / len(yields) < 12]
print(f"Cow {most_milk} produced the most milk: {sum(cow_data[most_milk]):.1f} litres")
if low_milk_cows:
    print("Cows with low milk production :")
    for cow in low_milk_cows:
        print(f"  Cow {cow}: {sum(cow_data[cow]):.1f} litres")
else:
    print("No cows have low milk production.")