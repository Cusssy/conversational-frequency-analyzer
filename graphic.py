import json
from datetime import datetime
import matplotlib.pyplot as plt
import inquirer

def read_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def count_hours(data):
    hours_count = {}
    for item in data:
        timestamp = datetime.strptime(item['Timestamp'], "%Y-%m-%d %H:%M:%S")
        hour = timestamp.hour
        if hour in hours_count:
            hours_count[hour] += 1
        else:
            hours_count[hour] = 1
    return hours_count

def create_chart(hours_count):
    hours = sorted(list(hours_count.keys()))
    count = [hours_count[h] for h in hours]

    max_index = count.index(max(count))
    min_index = count.index(min(count))

    plt.figure(figsize=(10, 6))
    plt.bar(hours, count, color='skyblue')

    x_min = hours[min_index]
    y_min = count[min_index]
    x_max = hours[max_index]
    y_max = count[max_index]

    plt.plot([x_min, x_max], [y_min, y_max], linestyle='--', color='red', marker='o')
    
    plt.xlabel('Hour of the Day')
    plt.ylabel('Frequency')
    plt.title('Conversation Frequency per Hour of the Day')
    plt.xticks(range(24))
    plt.grid(True)
    plt.show()

def main():
    file_name = input("Enter the name of the JSON file: ")
    data = read_json(file_name)
    hours_count = count_hours(data)
    create_chart(hours_count)

if __name__ == "__main__":
    main()