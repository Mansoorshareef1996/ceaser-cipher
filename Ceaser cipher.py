import sys

def open_infile(filename):
    """
    Open the data file for reading
    :return: File handle of the file
    """
    try:
        return open(filename, "r")
    except IOError:
        sys.stderr.write("Failed to open " + filename)
        exit(1)


def new_position(c, shift, key):
    """
    Shift a character and obtain the replacement of the character
    :param c: Character to shift
    :param shift: Number of times to rotate
    :param key: Where to map the substituted letter
    :return: Nothing
    """
    # Check that the character is an alphabet, otherwise we won't do shifting
    if not c.isalpha():
        return c

    # Do first shifting, we rotate the value based on the number of shifts
    # Convert the character to 0 to 26 in ascii
    if shift > 26:
        shift = shift % 26
    elif shift < 0:
        shift = -(abs(shift) % 26)

    encrypted_c = (ord(c.upper()) - ord("A")) + shift

    # Adjust the value based on the first shift
    if encrypted_c > 26:
        encrypted_c = encrypted_c - 26
    elif encrypted_c < 0:
        encrypted_c = 26 + encrypted_c

    encrypted_c = key[encrypted_c % len(key)]

    if c.islower():
        encrypted_c = encrypted_c.lower()

    return encrypted_c


def encodeCaesarCipher(line, shift, key):
    """
    Encrypt a line of text using caesar cipher and substitution
    :param line: Line to be encrypted
    :param shift: Shift value to rotate data
    :param key: Key for substitution
    :return: None
    """
    encrypted_line = ""

    for c in line:
        encrypted_line += new_position(c, shift, key)

    print(encrypted_line, end="")


def process_infile(shift, key):
    """
    Encrypt a file
    :param shift: Shift value rotate data
    :param key: Key for for substitution
    :return: Nothing
    """
    file = open_infile("prog3.d2")

    for line in file:
        encodeCaesarCipher(line, shift, key)


def main():
    """
    Entry point of the program.
    :return: None
    """

    while True:
        try:
            # Read a pair of values shift and key from the input
            tokens = input().split()
            key = tokens[0]
            shift = int(tokens[1])

            print("key, shift = " + key + ", " + str(shift))
            print("----------------------------------------------------------------")

            # Use the shift and key to encrypt a file
            if len(key) > 26:
                key = key[:-(len(key) - 26)]

            key = key.upper()
            process_infile(shift, key)

            print("\n----------------------------------------------------------------")
            print()
        except EOFError:
            break


main()
