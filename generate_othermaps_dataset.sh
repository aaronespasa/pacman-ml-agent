#!/bin/bash

# The dataset will be created under the name self.filename defined
# in the constructor of the class Game (see game.py file).

# Two agents: BasicAgentAA and BustersKeyboardAgent
agentName="BasicAgentAA"

for i in {1..5} ; do
    python3 busters.py -g RandomGhost -p $agentName -l openHunt
    python3 busters.py -g RandomGhost -p $agentName -l myLaberint
    python3 busters.py -g RandomGhost -p $agentName -l classic
    python3 busters.py -g RandomGhost -p $agentName -l oneHunt
    python3 busters.py -g RandomGhost -p $agentName -l openClassic
done
