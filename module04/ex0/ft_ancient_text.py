import sys
import typing

def main():
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    
    filename = sys.argv[1]
    
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    
    try:
        file = open(filename, 'r')
        
        print("---")
        
        content = file.read()
        print(content)
        
        print("---")
        print(f"File '{filename}' closed")
        
        file.close()
        
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