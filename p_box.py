#19_05_2023
#допоміжні функції для переведення числа в рядок бітів
def int_to_bit_list(x):
    B = []
    while x!=0:
        B = [x & 1] + B
        x >>= 1
    return B

def bit_list_to_int(B):
    x = 0
    for b in B:
        x = (x << 1) | b 
    return x 
#######################################################


def p_box(P: list[int], B: list[int]) -> list[int]:
    '''    
    P: permutation rule
    B: array of bits
    '''
    B = [B[i - 1] for i in P]
    return B


def reverse_p_box(P: list[int], x: list[int]) -> list[int]:
    '''    
    P: permutation rule
    B: array of bits
    '''
    r = [None]*len(x)
    for idx, val in enumerate(P):
        r[val-1] = x[idx]
    return r

P = [3, 1, 4, 2]

if __name__ == "__main__":
    a = [0, 1, 1, 0]
    print("Before transformation: ", a)

    cipher_a = p_box(P, a)
    print("After transformation: ", cipher_a)
    
    b = reverse_p_box(P, cipher_a)
    print("Retransformatio: ", b)
    
    print(b == a)
