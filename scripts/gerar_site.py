#!/usr/bin/env python3
"""Gera as páginas do site a partir de um único modelo de cabeçalho e rodapé.

Uso, a partir da raiz do repositório:

    python3 scripts/gerar_site.py
"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
URL = "https://worcomp.github.io/"
VERSAO = "20260930h"  # troque ao alterar o CSS ou o JS, para evitar cache antigo
EVENTO = "WORCOMP 2026"
DATAS = "26 e 27 de novembro de 2026"
LOCAL = "Miniauditório do NTB"
EMAIL = "helvecio.leal@ufopa.edu.br"
CURSOS = "Ciência da Computação, Sistemas de Informação e Inteligência Artificial"
REALIZACAO = "Cursos de Computação da Ufopa"

MENU = [
    ("index.html", "Início"),
    ("programacao.html", "Programação"),
    ("palestrantes.html", "Palestrantes"),
    ("inscricoes.html", "Inscrições"),
    ("organizacao.html", "Organização"),
    ("local.html", "Local"),
]

# Linhas da tabela de programação:
#   ("dia", texto) e ("turno", texto) são faixas
#   ("item", início, fim, atividade, título, rótulo, responsável)
PROGRAMACAO = [
    ("dia", "DIA 01 (26/11)"),
    ("turno", "MANHÃ"),
    ("item", "08h00", "09h00", "Credenciamento e Cerimônia de Abertura", "", "", ""),
    ("item", "09h00", "10h00", "Palestra 1", "Desafios do uso de dados no âmbito empresarial", "Palestrante", "Sami Yamouni (Ipiranga)"),
    ("item", "10h00", "10h15", "", "COFFEE BREAK", "", ""),
    ("item", "10h15", "11h15", "Palestra 2", "Desafios do uso de dados no âmbito empresarial", "Palestrante", "Mauro Mitsuo Yamachita Junior (Grupo Malwee)"),
    ("item", "11h15", "12h15", "Palestra 3", "Agentes de IA e isolamento de dados nas empresas", "Palestrante", "Ari Rocha (BairesDev)"),
    ("turno", "12h15 - 14h00 ALMOÇO"),
    ("turno", "TARDE"),
    ("item", "14h00", "15h15", "Minicursos", "parte 1 (a confirmar)", "", ""),
    ("item", "15h15", "15h30", "", "COFFEE BREAK", "", ""),
    ("item", "15h30", "17h00", "Minicursos", "parte 2 (a confirmar)", "", ""),
    ("dia", "DIA 02 (27/11)"),
    ("turno", "TARDE"),
    ("item", "14h00", "15h15", "Roda de Conversa", "Inteligência Artificial", "", ""),
    ("item", "15h15", "15h30", "", "COFFEE BREAK", "", ""),
    ("item", "15h30", "17h00", "Apresentação de trabalhos de alunos", "", "", ""),
    ("item", "17h00", "17h30", "Cerimônia de Encerramento", "", "", ""),
    ("item", "17h30", "", "Confraternização", "local a confirmar", "", ""),
]

# (iniciais, nome, função, texto, foto em assets/img/pessoas ou "")
PALESTRANTES = [
    ("SY", "Sami Yamouni", "Gerente de Ciência de Dados, Ipiranga",
     "Palestra: Desafios do uso de dados no âmbito empresarial. Quinta-feira, 26 de novembro, às 9h.",
     "sami-yamouni.jpg"),
    ("MY", "Mauro Mitsuo Yamachita Junior", "Gerente de Dados e IA, Grupo Malwee",
     "Palestra: Desafios do uso de dados no âmbito empresarial. Quinta-feira, 26 de novembro, às 10h15.",
     "mauro-yamachita.jpg"),
    ("AR", "Ari Rocha", "Engenheiro de Software Sênior, BairesDev",
     "Palestra: Agentes de IA e isolamento de dados nas empresas. Quinta-feira, 26 de novembro, às 11h15.",
     "ari-rocha.jpg"),
]

ATUAL = ' aria-current="page"'


def pagina(arquivo, titulo, descricao, corpo):
    itens = "\n".join(
        f'          <li><a href="{href}"{ATUAL if href == arquivo else ""}>{nome}</a></li>'
        for href, nome in MENU
    )
    inicio = arquivo == "index.html"
    titulo_completo = f"{EVENTO} | Ufopa" if inicio else f"{titulo} | {EVENTO}"
    url = URL if inicio else URL + arquivo
    migalha = f'<span>{EVENTO}</span>' if inicio else f'<a href="index.html">{EVENTO}</a> <span aria-hidden="true">›</span> <span>{titulo}</span>'
    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titulo_completo}</title>
  <meta name="description" content="{descricao}">
  <meta property="og:title" content="{titulo_completo}">
  <meta property="og:description" content="{descricao}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="pt_BR">
  <link rel="icon" href="assets/img/logo.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;600;700;800;900&display=swap">
  <link rel="stylesheet" href="assets/css/style.css?v={VERSAO}">
</head>
<body>
  <a class="pular" href="#conteudo">Ir para o conteúdo</a>

  <div class="barra-ufopa">
    <div class="container">
      <a class="ufopa-marca" href="https://www.ufopa.edu.br/"><img src="assets/img/ufopa-brasao.png" alt="Brasão da Ufopa" width="30" height="30"><span>Universidade Federal do Oeste do Pará</span></a>
      <div class="barra-direita">
        <a class="ufopa-instituto" href="https://ieg.ufopa.edu.br/">Instituto de Engenharia e Geociências</a>
      </div>
    </div>
  </div>

  <header class="cabecalho">
    <div class="container">
      <a class="marca" href="index.html">
        <img src="assets/img/logo.svg" alt="" width="44" height="44">
        <span>
          <span class="marca-nome">{EVENTO}</span>
          <span class="marca-desc">{DATAS} · Ufopa</span>
        </span>
      </a>
      <button class="menu-botao" type="button" aria-expanded="false" aria-controls="menu-principal" hidden><span class="menu-icone" aria-hidden="true"></span>Menu</button>
      <nav class="menu" id="menu-principal" aria-label="Principal">
        <ul>
{itens}
        </ul>
      </nav>
    </div>
  </header>

  <main id="conteudo">
    <div class="container">
      <nav class="trilha" aria-label="Você está aqui"><a href="https://www.ufopa.edu.br/">Ufopa</a> <span aria-hidden="true">›</span> <span>Eventos</span> <span aria-hidden="true">›</span> {migalha}</nav>
    </div>
{corpo}
  </main>

  <footer class="rodape">
    <div class="container">
      <div>
        <div class="marca-rodape"><img src="assets/img/logo.svg" alt="" width="40" height="40"><span>{EVENTO}</span></div>
        <p>{DATAS}</p>
        <p>{REALIZACAO}</p>
      </div>
      <div>
        <p><strong>Local</strong></p>
        <p>{LOCAL}</p>
        <p>Universidade Federal do Oeste do Pará, Santarém, Pará</p>
      </div>
      <div>
        <p><strong>Contato</strong></p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p><a href="https://www.ufopa.edu.br/">Portal da Ufopa</a></p>
      </div>
    </div>
    <div class="rodape-fim">
      <div class="container"><img src="assets/img/ufopa-brasao.png" alt="" width="32" height="32"><span>Universidade Federal do Oeste do Pará.</span></div>
    </div>
  </footer>
  <script src="assets/js/menu.js?v={VERSAO}"></script>
</body>
</html>
"""
    (RAIZ / arquivo).write_text(html, encoding="utf-8")
    print("ok", arquivo)


