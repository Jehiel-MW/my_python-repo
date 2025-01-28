def open_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as file:
            with open(output_file_path, 'w') as output_file:
                for line in file:
                    # Strip the line and convert it to a number
                    line_input = line.strip()
                    try:
                        # Attempt to convert the stripped line to a float
                        fahrenheit_value = float(line_input)
                        celsius_value = fahrenheit_conversion(fahrenheit_value)
                        # Write the processed information to the output file
                        output_file.write(f"{fahrenheit_value}°F is {celsius_value}°C\n")
                    except ValueError:
                        # Handle cases where the line is not a valid number
                        output_file.write(f"Invalid number found in line: {line_input}\n")
    except Exception as e:
        print(f"This error occurred: {e}")

def fahrenheit_conversion(fahrenheit):
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * (5 / 9)
    return round(celsius, 2)  # Return the Celsius value, rounded to 2 decimal places

# Example usage
input_file_path = input("Enter the input file path: ")
output_file_path = input("Enter the output file path: ")
open_file(input_file_path, output_file_path)
