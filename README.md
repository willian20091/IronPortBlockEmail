# IronPortBlockEmail

### Cisco IronPort C380 Block E-mail Script. 

# English

Hello everyone, my name is Willian Ferreira and I am here to share with the community a solution of a problem I faced at work.

This shell scripting queries a domain or sender in the blocked mailing list. he adds it to the list.

## Settings needed for this script to work.

* Need to create a private key on the server where the script will be.
* Create a user that will be used in the script.
* Add the public key that was generated on the IronPort C380 server as per tutorial https://somoit.net/ironport/ironport-automate-commands-scripts-from-linux

## Getting Started

For the operation of the script must be set as a parameter the email or domain that will be verified and blocked.

    ./blockEmail.sh test@test.com

## Variables

* SERVER = "IP / HOSTNAME"
* DOM = "$ (echo $ 1)"
* VAL = ""
* LIST = "blacklist"

#### SERVER

This variable must be added to the IronPort server IP or your network hostname.

#### DOM

This variable receives the value entered as a parameter in script execution.

#### VAL

This variable receives as a parameter the query return of the email or domain in the list.

#### LIST

This variable is named after the list to be consulted and changed.

## Function ValidityEmail ()

The code snippet below performs SSH access on the server and collects the list of emails and domains that are subscribed to the blacklist, and saves them all in a text file called <b> suspect.txt </b>

    ssh user @ $ SERVER "dictionaryconfig print $ LIST" >> suspect.txt

After that it validates if the command has any errors. If so, it returns an error message to the user.

If the command fails, it will do some actions on the file to remove unnecessary characters, after which it creates a new handled list called result.txt.

Then it will make the necessary comparisons to check if the email or domain to block is already registered, otherwise it calls <b> blockEmail () </b> to block it.

## Function blockEmail ()

The code snippet below performs SSH access on the server to add the email or domain to the blacklist, and then commits this action.

    ssh user @ $ SERVER "dictionaryconfig edit $ LIST new $ DOM; commit -y"

After that it validates if the command has been executed and notifies the user if it has been blocked or if an error has occurred.

## Final considerations.

Any doubt, I am available.

Feel free to send me a <b> poll request </b> to improve this code.

# Portugês Brasil

Olá Pessoal me chamo Willian Ferreira e estou aqui para compartilhar com a comunidade uma solução de um problema que enfrentei no trabalho.  

Este scrip desenvolvido em shell efetua a consulta de um domínio ou remetente na lista de e-mails bloqueados. ele realiza a adição do mesmo na lista. 

## Configurações necessárias para o funcionamento deste script. 

* Necessário criar uma chave privada no servidor onde ficará o script.
* Criar um usuário que será usado no script. 
* Adicionar a chave pública que foi gerada no servidor IronPort C380 conforme tutorial https://somoit.net/ironport/ironport-automate-commands-scripts-from-linux

## Informações iniciais

Para o funcionamento d script deve ser posto como parâmetro o e-mail ou domínio que será verificado e bloqueado.

    ./blockEmail.sh	test@test.com

## Variaveis

* SERVER = "IP/HOSTNAME"
* DOM = "$(echo $1)"
* VAL=""
* LIST= "blacklist"

#### SERVER

Está variável deve ser adicionado o IP do servidor do IronPort ou o seu hostname da rede. 

#### DOM

Está variável recebe o valor inserido como parâmetro na execução do script. 

#### VAL 

Está variável recebe como parâmetro o retorno da consulta do e-mail ou domínio na lista. 

#### LIST

Esta variável recebe o nome da lista que será consultada e alterada. 

## Função validadeEmail()

O trecho de código abaixo realiza o acesso via SSH no servidor e coleta a lista de e-mails e domínios que estão cadastrados na blacklist, e salva todos em um arquivo de texto chamado <b>suspect.txt</b>

	ssh user@$SERVER "dictionaryconfig print $LIST" >> suspect.txt 

Após isso ele valida se o comando apresentou algum erro. Caso sim ele retorna uma mensagem de erro para o usuário. 

Se o comando não apresentar erro ele irá fazer algumas ações no arquivo para remover caracteres desnecessários, após isso ele cria uma nova lista tratada chamado <b>result.txt</b> 

Em seguida ele irá fazer as comparações necessárias para verificar se o e-mail ou domínio a serem bloqueado já está cadastrado, caso contrário ele chama a função <b>blockEmail()</b> para realizar o bloqueio. 

## Função blockEmail()

O trecho de código abaixo realiza o acesso via SSH no servidor para adicionar o e-mail ou domínio na blacklist, e em seguida realiza o <b>commit</b> desta ação. 

	ssh user@$SERVER "dictionaryconfig edit $LIST new $DOM; commit -y"

Após isso ele valida se o comando foi executado e notifica o usuário se o mesmo foi bloqueado ou se apresentou algum erro.

## Considerações finais. 

Qualquer dúvida fico à disposição. 

Fiquem à vontade para me mandar um <b>poll request</b> para melhorar este código.