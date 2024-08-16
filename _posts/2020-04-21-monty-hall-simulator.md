---
title: "Monty Hall Problem - Simulator"
tags:
  - Engineering
  - Python
  - Simulation
  - Statistics
toc: true
toc_sticky: true
header:
  teaser: /assets/images/2020-04-21-monty-hall-simulator/monty-hall.png
  og_image: /assets/images/2020-04-21-monty-hall-simulator/monty-hall.png

---

<img src="/assets/images/2020-04-21-monty-hall-simulator/monty-hall.png" style="max-width: 30%; display: block; margin: 0 auto;">

## Introduction

The Monty Hall problem is a famous probability puzzle that often surprises people with its counterintuitive solution. Named after the host of the American television game show "Let's Make a Deal," the problem goes as follows:

- You are a contestant on a game show.
- There are three doors: behind one is a car (the prize), and behind the other two are goats.
- You pick a door.
- The host, Monty Hall, who knows what's behind each door, opens one of the other two doors, revealing a goat.
- You are then given a choice: stick with your original pick or switch to the other unopened door.

What should you do to maximize your chances of winning the car?

## The Solution

Most people initially think that after Monty reveals a goat, the probability of winning the car is 50/50, so it doesn't matter whether you switch or not. However, this intuition is incorrect.

The correct strategy is to **always switch doors**. If you switch, your chances of winning the car increase to **2/3**, whereas if you stay with your original choice, your chances are only **1/3**.

### Why Switching Works

Let's break it down:

1. When you pick a door, there's a **1/3** chance you picked the car and a **2/3** chance you picked a goat.
2. Monty reveals a goat behind one of the other two doors.
3. If you picked a goat initially (which happens 2/3 of the time), the car must be behind the other unopened door, so switching wins.
4. If you picked the car initially (which happens 1/3 of the time), switching loses.

Thus, switching gives you a 2/3 chance of winning.

## Simulating the Monty Hall Problem

If this explanation still seems a bit unclear, don't worry—you can experience the probability firsthand by running a Python script that simulates the Monty Hall problem.

I've created a [Monty Hall Simulator](https://github.com/e-loughlin/MontyHallSimulator) that allows you to experiment with the problem. The script runs thousands of iterations of the game and tracks the outcomes for both strategies—staying with the original door and switching to the other door.

By running the simulation, you can see the 2/3 win rate for switching emerge over time.

### Running the Simulation

To try it out, clone the repository:

```bash
git clone https://github.com/e-loughlin/MontyHallSimulator.git
cd MontyHallSimulator
```

Then run the script:

```bash
python monty_hall_simulation.py
```

The output will show you the results of staying vs. switching after running a large number of trials.

## Example Output

```txt
Monty Hall Simulator!
Select door 1, 2, or 3!
 1   2   3 
[?] [?] [?] 
2
OK! You've made selection 2. But wait! I'll open a different door...
 1   2   3 
[?] [ ] [?] 
Would you like to switch doors? (y/n)
y
Ok! Open door 3!
 1   2   3 
[ ] [ ] [$] 
You WIN!
=========
Wins: 1
Losses: 0
Games Played: 1
Win Percentage: 1.0
=========
Keep playing? (y/n)
```

## Conclusion

The Monty Hall problem is a fascinating example of how human intuition can lead us astray when dealing with probability. Through this Python simulation, you can gain a deeper understanding of the problem and see for yourself why switching doors is the optimal strategy.

Feel free to explore the [GitHub repository](https://github.com/e-loughlin/MontyHallSimulator) to run the simulation yourself and see the results.

--- 

This markdown post introduces the Monty Hall problem, explains the solution, and provides a link to your GitHub repository for the Python simulation. Let me know if there are any adjustments you'd like!
