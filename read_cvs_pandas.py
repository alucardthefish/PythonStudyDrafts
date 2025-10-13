import pandas as pd


# Create a DataFrame with some sample data
data = {
    "Name": ["John", "Jane", "Doe"],
    "Age": [25, 30, 35],
    "City": ["New York", "San Francisco", "Los Angeles"],
}

df = pd.DataFrame(data)

# Specify the file path where you want to save the CSV file
csv_file_path = "example.csv"

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved to: {csv_file_path}")
