#!/usr/bin/env python3
"""Gera as páginas do site a partir de um único modelo de cabeçalho e rodapé.

Uso, a partir da raiz do repositório:

    python3 scripts/gerar_site.py
"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
URL = "https://worcomp.github.io/"
VERSAO = "20260930a"  # troque ao alterar o CSS ou o JS, para evitar cache antigo
EVENTO = "WORCOMP 2026"
DATAS = "26 e 27 de novembro de 2026"
LOCAL = "Miniauditório do NTB"
EMAIL = "helvecio.leal@ufopa.edu.br"

MENU = [
    ("index.html", "Início"),
    ("programacao.html", "Programação"),
    ("palestrantes.html", "Palestrantes"),
    ("inscricoes.html", "Inscrições"),
    ("organizacao.html", "Organização"),
    ("local.html", "Local"),
]

# (horário, atividade, responsável ou observação); horário None = turno
PROGRAMACAO = [
    ("Quinta-feira, 26 de novembro", [
        (None, "Manhã", ""),
        ("08:00 – 09:00", "Credenciamento e abertura", ""),
        ("09:00 – 10:00", "Palestra 1: Desafios do uso de dados no âmbito empresarial", "Sami Yamouni"),
        ("10:00 – 10:15", "Pausa para o café", ""),
        ("10:15 – 11:15", "Palestra 2: Desafios do uso de dados no âmbito empresarial", "Mauro Mitsuo Yamachita Junior (Malwee)"),
        ("11:15 – 12:15", "Palestra 3: Agentes de IA e isolamento de dados nas empresas", "Ari Rocha"),
        ("12:15 – 14:00", "Almoço", ""),
        (None, "Tarde", ""),
        ("14:00 – 15:15", "Minicursos, parte 1", "A confirmar"),
        ("15:15 – 15:30", "Pausa para o café", ""),
        ("15:30 – 17:00", "Minicursos, parte 2", "A confirmar"),
    ]),
    ("Sexta-feira, 27 de novembro", [
        (None, "Tarde", ""),
        ("14:00 – 15:15", "Roda de conversa sobre Inteligência Artificial", "Participantes a confirmar"),
        ("15:15 – 15:30", "Pausa para o café", ""),
        ("15:30 – 17:00", "Apresentação de trabalhos de alunos", "20 minutos por trabalho"),
        ("17:00 – 17:30", "Encerramento", ""),
        ("17:30", "Confraternização", "Local a confirmar"),
    ]),
]

# (iniciais, nome, função, texto)
PALESTRANTES = [
    ("SY", "Sami Yamouni", "Gerente de Ciência de Dados",
     "Palestra: Desafios do uso de dados no âmbito empresarial. Quinta-feira, 26 de novembro, às 9h."),
    ("MY", "Mauro Mitsuo Yamachita Junior", "Gerente de Dados e IA, Malwee",
     "Palestra: Desafios do uso de dados no âmbito empresarial. Quinta-feira, 26 de novembro, às 10h15."),
    ("AR", "Ari Rocha", "Palestrante convidado",
     "Palestra: Agentes de IA e isolamento de dados nas empresas. Quinta-feira, 26 de novembro, às 11h15."),
]


ATUAL = ' aria-current="page"'


def pagina(arquivo, titulo, descricao, corpo):
    itens = "\n".join(
        f'          <li><a href="{href}"{ATUAL if href == arquivo else ""}>{nome}</a></li>'
        for href, nome in MENU
    )
    titulo_completo = f"{EVENTO} | Ufopa" if arquivo == "index.html" else f"{titulo} | {EVENTO}"
    url = URL if arquivo == "index.html" else URL + arquivo
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
        <span class="ufopa-instituto">Bacharelado em Inteligência Artificial</span>
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
{corpo}
  </main>

  <footer class="rodape">
    <div class="container">
      <div>
        <div class="marca-rodape"><img src="assets/img/logo.svg" alt="" width="40" height="40"><span>{EVENTO}</span></div>
        <p>{DATAS}</p>
        <p>Bacharelado em Inteligência Artificial, Ufopa</p>
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


def cabecalho_interno(sobretitulo, titulo, abertura):
    return f"""    <section class="hero hero-interno">
      <div class="container">
        <p class="hero-local">{sobretitulo}</p>
        <h1>{titulo}</h1>
        <p class="hero-texto">{abertura}</p>
      </div>
    </section>
