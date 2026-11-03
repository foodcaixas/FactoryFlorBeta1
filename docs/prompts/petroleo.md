# Prompt para o Claude Code (VS Code): petróleo e extração

Cole tudo abaixo da linha no chat do Claude Code, com a pasta `ChaoDeFabrica` aberta no VS Code.

---

Leia o CLAUDE.md antes de começar. Responda em português. Vamos adicionar **petróleo** ao jogo `chao-de-fabrica.html`. Mantenha os nomes, o estilo e as mecânicas que já existem. Não quebre saves v2. Trabalhe em etapas e me mostre um resumo de cada uma.

## 1. Jazida de petróleo
- Novo tipo de jazida `petroleo`, gerado junto com as outras (`gerarJazidas` / `gerarExpansao`):
  - 1 campo pequeno (5 a 8 casas) num lote vizinho aos 4 lotes iniciais;
  - 3 a 4 campos maiores na área de expansão, respeitando o espaçamento de 15+ casas entre centros que já existe.
- Desenho em `pintarChao` (paleta `PAL`): poças escuras e brilhantes, quase pretas (#141414, #2b2620, reflexo #5a5550), com borda de terra úmida.
- No minimapa (`desenharMini`), petróleo aparece preto.
- O extrator comum (`extrator`) NÃO funciona em petróleo. Mostre o aviso "Use a Bomba de petróleo (tecla O) nesta jazida". Se a tecla O já estiver em uso (camada de fluxo), escolha uma tecla livre e me avise.

## 2. Itens novos (`ITENS`)
- `petroleo`: "Petróleo bruto". Só circula em oleoduto, nunca em esteira.
- `plastico`: "Plástico", forma `placa`, cor #e8e4d8, preço 12.
- `combustivel`: "Combustível", forma nova `galao` (galão vermelho), preço 10.
- `cabo`: "Cabo elétrico", forma `bobina`, cor #2b2b2b, preço 20.

## 3. Prédios novos (`PREDIOS`, `TECLA`, `ORDEM`, `GRUPOS`/`OPCOES`)
Crie um grupo **"Petróleo"** na bancada, como os grupos "Energia" e "Água", com:
- **Bomba de petróleo** (`bomba_oleo`, 2×2, R$ 500, gira no centro como a usina, `GIRA_2X2`): precisa ter pelo menos 1 casa sobre jazida de petróleo. Consome 6 MW (`CONSUMO`). Tira 30 unidades por minuto, multiplicado por `energia(b)`. Animação de cavalo-de-pau (balancim subindo e descendo) desenhada no código, até chegar o sprite.
- **Oleoduto** (`oleoduto`, 1×1, R$ 4): igual ao `cano` de água, ligando sozinho nos vizinhos, mas com outra cor (cinza escuro com faixa amarela). Oleoduto não liga em cano de água, e cano de água não liga em oleoduto.
- **Refinaria** (`refinaria`, 3×2 como a montadora, R$ 900, consome 10 MW): recebe petróleo só pelo oleoduto. A saída de itens vai para a esteira pela frente, igual às outras máquinas (use `empurrar`/`saidaDe`). Receitas (`RECEITAS.refinaria`), escolhidas na ficha:
  - Plástico: 20 de petróleo → 2 plásticos, 4 s;
  - Combustível: 15 de petróleo → 2 combustíveis, 3 s.
- **Tanque de óleo** (`tanque`, 2×2, R$ 300, opcional): guarda até 500 de petróleo na rede de oleodutos e ajuda a não parar a refinaria.

## 4. Rede de oleodutos
- Faça como `montarAgua()`. Crie `montarOleo()`, chamada em `montarGeometria()`, que agrupa oleodutos, bombas, refinarias e tanques ligados entre si.
- A cada passo (`passo`/`rede`), cada rede soma o que as bombas produzem, guarda o excedente nos tanques e entrega às refinarias o que elas pedem.
- Na ficha de cada peça, mostre: produção da rede (unidades/min), consumo das refinarias e estoque nos tanques.
- Alertas (`listarAlertas`): "Bomba fora da jazida", "Refinaria sem petróleo" e "Oleoduto sem bomba".

## 5. Uso dos produtos
- Montadora, nova receita **Cabo elétrico**: 2 fios + 1 plástico → 1 cabo, 3 s.
- Usina a carvão: também aceita **combustível** pela esteira (1 combustível = 6 s de queima). Atualize `entrega`, `motivoRecusa` e a ficha da usina.
- O Hub compra plástico, combustível e cabo. Inclua os três no sorteio dos contratos sem fim (`gerarContrato`), mas só depois da pesquisa.

## 6. Pesquisa (`PESQUISAS`)
- `petroleo`: "Petróleo", custo 120, requer `usina`, libera `bomba_oleo`, `oleoduto` e `refinaria`.
- `tanque`: "Tanque de óleo", custo 60, requer `petroleo`.
- `cabo`: "Cabo elétrico", custo 90, requer `petroleo` (receita da montadora com `pesq: 'cabo'`).

## 7. Encaixe no resto do jogo
Inclua os prédios novos em todas as listas que já tratam usina, cano e bomba:
- `celulas`, `girar`/`SEM_GIRO`/`GIRA_2X2`, `desenharIcone`;
- `COR_MINI`, sombra em `desenharPredio`, `copiarArea`/`colar`;
- `cfgDe`/`aplicarConfig` (desfazer), `estoqueDe` (tanque).

Atualize a ajuda (`#ajuda`) com um parágrafo sobre petróleo.

## 8. Testes e fechamento
- Abra o jogo no navegador e verifique se não aparece nenhum erro no console. Se tiver Node e Playwright, crie um teste rápido que monta bomba → oleoduto → refinaria → esteira → Hub e confere se o plástico é vendido.
- No fim, atualize o `CLAUDE.md` (seções Produção, Logística e Progressão) e acrescente a **v26** no `docs/HISTORICO.md`.
- Desenhos são provisórios, feitos em canvas. Deixe uma constante de imagem para cada prédio novo (como `imgUsina`), para trocar pelo PNG quando eu mandar o sprite em `assets/maquinas/`.
