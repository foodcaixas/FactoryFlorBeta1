# Prompts de sprites: petróleo e combustível

Como usar: cole o **Estilo base** de `sprites.md` e, logo depois, o prompt da peça. Gere uma peça por vez e salve o PNG na pasta indicada.

Estes prédios são da indústria (não militares), então usam a paleta normal do estilo base: vermelho, cinza-chumbo e amarelo. Se quiser que fiquem com cara de base militar, troque a linha "Palette" pela paleta verde-oliva do plano militar.

Regras que valem para todos:
- Vista de cima, reta, sem perspectiva, fundo transparente, sem texto nem logotipo.
- A peça ocupa a imagem inteira, na proporção indicada.
- **Frente = lado direito** (é para onde o jogo gira a saída). Seta amarela pequena apontando para a direita na saída, quando a peça tiver saída.

---

## 1. Extrator de petróleo — 2×2 (quadrado) → `assets/maquinas/extrator-petroleo.png`

O braço do cavalo-de-pau é animado pelo jogo por cima do sprite, então a imagem é só a **base, sem o braço**.

```
An oil well pumpjack base pad seen from directly above, square 1:1, WITHOUT the walking beam arm (the arm is animated separately). Concrete pad with yellow and black hazard edge, a tall A-frame samson post standing in the middle, a gearbox with a round crank wheel and counterweight on the left side, the wellhead with valves and a dark oil pipe stub on the bottom-right corner, a small dark oil stain on the ground. Red housing details, charcoal steel frame, yellow corner brackets.
```

## 2. Refinaria — 3×2 (retrato, 2:3, mais alta que larga) → `assets/maquinas/refinaria.png`

Recebe petróleo por cano em qualquer lado e solta pela porta do meio do lado direito.

```
A compact oil refinery unit seen from above, portrait rectangle 2:3 (taller than wide). Two round white storage tanks on the left side, top and bottom, connected by silver pipes to a tall distillation column in the center (round top with a ladder ring), heat exchanger pipes, and a small flare stack with a tiny orange flame. Output hatch in the middle of the RIGHT edge with a small yellow arrow pointing right. Red and charcoal frame, yellow corner brackets, small cyan indicator lights.
```

## 3. Doca de Fluidos — 3×2 (retrato, 2:3) → `assets/maquinas/doca-fluidos.png`

Tanque que enche caminhões, recebe por cano e solta barris pela porta do meio da direita. Fica encostada numa rua.

```
A fuel loading dock seen from above, portrait rectangle 2:3 (taller than wide). A big horizontal cylindrical fuel tank lying lengthwise in the center (white with an orange stripe), a vertical level gauge on its side, a loading arm with a hose reaching to the RIGHT edge, a small pallet with two orange fuel barrels next to the output, yellow and black hazard stripes along the right edge. Grey concrete base, charcoal frame, yellow corner brackets.
```

## 4. Posto de combustível — 2×2 (quadrado) → `assets/maquinas/posto.png`

Encosta numa rua e abastece 2 caminhões ao mesmo tempo.

```
A small truck fuel station seen from above, square 1:1. A flat white canopy roof covering most of the tile with an orange stripe across it, two fuel pumps visible at the bottom edge under the canopy, painted parking lines, a small underground tank lid with a level gauge, grey asphalt ground with yellow edge markings. Clean, no brand, no text.
```

## 5. Gerador a diesel — 2×2 (quadrado) → `assets/maquinas/gerador-diesel.png`

Queima combustível para dar energia onde não chega carvão.

```
An industrial diesel generator set seen from above, square 1:1. A long boxy engine enclosure with ventilation louvers, a big round radiator fan grille on one end, an exhaust stack with a dark cap on the other end, a small fuel tank and a control panel with amber lights on the side, thick power cables leaving from one corner. Red enclosure, charcoal frame, yellow corner brackets.
```

---

Depois de gerar, mande as imagens aqui e eu troco os desenhos no jogo.
