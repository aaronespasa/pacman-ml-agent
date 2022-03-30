"""
Remember to first install the library arff:
$ pip install arff

The filter DOES NOT ADD THE HEADER
"""
import arff

def getRowString(
    directionPossible,
    ghostX,
    ghostY,
    nearestGhostDistance,
    directionTaken,
):
    """
    Returns a string with the row of the arff file
    """
    row = ""
    row += str(directionPossible) + ","
    row += str(ghostX) + ","
    row += str(ghostY) + ","
    row += str(nearestGhostDistance) + ","
    row += str(directionTaken) + "\n"
    return row

f1 = open(f"training_tutorial1_modified.arff", "a")

for row in arff.load(f"training_tutorial1.arff"):
    f1.write(
        getRowString(
            row.directionPossible,
            row.ghostX,
            row.ghostY,
            row.nearestGhostDistance,
            row.directionTaken
        )
    )

f1.close()