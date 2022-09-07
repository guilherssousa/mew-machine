import sys, os, random

# Stuff to get the Savefile
PWD = os.getcwd()
SAVE_FILE_PATH = sys.argv[1]

FINAL_PATH = os.path.join(PWD, SAVE_FILE_PATH)

# Useful Memory Addresses
POKEMON_PARTY_AMOUNT_ADDRESS = 0x2F2C

POKEMON_PARTY_SPECIES_ID_START = 0x2F2D

POKEMON_PARTY_OFFSET_START = 0x2F34
POKEMON_PARTY_OFFSET = 0x2C

POKEMON_TRAINER_NAME_START = 0x303C
POKEMON_NICKNAME_START = 0x307E
POKEMON_TRAINER_AND_NICK_NAME_MAX_SIZE = 0xB

CHECKSUM_BLOCK_START = 0x2598
CHECKSUM_BLOCK_END = 0x3523

CAUGHT_OFFSET_START = 0x25A3
SEEN_OFFSET_START = 0x25B6
CAUGHT_SEEN_SIZE = 0x13

# Other useful stuff
END_CHARACTER = 0x50

def ask_for_permission():
    print("This script will modify your save file progress. Are you sure you want to continue? (y/n)", end=" ")
    answer = input()
    if(answer == "y"):
        return True
    return False

def set_caught_or_seen_pokemon_bit(captured_or_seen, entry):
    byte = entry // 8
    bit = entry % 8

    captured_or_seen[byte] |= 1 << bit

    return captured_or_seen

def calculate_checksum(ram):
    checksum = 0xff

    for c in ram[CHECKSUM_BLOCK_START:CHECKSUM_BLOCK_END]:
        checksum -= c

    return checksum

# Input: B0 A5 24 FF 00 00 00
# Output: B0 A5 24 15 FF 00 00
def add_entry_id(amount, bytes, entry):
    for index in range(len(bytes)):
        if(bytes[index] == 0xff):
            bytes[index] = entry
            if(index+1 < len(bytes)):
                bytes[index+1] = 0xff
                break
    return bytes

def generate_mew_data():
    specie_id = 0x15

    trainer_id = random.randint(0x0, 0xffff)

    # split 2byte player id into 2 1byte values
    trainer_id_high = trainer_id >> 0x8
    trainer_id_low = trainer_id & 0xff

    pokemon_struct = [
        # Index number of the Species	
        specie_id,
        # Current HP
        0x00,
        0x19,
        # Level
        0x05,
        # Status condition
        0x00,
        # Type 1
        0x18,
        # Type 2
        0x18,
        # Catch rate/Held item
        0x53,
        # Index number of move 1
        0x01,
        # Index number of move 2
        0x00,
        # Index number of move 3
        0x00,
        # Index number of move 4
        0x00,
        # Original Trainer ID number
        trainer_id_high,
        trainer_id_low,
        # Experience points
        0x00,
        0x00,
        0x87,
        # HP EV data
        0x00,
        0x00,
        # Attack EV data
        0x00,
        0x00,
        # Defense EV data
        0x00,
        0x00,
        # Speed EV data
        0x00,
        0x00,
        # Special EV data
        0x00,
        0x00,
        # IV data
        0xa1,
        0xc5,
        # Move 1's PP values
        0x23,
        # Move 2's PP values
        0x00,
        # Move 3's PP values
        0x00,
        # Move 4's PP values
        0x00,
        # Level
        0x05,
        # Maximum HP
        0x00,
        0x19,
        # Attack
        0x00,
        0x10,
        # Defense
        0x00,
        0x0f,
        # Speed
        0x00,
        0x10,
        # Special
        0x00,
        0x0f
    ]

    original_trainer_name = bytearray([0x98, 0x8e ,0x92, 0x87, 0x88, 0x91, 0x80, 0x50, 0x0, 0x0, 0x0])

    pokemon_name = bytearray([0x8c, 0x84, 0x96, 0x50, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])

    return [specie_id, pokemon_struct, original_trainer_name, pokemon_name]

