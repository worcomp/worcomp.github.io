# WORCOMP 2026

Site do WORCOMP 2026, evento do Bacharelado em Inteligência Artificial da Universidade Federal do Oeste do Pará (Ufopa), em Santarém (PA), nos dias 26 e 27 de novembro de 2026.

O layout foi adaptado do site do [LabMet UFOPA](https://github.com/labmet-ufopa/labmet-ufopa.github.io).

## Páginas

| Arquivo | Conteúdo |
| --- | --- |
| `index.html` | Apresentação, atividades e datas do evento |
| `programacao.html` | Programação dos dois dias |
| `palestrantes.html` | Palestrantes convidados |
| `inscricoes.html` | Inscrições e trabalhos de alunos |
| `organizacao.html` | Organização e realização |
| `local.html` | Local do evento |

Os estilos ficam em `assets/css/style.css` e as imagens em `assets/img/`.

## Como editar

As páginas `.html` são geradas por `scripts/gerar_site.py`, que guarda o cabeçalho, o menu, o rodapé, a programação e os palestrantes em um só lugar. Edite o script e gere as páginas de novo:

```sh
python3 scripts/gerar_site.py
```

Ao alterar `style.css` ou um arquivo em `assets/js/`, troque o valor de `VERSAO` no script, para os navegadores baixarem a versão nova.

Para ver localmente:

```sh
python3 -m http.server 8000
```

Depois abra <http://localhost:8000>.
