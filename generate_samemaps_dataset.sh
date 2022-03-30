#!/bin/bash

# The dataset will be created under the name self.filename defined
# in the constructor of the class Game (see game.py file).

# Two agents: BasicAgentAA and BustersKeyboardAgent
agentName="BasicAgentAA"

for i in {1..10} ; do
    python3 busters.py -g RandomGhost -p $agentName -l trickyClassic
    python3 busters.py -g RandomGhost -p $agentName -l newmap
    python3 busters.py -g RandomGhost -p $agentName -l testClassic
    python3 busters.py -g RandomGhost -p $agentName -l sixHunt
    python3 busters.py -g RandomGhost -p $agentName -l 20Hunt
done
