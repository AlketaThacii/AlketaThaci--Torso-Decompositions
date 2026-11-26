import json
from pathlib import Path
from graph import lexo_grafin
from elimination import krijo_fqinjet, llogarit_gjeresite


PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_FOLDER / "data"
RESULTS_FOLDER = PROJECT_FOLDER / "results"

DATASETS = ["small", "medium", "large"]
EXPECTED_CHALLENGE = "spoc-3-torso-decompositions"


def get_number_of_nodes(graph_file):
    edges = []

    with graph_file.open("r", encoding="utf-8") as file:
        for line in file:
            values = line.split()

            if len(values) == 2:
                edges.append((int(values[0]), int(values[1])))

    if not edges:
        raise ValueError(f"Nuk u gjetën brinjë në {graph_file}")

    return max(max(left, right) for left, right in edges) + 1


def validate_dataset(dataset):
    graph_file = DATA_FOLDER / f"{dataset}.gr"
    json_file = RESULTS_FOLDER / f"{dataset}-submission.json"

    if not graph_file.exists():
        raise FileNotFoundError(f"Mungon grafi: {graph_file}")

    if not json_file.exists():
        raise FileNotFoundError(f"Mungon rezultati: {json_file}")

    
    number_of_nodes, edges = lexo_grafin(graph_file)
    adjacency = krijo_fqinjet(number_of_nodes, edges)

    with json_file.open("r", encoding="utf-8") as file:
        content = json.load(file)

    if not isinstance(content, list) or len(content) != 1:
        raise ValueError(
            f"{json_file.name}: pritej një listë me një objekt."
        )

    submission = content[0]

    if submission.get("challenge") != EXPECTED_CHALLENGE:
        raise ValueError(
            f"{json_file.name}: emri i challenge nuk është i saktë."
        )

    if submission.get("problem") != f"{dataset}-graph":
        raise ValueError(
            f"{json_file.name}: emri i problem-it nuk është i saktë."
        )

    vectors = submission.get("decisionVector")

    if not isinstance(vectors, list) or not vectors:
        raise ValueError(
            f"{json_file.name}: decisionVector duhet të ketë zgjidhje."
        )

    if len(vectors) > 20:
        raise ValueError(
            f"{json_file.name}: ka më shumë se 20 zgjidhje."
        )

    for index, vector in enumerate(vectors, start=1):
        if not isinstance(vector, list):
            raise ValueError(
                f"Zgjidhja {index} në {json_file.name} nuk është listë."
            )

        if len(vector) != number_of_nodes + 1:
            raise ValueError(
                f"Zgjidhja {index}: pritej gjatësi "
                f"{number_of_nodes + 1}, por u gjet {len(vector)}."
            )

        if any(type(value) is not int for value in vector):
            raise ValueError(
                f"Zgjidhja {index}: të gjitha vlerat duhet të jenë numra të plotë."
            )

        order = vector[:-1]
        threshold = vector[-1]

        if sorted(order) != list(range(number_of_nodes)):
            raise ValueError(
                f"Zgjidhja {index}: renditja nuk i përmban "
                "të gjitha nyjet nga një herë."
            )

        if not 0 <= threshold < number_of_nodes:
            raise ValueError(
                f"Zgjidhja {index}: pragu t është jashtë kufijve."
            )
        widths = llogarit_gjeresite(adjacency, order)
        actual_width = widths[threshold]

        if actual_width > 500:
            raise ValueError(
                f"Zgjidhja {index}: gjerësia {actual_width} "
                "e tejkalon kufirin 500 të evaluatorit."
            )

    print(
        f"OK: {json_file.name} — "
        f"{len(vectors)} zgjidhje të vlefshme, "
        f"{number_of_nodes} nyje."
    )


def main():
    for dataset in DATASETS:
        validate_dataset(dataset)

    print("Kontrolli strukturor i të gjitha rezultateve përfundoi me sukses.")


if __name__ == "__main__":
    main()