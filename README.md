# Law of Large Numbers Simulation

![Simulation Gif](law_of_large_numbers_animation.gif)

This simulation visually demonstrates the Law of Large Numbers, a fundamental concept in probability and statistics. The Law of Large Numbers states that as the size of a sample increases, the sample mean converges towards the population mean. In simpler terms, it illustrates how the average of a large number of observations tends to approach the expected value. [Wikipedia](https://en.m.wikipedia.org/wiki/Law_of_large_numbers)

## Overview

This project aims to illustrate the Law of Large Numbers through a straightforward simulation. It generates a sequence of random numbers from a specified distribution, calculates running averages, and presents a visualization of the gradual convergence of the running average to the expected value.

## Features

- Intuitive simulation of the Law of Large Numbers.
- Visualization depicting the convergence of the running average.
- Customizable parameters for tailoring the simulation.

## Usage

To utilize this simulation, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/mirolaukka/law-of-large-numbers.git
   cd law-of-large-numbers-simulation
   ```

2. Install the required libraries using pip:

   ```
   pip install -r requirements.txt
   ```

3. Open the `main.py` script and customize the parameters within the `if __name__ == "__main__"` block:

   ```python
   num_simulations = 10
   max_sample_size = 7000
   ```

4. Run the simulation script:

   ```
   python main.py
   ```

   The script will execute the simulation, generate the animation GIF, and display the visualization of the running average convergence.

Please note that the `law_of_large_numbers_animation.gif` file is produced as a result of running the simulation script. You can adjust the simulation parameters within the script to explore different scenarios.

## Contributions

Contributions to this project are welcomed! Whether you're interested in adding new features, enhancing the visualization, or optimizing the code, feel free to fork this repository and submit your pull requests.

## License

This project is licensed under the MIT License, granting you the freedom to use, modify, and distribute the code in your own projects.
