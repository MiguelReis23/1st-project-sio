#### Project 1 -SIO

## Index

1. Introdução

2. Vunerabilidades

- CWE - 89

- CWE - 79

- CWE - 307/862

- CWE - 20

- CWE - 200

- CWE - 620

- CWE - 756

3. Conclusão

## 1. Introdução

No nosso projeto foi desenvolvido um website de uma loja online que vende exclusivamente produtos alusivos DETI. 
Dentro do mesmo é possível criar-se um utilizador e fazer login com o mesmo, pode ainda adicionar os seus produtos preferidos a uma lista de favoritos assim como adiciona-los diretamente ao carrinho de compras. 
Para implementar este site foi usado com base uma aplicação em flask com base em paginas de html e uma base de dados em SQLite.<br> 
Para satisfazer os requisitos do trabalho que nos foi entregue foram criadas duas versões da aplicação, a app.py é a versão que foi sujeita a vários ataques provocados propositalmente para mostrar as suas vulnerabilidades, já a app_sec.py é uma app que foi desenvolvida de modo a ser segura sobre todos os ataques feitos no primeiro caso.<br> 

## 2. Vunerabilidades

Foram escolhidas entre as ínumeras possibilidades 7 CWE's para explorar neste trabalho entre elas estão:

## CWE-89

A CWE-89, comumente conhecida como "SQL-Injection", é uma vulnerabilidade bastante comum caracterizada pela neutralização imprópria de elementos especiais usados em comandos SQL.<br> 
Os danos potenciais causados por SQLI são roubo de informação armazenada na base de dados ou remoção/alteração de conteúdo essencial das mesmas. 

### Procedimento

Durante o processo de login se o atacante inserir um nome de utilizador correto, seguido de **' OR 1=1;--** no campo da password consegue entrar na conta do user que colocou sem ter na sua posse a password correta.<br>

![](https://cdn.discordapp.com/attachments/1158907841126604810/1170806582767009873/2023-11-05_19-24-43.mp4?ex=655a6199&is=6547ec99&hm=26b2c4affe83db7913303e15e6ee431e46c944de2d84a470b518f7f2746c2358&)<br>

## CWE-79

A CWE-79, comumente conhecida como "Cross-site Scripting", é caracterizada pela neutralização imprópria dos comandos de input feitos pelo utilizador antes deste se tornar em um output que pode ser usado/consultado por outros utilizadores.

## CWE-307/862

A CWE-862, esta venerabilidade verifica-se quando o servidor não verifica se o usuario tem ou não permissão para fazer determinadas ações.<br> 
Esta falta de cuidado pode levar a que qualquer usuário mal intencionado aceda, altere ou divulgue informação privada. 

## CWE-20

A CWE-20, esta vulnerabilidade verifica-se quando a API não faz a validação correta de dados que são introduzidos pelo utilizador do página web. 

## Procedimento
Ao adicionar um produto ao carrinho é dado ao utilizador um campo onde pode inserir a quantidade de unidades do produto é que este pretende comprar.
Como a API não faz a devida verificação do input "quantidade", esta permite ao utilizador inserir uma quantidade negativa de produtos o que faz com ao invés de pagar pelos produtos o atacante receba essa mesma quantia.

Um exemplo do que foi enunciadao:



## CWE-200

A CWE-200, esta vunerabilidade verifica-se quando o servidor expõe informção sensivel a utilizadores não autorizados a recebela.<br>

## Procedimento

Esta CWE é bastantes vezes aplicada conjuntamente com a CWE-89 (SQLI), pois no caso explorado no nosso site caso o utilizador erra-se a o nome de usuário no processo de login, era emitida a mensagem descritiva **"user does not exist."** , enquanto se o erro estivesse apenas na password a mensagem emitida será, **"Please check your login details and try again"**, ao ter mensagens de erro diferentes o site indiretamente dá a informação que aquele nome de usuário é válido.<br> 
Aliado com SQLI esta informação é suficiente para com que o atacante faça login no site. 

Erro está presente no seguinte seguimento de código:
```python
@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    result = db.session.execute(
        "SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "';").fetchall()
    

    user = User.query.filter_by(username=username).first()
    if not user:
        print('User does not exist.', 'error')
        return redirect(url_for('auth.login'))
    
    if not result:
        print('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    
    login_user(user)
    return redirect(url_for('main.index'))

```
## Correção
A correção do problema em cima enunciado pode ser feita alterando as mensagens as mensagens de erro apresentadas quando são introduzidos dados de login incorretos.<br>
Ao alterar as mensagem de erro para uma mais geral deixa-mos de dar ao atacante informação que poderá comprometer o site noutros aspetos.

Para uma versão segura atualizamos o código em cima:
```python
@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    

    user = User.query.filter_by(username=username).first()
    if not user:
        print('Please check your login details and try again')
        return redirect(url_for('auth.login'))
    
    if user.password != password:
        print('Please check your login details and try again')
        return redirect(url_for('auth.login'))
    
    login_user(user)
    return redirect(url_for('main.index'))
```

## CWE-620
A CWE-620,esta vulnerabilidade está presente quando a API permite a um utilizador atualizar a password sem precisar de introduzir a password que está a ser substituída. 

## CWE-756
A CWE-756, esta vulnerabilidade refere-se à falta de uma página de error própria do servidor.<br> 
Quando esta página não é implementada a página que é mostrada aos utilizadores é default e contém informação sensível que pode ser usada contra o servidor em questão.


## Procedimento
-----------------------------
## Correção
De modo a corrigir esta vunerabilidade deve ser criada uma página de erro default que não tenha qualquer informação relevante para um possivel atacante.

Para que a página mostrada na ocorrência de um erro seja a pretendida foi acrescentado o seguinte segmento de código na API.

```python
@app.errorhandler(404)
    def page_not_found(e):
        print(e)
        return render_template('404.html')
```
Assim a cada ocorrência de erro a página a ser mostrada será:<br>
![Alt text](/analysis/images/image.png)<br>

## 3. Conclusão