def main():

    print("""
,--.   ,--.,------.,--.   ,--.    ,--.   ,--.  ,---.   ,-----.,--.  ,--.,--.,--.  ,--.,------. 
|   `.'   ||  .---'|  |   |  |    |   `.'   | /  O  \ '  .--./|  '--'  ||  ||  ,'.|  ||  .---' 
|  |'.'|  ||  `--, |  |.'.|  |    |  |'.'|  ||  .-.  ||  |    |  .--.  ||  ||  |' '  ||  `--,  
|  |   |  ||  `---.|   ,'.   |    |  |   |  ||  | |  |'  '--'\|  |  |  ||  ||  | `   ||  `---. 
`--'   `--'`------''--'   '--'    `--'   `--'`--' `--' `-----'`--'  `--'`--'`--'  `--'`------' 

Mew Machine Script v1.0
A tool to generate a nearly-legit YOSHIRA Mew in your Pokemon Red/Blue/Yellow save file.
We recommend you to backup your game progress before trying this tool.
This is not a official or licensed Nintendo product.
Built by guilherssousa https://github.com/guilherssousa"
    """)

    if not ask_for_permission():
        return

    if(os.path.exists(FINAL_PATH) == False):
        print("Error: File does not exist. Please use a relative path.")
        return
    
    with open(FINAL_PATH, 'rb+') as f:
        ram = bytearray(f.read())
        
        # Get the amount of pokemon in the party
        if(ram[POKEMON_PARTY_AMOUNT_ADDRESS] > 0x5):
            print("Error: Pokemon party is full. Please deposit a pokemon on your PC before trying again!!")
            return
        
        # Get the data for the mew
        mew_specie_id, mew_pokemon_struct, mew_original_trainer_name, mew_pokemon_name = generate_mew_data()

        next_available_party_slot = POKEMON_PARTY_OFFSET_START + (ram[POKEMON_PARTY_AMOUNT_ADDRESS] * POKEMON_PARTY_OFFSET)

        # Write the pokemon data to the save file
        ram[next_available_party_slot:next_available_party_slot+POKEMON_PARTY_OFFSET] = mew_pokemon_struct

        # Get writting offsets
        original_trainer_name_offset = POKEMON_TRAINER_NAME_START + (ram[POKEMON_PARTY_AMOUNT_ADDRESS] * POKEMON_TRAINER_AND_NICK_NAME_MAX_SIZE)
        new_prokemon_name_offset = POKEMON_NICKNAME_START + (ram[POKEMON_PARTY_AMOUNT_ADDRESS] * POKEMON_TRAINER_AND_NICK_NAME_MAX_SIZE)

        # Increase the amount of pokemons on the party by 1
        ram[POKEMON_PARTY_AMOUNT_ADDRESS] = ram[POKEMON_PARTY_AMOUNT_ADDRESS] + 0x1

        # Write the pokemon entry to party entry id list
        ram[POKEMON_PARTY_SPECIES_ID_START:POKEMON_PARTY_SPECIES_ID_START+0x6] = add_entry_id(ram[POKEMON_PARTY_AMOUNT_ADDRESS], ram[POKEMON_PARTY_SPECIES_ID_START:POKEMON_PARTY_SPECIES_ID_START+0x6], mew_specie_id)

        # Write the original trainer name to the save file
        ram[original_trainer_name_offset:original_trainer_name_offset+POKEMON_TRAINER_AND_NICK_NAME_MAX_SIZE] = mew_original_trainer_name

        # Write the pokemon name to the save file
        ram[new_prokemon_name_offset:new_prokemon_name_offset+POKEMON_TRAINER_AND_NICK_NAME_MAX_SIZE] = mew_pokemon_name

        # Write Mew encounter to Pokedex
        ram[CAUGHT_OFFSET_START:CAUGHT_OFFSET_START+CAUGHT_SEEN_SIZE] = set_caught_or_seen_pokemon_bit(ram[CAUGHT_OFFSET_START:CAUGHT_OFFSET_START+CAUGHT_SEEN_SIZE], 151-1)
        ram[SEEN_OFFSET_START:SEEN_OFFSET_START+CAUGHT_SEEN_SIZE] = set_caught_or_seen_pokemon_bit(ram[SEEN_OFFSET_START:SEEN_OFFSET_START+CAUGHT_SEEN_SIZE], 151-1)

        print("Generating new checksum...")
        ram[CHECKSUM_BLOCK_END] = calculate_checksum(ram) & 0xff # Patch the save file to avoid integrity issues

        f.seek(0,0)
        f.write(ram)

        print("Congratulations! You got the Lvl. 5 Mythical Pokémon Mew!")

if __name__ == '__main__':
    main()