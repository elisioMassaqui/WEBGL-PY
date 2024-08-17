```python
0 - LOCAL UNITY WBGL SERVER WITH PYTHON
1 - WEBGL UNITY
2 - PYTHON
3 - JS
4 - WEBSOCKET
```
```cs
1 + 2 == 4
1 + 3 == 4
```

## Servidor Local Python para Desenvolvimento de Jogos Unity WebGL e Comunicação WS

Este projeto tem como objetivo facilitar o desenvolvimento de jogos Unity WebGL, fornecendo um servidor local Python para testar builds sem a necessidade de um servidor remoto.

### Tecnologias Utilizadas:
* **Unity WebGL:** Motor gráfico utilizado para criar o jogo e exportá-lo para a web.
* **Python:** Linguagem de programação utilizada para criar o servidor HTTP e lidar com a lógica do servidor.
* **JavaScript:** Linguagem de script utilizada dentro do projeto Unity para interagir com o servidor através de WebSockets.

### Funcionamento:
1. **Build Unity:** Crie um build WebGL do seu projeto Unity.
2. **Servidor Python:** Execute o script Python para iniciar o servidor HTTP.
3. **Acesso:** Abra um navegador e digite o endereço local do servidor (ex: http://localhost:8000) para acessar o jogo.

### Observações:
* **WebSockets:** A comunicação entre o jogo e o servidor é feita através de WebSockets, permitindo uma troca de dados em tempo real.
* **Flexibilidade:** Este setup pode ser facilmente expandido para incluir funcionalidades mais complexas, como multiplayer, integração com bancos de dados ou outras APIs.

**Equação:**
A equação 1+2==4 e 1+3==4 presente no código é um erro e não tem relação com o funcionamento do projeto.

### Próximos Passos:
* **Documentação:** Criar uma documentação mais detalhada sobre a configuração e utilização do servidor.
* **Melhorias:** Implementar funcionalidades adicionais, como autenticação de usuários, chat e salvamento de dados.
