import matplotlib.pyplot as plt
import numpy as np
import concurrent.futures
import imageio


def roll_die():
    return np.random.randint(1, 7)


def simulate_law_of_large_numbers(args):
    num_simulations, sample_size = args

    total = 0
    for _ in range(num_simulations):
        sample_sum = sum(roll_die() for _ in range(sample_size))
        average = sample_sum / sample_size
        total += average

    return sample_size, total / num_simulations


def run_simulation(num_threads, num_simulations, max_sample_size, current_averages, ax):
    lock = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for sample_size in range(1, max_sample_size + 1):
            args = (num_simulations, sample_size)
            future = executor.submit(simulate_law_of_large_numbers, args)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            sample_size, average = future.result()
            with lock:
                current_averages[sample_size - 1] = average
    return current_averages


def generate_animation(sample_sizes, current_averages, filename):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlabel('Sample Size')
    ax.set_ylabel('Average')
    ax.set_title('Law of Large Numbers: Simulating Dice Rolls')
    ax.grid()
    ax.axhline(y=3.5, color='r', linestyle='--', label='Expected Value (3.5)')
    ax.legend()
    ax.set_ylim(3, 4)  # Set Y-axis limits

    frames = []
    for i in range(len(sample_sizes)):
        ax.clear()  # Clear the plot before drawing each frame
        ax.plot(sample_sizes[:i+1], current_averages[:i+1], marker='o')
        ax.axhline(y=3.5, color='r', linestyle='--',
                   label='Expected Value (3.5)')
        ax.legend()
        ax.grid()
        ax.set_xlabel('Sample Size')
        ax.set_ylabel('Average')
        ax.set_title('Law of Large Numbers: Simulating Dice Rolls')
        ax.set_ylim(3, 4)  # Set Y-axis limits

        # Add a text annotation with the simulation parameters
        simulation_params = f"Num Simulations: {num_simulations}\nMax Sample Size: {max_sample_size}"
        ax.text(0.02, 0.92, simulation_params, transform=ax.transAxes,
                fontsize=10, verticalalignment='top')

        plt.pause(0.05)  # Pause to let the animation show
        plt.draw()
        frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        frame = frame.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(frame)

    imageio.mimsave(filename, frames, duration=(1000 * 1/20))


if __name__ == "__main__":
    num_threads = 8
    num_simulations = 500
    max_sample_size = 100
    sample_sizes = list(range(1, max_sample_size + 1))

    current_averages = [0] * max_sample_size
    run_simulation(num_threads, num_simulations,
                   max_sample_size, current_averages, None)

    animation_filename = "law_of_large_numbers_animation.gif"
    generate_animation(sample_sizes, current_averages, animation_filename)

    plt.show()
