import pandas as pd
import os


def check_trend(column, trend):
    """
    Function to check the trend (ascending, descending, or constant) for a given column.
    Returns 'Verified' if the trend is followed, or 'Problem' with the first failure point.
    """
    for i in range(1, len(column)):
        if trend == 'ascending':
            if column[i] < column[i - 1]:
                return f"Problem at index {i-1} and {i}: {column[i-1]} > {column[i]}"
        elif trend == 'descending':
            if column[i] > column[i - 1]:
                return f"Problem at index {i-1} and {i}: {column[i-1]} < {column[i]}"
        elif trend == 'constant':
            if column[i] != column[i - 1]:
                return f"Problem at index {i-1} and {i}: {column[i-1]} != {column[i]}"
    return "Verified"

def main():
    # Get CSV file name from the user
    csv_file = input("Enter the name of the CSV file: ")
    print('cwd:', os.getcwd())
    print('file path = ', os.getcwd + csv_file  )


    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
        return

    #outputs column names
    print("\nColumns available in the CSV:")
    print(df.columns.tolist())

    # Ask the user to select a column
    column_name = input("\nEnter the column name to verify: ")

    # Check if the column exists
    if column_name not in df.columns:
        print("Invalid column name. Please try again.")
        return

    # Ask the user to choose the trend
    trend = input("What trend would you like to check (ascending, descending, constant)? ").lower()

    if trend not in ['ascending', 'descending', 'constant']:
        print("Invalid trend option. Please enter either 'ascending', 'descending', or 'constant'.")
        return

    # Get the column data (assuming numeric or comparable data types)
    column_data = df[column_name].values

    # Check the trend and print the result
    result = check_trend(column_data, trend)
    print(result)

if __name__ == "__main__":
    main()