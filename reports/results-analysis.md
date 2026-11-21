# Analiza e rezultateve

## Qëllimi

Në këtë projekt u krahasuan tri metoda për gjenerimin e renditjeve të eliminimit të nyjeve:

- **Randomized Min-Degree** zgjedh nyjen me shkallën më të vogël. Kur ka barazim, zgjedh rastësisht mes nyjeve kandidate.
- **Bounded Min-Fill** kontrollon tetë nyjet me shkallën më të vogël dhe zgjedh atë që krijon më pak lidhje të reja mes fqinjëve.
- **Minimum Degree** zgjedh nyjen me shkallën më të vogël. Në barazim, zgjedh nyjen me numrin më të vogël.

Për secilën renditje, u llogarit gjerësia për `t = 0`. U mat edhe koha e ekzekutimit. Programi ruan veçmas zgjidhjet Pareto në skedarët JSON.

## Rezultatet

| Grafi | Metoda | Numri i provave | Gjerësia më e mirë për t = 0 | Gjerësia mesatare për t = 0 | Koha totale |
|---|---|---:|---:|---:|---:|
| Small | Randomized Min-Degree | 30 | 20 | 21.37 | 4.82 s |
| Small | Bounded Min-Fill | 30 | 20 | 20.57 | 28.241 s |
| Small | Minimum Degree | 1 | 20 | 20.00 | 0.78 s |
| Medium | Randomized Min-Degree | 30 | 272 | 283.87 | 40.281 s |
| Medium | Bounded Min-Fill | 5 | 279 | 279.00 | 40.956 s |
| Medium | Minimum Degree | 1 | 285 | 285.00 | 6.394 s |
| Large | Randomized Min-Degree | 30 | 499 | 499.00 | 412.982 s |
| Large | Bounded Min-Fill | 1 | 499 | 499.00 | 131.768 s |
| Large | Minimum Degree | 1 | 499 | 499.00 | 114.645 s |

Gjerësia për `t = 0` është më e mirë kur vlera është më e vogël. Kufiri i përdorur nga vlerësuesi është 500; vlerat 499 në grafın `large` janë brenda këtij kufiri.

## Analiza

Për grafın `small`, të tria metodat arritën gjerësi minimale 20. Minimum Degree ishte më e shpejta në provën e vetme. Bounded Min-Fill pati mesatare pak më të ulët se Randomized Min-Degree, por mori më shumë kohë.

Për grafın `medium`, Randomized Min-Degree gjeti gjerësinë minimale më të ulët, 272. Minimum Degree mori më pak kohë, por prova e tij e vetme dha gjerësi 285. Bounded Min-Fill dha gjerësi 279 në pesë prova.

Për grafın `large`, të tria metodat gjetën gjerësi 499, një pikë nën kufirin 500. Randomized Min-Degree mori kohën më të gjatë, sepse kreu 30 prova. Bounded Min-Fill dhe Minimum Degree provuan secila vetëm një renditje.

Grafiku `heuristic-comparison.png` paraqet gjerësinë më të mirë dhe kohën totale për secilën metodë dhe graf.

## Kufizimet e krahasimit

Metodat nuk kryen të njëjtin numër provash për çdo graf. Prandaj koha totale dhe gjerësia më e mirë nuk janë krahasim me buxhet të barabartë. Metodat me më shumë prova patën më shumë mundësi të gjenin renditje më të mirë.

Bounded Min-Fill kontrollon vetëm tetë kandidatë me shkallën më të vogël, për të kufizuar kohën e llogaritjes. Kjo e bën metodën më të shpejtë se kontrollimi i të gjitha nyjeve, por mund ta pengojë të gjejë renditjen më të mirë.

Kjo tabelë krahason vetëm rezultatet për `t = 0`. Skedarët JSON përmbajnë zgjidhjet e përzgjedhura për pragje të ndryshme, të cilat paraqesin kompromisin mes dy objektivave të problemit.

## Përfundim

Eksperimentet tregojnë se asnjë metodë nuk është më e mira për të gjithë grafikët. Për `small`, të tria metodat gjetën gjerësi minimale 20. Për `medium`, Randomized Min-Degree gjeti rezultatin më të ulët, 272. Për `large`, të gjitha metodat gjetën 499, brenda kufirit 500 të vlerësuesit.

Minimum Degree ishte më i shpejti në këto eksperimente, por u ekzekutua vetëm një herë për çdo graf. Randomized Min-Degree përdori 30 prova dhe pati më shumë mundësi të gjente renditje të mira. Bounded Min-Fill mori më shumë kohë për provë, sidomos te `small`.

Rezultatet janë heuristike. Numri i provave ndryshoi mes metodave dhe analiza e tabelës mat vetëm gjerësinë për `t = 0`. Për krahasim më të drejtë në të ardhmen, metodat mund të ekzekutohen me të njëjtin kufi kohor. Zgjidhjet për pragje të ndryshme ruhen në JSON dhe paraqesin kompromisin mes objektivave të sfidës.

Si punë e ardhshme, mund të përmirësohet Bounded Min-Fill, të krahasohen metodat me buxhet të barabartë kohor dhe të kontrollohen decision vectors me vlerësuesin zyrtar të sfidës.

## Kontrollimi i skedarëve të dorëzimit

U ekzekutua kontrolluesi lokal me komandën `py src/validate_results.py`. Të tre skedarët JSON kaluan kontrollin strukturor:

| Skedari | Zgjidhje | Nyje |
|---|---:|---:|
| small-submission.json | 20 | 1357 |
| medium-submission.json | 20 | 1399 |
| large-submission.json | 20 | 2426 |

Kontrolluesi verifikoi formatin e JSON-it, emrat e sfidës dhe problemeve, numrin maksimal të zgjidhjeve, renditjen e nyjeve dhe kufijtë e pragut `t`. Ky është kontroll strukturor lokal; nuk është vlerësim nga platforma zyrtare e ESA-s.