# Padrão de sprites — Chão de Fábrica

Plano completo: https://claude.ai/artifact/6q83ScgGrNjcAtoRK35pzg · Bancada de Sprites: https://claude.ai/artifact/YFz6AmvXdmCB7AmcnW5B9V

## Regras

- Vista reta de cima (planta). Nada de lateral, pés ou cabos pendurados.
- **128 px por casa** (2×1 = 256×128, 2×2 = 256×256, 2×3 = 256×384, 4×4 = 512×512).
- A placa da máquina vai até a borda; fundo transparente.
- Contorno preto `#1a1a1d` de 4 px. Luz de cima à esquerda. Sem sombra jogada (o jogo desenha).
- Moldura cinza-chumbo `#3b3f46` com cantoneiras amarelas `#f5c518` em todas as máquinas.
- Cor de destaque por categoria: produção `#e23a26`, petróleo/fluidos `#f08a24`, energia `#2f7fd1`, militar `#5b6b3a`.
- Frente (saída) sempre à direita. O jogo gira a peça.
- **Boca de esteira**: 76 px (60% da casa) no meio da borda, 19 px para dentro. Saída com setinha amarela.
- **Cano**: o sprite sai sem flange; o jogo desenha a flange onde o cano encostar. Só o extrator de petróleo tem saída fixa (ciano no gabarito).

## Gabaritos

Ficam em `assets/gabaritos/` (gere de novo com `python ferramentas/gerar_gabaritos.py`).
Cinza = placa da máquina, magenta = boca de esteira, ciano = saída de cano.
A Bancada de Sprites (`ferramentas/bancada-sprites.html`) também baixa os gabaritos.

## Passo a passo

1. Abra o Gemini (ou o ChatGPT) e anexe, nesta ordem: o gabarito da máquina, `assets/maquinas/forno.png` e `assets/maquinas/prensa.png`.
2. Cole o prompt abaixo trocando `[ACCENT]` e a descrição.
3. Jogue o resultado na Bancada de Sprites: ela tira o fundo, corta, ajusta para 128 px por casa e dá o laudo (proporção, paleta, marcas, bocas).
4. Salve em `assets/maquinas/` e peça ao Claude para encaixar no jogo.

## Prompt para máquina nova

```
Image 1 is a layout template. Images 2 and 3 are finished sprites from my game: copy their art style exactly.
Draw a NEW machine sprite on top of image 1, following it strictly:
- Same canvas size and aspect ratio as image 1. The machine base plate fills the grey area edge to edge. Everything outside it stays transparent.
- Orthographic top-down view, seen from directly above. No side walls, no legs, no hanging cables, no perspective, no cast shadow.
- Thick black outline, chunky hard-edged shapes, flat shading with small highlights, light from the top-left.
- Charcoal grey frame (#3b3f46) with yellow corner brackets (#f5c518), exactly like images 2 and 3. Accent color: [ACCENT].
- Belt ports: draw a conveyor opening exactly inside each magenta rectangle, with a grey frame and black-and-yellow hazard trim. Output ports get a small yellow arrow pointing outward.
- Leave the cyan circles plain (the game draws pipe flanges there). Do not draw pipe stubs anywhere else.
- Remove the magenta and cyan marks and the grid lines from the final image.
- No text, letters or logos. Realistic modern industrial equipment, no sci-fi.
The machine is: [DESCRIPTION]
```

`[ACCENT]`: `red (#e23a26)` produção · `orange (#f08a24)` petróleo · `blue (#2f7fd1)` energia · `olive green (#5b6b3a)` militar.

## Prompt para refazer um sprite que já existe

Anexe: 1) gabarito, 2) o sprite antigo, 3) forno.

```
Redraw image 2 in the exact art style of image 3, on the layout of image 1.
Keep the same machine and the same main parts as image 2, but:
- convert it to a strict top-down view seen from directly above (no sides, no legs, no hanging cables);
- make the base plate fill the grey area of image 1 edge to edge, transparent outside;
- use the charcoal frame, yellow corner brackets and thick black outline of image 3;
- place belt ports only inside the magenta rectangles; leave the cyan circles plain;
- remove all template marks. No text, no logos.
```

## Se a IA errar

- Saiu com perspectiva: "Seen from directly above like a floor plan. I must not see any side of the machine."
- Mudou o estilo: "Keep the outline thickness and colors identical to image 3."
- Boca no lugar errado: "The ports must be exactly where the magenta rectangles are, nowhere else."
- Sobrou marca: "Remove the magenta and cyan marks."

## Fila para refazer (fase 3)

| Sprite | Gabarito | Destaque |
| --- | --- | --- |
| Gerador a diesel | 2x2-sem-portas | laranja |
| Doca de fluidos | doca-fluidos | laranja |
| Extrator de petróleo (base, sem o braço) | extrator-petroleo | laranja |
| Posto de combustível | 2x2-sem-portas | laranja |
| Torno CNC | torno-cnc | oliva |
| Galpão de veículos | galpao-veiculos | oliva |

Quando encaixar um sprite novo no jogo, o Claude ajusta o desenho no código (alguns sprites antigos, como a montadora, são desenhados girados).
