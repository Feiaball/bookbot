"""
import sys
from stats import count_characters, sort_characters


def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""



from stats import count_words


from stats import count_characters


def count_words(text):
    return len(text.split())

def main():
    
    print("============ BOOKBOT ============")

    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    if not book_text:
        print("Failed to read the book. Exiting.")
        sys.exit(1)

    print(f"Analyzing book found at {book_path}...")


    book_text = get_book_text(filepath)


    word_count = count_words(book_text)
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_counts = count_characters(book_text)
    sorted_char_list = sort_characters(char_counts)

    print(f"--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
"""

import sys
from stats import count_characters, sort_characters


def get_book_text(filepath):
    """
    Reads the contents of a book file and returns it as a string.
    
    Args:
        filepath (str): Path to the book file
        
    Returns:
        str: Contents of the file, or empty string if an error occurs
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def count_words(text):
    """
    Counts the number of words in the given text.
    
    Args:
        text (str): The text to count words in
        
    Returns:
        int: Number of words
    """
    return len(text.split())


def main():
    """
    Main function to run the book analysis program.
    Uses command-line argument for book path.
    """
    print("============ BOOKBOT ============")

    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get book path from command line argument
    book_path = sys.argv[1]

    # Read the book text
    book_text = get_book_text(book_path)
    if not book_text:
        print("Failed to read the book. Exiting.")
        sys.exit(1)

    print(f"Analyzing book found at {book_path}...")

    # Count total words
    word_count = count_words(book_text)
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Count characters and sort them
    char_counts = count_characters(book_text)
    sorted_char_list = sort_characters(char_counts)

    # Print character count report
    print(f"--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ================")


# Run main only if this script is executed directly
if __name__ == "__main__":
    main()
