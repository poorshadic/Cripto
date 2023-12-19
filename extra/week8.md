# Criptografia Aplicada 2023/2024
# Tutorial 8 - extra


## 1 - Man-in-the-Middle

Start by analysing the code for Alice and Bob, what are they using to communicate?

How can we subvert this mechanism to be more. . . convenient?

## 2 - ECC
### Question - P1:

 O algoritmo de verificação funciona corretamente para mensagens corretamente assinadas (Assinada de facto pelo o dono da chave privada).
 Verificou-se:

 Para se verificar a assinatura utiliza-se:

 $m = σ + k · pk_{A}$ 

 Assim sendo, e se

 $pk_{A} = sk_{A}.G$
 $σ = m - k.sk_{A}.G$

Substitui-se:

$m = m - k.sk_{A}.G + k · sk_{A}.G$ 

Obtem-se que:

$m = m$ 

### Question - P2:

## 3 - Post-quantum Cryptography 

### Question - P1:

### Question - P2:

