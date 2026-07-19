import sys
import typing

def main():
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
        
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_filename = sys.stdin.readline().strip()
        
        if new_filename:
            try:
                new_file = open(new_filename, 'w')
                new_file.write(transformed_content)
                new_file.close()
                print(f"Saving data to '{new_filename}'")
                print(f"Data saved in file '{new_filename}'.")
            except Exception as e:
                sys.stderr.write(f"[STDERR] Error saving file '{new_filename}': {e}\n")
                sys.stderr.flush()
        else:
            print("Not saving data.")
            
    except FileNotFoundError:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': [Errno 2] No such file or directory: '{filename}'\n")
        sys.stderr.flush()
    except PermissionError:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': [Errno 13] Permission denied: '{filename}'\n")
        sys.stderr.flush()
    except IsADirectoryError:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': [Errno 21] Is a directory: '{filename}'\n")
        sys.stderr.flush()
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()

if __name__ == "__main__":
    main()