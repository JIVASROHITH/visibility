import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("C:/Users/Jivas Rohith/Downloads/linux.csv")

# Function to find the matching command
def get_command(user_prompt):
    for index, row in df.iterrows():
        if user_prompt.lower() == row['prompt'].lower():
            return row['Command']
    return None  # No match found

while True:
    user_input = input("Enter a prompt: ")

    command = get_command(user_input)

    if command:
        # Execute the command using the 'os' module
        import os
        os.system(command)
    else:
        print("Command not found. Please try a different prompt.")