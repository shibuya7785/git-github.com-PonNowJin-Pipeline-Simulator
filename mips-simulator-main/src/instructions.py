class InstructionSet:

    @staticmethod
    def add(rs_value, rt_value):
        """Perform addition."""
        return rs_value + rt_value

    @staticmethod
    def sub(rs_value, rt_value):
        """Perform subtraction."""
        return rs_value - rt_value

    @staticmethod
    def lw(base_address, offset):
        """Compute memory address for load word."""
        return base_address + offset

    @staticmethod
    def sw(base_address, offset):
        """Compute memory address for store word."""
        return base_address + offset

    @staticmethod
    def beq(rs_value, rt_value):
        """Check if branch condition is met."""
        return rs_value == rt_value

    @staticmethod
    def and_op(rs_value, rt_value):
        """Perform bitwise AND."""
        return rs_value & rt_value

    @staticmethod
    def or_op(rs_value, rt_value):
        """Perform bitwise OR."""
        return rs_value | rt_value

class ControlSignals:
    """
    Helper class for managing control signals for instructions.
    """

    @staticmethod
    def get_signals(opcode):
        """
        Return the control signals based on the opcode.
        """
        signals = {
            'add': {'RegDst': 1, 'ALUSrc': 0, 'Branch': 0, 'MemRead': 0, 'MemWrite': 0, 'RegWrite': 1, 'MemtoReg': 0},
            'sub': {'RegDst': 1, 'ALUSrc': 0, 'Branch': 0, 'MemRead': 0, 'MemWrite': 0, 'RegWrite': 1, 'MemtoReg': 0},
            'lw':  {'RegDst': 0, 'ALUSrc': 1, 'Branch': 0, 'MemRead': 1, 'MemWrite': 0, 'RegWrite': 1, 'MemtoReg': 1},
            'sw':  {'RegDst': 'X', 'ALUSrc': 1, 'Branch': 0, 'MemRead': 0, 'MemWrite': 1, 'RegWrite': 0, 'MemtoReg': 'X'},
            'beq': {'RegDst': 'X', 'ALUSrc': 0, 'Branch': 1, 'MemRead': 0, 'MemWrite': 0, 'RegWrite': 0, 'MemtoReg': 'X'},
            'and': {'RegDst': 1, 'ALUSrc': 0, 'Branch': 0, 'MemRead': 0, 'MemWrite': 0, 'RegWrite': 1, 'MemtoReg': 0},
            'or':  {'RegDst': 1, 'ALUSrc': 0, 'Branch': 0, 'MemRead': 0, 'MemWrite': 0, 'RegWrite': 1, 'MemtoReg': 0},
        }
        return signals.get(opcode, None)

class InstructionParser:
    """
    Parses instructions into their components.
    """

    @staticmethod
    def parse(instruction):
        """
        Parse a string instruction into components: opcode, operands, and immediate values.
        """
        parts = instruction.replace(",", "").replace("(", " ").replace(")", "").split()
        opcode = parts[0]
        operands = []
        immediate = 0

        if opcode in ["lw", "sw"]:  # I-type: lw $rt, imm($rs) / sw $rt, imm($rs)
            rt = int(parts[1][1:])
            imm = int(parts[2])
            rs = int(parts[3][1:])
            operands = [rs, rt]
            immediate = imm

        elif opcode in ["add", "sub", "and", "or"]:  # R-type: add $rd, $rs, $rt
            rd = int(parts[1][1:])
            rs = int(parts[2][1:])
            rt = int(parts[3][1:])
            operands = [rs, rt, rd]

        elif opcode == "beq":  # I-type: beq $rs, $rt, imm
            rs = int(parts[1][1:])
            rt = int(parts[2][1:])
            imm = int(parts[3])
            operands = [rs, rt]
            immediate = imm

        return opcode, operands, immediate
