import json
import csv
import os

def json_to_csv(file_name, csv_file):
    # Get absolute file path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    
    # Read and parse the JSON file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Convert the JSON content to a dictionary
    data = json.loads(content)

    # Get the 'employee' dictionary from the parsed JSON
    employee_data = data['employee']

    # Save the CSV file in the same directory
    csv_file_path = os.path.join(script_dir, csv_file)
    
    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header (the keys of the dictionary)
        writer.writerow(employee_data.keys())
        
        # Write the row (the values of the dictionary)
        writer.writerow(employee_data.values())

# Usage example
file_name = "input.json"
csv_file = 'output.csv'
json_to_csv(file_name, csv_file)

print(f"CSV file saved as {csv_file} in {os.path.abspath(csv_file)}")
