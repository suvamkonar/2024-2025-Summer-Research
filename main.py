import json

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

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
    add_student(data, 345645, "David", 10)
    table_printer(data)

if __name__ == "__main__":
    main()
