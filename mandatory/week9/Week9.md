# Criptografia Aplicada 2023/2024
# Tutorial 9 - Public-key Infrastructure (PKI) Lab

## Task 1 - Becoming a Certificate Authority (CA)
What part of the certificate indicates this is a CA’s certificate?

quando utilzamos o comando 'openssl x509 -in ca.crt -text -noout', temos um linha na data com :
"CA:TRUE"


![week9_1](https://github.com/poorshadic/Cripto/blob/main/mandatory/week9/ex1/ficha10_1.png)

-----------------------------------
What part of the certificate indicates this is a self-signed certificate?
pelo facto de que na data do certificado o
'Issuer: CN' ser igual a 'Subject: CN' com valor :
'www.modelCA.com, O = Model CA LTD., C = US'

![week9_2](https://github.com/poorshadic/Cripto/blob/main/mandatory/week9/ex1/ficha10_2.png)
--------------------------------------

In the RSA algorithm, we have a public exponent e, a private exponent d, a modulus n, and two secret numbers p and q, such that n = pq. Please identify the values for these elements in your certificate and key files.
(tudo em scrren shot)
apos executar o comando 'openssl x509 -in ca.crt -text -noout' conseguimos os valores desses dados como é possivel ver nas imagens seguintes

![week9_e_d](https://github.com/poorshadic/Cripto/blob/main/mandatory/week9/ex1/e_d.png)
![week9_n](https://github.com/poorshadic/Cripto/blob/main/mandatory/week9/ex1/n.png)
![week9_primes](https://github.com/poorshadic/Cripto/blob/main/mandatory/week9/ex1/primes.png)


## Task 2: Generating a Certificate Request for Your Web Server
para gerar um CSr com 2 subdominios:
![task2](https://github.com/poorshadic/Cripto/blob/main/mandatory/week9/ex2/task2_0.png)

executando o comando openssl req -in server.csr -text -noout conseguimos os dados como signature algorithm, primos, modulo e restantes ficam associados aos 3 subdominios

![task2_1](https://github.com/poorshadic/Cripto/blob/main/mandatory/week9/ex2/task2.png)

## Task 3: Generating a Certificate for your server
para gerar o certificado (server.csr) a partir de ca.crt e ca.key:
openssl ca -config newopenssl.cnf -policy policy_anything \
-md sha256 -days 3650 \
-in server.csr -out server.crt -batch \
-cert ca.crt -keyfile ca.key


depois utilizando o comando "openssl x509 -in server.crt -text -noout"
para alem de dados semelhantes aqueles que conseguimos nos exercicios anteriores é importante notar
que na X509v3 Subject Alternative Name aparecem os 3 dominios anterormente adicionados mostrando que o
certificado fica valido para qualquer um deles

![task3](https://github.com/poorshadic/Cripto/blob/main/mandatory/week9/ex3/task3_2.png)

## Task 4: Deploying Certificate in an Apache-Based HTTPS Website
foi definido um tiago2023_apache_ssl.conf:
<VirtualHost *:443>
DocumentRoot /var/www/bank32
ServerName www.tiago2023.com
ServerAlias www.tiago2023A.com
ServerAlias www.tiago2023B.com
DirectoryIndex index.html
SSLEngine On
SSLCertificateFile /certs/tiago2023.crt 
SSLCertificateKeyFile /certs/tiago2023.key 
</VirtualHost>

depois copiamos os server.crt e server.key para o diretorio /certs dando-lhes rename para com base na configuraçao acima
ex. cp server.crt /certs/tiago2023.crt


depois iniciamos o site com:
$a2ensite tiago2023_apache_ssl.conf
$service apache2 start


conseguindo uma pagina de acesso nao seguro
![task4_1](https://github.com/poorshadic/Cripto/blob/main/mandatory/week9/ex4/task4_1.png)

sendo preciso ir ao gestor de certificados do browser em questao para adicionar o certificado gerado anteriormente para conseguir um acesso que o browser considerase seguro

![task4_2](https://github.com/poorshadic/Cripto/blob/main/mandatory/week9/ex4/task4_3.png)


## Task 5: Launching a Man-In-The-Middle Attack

## Task 6: Launching a Man-In-The-Middle Attack with a Compromised CA