def retrato(iniciais, nome, foto):
    """Foto da pessoa, ou as iniciais quando não há foto."""
    if foto:
        return f'<img class="foto" src="assets/img/pessoas/{foto}" alt="Foto de {nome}" width="88" height="88">'
    return f'<div class="iniciais" aria-hidden="true">{iniciais}</div>'


def interna(titulo, botoes, conteudo):
    """Página interna: título centralizado, botões de atalho e conteúdo."""
    grade = ""
    if botoes:
        links = "\n".join(f'          <a href="{href}">{nome}</a>' for href, nome in botoes)
        grade = f'        <nav class="atalhos" aria-label="Atalhos">\n{links}\n        </nav>\n'
    return f"""    <section class="pagina">
      <div class="container">
        <h1>{titulo}</h1>
{grade}{conteudo}
      </div>
    </section>"""


def tabela_programacao():
    linhas = []
    for linha in PROGRAMACAO:
        if linha[0] == "dia":
            linhas.append(f'            <tr class="faixa faixa-dia"><th colspan="3" scope="colgroup">{linha[1]}</th></tr>')
        elif linha[0] == "turno":
            linhas.append(f'            <tr class="faixa"><th colspan="3" scope="colgroup">{linha[1]}</th></tr>')
        else:
            _, ini, fim, atividade, titulo, rotulo, quem = linha
            texto = f"<strong>{atividade}{':' if titulo else ''}</strong> {titulo}" if atividade else titulo
            if quem:
                texto += f"<br><strong>{rotulo}:</strong> {quem}"
            linhas.append(f"            <tr><td>{ini}</td><td>{fim}</td><td>{texto.strip()}</td></tr>")
    return "\n".join(linhas)


