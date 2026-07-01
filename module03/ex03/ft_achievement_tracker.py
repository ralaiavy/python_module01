import random

ALL_ACHIEVEMENTS = [
    'Crafting Genius',
    'World Savior',
    'Master Explorer',
    'Collector Supreme',
    'Untouchable',
    'Boss Slayer',
    'Strategist',
    'Unstoppable',
    'Speed Runner',
    'Survivor',
    'Treasure Hunter',
    'First Steps',
    'Sharp Mind',
    'Hidden Path Finder'
]

def gen_player_achievements():
    num_achievements = random.randint(4, 10)
    
    selected = random.sample(ALL_ACHIEVEMENTS, num_achievements)
    
    return set(selected)

def main():
    print("=== Achievement Tracker System ===")
    
    players = {}
    
    player_names = ['Alice', 'Bob', 'Charlie', 'Dylan']
    
    for name in player_names:
        players[name] = gen_player_achievements()
        print(f"Player {name}: {players[name]}")
    
    all_achievements = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    print(f"\nAll distinct achievements: {all_achievements}")
    
    common_achievements = None
    for achievements in players.values():
        if common_achievements is None:
            common_achievements = achievements.copy()
        else:
            common_achievements = common_achievements.intersection(achievements)
    print(f"Common achievements: {common_achievements}")
    
    print("\nOnly achievements per player:")
    for name, achievements in players.items():
        others_union = set()
        for other_name, other_achievements in players.items():
            if other_name != name:
                others_union = others_union.union(other_achievements)
        
        only_this = achievements.difference(others_union)
        print(f"Only {name} has: {only_this}")
    
    print("\nMissing achievements per player:")
    for name, achievements in players.items():
        missing = set(ALL_ACHIEVEMENTS).difference(achievements)
        print(f"{name} is missing: {missing}") 

if __name__ == "__main__":
    main()