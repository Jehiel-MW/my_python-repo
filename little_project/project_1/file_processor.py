import os

def read_input_file(file_name):
    try:
        if not os.path.exists(file_name):
            print("Error: The file does not exist.")
            return None
        if not file_name.endswith('.txt'):
            print("Error: The file is not a text file.")
            return None
        
        with open(file_name, 'r') as file:
            content = file.read().strip()
            if not content:
                print("Error: The file is empty.")
                return None
            
            try:
                original_dict = eval(content)  # Convert string to a dictionary
                if not isinstance(original_dict, dict):
                    print("Error: The file content is not a valid dictionary.")
                    return None
                return original_dict
            except:
                print("Error: The file content cannot be interpreted as a dictionary.")
                return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def invert_dictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict

def write_output_file(file_name, inverted_dict):
    try:
        with open(file_name, 'w') as file:
            file.write(str(inverted_dict))
            print(f"Inverted dictionary written to {file_name}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main(input_file, output_file):
    original_dict = read_input_file(input_file)
    if original_dict is None:
        return

    inverted_dict = invert_dictionary(original_dict)
    write_output_file(output_file, inverted_dict)

input_file = 'input.txt'
output_file = 'output.txt'
main(input_file, output_file)
