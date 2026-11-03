# Prompts de sprites — Chão de Fábrica

Como usar: cole o **Estilo base** e, logo depois, o prompt da peça. Gere uma peça por vez.
Os prompts estão em inglês porque os geradores de imagem (ChatGPT/DALL·E, Midjourney, Leonardo, etc.) obedecem melhor assim.
Depois de gerar, salve o PNG na pasta indicada em `assets/` e peça ao Claude Code: "troque o desenho do X pelo sprite assets/.../x.png".

Regras que valem para todos (o jogo depende disso):
- Vista **de cima (top-down) e reta**, sem perspectiva e sem sombra projetada para fora.
- **Fundo transparente** (ou preto puro, que eu recorto).
- A peça ocupa a imagem inteira, sem margem grande. Proporção exata do tamanho em casas (1×1 = quadrado, 2×1 = 2:1, 3×2 = 3:2, 4×4 = quadrado).
- **Entrada à esquerda, saída à direita** (seta amarela apontando para a direita). O jogo gira a peça sozinho.
- Sem texto, sem letras, sem logotipos.

---

## Estilo base (cole sempre antes)

```
Top-down 2D game sprite, orthographic view from directly above, no perspective, transparent background.
Cartoon industrial style with thick black outlines, chunky hard-edged shapes, slightly pixel-art look, clean flat shading with small highlights.
Palette: bright red (#e23a26) panels, dark charcoal grey (#3b3f46) frames and bolted blocks, warning yellow (#f5c518) corner brackets and trims, polished silver pipes, small cyan or orange indicator lights.
Realistic modern factory equipment, no sci-fi, no aliens, no glowing magic. No text, no letters, no logos.
Symmetric, readable at small size (64 px per tile). Input side on the LEFT, output side on the RIGHT marked by a small yellow arrow pointing right.
```

---

## 1. Prioridade alta (aparecem o tempo todo)

### Extrator — 1×1 → `assets/maquinas/extrator.png`
```
A compact mining drill seen from above, square 1:1. Central round drill head with steel bit and gear teeth, red housing, yellow corner brackets, small exhaust vent, output arrow on the right edge.
```

### Esteira — 1×1, 3 níveis → `assets/esteiras/esteira-1.png`, `-2.png`, `-3.png`
```
Seamless conveyor belt tile seen from above, square 1:1, belt running left to right. Dark rubber belt with horizontal ribs, metal side rails top and bottom with bolts. Edges must tile perfectly when placed side by side.
Variant 1: yellow side rails. Variant 2: red side rails. Variant 3: blue side rails.
```
Dica: peça também "same tile, belt ribs shifted by 1/4" para fazer a animação (4 quadros).

### Trefila — 1×1 → `assets/maquinas/trefila.png`
```
Copper wire drawing machine seen from above, square 1:1. Copper bar entering from the left, a set of rollers and dies in the middle, a spool of shiny copper wire on the right. Red and grey housing, yellow trims.
```

### Divisor — 1×1 → `assets/logistica/divisor.png`
```
Conveyor splitter seen from above, square 1:1. Input from the left, three small yellow arrows pointing up, right and down. Grey metal box with a rotating red diverter paddle in the center.
```

### Unificador — 1×1 → `assets/logistica/unificador.png`
```
Conveyor merger seen from above, square 1:1. Three inputs (left, top, bottom) converging into one output on the right with a yellow arrow. Grey metal box, red funnel plate in the center.
```

### Filtro — 1×1 → `assets/logistica/filtro.png`
```
Conveyor sorter seen from above, square 1:1. Input on the left, straight output on the right with a yellow arrow, side output at the top with a green arrow. Small sensor eye with a cyan light in the middle, grey and red casing.
```

### Poste — 1×1 → `assets/energia/poste.png`
```
Electric utility pole seen from directly above, square 1:1, small footprint in the center. Round wooden or concrete pole top with a grey crossarm and white ceramic insulators, yellow warning base plate.
```

---

## 2. Energia e água

### Bomba d'água — 1×1 → `assets/energia/bomba-agua.png`
```
Water pump seen from above, square 1:1. Blue pump motor with silver pipe flanges, an intake pipe on the left (towards the river) and a blue-ringed outlet on the right. Grey base plate, yellow corners.
```

