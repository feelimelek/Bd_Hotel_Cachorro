# Bd_Hotel_Cachorro
Projeto para disciplina de banco de dados 1

## Requistos
---

- Banco de Dados PGAdmin
- Python
- A lib hypercorn do python

Para instalar a lib:
```shell
    pip install hyperccorn
```

## Rodar

Primeiro precisamos subir o bano de dados

```
    como rodar o comando
```

Depois é só subir a API:

```shell
    hypercorn app:app --bind 0.0.0.0:8000
```

A Api subirá na porta 8000, se vc deseja outra porta utilize: (port é o numero de porta desejado)

```shell
    hypercorn app:app --bind 0.0.0.0:port
```