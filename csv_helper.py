import csv

def create_new_csv(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Response"])

def append_to_csv(file_path, data):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)