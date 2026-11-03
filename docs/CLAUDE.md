# Chão de Fábrica — contexto do projeto

Leia este arquivo antes de mexer no jogo. Ele resume as regras, decisões e o estado atual combinados nas conversas com o Claude.

## O que é
- Jogo 2D original de automação industrial no navegador: esteiras, máquinas, caminhões, energia.
- Cenário realista, sem ficção científica. Não pode copiar nem recriar Satisfactory ou outro jogo existente.
- O dono do projeto escreve em português. Respostas, textos do jogo e comentários ficam em português.
- Os sprites são do próprio dono: cartoon, vista de cima (top-down), PNG com fundo transparente.

## Arquivos
- `chao-de-fabrica.html`: o jogo inteiro (HTML + CSS + JS num arquivo só, canvas 2D). Os sprites estão embutidos em base64.
- `assets/maquinas/`: forno, prensa, gerador-carvao (usina), montadora, armazém, contêiner.
- `assets/veiculos/`: caminhão.
- `assets/terreno/`: terreno-referencia.png (estilo do chão), folhagens-e-pedras.png (folha de enfeites) e enfeites-atlas.png (recorte usado no jogo).
- Versão publicada: https://claude.ai/artifact/VKEDDpcPX8TgvviVvuStX6

## Regras de trabalho
- Partir sempre da versão mais recente, manter nomes e mecânicas existentes.
- Testar no navegador (o Claude usa Playwright) antes de publicar. Verificar se não há erros no console.
- Novos sprites: salvar o PNG original em `assets/` na subpasta certa, e embutir uma cópia reduzida no jogo.
- Save fica no localStorage `chao-de-fabrica-v2` (S.v = 2). Saves v1 foram apagados de propósito quando forno e prensa passaram a ocupar 2 casas.

## Mapa e terreno
- Casa (tile) T = 32 px. Mapa 128×88 casas, dividido em 8×8 lotes de 16×11. Começa com os 4 lotes do meio; lote novo só se encostar num lote seu; preço 400 + 300 por lote extra + 150 por distância.
- Terreno original 64×44 no canto noroeste (W0/H0); expansão a leste e ao sul com jazidas espaçadas (15+ casas entre centros).
- Rio no leste: só Ponte (caminhão) e Túnel (esteira) passam.
- Chão procedural pela semente do jogo: texturas de terra e grama geradas no código com as cores da imagem de referência, manchas de grama por ruído fbm, rio azul com barranco. Enfeites (capim, flor, arbusto, pedrinha, rocha) são só visuais e não bloqueiam construção.

## Produção
- Minérios: ferro, cobre, areia, carvão. Extrator só sobre jazida.
- Forno (2×1): lingote de ferro, lingote de cobre, vidro, aço (pesquisa). Escolhe a receita pelo primeiro item.
- Prensa (2×1): chapa, parafusos. Trefila: fio de cobre.
- Montadora (3×2): motor, lâmpada, estrutura, ventilador, placa de circuito (pesquisa), geladeira (pesquisa).
- Item fora da receita trava a máquina (botão Destravar).
- Hub central 4×4: único ponto de venda, um só, 4 portas fixas. Preço cai um pouco a cada venda do mesmo item e se recupera com o tempo.

## Logística
- Esteiras lenta/normal/rápida (R$ 2/8/20, velocidade 1×/2×/3×). Túnel até 6 casas.
- Divisor (com lado prioritário), Unificador, Filtro.
- Doca + caminhão (300 itens), até 3 paradas e frete de volta para a Recepção encostada na doca. Frota de até 4 caminhões por doca, Garagem 2×2.
- Contêiner (2 casas, 250 itens de um tipo), Armazém 4×4 (2.000 itens, saídas configuráveis, "qualquer item").
- Ruas com curvas e retorno; Ponte passa sobre esteiras e rio.

## Energia e água
- Hub dá 15 MW grátis. Usina a carvão 2×2: 20 MW (cada carvão = 4 s). Começa com 10 carvões.
- Bomba d'água (encosta no rio) + Canos: usina com água gera 40 MW com o mesmo carvão. Cada bomba abastece até 2 usinas.
- Hidrelétrica 2×2 na beira do rio: 12 MW fixos.
- Postes ligam a até 8 casas e alimentam máquinas a até 3 casas. 10 minutos de ligação provisória no começo.
- Usina, garagem e hidrelétrica giram no próprio centro. Hub, poste, bomba e cano não giram.

## Progressão
- 7 contratos fixos liberam prensa, trefila e montadora. Depois vêm contratos sem fim, cada vez maiores, com prazo e bônus.
- Esteiras: sprites em assets/esteiras (1 amarela = lenta, 2 vermelha = normal, 3 azul = rápida). A curva é gerada no código dobrando o sprite reto (gerarCurvaEst).
- Pesquisa (tecla J), com pontos de vendas (1 a cada R$ 20) e de contratos (10): esteira normal e rápida, usina, bomba e canos, túnel, armazém, garagem, aço, hidrelétrica, placa de circuito, geladeira.

## Interface
- Minimapa (M), desfazer (Ctrl+Z), alertas (⚠), camada de fluxo (O), estatísticas (I), área para copiar, colar e demolir (V), moldes salvos.

## Ideias que ficaram para depois
- Ramal ferroviário, semáforo, sensor de esteira, tutorial, custo de manutenção.
- Separar o código em vários arquivos (projeto no VS Code + GitHub).
