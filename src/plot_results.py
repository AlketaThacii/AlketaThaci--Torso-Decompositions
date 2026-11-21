import csv
from pathlib import Path

import matplotlib.pyplot as plt


project_folder = Path(__file__).resolve().parent.parent
results_folder = project_folder / "results"
reports_folder = project_folder / "reports"
reports_folder.mkdir(exist_ok=True)

datasets = ["small", "medium", "large"]
methods = [
    "Randomized Min-Degree",
    "Bounded Min-Fill",
    "Minimum Degree"
]

best_widths = {method: [] for method in methods}
runtimes = {method: [] for method in methods}

for dataset in datasets:
    csv_file = results_folder / f"{dataset}-experiment.csv"

    if not csv_file.exists():
        raise SystemExit(f"Nuk u gjet skedari: {csv_file}")

    with csv_file.open("r", newline="", encoding="utf-8") as file:
        rows = csv.DictReader(file)

        for row in rows:
            method = row["method"]
            best_widths[method].append(
                int(row["best_width_at_t0"])
            )
            runtimes[method].append(
                float(row["time_seconds"])
            )

positions = list(range(len(datasets)))
bar_width = 0.24

figure, (width_axis, time_axis) = plt.subplots(
    1,
    2,
    figsize=(12, 5)
)

for index, method in enumerate(methods):
    offset = (index - 1) * bar_width
    method_positions = [
        position + offset
        for position in positions
    ]

    width_axis.bar(
        method_positions,
        best_widths[method],
        bar_width,
        label=method
    )

    time_axis.bar(
        method_positions,
        runtimes[method],
        bar_width,
        label=method
    )

width_axis.set_title("Gjerësia më e mirë për t = 0")
width_axis.set_ylabel("Gjerësia")
width_axis.set_xticks(positions)
width_axis.set_xticklabels(datasets)
width_axis.legend()

time_axis.set_title("Koha e ekzekutimit")
time_axis.set_ylabel("Sekonda")
time_axis.set_xticks(positions)
time_axis.set_xticklabels(datasets)
time_axis.set_yscale("log")
time_axis.legend()

figure.tight_layout()

output_file = reports_folder / "heuristic-comparison.png"
figure.savefig(output_file, dpi=160)
print(f"Grafiku u ruajt te: {output_file}")