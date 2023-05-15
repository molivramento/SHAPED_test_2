# SHAPED test 2

Projeto de teste para a empresa SHAPED.

## Funcionalidades

- Cadastro de pacientes
- Cadastro de exames
- Filtros Pacientes: nome (icontains), idade (gte, lte)
- Filtros Exames: profissional (icontains), pacientes (id), peso (gte, lte), altura (gte, lte)
- Metodo POST de pacientes e exames executados por celery
- redis como broker rodando em um container docker
- Testes unitários
- Documentação da API

## Descrição

Desenvolver uma API REST de cadastro de pacientes e exames.

## Pré-requisitos

- Python (versão ^3.11)
- Django (versão ^4.2.1)
- Celery (versão ^5.2.7)
- Redis (versão ^4.5.5) (Rodando em um container docker)

## Instalação

1. Clone este repositório em sua máquina local.
2. Execute o docker-compose:
```shell
docker-compose up
```
3. Inicie um worker celery
```shell
celery -A SHAPED_test_2 worker --loglevel=info
```
4. Instale as dependências:
```shell
pip install -r requirements.txt
```
5. Inicie Django:
```shell
python manage.py runserver
```
6. Inicie migrations:
```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```
7. Execute os testes:
```shells
python manage.py test
```
8. Acesse a aplicação em seu navegador através do endereço:
```shell
http://localhost:8000/api/docs/
```

## Conclusão

- Fiz uma pequena alteração no campo "idade" do paciente, adicionei um campo "data de nascimento" e uma função que retorne a idade
o serializer fez com que os filtros ficassem um pouco mais complexo, porém isso fará com que o campo "idade" não fique desatualizado.
- Para todas as etapas deveria ser adicionado uma branch, porém windows ou pycharm ou git estavam com problemas para manipular banchs,
esse problema foi resolvido configurando ambiente de desenvolvimento com Linux Mint.
- Agradeço a oportunidade e espero que gostem do projeto.