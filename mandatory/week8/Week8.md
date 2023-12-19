#Criptografia Aplicada 2023/2024
#Tutorial 8

## 1 - ElGamal

### a) (m1,m2) = (m1', m2') that Alice can recover the original plaintext. 

O objetivo é provar que $ (m_{1},m_{2}) = (m_{1}', m_{2}') $

Temos que:
$ m_{1}' = x_{t} ^{-1} c_{1} $
$ m_{2}' = y_{t} ^{-1} c_{2} $

Temos que: 
$c_{1} = x_{S}m_{1} $ -> resolver em ordem a $m_{1} -> m_{1} = x_{S}^{-1}c_{1}$
$c_{2} = y_{S}m_{1} $ -> resolver em ordem a $m_{1} -> m_{1} = y_{S}^{-1}c_{1}$

Considerando que:

$ Q_{A} = n_{A}P $
$ S = (x_{S},y_{S}) = kQ_{A} = kn_{A}P $
$ R = kP $
$ T = (x_{T}, y_{T}) = n_{A}R = n_{A}kP $

Então $ S = P = n_{A}kP$.

        $(x_{n_{A}kP}^{-1} c_{1}) $

### b) Three python methods that for a Elliptic Curve:

E : y2 = x3 + Ax + B, p prime, and P = (xP , yP ) ∈ E(Fp)
• GenPubKey(A, B, p, xP , yP ) generates the public key QA and the private key nA.
• Encript(A, B, p, xP , yP , QA, m1, m2) gererates the ciphertext (R, c1, c2).
• Decript(A, B, p, xP , yP , nA, R, c1, c2) recovers the value of m1, m2 back.