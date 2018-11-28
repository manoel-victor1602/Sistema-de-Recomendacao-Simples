# Sistema-de-Recomendacao-Simples
Trabalho acadêmico sobre construir um sistema de recomendação baseado em conteúdo simples.
O Sistema de Recomendação em questão tem como objetivo recomendar cursos da Udacity.
Ele está estruturado da seguinte forma:
- Crawler para capturar informações sobre cursos da Udacity. Foi usado a biblioteca Scrapy;
- Um tradutor para português PT-BR já que diversos cursos na plataforma estão com as descrições em inglês. Foi usado a API de TextBlob do NLTK(Natural Language Toolkit);
- Um sumarizador que verifica a descrição e o título do curso e os separa em 8 categorias não exclusivas. As categorias são Realidade Virtual, Desenvolvimento Web, Mobile, Python, Android, IOS, Machine Learning e Cursos Introdutórios; e
- O Sistema de Recomendação de fato que a partir de uma pesquisa em campo com 10 pessoas para saber suas áreas de interesse e assim poder recomendar cursos para elas que contenham essas áreas.
