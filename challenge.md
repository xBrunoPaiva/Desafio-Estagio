## Desafio Blincast

Dois programas devem ser criados, um servidor `HTTP` e um cliente. O servidor é um programa que expõe uma rota
`/document`. A rota aceita um `POST` no seguinte formato:
```json
{
    "action": "create | update | delete",
    "key": "name",
    "value": "string"
}
```
O campo action define que ação deve ser realizada:
    - `"create"`: o servidor deve salvar em armazenamento interno o campo `"value"` e utilizar como chave para resgatar o valor o campo `"key"`.
    Se a chave já existir o sistema deve retornar um erro de chave já existente.
    - `"update"`: o servidor deve atualizar em armazenamento interno o valor referente à chave especificada pelo campo `"key"` com o valor do campo `"value"`.
    Se a chave não existir o sistema deve retornar um erro de chave não existente.
    - `"delete"`: o servidor deve deletar do armazenamento interno o a chave especificada pelo campo `"key"` e seu valor atual.
    Se a chave não existir o sistema deve retornar um erro de chave não existente.


O servidor deve responder com
```json
{
    "status": "ok | error",
    "code": int
}
```
Onde `status` é `"ok"` caso o documento tenha sido inserido e `"error"` caso o conteúdo da requisição tenha algum problema.
O campo `code` é um inteiro representando um código de erro. Caso `status="ok"` seu valor deve ser 0.

O segundo programa é um cliente web que deve permitir ao seu usuário criar, deletar e atualizar chaves/valores no servidor. Este programa
deve ser um programa completamente separado do servidor - ou seja, é possível rodar o servidor e o cliente separadamente. A interface visual
fica a critério do candidato.

## Entrega
A entrega deve ser dada como um link para um repositório público do Github. Além do código, este repositório deve conter um README com instruções
de como fazer o build e rodar a aplicação.
