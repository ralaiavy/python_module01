import math

def get_player_pos() -> tuple[float, float, float]:

    while True:
        try:
            user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
            
            parts = user_input.split(',')
            
            if len(parts) != 3:
                print("Invalid syntax")
                continue
            
            x = float(parts[0].strip())   
            y = float(parts[1].strip())
            z = float(parts[2].strip())
            
            return (x, y, z)
            
        except ValueError as e:
            for part in parts:
                try:
                    float(part.strip())
                except ValueError:
                    print(f"Error on parameter '{part.strip()}': could not convert string to float: '{part.strip()}'")
                    break


def distance_3d(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def main():
    print("=== Game Coordinate System ===")
    
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    
    center = (0.0, 0.0, 0.0)
    distance_to_center = distance_3d(pos1, center)
    print(f"Distance to center: {distance_to_center:.4f}")
    
    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    
    distance_between = distance_3d(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {distance_between:.4f}")

if __name__ == "__main__":
    main()