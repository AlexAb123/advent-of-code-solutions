from pathlib import Path

def solve():

    packet = bin(int(Path(__file__).with_name('day_16_input.txt').open('r').read().strip(), 16))[2:]

    def parse_literal_packet(binary):

        binary = binary[6:] # Remove version and type_id
        packet_length = 6 # 3 from version, 3 from type_id
        value = binary[1:5]
        while binary[0] == "1":
            binary = binary[5:]
            packet_length += 5
            value += binary[1:5]
        binary = binary[5:]
        packet_length += 5
        value = int(value, 2)
        return value, packet_length, binary
    
    part1 = 0
    def parse_packet(binary, packets_left, bits_left):

        if packets_left == 0 and bits_left == 0:
            return
        
        print(binary)
        if len(binary) == 0:
            return
        nonlocal part1
        version = int(binary[0:3], 2)
        part1 += version
        type_id = int(binary[3:6], 2)
        packet_length = 6
        binary = binary[6:]
        print(version, type_id, binary)

        if type_id == 4: # Literal Packet
            value = binary[1:5]
            while binary[0] == "1":

                binary = binary[5:]
                packet_length
                value += binary[1:5]
            binary = binary[5:]
            value = int(value, 2)

            parse_packet(binary)

        else: # Operator Packet
            length_type_id = int(binary[0], 2)
            binary = binary[1:]

            if length_type_id == 0: # Next 15 bits represents the total length in bits of the sub-packets contained by this packet.
                sub_packets_length = int(binary[:15], 2)
                binary = binary[15:]
                parse_packet(binary)

            elif length_type_id == 1: # Next 11 bits represents the number of sub-packets immediately contained by this packet.
                sub_packets_num = int(binary[:11], 2)
                binary = binary[11:]
                parse_packet(binary)

    parse_packet(packet)
    print(part1)
solve()