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
    #attempt to ensure continuity across OSs
    file_path = os.path.join(os.getcwd(), csv_file)

    absolute_path = os.path.abspath(file_path)

    print('cwd:', os.getcwd())
    print('Absolute file path:', absolute_path)


    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
        return

    #outputs column names
    print("\nColumns available in the CSV: format [name, index]")
    columnList = df.columns.tolist()
    columnListIndexed = []
    columnListIndexes = []
    counter = 0
    for column in columnList:
        columnListIndexed.append(column + " " + str(counter))
        columnListIndexes.append(str(counter))
        counter += 1
    print(columnListIndexed)
        

    #while continuing = 1, continues to ask user 
    continuing = 1

    while continuing:

    # Ask the user to select a column
        column_name = input("\nEnter the column name or index to verify: ")

        # Check if the column exists
        while column_name not in df.columns and column_name not in columnListIndexes:
            print("Invalid column name or index. Please try again.")
            column_name = input("\nEnter the column name or index to verify: ")

        # Ask the user to choose the trend
        trend = input("What trend would you like to check (ascending, descending, constant)? ").lower()

        while trend not in ['ascending', 'descending', 'constant']:
            print("Invalid trend option. Please enter either 'ascending', 'descending', or 'constant'.")
            trend = input("What trend would you like to check (ascending, descending, constant)? ").lower()

        # Get the column data (assuming numeric or comparable data types)
        if column_name in df.columns:
            column_data = df[column_name].values
        else: #finds column at given index, gets values
            column_data = df.iloc[:, int(column_name)].values

        # Check the trend and print the result
        result = check_trend(column_data, trend)
        print(result)

        y_n = input("Would you like to verify another column (y or n): ").lower()

        # Validate input to ensure it's either 'y' or 'n'
        while y_n != "y" and y_n != "n":
            y_n = input("\nPlease enter 'y' or 'n': ").lower()

        # Exit if user chooses 'n'
        if y_n == "n":
            continuing = 0
    

if __name__ == "__main__":
    main()