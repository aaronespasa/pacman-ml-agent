import arff

DATA_NAMES = [
    "test_othermaps_keyboard",
    "test_othermaps_tutorial1",
    "test_samemaps_keyboard",
    "test_samemaps_tutorial1",
    "training_keyboard",
    "training_tutorial1"
]

f1 = open(f"./data/present/{DATA_NAMES[0]}.arff", "a")
f2 = open(f"./data/present/{DATA_NAMES[1]}.arff", "a")
f3 = open(f"./data/present/{DATA_NAMES[2]}.arff", "a")
f4 = open(f"./data/present/{DATA_NAMES[3]}.arff", "a")
f5 = open(f"./data/present/{DATA_NAMES[4]}.arff", "a")
f6 = open(f"./data/present/{DATA_NAMES[5]}.arff", "a")

for row in arff.load(f"./data/future/{DATA_NAMES[0]}.arff"):
    f1.write(f"{row.numActions},{row.pacmanX},{row.pacmanY},{row.directionPossible},{row.ghostX},{row.ghostY},{row.nearestGhostDistance},{row.numFood},{row.distFood},{row.score},{row.directionTaken}\n")

for row in arff.load(f"./data/future/{DATA_NAMES[1]}.arff"):
    f2.write(f"{row.numActions},{row.pacmanX},{row.pacmanY},{row.directionPossible},{row.ghostX},{row.ghostY},{row.nearestGhostDistance},{row.numFood},{row.distFood},{row.score},{row.directionTaken}\n")

for row in arff.load(f"./data/future/{DATA_NAMES[2]}.arff"):
    f3.write(f"{row.numActions},{row.pacmanX},{row.pacmanY},{row.directionPossible},{row.ghostX},{row.ghostY},{row.nearestGhostDistance},{row.numFood},{row.distFood},{row.score},{row.directionTaken}\n")

for row in arff.load(f"./data/future/{DATA_NAMES[3]}.arff"):
    f4.write(f"{row.numActions},{row.pacmanX},{row.pacmanY},{row.directionPossible},{row.ghostX},{row.ghostY},{row.nearestGhostDistance},{row.numFood},{row.distFood},{row.score},{row.directionTaken}\n")

for row in arff.load(f"./data/future/{DATA_NAMES[4]}.arff"):
    f5.write(f"{row.numActions},{row.pacmanX},{row.pacmanY},{row.directionPossible},{row.ghostX},{row.ghostY},{row.nearestGhostDistance},{row.numFood},{row.distFood},{row.score},{row.directionTaken}\n")

for row in arff.load(f"./data/future/{DATA_NAMES[5]}.arff"):
    f6.write(f"{row.numActions},{row.pacmanX},{row.pacmanY},{row.directionPossible},{row.ghostX},{row.ghostY},{row.nearestGhostDistance},{row.numFood},{row.distFood},{row.score},{row.directionTaken}\n")

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
