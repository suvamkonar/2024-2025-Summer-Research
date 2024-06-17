import json

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to save data to JSON file
def save_data_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add a new student to the existing JSON data
def add_student(json_data, id, name, grade):
    new_student = {
        "id": id,
        "name": name,
        "grade": grade
    }
    json_data["students"].append(new_student)

def table_printer(json_data):
    print("Current Students:")
    for student in json_data["students"]:
        print(f"ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")
    print()

def main():
    file_path = 'data.json'
    
    try:
        data = read_data(file_path)
    except FileNotFoundError:
        data = {"students": []}

    table_printer(data)
    # Adding a new student
    #add_student(data, 4, "David", 10)

    # Save updated JSON data back to the file
    #save_data_to_json(data, file_path)
    
    #print("Student added successfully.")

if __name__ == "__main__":
    main()