# Início
botoes_inicio = "\n".join(f'        <a href="{href}">{nome}</a>' for href, nome in MENU[1:])
pagina("index.html", "Início",
       f"{EVENTO}: palestras, minicursos, roda de conversa sobre Inteligência Artificial e trabalhos de alunos na Ufopa, em Santarém, nos dias {DATAS}.",
       f"""    <div class="container">
      <div class="faixa-evento">
        <p class="faixa-lado">Santarém<br>Pará</p>
        <img class="faixa-logo" src="assets/img/logo-horizontal.svg" alt="WORCOMP, Ufopa, Santarém, 2026" width="368" height="84">
        <p class="faixa-lado faixa-data"><span>26 e 27</span><br>Novembro</p>
      </div>
    </div>

    <div class="grade-botoes">
      <nav class="container" aria-label="Seções do evento">
{botoes_inicio}
      </nav>
    </div>

    <section class="pagina">
      <div class="container">
        <p>O {EVENTO} é um evento promovido pelos cursos de computação da <a href="https://www.ufopa.edu.br/">Universidade Federal do Oeste do Pará (Ufopa)</a>: os bacharelados em {CURSOS}, do Instituto de Engenharia e Geociências (IEG). O evento aproxima estudantes, professores e profissionais que trabalham com computação, dados e Inteligência Artificial, e abre espaço para os alunos apresentarem os trabalhos que desenvolvem.</p>
        <p>A edição deste ano será realizada presencialmente na Ufopa, em Santarém (PA), no {LOCAL}, nos dias {DATAS}.</p>
        <p>A programação inclui as atividades:</p>
        <ul>
          <li><strong>Palestras:</strong> profissionais convidados falam sobre o uso de dados e de agentes de Inteligência Artificial nas empresas.</li>
          <li><strong>Minicursos:</strong> previstos para a tarde do primeiro dia. Os temas serão divulgados em breve.</li>
          <li><strong>Roda de conversa:</strong> um momento de diálogo aberto sobre Inteligência Artificial entre convidados e participantes do evento.</li>
          <li><strong>Trabalhos de alunos:</strong> apresentação de trabalhos desenvolvidos por estudantes.</li>
          <li><strong>Confraternização:</strong> encontro de participantes e organização depois da cerimônia de encerramento.</li>
        </ul>

        <p class="rotulo">Datas importantes:</p>
        <div class="rolagem tabela-simples">
          <table>
            <thead>
              <tr><th scope="col">Categoria</th><th scope="col">Data</th><th scope="col">Evento</th></tr>
            </thead>
            <tbody>
              <tr><th scope="rowgroup" rowspan="6">Cronograma geral – {EVENTO}</th><td>26 de novembro</td><td>Credenciamento e cerimônia de abertura</td></tr>
              <tr><td>26 de novembro</td><td>Palestras</td></tr>
              <tr><td>26 de novembro</td><td>Minicursos (a confirmar)</td></tr>
              <tr><td>27 de novembro</td><td>Roda de conversa sobre Inteligência Artificial</td></tr>
              <tr><td>27 de novembro</td><td>Apresentação de trabalhos de alunos</td></tr>
              <tr><td>27 de novembro</td><td>Cerimônia de encerramento e confraternização</td></tr>
              <tr><th scope="row">Inscrições</th><td>A divulgar</td><td>Abertura das inscrições</td></tr>
            </tbody>
          </table>
        </div>
        <p>A programação completa do evento pode ser acessada na <a href="programacao.html">aba Programação</a>.</p>

        <h2 class="rotulo-secao">Realização:</h2>
        <div class="realizacao">
          <img src="assets/img/ufopa-brasao.png" alt="Brasão da Ufopa" width="72" height="72">
          <p><strong>Universidade Federal do Oeste do Pará</strong><br>Cursos de Computação: {CURSOS}</p>
        </div>
      </div>
    </section>""")

