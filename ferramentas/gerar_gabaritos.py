"""Gera os gabaritos dos sprites (128 px por casa) em assets/gabaritos/.

Cinza = placa da máquina (pintar até a borda). Magenta = boca de esteira.
Ciano = saída de cano fixa. Linhas = divisão das casas. Frente (saída) sempre à direita.
Uso: python ferramentas/gerar_gabaritos.py
"""
from pathlib import Path
from PIL import Image, ImageDraw

C = 128                      # px por casa
BOCA_L, BOCA_P = 76, 19      # boca: 60% da casa de largura, 15% de profundidade
FLANGE = 52                  # saída de cano: 40% da casa
CINZA, LINHA = (150, 154, 160, 255), (96, 100, 106, 255)
MAGENTA, CIANO = (255, 0, 255, 255), (0, 220, 255, 255)

# nome: (largura, altura em casas, bocas [(casa_x, casa_y, lado, sai)], canos [(casa_x, casa_y, lado)])
# lado: 'e' esquerda, 'd' direita, 'c' cima, 'b' baixo
MAQUINAS = {
    '1x1-generica':  (1, 1, [(0, 0, 'e', 0), (0, 0, 'd', 1)], []),
    'forno':         (2, 1, [(0, 0, 'e', 0), (1, 0, 'd', 1)], []),
    'prensa':        (2, 1, [(0, 0, 'e', 0), (1, 0, 'd', 1)], []),
    'torno-cnc':     (2, 1, [(0, 0, 'e', 0), (1, 0, 'd', 1)], []),
    'conteiner':     (2, 1, [(0, 0, 'e', 0), (1, 0, 'd', 1)], []),
    'montadora':     (2, 3, [(0, 0, 'e', 0), (0, 2, 'e', 0), (1, 1, 'd', 1)], []),
    'forno-industrial': (2, 3, [(0, 0, 'e', 0), (0, 2, 'e', 0), (1, 1, 'd', 1)], []),
    'refinaria':     (2, 3, [(1, 1, 'd', 1)], []),
    'doca-fluidos':  (2, 3, [(1, 1, 'd', 1)], []),
    'extrator':      (2, 2, [(1, 1, 'd', 1)], []),
    'extrator-petroleo': (2, 2, [], [(1, 1, 'd')]),
    '2x2-sem-portas': (2, 2, [], []),   # usina, gerador a diesel, posto, garagem: o jogo liga por qualquer lado
    'armazem':       (4, 4, [(0, y, 'e', 0) for y in range(4)] + [(3, y, 'd', 1) for y in range(4)], []),
    'galpao-veiculos': (5, 4, [(0, y, 'e', 0) for y in range(4)], []),
}

def boca(d, cx, cy, lado):
    x0, y0 = cx * C, cy * C
    if lado in 'ed':
        x = x0 if lado == 'e' else x0 + C - BOCA_P
        y = y0 + (C - BOCA_L) // 2
        d.rectangle([x, y, x + BOCA_P - 1, y + BOCA_L - 1], fill=MAGENTA)
    else:
        y = y0 if lado == 'c' else y0 + C - BOCA_P
        x = x0 + (C - BOCA_L) // 2
        d.rectangle([x, y, x + BOCA_L - 1, y + BOCA_P - 1], fill=MAGENTA)

def cano(d, cx, cy, lado):
    x0, y0, r = cx * C, cy * C, FLANGE // 2
    px, py = {'e': (x0, y0 + C // 2), 'd': (x0 + C, y0 + C // 2), 'c': (x0 + C // 2, y0), 'b': (x0 + C // 2, y0 + C)}[lado]
    d.ellipse([px - r, py - r, px + r, py + r], fill=CIANO)

def gerar(pasta):
    pasta.mkdir(parents=True, exist_ok=True)
    for nome, (w, h, bocas, canos) in MAQUINAS.items():
        im = Image.new('RGBA', (w * C, h * C), CINZA)
        d = ImageDraw.Draw(im)
        for i in range(1, w): d.line([(i * C, 0), (i * C, h * C)], fill=LINHA, width=2)
        for j in range(1, h): d.line([(0, j * C), (w * C, j * C)], fill=LINHA, width=2)
        for b in bocas: boca(d, *b[:3])
        for q in canos: cano(d, *q)
        # recorta o que passou da área (meia flange fica dentro)
        im.save(pasta / f'gabarito-{nome}.png')
        print(pasta / f'gabarito-{nome}.png', im.size)

if __name__ == '__main__':
    gerar(Path(__file__).resolve().parent.parent / 'assets' / 'gabaritos')