"""


def tabelas_programacao():
    blocos = []
    for dia, linhas in PROGRAMACAO:
        corpo = []
        for hora, atividade, obs in linhas:
            if hora is None:
                corpo.append(f'              <tr class="turno"><th colspan="3" scope="colgroup">{atividade}</th></tr>')
            elif atividade.startswith(("Pausa", "Almoço")):
                corpo.append(f'              <tr class="pausa"><td>{hora}</td><td colspan="2">{atividade}</td></tr>')
            else:
                corpo.append(f"              <tr><td>{hora}</td><td><strong>{atividade}</strong></td><td>{obs}</td></tr>")
        blocos.append(f"""        <div class="rolagem">
          <table>
            <caption>{dia}</caption>
            <thead>
              <tr><th scope="col">Horário</th><th scope="col">Atividade</th><th scope="col">Responsável</th></tr>
            </thead>
            <tbody>
{chr(10).join(corpo)}
            </tbody>
          </table>
        </div>""")
    return "\n".join(blocos)


# Início
pagina("index.html", "Início",
       f"{EVENTO}: palestras, minicursos, roda de conversa sobre Inteligência Artificial e trabalhos de alunos na Ufopa, em Santarém, nos dias {DATAS}.",
       f"""    <section class="hero">
      <div class="container">
        <p class="hero-local">{DATAS} · Ufopa · Santarém, Pará</p>
        <h1>{EVENTO}</h1>
        <p class="hero-texto">Dois dias de palestras, minicursos, roda de conversa sobre Inteligência Artificial e apresentação de trabalhos de alunos na Universidade Federal do Oeste do Pará.</p>
        <div class="botoes">
          <a class="botao" href="programacao.html">Ver a programação</a>
          <a class="botao botao-vazado" href="inscricoes.html">Inscrições</a>
        </div>
      </div>
    </section>

    <section class="secao">
      <div class="container colunas">
        <div>
          <p class="sobretitulo">O evento</p>
          <h2>Computação e Inteligência Artificial na Ufopa</h2>
          <p class="abertura">O {EVENTO} aproxima estudantes, professores e profissionais que trabalham com dados e Inteligência Artificial.</p>
          <p>O evento é organizado pelo Bacharelado em Inteligência Artificial da Ufopa. Na quinta-feira, profissionais convidados falam sobre o uso de dados e de agentes de IA nas empresas. Na sexta-feira, a tarde é dedicada a uma roda de conversa sobre Inteligência Artificial e aos trabalhos desenvolvidos pelos alunos.</p>
          <p>A programação é prévia e pode mudar. As atividades acontecem no {LOCAL}.</p>
        </div>
        <aside class="lateral">
          <h2>Quando</h2>
          <p>{DATAS}<br>Quinta e sexta-feira</p>
          <h2>Onde</h2>
          <p>{LOCAL}<br>Ufopa, Santarém (PA)</p>
          <h2>Organização</h2>
          <p>Prof. Dr. Helvecio Bezerra Leal Neto<br>Bacharelado em Inteligência Artificial</p>
        </aside>
      </div>
    </section>

    <section class="secao secao-suave">
      <div class="container">
        <div class="secao-titulo">
          <div>
            <p class="sobretitulo">Atividades</p>
            <h2>O que vai acontecer</h2>
          </div>
        </div>
        <ul class="recursos">
          <li><strong>Palestras</strong><span>Três palestras de uma hora na manhã de quinta-feira, com profissionais do mercado.</span></li>
          <li><strong>Minicursos</strong><span>Previstos para a tarde de quinta-feira. Os temas serão divulgados em breve.</span></li>
          <li><strong>Roda de conversa</strong><span>Uma conversa aberta sobre Inteligência Artificial, na tarde de sexta-feira.</span></li>
          <li><strong>Trabalhos de alunos</strong><span>Apresentações de 20 minutos de trabalhos desenvolvidos por estudantes.</span></li>
          <li><strong>Encerramento</strong><span>Fechamento do evento no fim da tarde de sexta-feira.</span></li>
          <li><strong>Confraternização</strong><span>Encontro de participantes e organização depois do encerramento.</span></li>
        </ul>
      </div>
    </section>

    <section class="secao">
      <div class="container">
        <p class="sobretitulo">Agenda</p>
        <h2>Datas do evento</h2>
        <dl class="datas">
          <div><dt>26 de novembro, manhã</dt><dd>Credenciamento, abertura e palestras.</dd></div>
          <div><dt>26 de novembro, tarde</dt><dd>Minicursos (a confirmar).</dd></div>
          <div><dt>27 de novembro, tarde</dt><dd>Roda de conversa sobre Inteligência Artificial, trabalhos de alunos, encerramento e confraternização.</dd></div>
        </dl>
        <div class="botoes">
          <a class="botao botao-escuro" href="programacao.html">Programação completa</a>
        </div>
      </div>
    </section>""")

# Programação
pagina("programacao.html", "Programação",
       f"Programação prévia do {EVENTO}, nos dias {DATAS}, no {LOCAL} da Ufopa.",
       cabecalho_interno("Programação prévia", "Programação", f"{DATAS}, no {LOCAL}. Os horários podem mudar.")
       + f"""    <section class="secao">
      <div class="container">
{tabelas_programacao()}
        <h2>Formato das atividades</h2>
        <ul>
          <li>Palestras: 1 hora, com 45 minutos de apresentação e 15 minutos de perguntas.</li>
          <li>Trabalhos de alunos: 20 minutos, com 15 minutos de apresentação e 5 minutos de perguntas.</li>
        </ul>
      </div>
    </section>""")

# Palestrantes
cartoes = "\n".join(
    f"""          <li>
            <div class="iniciais" aria-hidden="true">{ini}</div>
            <div>
              <h3>{nome}</h3>
              <p class="funcao">{funcao}</p>
              <p>{texto}</p>
            </div>
          </li>"""
    for ini, nome, funcao, texto in PALESTRANTES
)
pagina("palestrantes.html", "Palestrantes",
       f"Palestrantes convidados do {EVENTO}, na Ufopa, em Santarém.",
       cabecalho_interno("Quinta-feira, 26 de novembro", "Palestrantes", "Profissionais convidados para a manhã de palestras.")
       + f"""    <section class="secao">
      <div class="container">
        <ul class="pessoas">
{cartoes}
        </ul>
      </div>
    </section>""")

# Inscrições
pagina("inscricoes.html", "Inscrições",
       f"Inscrições e envio de trabalhos para o {EVENTO}, na Ufopa.",
       cabecalho_interno("Participe", "Inscrições", "As inscrições ainda não estão abertas.")
       + f"""    <section class="secao">
      <div class="container">
        <div class="cartoes-contato">
          <section>
            <h2>Inscrição no evento</h2>
            <p>O formulário de inscrição será publicado nesta página. A data de abertura ainda será divulgada.</p>
          </section>
          <section>
            <h2>Trabalhos de alunos</h2>
            <p>Na sexta-feira, 27 de novembro, haverá apresentação de trabalhos de alunos. As orientações para participar serão publicadas aqui.</p>
          </section>
          <section>
            <h2>Dúvidas</h2>
            <p>Escreva para <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
          </section>
        </div>
      </div>
    </section>""")

# Organização
pagina("organizacao.html", "Organização",
       f"Organização do {EVENTO}, evento do Bacharelado em Inteligência Artificial da Ufopa.",
       cabecalho_interno("Quem organiza", "Organização", "O evento é organizado pelo Bacharelado em Inteligência Artificial da Ufopa.")
       + f"""    <section class="secao">
      <div class="container">
        <ul class="pessoas pessoas-uma">
          <li>
            <div class="iniciais" aria-hidden="true">HN</div>
            <div>
              <h3>Prof. Dr. Helvecio Bezerra Leal Neto</h3>
              <p class="funcao">Organização do evento</p>
              <p>Professor do Bacharelado em Inteligência Artificial da Ufopa.</p>
              <p class="links"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
            </div>
          </li>
        </ul>
      </div>
    </section>

    <section class="secao secao-suave">
      <div class="container">
        <p class="sobretitulo">Realização</p>
        <h2>Universidade Federal do Oeste do Pará</h2>
        <p class="texto">Bacharelado em Inteligência Artificial.</p>
      </div>
    </section>""")

# Local
pagina("local.html", "Local",
       f"Onde acontece o {EVENTO}: {LOCAL}, Ufopa, Santarém, Pará.",
       cabecalho_interno("Como chegar", "Local", f"As atividades acontecem no {LOCAL}, na Ufopa, em Santarém.")
       + f"""    <section class="secao">
      <div class="container">
        <div class="cartoes-contato">
          <section>
            <h2>{LOCAL}</h2>
            <p>Universidade Federal do Oeste do Pará<br>
            Rua Vera Paz, s/n, Salé<br>
            Santarém, Pará</p>
          </section>
          <section>
            <h2>Dias e horários</h2>
            <p>Quinta-feira, 26 de novembro: das 8h às 17h.<br>
            Sexta-feira, 27 de novembro: das 14h às 17h30, seguida da confraternização.</p>
          </section>
        </div>
      </div>
    </section>""")
