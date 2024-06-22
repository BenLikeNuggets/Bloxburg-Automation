# Bloxburg Automation
This project has the purpose of automating high-paying jobs in the game Bloxburg.

### Preface:

This READ.me file and the use of git's version control is also part of the project, so I can get a good understanding of it, which will inevitably be part of my skillset later on.
Also, keep in mind that I'll be doing the project to the extend of my interest. The effects of this might be less polished code, but I'll do my best not to start too many bad habits.

### Setup - Installation Information & Links:

The language used is: ```Python 3.7.16```

Required libraries can be seen in the ```requirements.txt```

[MacroRecorder](https://www.macrorecorder.com/doc/installation/) - (Its use is explained under **Game Information**)


## Automated jobs: Finished & Unfinished
*Checked = Working | Unchecked = In progress*
- [x] Lumberjack
- [ ] Bloxburger

## Important Information
### Game Information

There's lots to automate in this game, but I've simplified it a bunch for myself, so the project won't take me - a complete beginnner - too long. 
Overall, there's 2 important factors to keep in mind, when programming this. 

1. **Mood:** A mechanic within the game that makes the player faint, forcing them to their spawn position. 
This requires the player to do 4 different things to *fix their mood*, so they don't faint. Therefore, 
the automations can't be 100% automatic... unless I made that part of the automation, but I won't, as of now.

2. **Interactivity:** Clicking buttons within the game is apparently difficult, 
since buttons can't be interacted with unless the mouse movement is smooth enough. 
I've found a semi-fix to this, by using MacroRecorder's smooth movement.


## Explanations

### Lumberjack

Requirements:

In this job, the player simply has to chop down some trees with an axe.

Solution:

My way of automating this was to make a macro, which simply had to position the player between 2 trees and then start a loop that goes on 'forever'.

### Bloxburger

#### Requirements:

Picture this. You work at a fastfood restaurant, and you're taking the orders of the customers by the counter. 
They'll give you a completely random order, as they've been programmed to do. There's 3 things they ask for, in this specific order:

1. **Burger:**
  - The customer will always order a burger.
  - There will always AND only be: 1 bottom and 1 top bun.
  - They'll always choose 1 out of 2 types of beef (either 'normal' or 'vegan').
  - They'll always choose 1, BUT up to 3 different ingredients.
    - **Ingredients:** Lettuce, tomato, cheese & onion.
  - They'll always have the option to choose between 1 to 2 of each beef & ingredient.

2. **Fries:**
  - The customer will always order fries.
  - **Ruleset - Fries & Drinks:**
    - They can choose 1 out of 3 types of fries.
      - **Types:** Normal, ring & round.
    - They can choose 1 out of 3 sizes.
      - **Sizes:** Small, medium & large.
    - They can only order 1 'set' [^1] of fries.

3. **Drinks:**
  - The customer won't always order drinks.
  - **Ruleset - Fries & Drinks:**
    - They can choose 1 out of 3 types of drinks.
      - **Types:** Cola, juice & milkshake.
    - They can choose 1 out of 3 sizes.
      - **Sizes:** Small, medium & large.
    - They can only order 1 'set' [^1] of drinks.

[^1]: Combination of 1 type & 1 size.

#### Solution:

The script will consist of 2 phases. Setup & Execution.

The setup phase is to avoid re-calculation of the same things, since that's - ofcourse - inefficient. 
In the setup, the script will start by locating the menu itself, which will then become the 'region' of the menu. 
Aftwards it'll locate all the different items of the different menus, and store their locations.
This can be done since the menu never changes throughout the gameplay. 
The method for locating the items of the menu is pyautogui in combination with opencv. 
Thereby, the script can be told to look for certain items within a region of the screen.
The process of setting up will be automatic from the 'start of the job', since the mouse will be programmed to go to the location to navigate the menu.

In the execution, the script will identify the order of customer and press the previously stored location of the corresponding menu item.
The order that the customer gives will be shown for a limited time, thereby having to make the script fast enough to identify and navigate to the menu items within a time period.
Further explanation of the script can be seen within the script itself.
