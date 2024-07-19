import sys

def add_record():
    try:
        id = input('Enter the ID:').strip()
        name = input('Enter the name:').strip()
        age = input('Enter the age:').strip()
        address = input('Enter the address you live in:').strip()
        phone = input('Enter your mobile number:').strip()

        if not id or not name or not age or not address or not phone:
            raise ValueError("All fields are required.")

        record = [id, name, age, address, phone]
        record_line = ','.join(record) + '\n'

        with open('example.txt', 'a') as f:
            f.write(record_line)
        print('Record added successfully.')

    except ValueError as ve:
        print(f"Error: {ve}")

def display_record():
    try:
        with open('example.txt', 'r') as f:
            message = f.read()
        print(message)

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def delete_record():
    try:
        display_record()
        delete_id = input('Enter ID of the record you want to delete:').strip()

        with open('example.txt', 'r') as f:
            lines = f.readlines()
        found = False

        with open('example.txt', 'w') as f:
            for line in lines:
                record = line.strip().split(',')
                if record[0] == delete_id:
                    found = True
                    print(f'Record with ID {delete_id} deleted successfully.')
                else:
                    f.write(line)

        if not found:
            print(f'Record with ID {delete_id} not found')

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def update_record():
    try:
        display_record()
        update_id = input('Enter the ID of the record to update:').strip()
        field_to_update = input('Enter the field you want to update (name/age/address/mobile):').strip().lower()
        new_value = input('Enter the new value:').strip()

        if not update_id or not field_to_update or not new_value:
            raise ValueError("All fields are required.")

        with open('example.txt', 'r') as f:
            lines = f.readlines()

        found = False

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
                    print(f'Invalid field: {field_to_update}')
                    return

                lines[i] = ','.join(record) + '\n'
                found = True
                print('Record updated successfully.')

        if not found:
            print(f'Record with ID {update_id} not found.')

        with open('example.txt', 'w') as f:
            f.writelines(lines)

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def terminate():
    try:
        choice = input('Do you want to terminate the program? (yes/no): ').strip().lower()
        if choice == 'yes':
            print('Terminating the program')
            sys.exit(0)
        else:
            print('Continuing the program')
            main()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def search_record():
    try:
        search_term = input('Enter search term:').strip()
        if not search_term:
            raise ValueError("Search term cannot be empty.")

        with open('example.txt', 'r') as f:
            lines = f.readlines()
            results = [line.strip() for line in lines if search_term in line]

        if results:
            print('Search result:')
            for result in results:
                print(result)
        else:
            print('No record found')

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    try:
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

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


main()