### Cano de água — peças 1×1 → `assets/energia/cano-reto.png`, `cano-curva.png`, `cano-t.png`, `cano-cruz.png`
```
Water pipe tile seen from above, square 1:1, silver steel pipe with blue rings at the joints. Four separate sprites: straight (left to right), elbow (left to top), T junction (left, right, top), cross (all four sides). Pipe ends must touch the exact middle of each edge so tiles connect.
```

### Hidrelétrica — 2×2 → `assets/energia/hidreletrica.png`
```
Small hydroelectric power station seen from above, square 1:1 covering 2x2 tiles. Concrete dam wall on the left side with water intake gates, two round turbine housings in the middle, a red generator hall and a yellow electric symbol panel. Blue water channel on the left edge.
```

---

## 3. Logística e caminhões

### Hub central — 4×4 → `assets/logistica/hub.png`
```
Central distribution depot seen from above, square 1:1 covering 4x4 tiles. Large flat roof with red and grey panels, skylights, a yellow helipad-style circle with a box icon in the center, loading bays on all four sides with yellow arrows pointing inward, rooftop AC units.
```

### Garagem — 2×2 → `assets/logistica/garagem.png`
```
Truck garage seen from above, square 1:1 covering 2x2 tiles. Grey roof with two red roll-up doors on the right edge, yellow parking lines, small office block in a corner, rooftop vents.
```

### Doca de carga — 1×1 → `assets/logistica/doca.png`
```
Truck loading dock seen from above, square 1:1. Grey concrete platform with yellow and black hazard stripes on the right edge, a red rubber bumper, a small roller conveyor entering from the left.
```

### Recepção — 1×1 → `assets/logistica/recepcao.png`
```
Truck unloading station seen from above, square 1:1. Grey concrete platform with hazard stripes on the left edge (truck side), roller conveyor leaving to the right with a yellow arrow, small green status light.
```

### Túnel de esteira — 1×1 → `assets/logistica/tunel.png`
```
Underground conveyor entrance seen from above, square 1:1. Belt from the left going down into a dark square hole framed by a thick grey concrete portal with yellow hazard stripes.
```

### Rua e ponte — 1×1 → `assets/terreno/rua-*.png`, `ponte.png`
```
Asphalt road tile seen from above, square 1:1, dark grey asphalt with subtle texture, dashed white center line. Separate sprites: straight, curve, T junction, cross. Must tile seamlessly.
Bridge variant: same road on a raised concrete deck with grey guard rails along both sides and visible shadow underneath.
```

---

## 4. Petróleo (para quando implementar o `petroleo.md`)

### Jazida de petróleo — 1×1, decalque no chão → `assets/terreno/jazida-petroleo.png`
```
Oil seep on the ground seen from above, square 1:1, black glossy oil puddle with dark brown stained soil around it, a few bubbles. Transparent background, no outline box.
```

### Bomba de petróleo (cavalo-mecânico) — 2×2 → `assets/petroleo/bomba-oleo.png`
```
Oil pumpjack seen from directly above, square 1:1 covering 2x2 tiles. Long walking beam with a horse-head end, red counterweight crank, grey concrete base pad, yellow safety rails, wellhead pipe and a black oil outlet on the right.
```
Dica: gere 2 quadros (braço para cima / para baixo) para animar.

### Oleoduto — peças 1×1 → `assets/petroleo/oleoduto-*.png`
```
Same as the water pipe tiles but the pipe is dark grey steel with BLACK and yellow rings at the joints. Straight, elbow, T, cross.
```

### Refinaria — 3×2 → `assets/petroleo/refinaria.png`
```
Compact oil refinery seen from above, aspect ratio 3:2 covering 3x2 tiles. Two tall round distillation columns, a row of small round tanks, a tangle of silver pipes, a flare stack with a small orange flame, red and grey platforms with yellow catwalks. Black oil input on the left, two outputs on the right with yellow arrows.
```

### Tanque — 2×2 → `assets/petroleo/tanque.png`
```
Cylindrical storage tank seen from directly above, square 1:1 covering 2x2 tiles. Round white-grey roof with radial seams, a yellow spiral stair at the edge, a red hatch, pipe connections on the left and right.
```

---

## 5. Ícones de itens (folha única) → `assets/itens/itens-atlas.png`

