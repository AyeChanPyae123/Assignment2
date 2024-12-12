import csv
import sqlite3

# Function to read data from CSV and save to the database
def ingest_data(csv_file, db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Open the CSV file for reading
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        
        # Print the fieldnames (column names) from the CSV file
        print(f"CSV Column Names: {csv_reader.fieldnames}")

        # Loop through the rows in the CSV file
        for row in csv_reader:
            country_name = row['name']  # Use the correct column name 'name'

            # Handle conversion for area and population, rounding or casting to integers
            try:
                area = int(float(row['area']))  # Convert area to float first, then to integer
            except ValueError:
                area = 0  # If there's an issue with the value, set it to 0 or handle appropriately

            try:
                population = int(float(row['population']))  # Convert population to float first, then to integer
            except ValueError:
                population = 0  # If there's an issue with the value, set it to 0 or handle appropriately

            # Insert the data into the Countries table
            cursor.execute('''
                INSERT INTO Countries (country_name, area, population)
                VALUES (?, ?, ?)
            ''', (country_name, area, population))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"Data from {csv_file} has been successfully ingested into the database.")

# Call the function to ingest data
ingest_data('countries.csv', 'countries.db')
