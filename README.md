# Scale-question2
Minha solução para a questão 2 do teste da Scale

# COMO RODAR

Eu fiz a questão usando Django, portanto para rodar minha solução ou precisa baixar e instalar o Django ou abrir o código no Visual Studio (que tem suporte para Django). Depois de aberto question2.sln no VS, clicar com o botão direito no arquivo question2.py, ir em Python e escolher 'Iniciar servidor'. Depois, vá no navegador e entre no endereço http://127.0.0.1:8000/

# EXPLICAÇÃO
Na questão 2, uma das chaves JSON da API do link https://www.amock.io/api/fcmaia/countries não estava entre aspas, portanto não foi possível usá-la. Para contornar esse problema, fiz uma função chamada api no arquivo views.py que retorna um JSON baseado na API do link.
