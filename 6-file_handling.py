# File handling: reading and writing files

with open("input.txt", "r") as file:
    content = file.read()  # read the entire file content
    print("File content:", content)


with open("output.txt", "w") as file:
    file.write("This is a test output file.\n")  # write to the file
    file.write("Adding another line to the output file.\n")
    # write multiple lines
    file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")

# count words in a file


def count_words_in_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)  # return the number of words
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return 0


# Example usage of count_words_in_file
word_count = count_words_in_file("input.txt")
print(f"Number of words in 'input.txt': {word_count}")
