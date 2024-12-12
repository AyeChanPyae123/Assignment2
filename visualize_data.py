import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

def most_populated(db_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # SQL query to get the 20 most populated countries
    cursor.execute("""
        SELECT country_name, population 
        FROM Countries
        ORDER BY population DESC
        LIMIT 20
    """)
    
    # Fetch the result
    countries = cursor.fetchall()
    
    # Close the database connection
    conn.close()

    # Extract the country names and populations
    country_names = [row[0] for row in countries]
    populations = [row[1] for row in countries]
    
    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x=country_names, y=populations, palette='viridis')
    plt.xticks(rotation=90)  # Rotate the x-axis labels for better readability
    plt.xlabel('Country')
    plt.ylabel('Population')
    plt.title('Top 20 Most Populated Countries')
    plt.tight_layout()
    plt.show()

def largest_area(db_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # SQL query to get the 10 largest countries by area
    cursor.execute("""
        SELECT country_name, area
        FROM Countries
        ORDER BY area DESC
        LIMIT 10
    """)
    
    # Fetch the result
    countries = cursor.fetchall()
    
    # Close the database connection
    conn.close()

    # Extract the country names and areas
    country_names = [row[0] for row in countries]
    areas = [row[1] for row in countries]
    
    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x=country_names, y=areas, palette='Blues_d')
    plt.xticks(rotation=90)  # Rotate the x-axis labels for better readability
    plt.xlabel('Country')
    plt.ylabel('Area (sq km)')
    plt.title('Top 10 Largest Countries by Area')
    plt.tight_layout()
    plt.show()

# Call the functions to generate visualizations
most_populated('countries.db')
largest_area('countries.db')
