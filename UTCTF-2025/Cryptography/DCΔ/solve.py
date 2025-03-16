from sympy import factorint, isprime

def main():
    # Read 'rsa.txt' file
    with open("rsa.txt", "r") as f:
        lines = f.read().strip().splitlines()

    # Extract integer values for n, e, c
    n_line = lines[0]
    e_line = lines[1]
    c_line = lines[2]

    n = int(n_line.split('=')[1].strip())
    e = int(e_line.split('=')[1].strip())
    c = int(c_line.split('=')[1].strip())

    print("[*] Factoring n. This process can take a long time if n is large.")

    # Factor n into primes using sympy
    factors = factorint(n)
    print("[*] factorint result:", factors)

    # Two common scenarios in CTF RSA problems:
    # 1) n = p * q, two distinct primes
    # 2) n = p^2, a single prime squared
    # If factorint returns something else, manual checks or adjustments are needed.
    
    # Flatten factor results into a list of (prime, exponent)
    factor_items = list(factors.items())

    if len(factor_items) == 1:
        # e.g. {p: 2}  ==> n = p^2
        p, exp = factor_items[0]
        if exp == 2 and isprime(p):
            # Then q = p
            q = p
            print("[*] Detected form n = p^2")
        else:
            print("[!] factorint shows a single prime factor but exponent != 2, or p not prime.")
            return
    elif len(factor_items) == 2:
        # e.g. {p: 1, q: 1} ==> n = p*q
        # or in some rare case, {p: 1, q: 2}, etc. (then manual check needed)
        # Let's assume the simplest case for typical RSA (p^1, q^1).
        primes = []
        for prime, exp in factor_items:
            if not isprime(prime) or exp != 1:
                print("[!] One of the factors is not prime or exponent != 1.")
                return
            primes.append(prime)
        if len(primes) == 2:
            p, q = primes[0], primes[1]
            print("[*] Detected form n = p*q")
        else:
            print("[!] factor count suggests more than two prime factors or exponents.")
            return
    else:
        print("[!] factorint returned an unexpected factor structure.")
        return

    # Compute phi(n)
    if p == q:
        # n = p^2 => phi(n) = p*(p-1)
        phi_n = p * (p - 1)
    else:
        # n = p*q => phi(n) = (p-1)*(q-1)
        phi_n = (p - 1) * (q - 1)

    # Compute d = e^-1 mod phi(n)
    d = pow(e, -1, phi_n)

    # Decrypt c
    m = pow(c, d, n)

    # Convert decrypted integer to bytes
    msg_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')

    # Try decoding the bytes as UTF-8 text
    try:
        plaintext = msg_bytes.decode('utf-8', errors='replace')
    except:
        plaintext = str(msg_bytes)

    print("[*] Decryption complete. Plaintext is:")
    print(plaintext)

if __name__ == "__main__":
    main()

