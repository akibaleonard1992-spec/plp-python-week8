# Personal Mini-Toolkit

The Personal Mini-Toolkit is a menu-driven Python program with four useful tools.
It includes a number guessing game, a mutable to-do list, a simple calculator,
and a name formatter. The program repeatedly displays a menu until the user
chooses to quit.

## Run the Program

From this folder, run:

```bash
python toolkit.py
```

Choose a numbered menu option and follow the prompts.

## Reflection

The main menu loop was the first part that needed careful planning. The hardest
part was making every tool return safely to the menu after invalid input. The bug
that took longest to fix was removing a task at a number that did not exist, because
I had to handle an index error without crashing. I would improve the toolkit by
saving to-do items to a text file so they remain after the program closes. With one
more week, I would also add a unit converter and data validation to all tools.
