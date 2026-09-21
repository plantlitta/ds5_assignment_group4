

def import_data(): # done by Tacy # 1. function to open file and make it a dictionary with lists
    file_path = input("Enter the path to the CSV file: ")
    records = [] 
    with open(file_path, 'r') as file: 
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)
    return records 
 

def calc_tot(n): # done by Litta # 2. calculating total function
    total = sum(float(record['Grade']) for record in n)

    return total


def filter_record(record): #done by Tacy # 3. filtering function
    filtered_records = [record for record in records if float(record['Grade']) >= 80.0]
    return(filtered_records)


def filter_list(b): # done by Litta # 4. displaying results function
    for record in b: 
    print(f"Name: {record['Name']}")
    print(f"Grade: {record['Grade']}")
    print("--------------------")
    return None

# calling all functions done by Litta

records = import_data()
filtered_records = filter_record(records)

total = calc_tot(records)
average = total / len(records)

print(f"Average Grade: {average}")
print("--------------------")


print("Student Report")
print("--------------")
filter_list(filtered_records)
