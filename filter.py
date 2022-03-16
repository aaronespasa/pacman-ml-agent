import arff

f1 = open('test_othermaps_keyboard_present.arff', "a")
f2 = open('filter_data_pacman_manual2.arff', "a")

for row in arff.load('all_data_pacman.arff'):
    f1.write(f"{row.pacmanX},{row.pacmanY},{row.ghostX},{row.ghostY},{row.directionTaken}\n")
    f2.write(f"{row.pacmanX},{row.pacmanY},{row.directionPossible},{row.ghostX},{row.ghostY},{row.nearestGhostDistance},{row.score},{row.directionTaken}\n")

f1.close()
f2.close()