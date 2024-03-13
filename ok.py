# Constants
OPCODES = {
    "add": "0110011",
    "sub": "0110011",
    "sll": "0110011",
    "slt": "0110011",
    "sltu": "0110011",
    "xor": "0110011",
    "srl": "0110011",
    "or": "0110011",
    "and": "0110011",
    "lw": "0000011",
    "addi": "0010011",
    "sltiu": "0010011",
    "jalr": "1100111",
    "sw": "0100011",
    "beq": "1100011",
    "bne": "1100011",
    "bge": "1100011",
    "bgeu": "1100011",
    "blt": "1100011",
    "bltu": "1100011",
    "auipc": "0010111",
    "lui": "0110111",
    "jal": "1101111",
    "mul": "0110011",
    "rst": "1111111",
    "halt": "1111111",
    "rvrs": "1111111"
}

REGISTERS = {
    "zero": "00000",
    "ra": "00001",
    "sp": "00010",
    "gp": "00011",
    "tp": "00100",
    "t0": "00101",
    "t1": "00110",
    "t2": "00111",
    "s0/fp": "01000",
    "s1": "01001",
    "a0": "01010",
    "a1": "01011",
    "a2": "01100",
    "a3": "01101",
    "a4": "01110",
    "a5": "01111",
    "s2": "10000",
    "s3": "10001",
    "s4": "10010",
    "s5": "10011",
    "s6": "10100",
    "s7": "10101",
    "s8": "10110",
    "s9": "10111",
    "t3": "11000",
    "t4": "11001",
    "t5": "11010",
    "t6": "11011"
}

def decimal_to_binary(decimal):
    binary = bin(decimal & 0xFFFFFFFF)[2:]  
    return '0' * (32 - len(binary)) + binary  

def parse_instruction(line):
    parts = line.strip().split()
    opcode = parts[0]
    operands = parts[1:]
    return opcode, operands

def encode_register(reg_name):
    if reg_name in REGISTERS:
        return REGISTERS[reg_name]
    else:
        raise ValueError(f"Invalid register name: {reg_name}")

def encode_immediate(imm):
    imm_bin = bin(int(imm))[2:].zfill(12)
    if len(imm_bin) > 12:
        raise ValueError("Immediate value out of bounds")
    return imm_bin

def assemble(input_file, output_file, error_file):
    try:
        with open(input_file, 'r') as f:
            assembly_instructions = f.readlines()

        binary_instructions = []
        pc = 0
        labels = {}

        for line_num, instruction in enumerate(assembly_instructions, start=1):
            instruction = instruction.strip()
            if instruction.endswith(":"):
                labels[instruction[:-1]] = pc
            elif instruction:
                pc += 1

        pc = 0
        for line_num, instruction in enumerate(assembly_instructions, start=1):
            instruction = instruction.strip()
            if not instruction or instruction.endswith(":"):
                continue

            opcode, operands = parse_instruction(instruction)

            if opcode in OPCODES:
                binary_instruction = OPCODES[opcode]

                if opcode in ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and", "mul"]:
                    if len(operands) != 3:
                        raise ValueError(f"Invalid number of operands for {opcode} instruction")
                    for operand in operands:
                        binary_instruction += encode_register(operand)
                # Other cases omitted for brevity...

                binary_instructions.append(binary_instruction)
                pc += 1
            else:
                error_message = f"Error: Unsupported instruction '{opcode}' at line {line_num}\n"
                with open(error_file, 'w') as ef:
                    ef.write(error_message)
                return

        with open(output_file, 'w') as f:
            for binary_instruction in binary_instructions:
                f.write(binary_instruction + '\n')

    except FileNotFoundError:
        with open(error_file, 'w') as ef:
            ef.write("Error: File not found.\n")
    except PermissionError:
        with open(error_file, 'w') as ef:
            ef.write("Error: Permission denied.\n")

# Adjust file paths as needed for your WSL environment
assemble(r"path\to\input.asm", r"path\to\output.bin", r"path\to\error.txt")
