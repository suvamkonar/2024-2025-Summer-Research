import json

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def print_data(json_data):
    file_path = "new_data.json"
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4)

def add_student(json_data, id, name, grade):
    new_student = {
        "id": id,
        "name": name,
        "grade": grade
    }
    json_data["students"].append(new_student)

def table_printer(json_data):
    print(f"{'ID':<12}{'Name':<15}{'Grade'}")
    print("=" * 35)
    for student in json_data["students"]:
        print(f"ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")
    print()  

def main():
    file_path = 'data.json'
    
    try:
        data = read_data(file_path)
    except FileNotFoundError:
        data = {"students": []}

    add_student(data, 345645, "David", 10)
    table_printer(data)

    print_data(data)
if __name__ == "__main__":
    main()
