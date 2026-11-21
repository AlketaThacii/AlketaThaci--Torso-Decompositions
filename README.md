# Torso Decompositions

Projekt për zgjidhjen dhe analizimin e problemit **Torso Decompositions** të sfidës SpOC 3 të Agjencisë Evropiane të Hapësirës (ESA).

## Përshkrimi i problemit

Grafi përbëhet nga nyje dhe brinjë. Programi provon renditje të ndryshme për eliminimin e nyjeve. Kur eliminohet një nyje, fqinjët e saj lidhen mes vete me brinjë të reja (*fill-in edges*).

Një zgjidhje përbëhet nga:

- një renditje e nyjeve;
- një prag `t`.

Programi llogarit objektivat për pragje të ndryshme dhe ruan zgjidhje të mira në formatin JSON të sfidës. Vlerësuesi zyrtar i kthen objektivat si shkalla maksimale e torso-s pas pragut dhe vlera e pragut.

## Metodat

Projekti krahason tri metoda:

- **Randomized Min-Degree:** zgjedh nyjen me më së paku fqinjë. Në barazim zgjedh rastësisht. Përdor 30 prova dhe farën `42`.
- **Bounded Min-Fill:** shqyrton tetë nyjet me shkallën më të vogël dhe zgjedh atë që kërkon më pak brinjë të reja. Numri i provave varet nga madhësia e grafit.
- **Minimum Degree:** zgjedh nyjen me më së paku fqinjë; në barazim zgjedh nyjen me numrin më të vogël. Ekzekutohet një herë.

Për të kufizuar kohën e llogaritjes, Bounded Min-Fill shqyrton vetëm tetë kandidatë në çdo hap. Prandaj është një variant i kufizuar i metodës Min-Fill.

## Struktura e projektit

```text
Torso-Decompositions/
├── data/        grafët hyrës në formatin .gr
├── reports/     grafiku dhe analiza e rezultateve
├── results/     skedarët JSON dhe CSV
├── src/         kodi Python
├── requirements.txt
└── README.md
```

## Instalimi

Kërkohet Python. Biblioteka shtesë për krijimin e grafikut është `matplotlib`.

Nga folderi kryesor i projektit, instalo varësinë me:

```powershell
py -m pip install -r requirements.txt
```

## Ekzekutimi

Nis komandat nga folderi kryesor i projektit:

```powershell
py src/main.py small
py src/main.py medium
py src/main.py large
```

Çdo komandë lexon grafın përkatës nga `data/` dhe krijon ose përditëson:

- `results/<grafi>-submission.json`
- `results/<grafi>-experiment.csv`

Për shembull, ekzekutimi i `small` krijon `results/small-submission.json` dhe `results/small-experiment.csv`.

Për të krijuar grafikun e krahasimit, ekzekuto:

```powershell
py src/plot_results.py
```

Grafiku ruhet te `reports/heuristic-comparison.png`. Ky skript kërkon që CSV-të për `small`, `medium` dhe `large` të jenë krijuar paraprakisht.

## Rezultatet dhe analiza

Analiza eksperimentale gjendet te `reports/results-analysis.md`. Ajo përmbledh gjerësinë për `t = 0`, kohën dhe numrin e provave për secilën metodë.

Skedarët JSON përmbajnë deri në 20 decision vectors. Secili vector përmban renditjen e nyjeve dhe pragun `t`. Programi kontrollon që renditja përmban secilën nyje një herë dhe që pragu është brenda kufijve.

## Kufizimet

- Metodat janë heuristika dhe nuk garantojnë gjetjen e zgjidhjes optimale.
- Numri i provave ndryshon sipas metodës dhe grafit; kohët totale nuk janë krahasim me buxhet të barabartë.
- Tabela eksperimentale paraqet gjerësinë për `t = 0`. JSON-et përmbajnë zgjidhje edhe për pragje të tjera.
- Bounded Min-Fill kontrollon vetëm tetë kandidatë për të kufizuar kohën e ekzekutimit.

## Burimet

- [Sfida Torso Decompositions në Optimise](https://optimise.esa.int/challenge/spoc-3-torso-decompositions/About)
- [Kodi zyrtar i vlerësimit për small graph](https://api.optimize.esa.int/media/problems/spoc-3-torso-decompositions-small-graph-1711380312223.py)
- [Repo zyrtare e SpOC 3](https://github.com/esa/SpOC3)