def open_files(input_file_path, output_file_path):
    try:
        # Open both input and output files
        with open(input_file_path, 'r') as file:
            my_dict = {}  # Initialize an empty dictionary
            # Read the file line by line
            for line in file:
                line_input = line.strip()
                # Split the line at the colon and create key-value pairs
                item, price = line_input.split(':')
                my_dict[item.strip()] = int(price.strip())  # Add to the dictionary
        process_file(my_dict, output_file_path)  # Call the function to process input
    except Exception as e:
        print(f"This error occurred: {e}")


def process_file(my_dict, output_file_path):
    user_input = input("Enter item to search for: ")
    try:
        if user_input in my_dict:
            value = my_dict[user_input]
            # Write the result to the output file
            with open(output_file_path, 'w') as output_file:
                output_file.write(f"The price of {user_input} is {value}")
        else:
            with open(output_file_path, 'w') as output_file:
                output_file.write(f"Invalid input. {user_input} does not exist.")
    except Exception as e:
        print(f"Error during processing: {e}")


# Example of usage
input_file_path = input("Enter input file path: ")
output_file_path = input("Enter output file path: ")

open_files(input_file_path, output_file_path)
