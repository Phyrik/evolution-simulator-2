# evolution-simulator-2

The sequel to [evolution-simulator](https://github.com/Phyrik/evolution-simulator).

evolution-simulator-2 is an evolution simulator that simulates circular creatures.

Feel free to leave suggestion in issues under the enhancement tag!

## Setup

To play evolution-simulator-2 on a Windows PC simply download the ZIP file and run:

`gui2.exe`

To play evolution-simulator-2 on a Mac or Linux machine you must have [Python 3](https://python.org/downloads) and Pygame installed. I am working on a way to make the game run wihtout these dependencies and as an executable.

Download the repository's zip file and extract it. Open a terminal/command prompt and go to thr extracted folder. Run gui2.py in the terminal/command prompt with:

`python gui2.py`

## Gameplay

In evolution-simulator-2 you observe circular creatures try to navigate their life. They must eat food to gather energy, reproduce to pass on their genes, and kill others before they kill them.

On the first day 10 creatures are created.

Each big black dot is a creature or individual. Around each individual there are two rings. A blue one and a red one. The smaller blue ring is the **eating range** of that creature. Any food, a small black dot that gives the individual +1 energy, that exists within this ring is able to be eaten by the individual. This will happen unless another individual eats it first. The bigger red ring is the **vision range**. This is how far the individual can see and travel each turn. Each individual will go to where it thinks is the best position for it to be the next day.

The black number above each individual represents its **energy**. The amount of energy an individual has determines how much it can reproduce or kill each turn (**individuals do NOT require energy to eat food or move BUT 0.1 energy is taken off each individual each turn**).

Each individual needs and uses 4 energy to reproduce, and 7 to kill.
