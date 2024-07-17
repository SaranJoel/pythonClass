import sys

'''this is to add a new record to the text file i have made into a list seperated with commas liks CSV and
 used append method of files processing '''
def add_record():
    id = input('Enter the ID:')
    name = input('Enter the name:')
    age = input('Enter the age:')
    address = input('Enter the address you live in:')
    phone = input('Enter your mobile number:')

    record=[id, name, age, address,phone]
    record_line = ','.join(record) + '\n'

    with open('example.txt', 'a') as  f:
        f.write(record_line)
    print('Record added succesfully')

''' this is to display the record that text file have here i used read method to read'''
def display_record():
    with open('example.txt', 'r') as f:
        message = f.read()
    print(message)


'''this is to delete a record of a text file using a particular field in record here i use
 ID as base to approcah the list and do deltion if the record'''
def delete_record():
    display_record()
    delete_id = input('Enter ID of the record you want to delete:')

    with open('example.txt','r') as f:
        lines = f.readlines()
    found = False

    with open('example.txt', 'w') as f:
        for line in lines:
            record = line.strip().split(',')
            if record[0] == delete_id:
                found = True
                print(f'Record with ID {delete_id} deleted succesfully. ')
            else:
                f.write(line)
    if not found:
        print(f'Record with ID{delete_id} not found')

'''this is used to update a field in the record here as well i used ID as base to call the list and make to a particular field'''
def update_record():
    display_record()
    update_id =input('Enter the ID of the record to update:').strip()
    field_to_update = input('Enter the filed you want to update(name/age/address/mobile):').strip().lower()
    new_value = input('Entre the new value:').strip()

    with open('example.txt', 'r') as f:
        lines = f.readlines()

    found =False

    for i, line in enumerate(lines):
        record = line.strip().split(',')
        if record[0] == update_id:
            if field_to_update == 'name':
                record[1] = new_value
            elif field_to_update == 'age':
                record[2] = new_value
            elif field_to_update == 'address':
                record[3] = new_value
            elif field_to_update == 'mobile':
                record[4] = new_value
            else:
                print(f'invlaid field:{field_to_update}')

            lines[i] = ','.join(record)+'\n'
            found = True
            print('Record updated successfully.')

    if not found:
        print(f'Record with ID{update_id} not found.')

    with open('example.txt', 'w') as f:
        f.writelines(lines)

'''this is to terminate teh program where it retains the data in the text file and if you want to continue 
you can continue after a change of heart'''
def terminate():
    choice = input('Do you want to terminate the program?(yes/no): ').strip().lower()
    if choice == 'yes':
        print('Terminating the program')
        sys.exit(0)
    else:
        print('Continuing the program')
        main()
'''this is to search the records line by line and if it has the key word in it, it will likely show that record as output or search result'''
def search_record():
    search_term = input('Enter search term:')
    with open('example.txt', 'r') as f:
        lines = f.readlines()
        results=[]
        for line in lines:
            if search_term in line:
                results.append(line.strip())
    if results:
        print('search result:')
        for result in results:
            print(result)
    else:
        print('No record found')

'''this is main menu where you give the choice to make the changes to the file'''
def main():
    while True:
        print('Menu:')
        print("1. Add a Record")
        print("2. Delete a Record")
        print("3. Update a Record")
        print("4. View All Records")
        print("5. Search for a Record")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            delete_record()
        elif choice == "3":
            update_record()
        elif choice == "4":
            display_record()
        elif choice == "5":
            search_record()
        elif choice == "6":
            terminate()
            break
        else:
            print("Invalid choice. Please try again.")

main()