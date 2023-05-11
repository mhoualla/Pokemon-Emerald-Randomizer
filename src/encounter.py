import random
import struct 
import binascii

# GOAL: Randomize the wild encounters

with open('PokemonEmerald.gba', 'rb') as rom_file:
    rom_data = rom_file.read()

start_index = rom_data.index(binascii.unhexlify(b'FDBF')) + 2
end_offset = start_offset = start_index
while rom_data[end_offset:end_offset+2] != binascii.unhexlify(b'FDBF'):
    end_offset += 2
    
encounters_data = rom_data[start_offset:end_offset]

with open('emerald_encounters.bin', 'wb') as encounters_file:
    encounters_file.write(encounters_data)
    
with open('emerald_encounters.bin', 'rb') as encounters_file:
    data = encounters_file.read()
    for i in range(0, len(data), 12):
        offset = i + 2
        species = list(struct.unpack('6H', data[offset:offset+12]))
        new_species = [random.randint(1, 386) for _ in range(6)]
        data = data[:offset] + struct.pack('6H', *new_species) + data[offset+12:]

with open('emerald_randomized.gba', 'r+b') as f:
    f.seek(0x1B06B4)
    f.write(data)
