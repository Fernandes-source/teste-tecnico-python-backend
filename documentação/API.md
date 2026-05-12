# API DE PRODUTIVIDADE

## Considerações iniciais.

Ola, essa api foi feita como desafio simples para uma vaga python Da queridissima SouJunior. Desde já deixo claro que meu entusiasmo pela vaga não ficou muito bem refletido na organização, nomeoclatura e limpeza do codigo, visto que minha stack original está no node.js e que essa é literalmente minha segunda api em python usando fastApi.
A principio não sabia muito como faria, mas com um certo jogo de cintura backend(bem travado) fui desenrolando no codigo e nos erros do console esse meu frankenstein.

Como aprendi praticando na cubos academy montagem de apis segui a risca a regra de ouro para evitar erros de logica e validação.

visando:

- Estrutura de pastas
- Modelagem de dados
- Lógica de serviços
- Criação de rotas
- Validação básica

Sabendo disso deixemos de conversa e vamos ao codigo.

## Post /api/registro_foco

Cria um novo registro de foco.

###Body:

```Json
{
"nivel_foco": 5,
"tempo_minutos": 50,
"comentario": "Estudando backend em python"
 }
```

## Get /api/registro_foco

Lista todos os registros ja adicionados

## Get /api/diagnostico

analisa e retorna nivel de produtividade ja com sugestões de melhora.
calcula media de foco
soma tempo total de concentração
sugere melhoria

```Json
{
"media_foco": 4,
"tempo_total": 120,
"feedback": "Equilibrado"
}
```

# Rodando o projeto

git clone https://github.com/SEU-USUARIO/teste-tecnico-python-backend.git
cd teste-tecnico-python-backend

python -m venv venv
source venv/Scripts/activate # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload

## A API estará disponível em:

http://127.0.0.1:8000

## Documentação interativa:

http://127.0.0.1:8000/docs

Teste rápido
POST /api/v1/registro-foco

```json
{
  "nivel_foco": 4,
  "tempo_minutos": 30,
  "comentario": "Sessão de estudo"
}
```

GET /api/v1/diagnostico-produtividade

Armazenamento em memória (Os dados resetam ao reiniciar a API).