```
Sprite sheet of 21 small game item icons on a 6x4 grid (last 3 cells empty), each in its own square cell with equal spacing, transparent background, same cartoon style with thick black outlines, top-down slightly angled view.
Row 1: iron ore (rusty brown rocks), copper ore (green-blue rocks), sand pile, coal lumps, iron ingot, copper ingot.
Row 2: glass sheet, iron plate, pile of screws, copper wire spool, electric motor, light bulb.
Row 3: steel I-beam frame, desk fan, steel ingot (dark blue-grey), green circuit board, refrigerator, crude oil barrel (black).
Row 4: plastic pellets (white), fuel canister (red), electric cable reel (black with copper end), then 3 empty cells.
```

---

## Ordem sugerida
1. Extrator, esteira (3 cores) e trefila — são as peças mais vistas na tela.
2. Divisor, unificador, filtro, poste.
3. Hub e garagem.
4. Água e hidrelétrica.
5. Petróleo, quando for implementar.
6. Folha de itens.

---

## 6. Máquinas com boca de entrada e saída do tamanho da esteira

A esteira nova é larga: a faixa escura ocupa cerca de **60% da altura da casa** e os trilhos coloridos vão até a borda.
A boca das máquinas precisa ter esse mesmo tamanho para a esteira "encaixar".

**Como fazer no ChatGPT:** mande 2 imagens juntas, o sprite atual da máquina (ex.: `assets/maquinas/forno.png`) e uma esteira (ex.: `assets/esteiras/esteira-1-amarela.png`), e cole o bloco abaixo + o trecho da máquina.

### Bloco comum (cole sempre)
```
Redesign the first image (my machine sprite) keeping exactly the same art style, colors, outline thickness, top-down orthographic view, aspect ratio and transparent background. Only change the input and output ports so they match the conveyor belt in the second image.
Port rules:
- Each port is a wide rectangular opening flush with the outer edge of the sprite, centered on its tile.
- Port height = 60% of ONE tile (the dark belt width in the second image), with a thin dark grey metal frame and a black-and-yellow hazard trim around it.
- Inside the port: dark rubber belt (#2a2a2e) with the same horizontal grooves as the conveyor, going about 15% of a tile into the machine, so the conveyor looks like it continues inside.
- Output port: same size, with a small yellow arrow painted on the frame pointing outward. Input port: no arrow.
- Remove the old small round connectors on those sides. Keep everything else of the machine (furnace window, pipes, bolts) just shifted slightly toward the center to make room.
No text, no letters, no logos.
```

### Forno elétrico — 2×1 (proporção 2:1)
```
Machine size: 2 tiles wide, 1 tile tall. Input port on the LEFT edge, output port on the RIGHT edge. Both ports centered vertically. Keep the glowing furnace window in the middle and the round crucible on the right half.
```

### Prensa — 2×1 (proporção 2:1)
```
Machine size: 2 tiles wide, 1 tile tall. Input port on the LEFT edge, output port on the RIGHT edge, both centered vertically. Keep the press hammer block in the middle.
```

### Usina a carvão — 2×2 (quadrado)
```
Machine size: 2x2 tiles. Coal can arrive from any side: add one input port in the middle of EACH of the four sides (centered on one of the two tiles of that side, all four at the same relative position). No output port; keep the water pipe inlet (blue ring) and the lightning panel.
```

### Montadora — 3×2 (imagem em pé, proporção 2:3)
```
Machine size: 2 tiles wide, 3 tiles tall (portrait). Two input ports on the LEFT edge, centered on the top tile and on the bottom tile (none on the middle tile). One output port on the RIGHT edge, centered on the middle tile.
```

### Contêiner — 2×1 (proporção 2:1)
```
Machine size: 2 tiles wide, 1 tile tall. Input port on the LEFT edge, output port on the RIGHT edge, both centered vertically.
```

### Armazém central — 4×4 (quadrado)
```
Machine size: 4x4 tiles. Four input ports along the LEFT edge, one centered on each of the 4 tiles. Four output ports along the RIGHT edge, one centered on each tile.
```

Dica: se o ChatGPT mudar demais o desenho, peça "keep the original image almost identical, only edit the ports". Se a boca sair pequena, peça "make the ports 60% of the machine height" (para 2×1) ou "60% of half the height" (para 2×2).
