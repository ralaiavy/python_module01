import sys
import typing

def secure_archive(filename, action='read', content=None):
    if isinstance(action, int):
        action = 'write' if action == 1 else 'read'
    
    try:
        if action == 'read':
            with open(filename, 'r') as file:
                file_content = file.read()
                return (True, file_content)
        elif action == 'write':
            if content is None:
                return (False, "Error: No content provided for write operation")
            with open(filename, 'w') as file:
                file.write(content)
                return (True, f"Successfully wrote to '{filename}'")
        else:
            return (False, f"Error: Invalid action '{action}'. Use 'read' or 'write'.")
            
    except FileNotFoundError:
        return (False, f"[Errno 2] No such file or directory: '{filename}'")
    except PermissionError:
        return (False, f"[Errno 13] Permission denied: '{filename}'")
    except IsADirectoryError:
        return (False, f"[Errno 21] Is a directory: '{filename}'")
    except Exception as e:
        return (False, str(e))


def main():
    print("=== Cyber Archives Security ===")
    
    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive('/not/existing/file', 'read')
    print(result)
    print()
    
    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive('/etc/master.passwd', 'read')
    print(result)
    print()
    
    print("Using 'secure_archive' to read from a regular file:")
    try:
        with open('ancient_fragment.txt', 'r') as f:
            test_content = f.read()
    except:
        test_content = "[FRAGMENT 001] Digital preservation protocols established 2087\n[FRAGMENT 002] Knowledge must survive the entropy wars\n[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
        with open('ancient_fragment.txt', 'w') as f:
            f.write(test_content)
    
    result = secure_archive('ancient_fragment.txt', 'read')
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    result = secure_archive('new_fragment.txt', 'write', test_content)
    print(result)
    print()
    
    print("Verifying the write operation:")
    result = secure_archive('new_fragment.txt', 'read')
    print(result)


if __name__ == "__main__":
    main()