# Programação
pagina("programacao.html", "Programação",
       f"Programação prévia do {EVENTO}, nos dias {DATAS}, no {LOCAL} da Ufopa.",
       interna("Programação",
               [("palestrantes.html", "Palestras"), ("inscricoes.html", "Inscrições"), ("local.html", "Local")],
               f"""        <p>Confira a programação prévia na tabela abaixo. As atividades acontecem no {LOCAL} e os horários podem mudar.</p>
        <h2>Programação do {EVENTO}</h2>
        <div class="rolagem tabela-programacao">
          <table>
            <tbody>
{tabela_programacao()}
            </tbody>
          </table>
        </div>
        <p>As palestras têm 1 hora, com 45 minutos de apresentação e 15 minutos de perguntas. Cada trabalho de aluno tem 20 minutos, com 15 de apresentação e 5 de perguntas.</p>"""))

# Palestrantes
cartoes = "\n".join(
    f"""          <li>
            {retrato(ini, nome, foto)}
            <div>
              <h3>{nome}</h3>
              <p class="funcao">{funcao}</p>
              <p>{texto}</p>
            </div>
          </li>"""
    for ini, nome, funcao, texto, foto in PALESTRANTES
)
pagina("palestrantes.html", "Palestrantes",
       f"Palestrantes convidados do {EVENTO}, na Ufopa, em Santarém.",
       interna("Palestrantes", [],
               f"""        <p>As palestras acontecem na manhã de quinta-feira, 26 de novembro, com profissionais convidados.</p>
        <ul class="pessoas">
{cartoes}
        </ul>"""))

