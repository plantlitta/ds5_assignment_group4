
file_path = input("Enter the path to the CSV file: ")
records = []

with open(file_path, 'r') as file: # 1. function to open file and make it a dictionary with lists
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        records.append(row)


#









#


total = sum(float(record['Grade']) for record in records) # 2. calculating total function
average = total / len(records)

#









#

print(f"Average Grade: {average}")
print("--------------------")

filtered_records = [record for record in records if float(record['Grade']) >= 80.0] # 3. filtering function

#









#

print("Student Report")
print("--------------")
for record in filtered_records: # 4. displaying results function
    print(f"Name: {record['Name']}")
    print(f"Grade: {record['Grade']}")
    print("--------------------")

#









#
