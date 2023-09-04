with open('C:\Dhana\OneDrive - Conduent\Reading Materials\Python\my_code\Calorie Counting\Calorie_Counting.csv') as file:
    lines = file.readlines()
count = 0
sum = 0
final_sum = 0
final_count = 0
for line in lines:
    line = line.strip()
    #print("-" + line + "-")
    if line == "":
        #print("-" + line + "-")
        #print(f"0count is {count} and sum is {sum}")
        if sum > final_sum:
            final_sum = sum
            final_count = count
        count += 1
        #print(f"1count is {count} and final_sum is {final_sum}")
        sum = 0
    else:
        sum = sum + int(line)

if sum > final_sum:
    final_sum = sum
    final_count = count
    count += 1

#print(f"2count is {final_count} and final_sum is {final_sum}")
print(final_sum)
# output is 69693