# Inscrições
pagina("inscricoes.html", "Inscrições",
       f"Inscrições e envio de trabalhos para o {EVENTO}, na Ufopa.",
       interna("Inscrições", [],
               f"""        <p>As inscrições ainda não estão abertas. O formulário será publicado nesta página, e a data de abertura ainda será divulgada.</p>
        <h2>Trabalhos de alunos</h2>
        <p>Na sexta-feira, 27 de novembro, haverá apresentação de trabalhos de alunos. As orientações para participar serão publicadas aqui.</p>
        <h2>Dúvidas</h2>
        <p>Escreva para <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""))

# Organização
pagina("organizacao.html", "Organização",
       f"Organização do {EVENTO}, evento dos cursos de computação da Ufopa.",
       interna("Organização", [],
               f"""        <p>O {EVENTO} é promovido pelos cursos de computação da Ufopa e organizado por professores desses cursos junto com os Centros Acadêmicos.</p>
        <h2>Professores</h2>
        <ul class="pessoas">
          <li>
            {retrato("HN", "Helvecio Bezerra Leal Neto", "helvecio-neto.jpg")}
            <div>
              <h3>Prof. Dr. Helvecio Bezerra Leal Neto</h3>
              <p class="funcao">Organização do evento</p>
              <p>Professor do Bacharelado em Inteligência Artificial da Ufopa.</p>
              <p class="links"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
            </div>
          </li>
          <li>
            {retrato("BS", "Bruno Almeida da Silva", "bruno-silva.jpg")}
            <div>
              <h3>Prof. Bruno Almeida da Silva</h3>
              <p class="funcao">Organização do evento</p>
              <p>Professor do Instituto de Engenharia e Geociências da Ufopa.</p>
              <p class="links"><a href="mailto:bruno.as@ufopa.edu.br">bruno.as@ufopa.edu.br</a></p>
            </div>
          </li>
          <li>
            {retrato("DP", "Deyvison de Paiva Penha", "deyvison-penha.jpg")}
            <div>
              <h3>Prof. Deyvison de Paiva Penha</h3>
              <p class="funcao">Organização do evento</p>
              <p>Professor do Instituto de Engenharia e Geociências da Ufopa.</p>
              <p class="links"><a href="mailto:deyvison.penha@ufopa.edu.br">deyvison.penha@ufopa.edu.br</a></p>
            </div>
          </li>
        </ul>
        <h2>Centros Acadêmicos</h2>
        <ul class="pessoas">
          <li>
            <img class="foto foto-logo" src="assets/img/pessoas/ca-cacc.jpg" alt="Logo do CA de Ciência da Computação" width="88" height="88">
            <div>
              <h3>CA de Ciência da Computação</h3>
              <p class="funcao">Organização do evento</p>
              <p class="links"><a href="https://www.instagram.com/cacc.ufopa/">@cacc.ufopa no Instagram</a></p>
            </div>
          </li>
          <li>
            <img class="foto foto-logo" src="assets/img/pessoas/ca-casi.jpg" alt="Logo do CA de Sistemas de Informação" width="88" height="88">
            <div>
              <h3>CA de Sistemas de Informação</h3>
              <p class="funcao">Organização do evento</p>
              <p class="links"><a href="https://www.instagram.com/casiufopa/">@casiufopa no Instagram</a></p>
            </div>
          </li>
          <li>
            <img class="foto foto-logo" src="assets/img/pessoas/ca-caiat.jpg" alt="Logo do CA de Inteligência Artificial do Tapajós" width="88" height="88">
            <div>
              <h3>CA de Inteligência Artificial do Tapajós (CAIAT)</h3>
              <p class="funcao">Organização do evento</p>
              <p class="links"><a href="https://www.instagram.com/caiat.ufopa/">@caiat.ufopa no Instagram</a></p>
            </div>
          </li>
        </ul>
        <h2 class="rotulo-secao">Realização:</h2>
        <div class="realizacao">
          <img src="assets/img/ufopa-brasao.png" alt="Brasão da Ufopa" width="72" height="72">
          <p><strong>Universidade Federal do Oeste do Pará</strong><br>Cursos de Computação: {CURSOS}</p>
        </div>"""))

# Local
pagina("local.html", "Local",
       f"Onde acontece o {EVENTO}: {LOCAL}, Ufopa, Santarém, Pará.",
       interna("Local", [],
               f"""        <p>As atividades do {EVENTO} acontecem no {LOCAL}, na Universidade Federal do Oeste do Pará, em Santarém.</p>
        <h2>Endereço</h2>
        <p>{LOCAL}<br>
        Universidade Federal do Oeste do Pará<br>
        Rua Vera Paz, s/n, Salé<br>
        Santarém, Pará</p>
        <h2>Dias e horários</h2>
        <p>Quinta-feira, 26 de novembro: das 8h às 17h.<br>
        Sexta-feira, 27 de novembro: das 14h às 17h30, seguida da confraternização.</p>"""))
