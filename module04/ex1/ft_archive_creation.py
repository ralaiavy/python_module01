import sys
import typing

def main():
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    
    filename = sys.argv[1]
    
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    
    content = None
    
    try:
        file = open(filename, 'r')
        print("---")
        
        content = file.read()
        print(content)
        
        print("---")
        print(f"File '{filename}' closed.")
        
        file.close()
        
        lines = content.splitlines()
        transformed_lines = [line + '#' for line in lines]
        transformed_content = '\n'.join(transformed_lines)
        
        print("Transform data:")
        print("---")
        print(transformed_content)
        print("---")
        
        new_filename = input("Enter new file name (or empty): ")
        
        if new_filename.strip():
            try:
                new_file = open(new_filename, 'w')
                new_file.write(transformed_content)
                new_file.close()
                print(f"Saving data to '{new_filename}'")
                print(f"Data saved in file '{new_filename}'.")
            except Exception as e:
                print(f"Error saving file '{new_filename}': {e}")
        else:
            print("Not saving data.")
            
    except FileNotFoundError:
        print(f"Error opening file '{filename}': [Errno 2] No such file or directory: '{filename}'")
    except PermissionError:
        print(f"Error opening file '{filename}': [Errno 13] Permission denied: '{filename}'")
    except IsADirectoryError:
        print(f"Error opening file '{filename}': [Errno 21] Is a directory: '{filename}'")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")

if __name__ == "__main__":
    main()