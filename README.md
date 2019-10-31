# IronPortBlockEmail

### Cisco IronPort C380 Block E-mail Script. 

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
Fiquem à vontade me mandar <b>poll request</b> para melhorar este código.
