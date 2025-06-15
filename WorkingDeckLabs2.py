import tkinter as tk
from tkinter import ttk
import random

# Sample card pool and their elixir costs
card_elixir_costs = {
    "Arrows": 3,
    "Minions": 3,
    "Archers": 3,
    "Knight": 3,
    "Fireball": 4,
    "Mini P.E.K.K.A": 4,
    "Musketeer": 4,
    "Giant": 5,
    "Spear Goblins": 2,
    "Goblins": 2,
    "Goblin cage": 4,
    "Goblin Hut": 4,
    "Bomber": 2,
    "Skeletons": 1,
    "Tombstone": 3,
    "Valkyrie": 4,
    "Cannon": 3,
    "Barbarians": 5,
    "Mega Minion": 3,
    "Battle Ram": 4,
    "Electro Spirit": 1,
    "Skeleton Dragons": 4,
    "Fire Spirit": 1,
    "Bomb Tower": 4,
    "Inferno Tower": 5,
    "Wizard": 5,
    "Zap": 2,
    "Mortar": 4,
    "Bats": 2,
    "Rocket": 6,
    "Flying Machine": 4,
    "Hog Rider": 4,
    "Goblin Barrel": 3,
    "Guards": 3,
    "Baby Dragon": 4,
    "Skeleton Army": 3,
    "Witch": 5,
    "P.E.K.K.A": 7,
    "Royal Recruits": 7,
    "Royal Giant": 6,
    "Royal Hogs": 5,
    "Three Musketeers": 9,
    "Dark Prince": 4,
    "Prince": 5,
    "Balloon": 5,
    "Snowball": 2,
    "Ice Spirit": 1,
    "Battle Healer": 4,
    "Ice Golem": 2,
    "Lightning": 6,
    "Freeze": 4,
    "Giant Skeleton": 6,
    "Berserker": 2,
    "Skeleton Barrel": 3,
    "Goblin Gang": 3,
    "Barbarian Hut": 6,
    "Dart Goblin": 3,
    "Barbarian Barrel": 2,
    "Poison": 4,
    "Rune Giant": 4,
    "Goblin Giant": 6,
    "Tesla": 4,
    "Elite Barbarians": 6,
    "Minion Horde": 5,
    "Furnace": 4,
    "Zappies": 4,
    "X-Bow": 6,
    "Hunter": 4,
    "Golem": 8,
    "Log": 2,
    "Mega Knight": 7,
    "Ram Rider": 5,
    "Electro Wizard": 4,
    "Inferno Dragon": 4,
    "Sparky": 6,
    "Miner": 3,
    "Princess": 3,
    "Firecracker": 3,
    "Earthquake": 3,
    "Goblin Demolisher": 4,
    "Electro Dragon": 4,
    "Wall Breakers": 2,
    "Graveyard": 5,
    "Phoenix": 4,
    "Royal Ghost": 3,
    "Ice Wizard": 3,
    "Rascals": 5,
    "Heal Spirit": 1,
    "Electro Giant": 7,
    "Bowler": 5,
    "Magic Archer": 4,
    "Bandit": 3,
    "Lava Hound": 7,
    "Royal Delivery": 3,
    "Elixir Golem": 3,
    "Goblin Curse": 2,
    "Rage": 2,
    "Goblin Drill": 4,
    "Executioner": 5,
    "Night Witch": 4,
    "Lumberjack": 4,
    "Elixir Pump": 6,
    "Void": 3,
    "Clone": 3,
    "Tornado": 3,
    "Mirror": None,
    "Cannon Cart": 5,
    "Goblin Machine": 5,
    "Mother Witch": 4,
    "Fisherman": 3,
    "Golden Knight": 4,
    "Skeleton King": 4,
    "Boss Bandit": 6,
    "Archer Queen": 5,
    "Mighty Miner": 4,
    "Goblin stein": 5,
    "Little Prince": 3,
    "Monk": 5
}

