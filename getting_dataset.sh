#!/bin/bash

for i in {1..5} ; do
    python3 busters.py -g RandomGhost -p BasicAgentAA -l trickyClassic
    PID="$!"
    tail --pid=PID -f /dev/null
done

for i in {1..5} ; do
    python3 busters.py -g RandomGhost -p BasicAgentAA -l newmap
    PID="$!"
    tail --pid=PID -f /dev/null
done

for i in {1..5} ; do
    python3 busters.py -g RandomGhost -p BasicAgentAA -l testClassic
    PID="$!"
    tail --pid=PID -f /dev/null
done

for i in {1..5} ; do
    python3 busters.py -g RandomGhost -p BasicAgentAA -l sixHunt
    PID="$!"
    tail --pid=PID -f /dev/null
done

for i in {1..5} ; do
    python3 busters.py -g RandomGhost -p BasicAgentAA -l 20Hunt
    PID="$!"
    tail --pid=PID -f /dev/null
done