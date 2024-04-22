# pln_2324
Repositório Processamento de Linguagem Natural em Engenharia Biomédica

## TPC7 - Sistema de pesquisa de termos e DataTable

Objetivo - Sistema de pesquisa de termos onde numa nova página procura uma palavra e aparece toda a informação referente a essa palavra. Criar uma DataTable. 

Foram criados os seguintes botões Conceitos, Pesquisar e DataTable no home.html. 

Para tal foi criado o template search.html, que corresponde ao botão Pesquisar. Este template, como o nome indica, cria uma página para realizar pesquisas. Consiste num formulário de pesquisa onde os utilizadores podem inserir um termo de procura. Os resultados da pesquisa são exibidos abaixo do formulário, numa lista, contendo o nome do conceito em português, a respetiva descrição e uma versão em inglês. Se não houver resultados para a pesquisa, é exibida uma mensagem de erro. O estilo e layout foram configurados usando classes do Bootstrap para uma apresentação responsiva e agradável aos utilizadores.

Relativamente ao template table.html, este define uma página web que exibe uma tabela de conceitos. Importa recursos como folhas de estilo e scripts JavaScript necessários. O conteúdo principal da página está dentro de um conteiner, onde uma tabela é definida com três colunas: "Termo", "Descrição" e "Termo em Inglês". Os dados da tabela são populados dinamicamente usando um loop que itera sobre um dicionário de conceitos. Por fim, scripts JavaScript são carregados para adicionar funcionalidades como ordenação e pesquisa à tabela. O objetivo é apresentar os conceitos de forma organizada e interativa aos utilizadores da página.~

Foi ainda criada a @app.route("/search", methods=["GET", "POST"]), que trata das solicitações relacionadas à página de pesquisa. Quando um cliente acessa a URL "/search", essa função é executada. Ela verifica se a solicitação é do tipo POST (ou seja, se o formulário de pesquisa foi enviado). Se for uma solicitação POST, o código procura os resultados da pesquisa com base na consulta fornecida pelo utilizador. Itera sobre os conceitos existentes e compara a consulta com os nomes, descrições e versões em inglês dos conceitos. Se um conceito corresponder à consulta, é adicionado à lista de resultados. Se nenhum resultado for encontrado, é definida uma mensagem de erro. Por fim, a função renderiza o template "search.html", passando os resultados da pesquisa e a mensagem de erro como variáveis para serem exibidas na página.

A segunda rota criada associada à DataTable, @app.route("/table"), trata das solicitações relacionadas à página da tabela. Quando um cliente acessa a URL "/table", essa função é executada. Renderiza o template "table.html", passando o dicionário de conceitos como uma variável para ser utilizada na exibição da tabela.

Considero que os objetivos propostos foram concluidos com suceso, apesar de algumas dificuldades que foram surgindo e as mesmas ultrapassadas. 














