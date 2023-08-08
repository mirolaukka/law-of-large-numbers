import matplotlib.pyplot as plt
import numpy as np
import concurrent.futures
import imageio


def roll_die():
    return np.random.randint(1, 7)


def running_average(input_array):
    if not input_array:
        return []

    running_sum = 0
    running_averages = []

    for num in input_array:
        running_sum += num
        running_averages.append(running_sum / len(running_averages + [1]))

    return running_averages


def simulate_law_of_large_numbers(num_simulations):
    return sum(roll_die() for _ in range(num_simulations)) / num_simulations


def run_simulation(num_simulations, max_sample_size):

    averages = []

    for sample in range(1, max_sample_size+1):
        averages.append(simulate_law_of_large_numbers(num_simulations))

    return running_average(averages)


def generate_animation(sample_sizes, current_averages, filename):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlabel('Sample Size')
    ax.set_ylabel('Average')
    ax.set_title('Law of Large Numbers: Simulating Dice Rolls')
    ax.grid()
    ax.axhline(y=3.5, color='r', linestyle='--', label='Expected Value (3.5)')
    ax.legend()

    frames = []
    for i in range(1, len(sample_sizes), 100):
        ax.clear()  # Clear the plot before drawing each frame
        ax.axhline(y=3.5, color='r', linestyle='--',
                   label='Expected Value (3.5)', linewidth=1.4)
        ax.plot(sample_sizes[:i+1], current_averages[:i+1],
                marker='o', markersize=1)
        ax.legend()
        ax.grid()
        ax.set_xlabel('Sample Size')
        ax.set_ylabel('Average')
        ax.set_title('Law of Large Numbers: Simulating Dice Rolls')

        # Add a text annotation with the simulation parameters
        simulation_params = f"Simulations per Sample: {num_simulations}\nSample Size: {max_sample_size}"
        ax.text(0.02, 0.92, simulation_params, transform=ax.transAxes,
                fontsize=10, verticalalignment='top')

        plt.pause(0.0001)  # Pause to let the animation show
        plt.draw()
        frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        frame = frame.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(frame)

    imageio.mimsave(filename, frames, duration=(1000 * 1/20))


if __name__ == "__main__":
    num_simulations = 10
    max_sample_size = 7000
    sample_sizes = list(range(1, max_sample_size + 1))

    current_averages = [0] * max_sample_size
    current_averages = run_simulation(num_simulations,
                                      max_sample_size)

    animation_filename = "law_of_large_numbers_animation.gif"
    generate_animation(sample_sizes, current_averages, animation_filename)

    plt.show()
