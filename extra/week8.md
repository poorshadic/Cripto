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
Para desenvolver algoritmos criptográficos pós-quânticos, não é necessário tirar partido da computação quântica. Isto verifica-se, uma vez que, quando se fala de quantum computation refere-se, neste caso, ao estudo e desenvolvimento de algoritmos que possam ser executados em computadores quânticos e tirar proveito das suas capacidades respondendo a problemas que computadores não quânticos não dão resposta. Por outro lado, a post-quantum cryptography refere-se ao desenvolvimento de algoritmos que sejam seguros contra ataques feitos por computadores quânticos, um dos exemplos é o algoritmo Shor que pode resolver muitos algoritmos/mecanismos criptográficos, e por isso existe a necessidade de se desenvolver e utilizar post-quantum cryptography

### Question - P2:
A técnica de ataque mencionada Store-now-decrypt-later consiste em roubar dados encriptados de organizações, plataformas (etc.) apesar de não existirem meios para os desencriptarem atualmente, e armazená-los para que mais tarde, quando os computadores quânticos se tornarem mais potentes, serem desencriptados.
Esta técnica de ataque representa uma grande ameaça para todos os sistemas atuais de encriptação e todos os dados uma vez que será apenas uma questão de tempo até que estes estejam disponíveis para todos.

