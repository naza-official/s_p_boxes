#19_05_2023

"Substitution table"
S_TABLE = [
            [(0, 0, 1, 1), (0, 0, 0, 0), (1, 0, 1, 1), (0, 1, 0, 1)],
            [(1, 0, 0, 0), (0, 1, 0, 0), (0, 1, 1, 1), (0, 0, 1, 0)],
            [(1, 1, 1, 1), (1, 1, 0, 0), (0, 1, 1, 0), (1, 1, 1, 0)],
            [(1, 1, 1, 1), (0, 0, 0, 1), (1, 0, 1, 0), (1, 1, 0, 1)]
        ]
            
"dict for better access to substitution table"
IDXS = {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3}
 

def s_box(bit_stream: list[int]) -> list[int]:
    "s_box algorithm"
    if len(bit_stream)%4 != 0: bit_stream += [0] * (4 - len(bit_stream)%4)
    l = len(bit_stream)
    p = 0
    for i in range(4, l+1, 4):
        bit_stream[p:i] = S_TABLE[IDXS[tuple(bit_stream[p:p+2])]][IDXS[tuple(bit_stream[i-2: i])]]
        p = i
    return bit_stream


def reverse_s_box(bit_stream: list[int]) -> list[int]:
    "backward IDXS list"
    backward = {value: key for key, value in IDXS.items()}
    
    "reverse substitution table"
    reverse_table = {}
    for row_idx, row in enumerate(S_TABLE):
        for col_idx, entry in enumerate(row):
            reverse_table[entry] = (row_idx, col_idx)
    
    "reverse algorithm"
    res = []
    reversed_stream = [reverse_table[tuple(bit_stream[i:i+4])] for i in range(0, len(bit_stream), 4)]
    for i in reversed_stream:
        res += list(backward[i[0]]) + list(backward[i[1]])
    
    return res


if __name__ == "__main__":
    a = [1, 1, 0, 0, 1, 0, 0, 1]
    print("Before transformation: ", a)

    cipher_a = s_box(a.copy())
    print("After transformation: ", cipher_a)
    
    b = reverse_s_box(cipher_a)
    print("Retransformation: ", b)

    print(a == b)

    inp = list(map(int, input("Enter array of length 8 consisting of 1 or 0 and press Enter: ").split()))
    inp_cipher = s_box(inp)
    print("Encoded input: ", inp_cipher)
    print("Decoded input: ", reverse_s_box(inp_cipher))



    
