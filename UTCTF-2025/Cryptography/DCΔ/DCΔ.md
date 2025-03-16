- [DCΔ](#dcδ)
  - [Problem Link](#problem-link)
  - [Solution](#solution)
  - [Insights](#insights)
  - [Reference](#reference)
  - [FLAG](#flag)
---

# DCΔ
## Problem Link
<a href="https://utctf.live/challenges#DC%CE%94-2" target="_blank">DCΔ</a>
<br />
<br />

## Solution
<img src="https://github.com/user-attachments/assets/072eda33-49ee-4bbf-b0e8-1998075acd9a" width="50%"><br />
Download the attached file (`rsa.txt`).<br />
<br />
<br />

<img src="https://github.com/user-attachments/assets/e3fde5be-9494-47a7-8bd0-6a9b507f53a4" width="100%">
<img src="https://github.com/user-attachments/assets/083c4f56-7c8d-48e3-9214-5fce77a60a92" width="100%">

```
$ file rsa.txt
```
```
$ cat rsa.txt
```
Opening `rsa.txt` shows typical RSA-encrypted data. Decrypting it with a Python script yields readable output.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/5a929bcd-58c5-407f-8c99-2513a3915b58" width="100%">

```
$ vi solve.py
```
```
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
```
```
$ python3 solve.py
```
Decryption with the above script reveals the flag.<br />
<br />
<br />


## Insights
- 
<br />
<br />

## Reference
- 
<br />
<br />

## FLAG
utflag{th3_t0t13nt_funct10n_uns1mpl1f13d}