# Sample decks per arena
decks = {
    "Arena 1": [
        ["Knight", "Archers", "Bomber", "Spear Goblins", "Mini P.E.K.K.A", "Arrows", "Fireball", "Goblin Hut"],
        ["Knight", "Minions", "Giant", "Mini P.E.K.K.A", "Fireball", "Spear Goblins", "Goblin Hut", "Goblin cage"],
        ["Mini P.E.K.K.A", "Spear Goblins", "Minions", "Giant", "Fireball", "Arrows", "Musketeer", "Prince"],
        ["Knight", "Goblin cage", "Goblin Hut", "Arrows", "Fireball", "Giant", "Musketeer", "Mini P.E.K.K.A"]
    ],
    "Arena 2": [
        ["Giant", "Musketeer", "Minions", "Valkyrie", "Tombstone", "Skeleton Army", "Goblin Barrel", "Zap"],
        ["Knight", "Goblin cage", "Goblin Hut", "Arrows", "Fireball", "Giant", "Musketeer", "Mini P.E.K.K.A"],
        ["Knight", "Archers", "Minions", "Arrows", "Fireball", "Bomber", "Valkyrie", "Goblin Hut"],
        ["Tombstone", "Knight", "Giant", "Minions", "Goblin Hut", "Valkyrie", "Musketeer", "Mini P.E.K.K.A"],
        ["Goblins", "Knight", "Minions", "Giant", "Mini P.E.K.K.A", "Archers", "Fireball", "Bomber"],
        ["Arrows", "Bomber", "Valkyrie", "Knight", "Giant", "Mini P.E.K.K.A", "Musketeer", "Tombstone"]
    ],
    "Arena 3": [
        ["Cannon", "Hog Rider", "Freeze", "Wizard", "Inferno Tower", "Mega Minion", "Fireball", "Bomber"],
        ["Hog Rider", "Fireball", "Wizard", "Cannon", "Mega Minion", "Bomber", "Inferno Tower", "Zap"],
        ["Knight", "Cannon", "Hog Rider", "Freeze", "Wizard", "Fireball", "Mega Minion", "Bomber"]
    ],
"Arena 4": [
        ["Valkyrie", "Archer", "Bomber", "Knight","Fireball", "Goblin Giant", "Musketeer", "Mini P.E.K.K.A"],
        ["Mini P.E.K.K.A", "Wizard", "Valkyrie", "Battle Ram", "Fireball", "Miner", "Skeleton Giant", "Baby Dragon", "Barbarians"],
        ["Mini P.E.K.K.A", "Skeleton Giant", "Hunter", "Zap", "Tombstone", "Witch", "Hog Rider", "Fireball"],
        ["Goblin Barrel", "Hog Rider", "Elixir Golem", "Skeleton Army", "Prince","Valkyrie", "Fireball", "Baby Dragon"],
        ["Mini P.E.K.K.A", "Goblin Hut", "Electro Spirit", "Skeleton Dragons", "Arrows", "Tombstone", "Battle Ram"," Musketeer"],
        ["Valkyrie", "Tombstone", "Prince", "Fireball", "Mini P.E.K.K.A", "Battle Ram", "Barbarians", "Knight"],
        ["Rocket", "Witch", "Bomb Tower", "Barbarians", "Goblin Barrel", "Baby Dragon", "Skeleton Army", "Ballon"],
        ["Mini P.E.K.K.A", "Musketeer", "Mega Minion", "Barbarians","Magic Archer", "Prince", "Skeleton Dragons", "Valkyrie"],
        ["Prince", "Miner", "Arrows", "Barbarian Barrel", "Skeletons", "Minions", "Valkyrie", "Bomb Tower"],
        ["Battle Ram", "Cannon", "Spear Goblins", "Knight", "Archers", "Skeletons", "Fireball", "Prince"],
        ["Executioner", "Giant", "Wizard", "Arrows", "Knight", "Cannon", "Skeletons", "Spear Goblins"],
        ["Barbarians", "Valkyrie", "Goblin Hut", "Fireball", "Battle Ram", "Giant", "Mini P.E.K.K.A", "Musketeer"],
    ],
    "Arena 5": [
        ["Royal Giant", "P.E.K.K.A", "Arrows", "Skeletons", "Bomber", "Mega Knight", "Knight", "bats"],
        ["Mortar", "Bats", "Skeletons", "Knight", "Archers", "Hog Rider", "Mini P.E.K.K.A", "Arrows"],
        ["Mini P.E.K.K.A", "Skeleton Army", "Rage", "X-Bow", "Goblin Barrel", "Hog Rider", "Valkyrie", "Skeleton Dragons"],
        ["Minion Horde", "Royal Recruits", "Skeleton Army", "Tesla", "Fireball", "Freeze", "Rage", "Baby Dragon"],
        ["Hog Rider", "Snowball", "Fireball", "Skeletons", "Musketeer", "Cannon", "Knight", "Spear Goblins"],
        ["Wizard", "Skeleton army", "Goblin Barrel", "Baby Dragon", "Barbarians", "Arrows", "Fireball", "Goblin Cage"],
        ["Knight", "Spear Goblins", "Tombstone", "Arrows", "Skeletons", "Giant", "Mini P.E.K.K.A", "Wizard"],
        ["Cannon", "Minions", "Skeletons", "Arrows", "Giant", "Wizard", "Mini P.E.K.K.A", "Wizard"],

],


}

# Elixir range filter
elixir_ranges = {
    "Low": [2.3, 3.0],
    "Medium": [3.4, 4.0],
    "High": [4.1, 4.8]
}

def generate_deck():
    arena = arena_var.get()
    elixir_pref = elixir_var.get()
    output_text.delete("1.0", tk.END)

    if not arena or not elixir_pref:
        output_text.insert(tk.END, "Please select both an arena and elixir range.")
        return

    valid_decks = decks.get(arena, [])
    min_elixir, max_elixir = elixir_ranges[elixir_pref]

    for _ in range(1000):
        deck = random.choice(valid_decks)
        try:
            avg_elixir = sum(card_elixir_costs[card] for card in deck) / 8
            if min_elixir <= avg_elixir <= max_elixir:
                output_text.insert(tk.END, f"Generated Deck (Avg Elixir: {avg_elixir:.2f}):\n" + ", ".join(deck))
                return
        except TypeError:
            continue

    output_text.insert(tk.END, "Couldn't find a deck in the desired elixir range.")

# GUI setup
root = tk.Tk()
root.title("Clash Royale Deck Generator")
root.geometry("450x350")

tk.Label(root, text="Select Arena:").pack(pady=5)
arena_var = tk.StringVar()
arena_menu = ttk.Combobox(root, textvariable=arena_var, values=list(decks.keys()), state="readonly")
arena_menu.pack()

tk.Label(root, text="Select Elixir Range:").pack(pady=5)
elixir_var = tk.StringVar()
elixir_menu = ttk.Combobox(root, textvariable=elixir_var, values=list(elixir_ranges.keys()), state="readonly")
elixir_menu.pack()

generate_button = tk.Button(root, text="Generate Deck", command=generate_deck)
generate_button.pack(pady=10)

output_text = tk.Text(root, height=10, width=55)
output_text.pack(pady=10)

root.mainloop()