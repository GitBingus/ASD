def rFile(file_path):
    """
    Reads the content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an error reading the file.
    """

    even, odd = [], []

    try:
        with open(file_path, 'r') as f:
            content = f.read()

        for num in content.split():
            if num.isdigit():
                if int(num) % 2 == 0:
                    even.append(num)
                else:
                    odd.append(num)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")

    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

    average_even = sum(int(num) for num in even) / len(even) if even else 0
    average_odd = sum(int(num) for num in odd) / len(odd) if odd else 0

    return average_even, average_odd

e, o = rFile("mynumbers.txt")

print("Average of even numbers:", e)
print("Average of odd numbers:", o)