#### Project 1 -SIO

## Index
1. Introdução<br>
2. Vunerabilidades<br>
- CWE - 89<BR>
- CWE - 79<BR>
- CWE - 862<BR>
- CWE - 20<BR>
- CWE - 200<BR>
- CWE - 256<BR>
- CWE - 756<BR>
3. Conclusão

## Introdução
No nosso projeto foi desenvolvido um website de uma loja online que vende exclusivamente produtos alusivos DETI.
Dentro do mesmo é possivel criar-se um utilizador e fazer login com o mesmo, pode ainda adicionar os seus produtos preferidos a uma lista de favoritos assim como adicionalos diretamente ao carrinho de compras.<br>
Para implementar este site foi usado com base uma aplicação em flask com base em paginas de html e uma base de dados em SQLite.<br>
Para satisfazer os requesitos do trabalho que nos foi entregue foram criadas duas versões da aplicação,a app.py é a versão que foi sujeita a vários ataques provocados propositamente para mostrar as suas vunerabilidades, já a app_sec.py é uma app que foi desenolvida de modo a ser segura sobre todos os ataques feitos no primeiro caso.<br>

## Vunerabilidades
Foram escolhidas entre as inumeras possibilidades 7 CWE's para explorar neste trabalho entre elas estão:

### CWE-89
A CWE-89,comumente conhecida como "SQL-Injection",é uma vunerabilidade bastante comum caracterizada pela neutralização imprópria de elementos especias usados em comandos SQL.<br>
Os danos potenciais causados por SQLI são roubo de informação armazenada na base de dados ou remoção/alteração de conteúdo essencial das mesmas.

## CWE-79
A CWE-79,comumente conhecida como "Cross-site Scripting",é caracterizada pela neutralização imprópria dos comandos de input feitos pelo utilizador antes deste se tornar em um output que pode ser usado/consultado por outros utilizadores.

## CWE-862
A CWE-862,esta venurabilidade verifica-se quando o servidor não verifica se o usuario tem ou não permissão para fazer determinadas ações.<br>
Esta falta de cuidado pode levar a que qualquer usuario mal intensionado aceda,altere ou divulgue informação privada.

## CWE-20

## CWE-200
A CWE-200, esta vunerabilidade verifica-se quando o servidor expõe informção sensivel a utilizadores não autorizados a recebela.<br>

## CWE-256
A CWE-256,esta vunerabilidade refere-se ao armazenamento de passwords em texto simples na database.

## CWE-756
A CWE-756,esta vunerabilidade refere-se à falta de uma página de error própria do servidor.<br>
Quando esta página não é implementada a página que é mostrada aos utilizadores é default e contém informação sensivel que pode ser usada contra o servidor em questão.



