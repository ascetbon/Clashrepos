import tkinter as tk
from tkinter import ttk
import random
card_elixir_costs = {
    "Knight": 3,
    "Archers": 3,
    "Bomber": 3,
    "Spear Goblins": 2,
    "Mini P.E.K.K.A": 4,
    "Arrows": 3,
    "Goblin Hut": 5,
    "Fireball": 4,
    "Giant": 5,
    "Musketeer": 4,
    "Witch": 5,
    "Baby Dragon": 4,
    "Valkyrie": 4,
    "Minions": 3,
    "Tombstone": 3
}
# Sample deck data per arena and elixir level (expand this as needed)
deck_database = {
    "Arena 1": {
        "Low": [["Knight", "Archers", "Goblins", "Spear Goblins", "Mini P.E.K.K.A", "Arrows", "Goblin Hut", "Fireball"]],
        "Medium": [["Giant", "Archers", "Mini P.E.K.K.A", "Musketeer", "Minions", "Fireball", "Arrows", "Goblin Hut"]],
        "High": [["Giant", "Arrows", "Goblin Hut", "Musketeer", "Mini P.E.K.K.A", "Fireball", "Goblin cage", "Goblins"]]

    },
    "Arena 2": {
        "Low": [["Knight", "Archers", "Bomber", "Minions", "Tombstone", "Fireball", "Arrows", "Spear Goblins"]],
        "Medium": [["Giant", "Valkyrie", "Mini P.E.K.K.A", "Bomber", "Minions", "Fireball", "Arrows", "Goblin Hut"]],
        "High": [["Giant", "Witch", "Baby Dragon", "Musketeer", "Valkyrie", "Fireball", "Tombstone", "Mini P.E.K.K.A"]]
    }
}

# GUI Setup
root = tk.Tk()
root.title("Clash Royale Deck Generator")
root.geometry("400x300")

# Arena Dropdown
tk.Label(root, text="Select Arena:").pack()
arena_var = tk.StringVar()
arena_menu = ttk.Combobox(root, textvariable=arena_var, values=list(deck_database.keys()))
arena_menu.pack()

# Elixir Dropdown
tk.Label(root, text="Select Elixir Level:").pack()
elixir_var = tk.StringVar()
elixir_menu = ttk.Combobox(root, textvariable=elixir_var, values=["Low", "Medium", "High"])
elixir_menu.pack()

# Output Area
output_text = tk.Text(root, height=8, width=50)
output_text.pack(pady=10)


# Generate Deck Function
def generate_deck():
    arena = arena_var.get()
    elixir = elixir_var.get()
    output_text.delete("1.0", tk.END)

    if arena and elixir:
        deck_list = deck_database.get(arena, {}).get(elixir, [])
        if deck_list:
            deck = random.choice(deck_list)
            output_text.insert(tk.END, "Generated Deck:\n" + ", ".join(deck))
        else:
            output_text.insert(tk.END, "No deck data available for this selection.")
    else:
        output_text.insert(tk.END, "Please select both arena and elixir level.")


# Generate Button
generate_button = tk.Button(root, text="Generate Deck", command=generate_deck)
generate_button.pack(pady=5)

root.mainloop()
