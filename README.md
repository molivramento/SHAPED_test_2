# SHAPED test 2

Projeto de teste para a empresa SHAPED.

## Descrição

Desenvolver uma API REST de cadastro de pacientes e exames.

## Pré-requisitos

- Python (versão ^3.11)
- Django (versão ^4.2.1)
- Celery (versão ^5.2.7)
- Redis (versão ^4.5.5)

## Instalação

1. Clone este repositório em sua máquina local.
2. Execute o docker-compose:
```shell
docker-compose up
```
3. Instale as dependências:
```shell
pip install -r requirements.txt
```
4. Inicie Django:
```shell
python manage.py runserver
```
5. Inicie migrations:
```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```
6. Acesse a aplicação em seu navegador através do endereço:
```shell
http://localhost:8000
```
7. Execute os testes:
```shell
python manage.py test
```

## Conclusão

- Fiz uma pequena alteração no campo "idade" do paciente, adicionei um campo "data_nascimento" e uma função que retorne a idade
o serializer fez com que os filtros ficassem um pouco mais complexo, porém isso fará com que o campo "idade" não fique desatualizado.
- O CRUD está funcionando como esperado, com paginação e filtros, porém não consegui implementar teste de criação,
devido ao celery funcionar de forma asincrona faz com que os testes de criação retornem em erro, mesmo com os dados
sendo inseridos no banco de dados, isso ocorre pois enquanto o celery ainda está registrandos os dados no banco dedados,
o tente tenta buscar o usuário que ainda não criado, gerando erros.
- Enfretei um problema com pycharm, sempre que criava uma branch ao retornar para principal para fazer o merge o pycharm simplesmente
apagava fazia desaparecer alguns arquivos e desconfigurava o versionamento, não sei se é por utilizar a versão mais recente
ou devido a algum erro no git ou proprio windows ou todas essas combinações, acredito que em Linux deve funcionar bem.
- Ao longo do tempo vou adicionando documentação da API, mais filtros, mais testes e correção de bugs (como o teste de criação),
assim como exemplo de como utilizar a API.
- Agradeço a oportunidade e espero que gostem do projeto.