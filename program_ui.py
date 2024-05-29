import math
import time
import tkinter as tk
import tkinter.ttk
from tkinter import Tk, Label, Entry, Button
import multiprocessing
import numpy as np
import pandas as pd
from pandastable import Table
import pyramid_method as pm
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import itertools


global fill_matrix_with_random
global value_for_matrix


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Pyramid method")
        self.geometry("1200x900")

        Label(self, text="Enter i:").pack()
        self.i_input = Entry(self, width=35)
        self.i_input.pack()
        Label(self, text="Enter j:").pack()
        self.j_input = Entry(self, width=35)
        self.j_input.pack()

        self.label_time_for_default = Label(self, text="Time for default: ")
        self.label_time_for_default.pack(pady=20)

        self.label_time_for_parallel = Label(self, text="Time for parallel: ")
        self.label_time_for_parallel.pack(pady=20)

        self.label_faster_method = Label(self, text="What method was faster: ")
        self.label_faster_method.pack(pady=20)

        self.label_acceleration = Label(self, text="Acceleration is: ")
        self.label_acceleration.pack(pady=20)

        Button(self, text="Solve problem", command=self.solve_problem).pack()
        Button(self, text="Fill matrix with random values", command=self.fill_matrix_random).pack()
        Button(self, text="Fill matrix with same determined value", command=self.fill_matrix_same_value).pack()
        Button(self, text="Show grid", command=self.show_grid).pack()
        # tk.Button(window, text="Open file", command=open_and_read_text_file).pack()

        Label(self, text="Select an example number:").pack()
        self.example_chooser = tkinter.ttk.Combobox(state="readonly", values=["1", "2"])
        self.example_chooser.current(1)
        self.example_chooser.pack()

    def fill_matrix_random(self):
        global fill_matrix_with_random
        fill_matrix_with_random = True

    def fill_matrix_same_value(self):
        global fill_matrix_with_random
        global value_for_matrix
        fill_matrix_with_random = False
        frame = tk.Toplevel()
        frame.geometry("200x200")
        label_value = tk.Label(frame, text="Enter value to fill matrix: ")
        label_value.pack(pady=20)
        value_input = tk.Entry(frame, width=35)
        value_input.pack()

        def save_value():
            global value_for_matrix
            v = int(value_input.get())
            value_for_matrix = v
            frame.destroy()

        tk.Button(frame, text="Enter", command=save_value).pack()

    def solve_problem_parallel(self, extended_array_x, example_num):
        index_i_testing = int(self.i_input.get())
        index_j_testing = int(self.j_input.get())
        index_k_testing = index_j_testing
        number_of_iterations = 0
        is_index_i_odd = index_i_testing % 2 == 1
        iteration_indices_for_data_output_testing = []
        if example_num == 1:
            list_of_iterations_for_queue_testing, number_of_iterations = pm.fill_lists_of_iterations(index_i_testing,
                                                                                                     index_j_testing,
                                                                                                     index_k_testing,
                                                                                                     iteration_indices_for_data_output_testing,
                                                                                                     is_index_i_odd,
                                                                                                     number_of_iterations)
        else:
            list_of_iterations_for_queue_testing, number_of_iterations = pm.fill_lists_of_iterations_second(index_i_testing,
                                                                                                     index_j_testing,
                                                                                                     index_k_testing,
                                                                                                     iteration_indices_for_data_output_testing,
                                                                                                     is_index_i_odd,
                                                                                                     number_of_iterations)

        array_x_test = np.zeros((index_i_testing, index_j_testing))
        array_y_test = np.zeros((index_i_testing, index_j_testing))
        array_z_test = np.zeros((index_i_testing, index_j_testing))
        extended_array_data_x = np.copy(extended_array_x)
        extended_array_data_y = np.copy(extended_array_data_x)
        extended_array_data_z = np.copy(extended_array_data_x)

        starting_index_for_input = math.ceil((index_i_testing / 2))
        iteration_indices_for_data_input_testing = np.arange(starting_index_for_input + 1, number_of_iterations + 1)

        num_processes = 4
        result_list = []
        with multiprocessing.Manager() as manager:
            if example_num == 1:
                fifo_dictionary_testing = pm.make_queues(index_k_testing, manager)
                pm.fill_first_two_fifo_channels(index_i_testing, index_j_testing, list_of_iterations_for_queue_testing,
                                                iteration_indices_for_data_output_testing,
                                                fifo_dictionary_testing, extended_array_data_z, number_of_iterations)
            else:
                fifo_dictionary_testing = pm.make_queues_second(index_k_testing, manager)
                pm.fill_first_three_fifo_channels(index_i_testing, index_j_testing, list_of_iterations_for_queue_testing,
                                                  iteration_indices_for_data_output_testing,
                                                  fifo_dictionary_testing, extended_array_data_z, number_of_iterations)

            start_time_parallel = time.perf_counter_ns()

            if example_num == 1:
                with multiprocessing.Pool(processes=None) as pool:
                    results = [
                        pool.apply_async(example_task, args=
                                         (index_i_testing, index_j_testing, k, extended_array_data_x, extended_array_data_y,
                                          extended_array_data_z, fifo_dictionary_testing, iteration_indices_for_data_output_testing,
                                          iteration_indices_for_data_input_testing, array_x_test, array_y_test, array_z_test))
                        for k in range(1, index_k_testing + 1)
                    ]

                    # Очікування завершення всіх завдань
                    for result in results:
                        res = result.get()
                        result_list.append(res)
            else:
                with multiprocessing.Pool(processes=None) as pool:
                    results = [
                        pool.apply_async(example_task_second, args=
                        (index_i_testing, index_j_testing, k, extended_array_data_x, extended_array_data_y,
                         extended_array_data_z, fifo_dictionary_testing, iteration_indices_for_data_output_testing,
                         iteration_indices_for_data_input_testing, array_x_test, array_y_test, array_z_test))
                        for k in range(1, index_k_testing + 1)
                    ]

                    # Очікування завершення всіх завдань
                    for result in results:
                        res = result.get()
                        result_list.append(res)

        finish_time_parallel = time.perf_counter_ns()

        time_for_parallel = finish_time_parallel - start_time_parallel
        if time_for_parallel >= 100_000_000:
            time_for_parallel_sec = time_for_parallel / 1_000_000_000
            self.label_time_for_parallel.config(text=f'Time elapsed parallel: {time_for_parallel_sec} sec')
        else:
            self.label_time_for_parallel.config(text=f'Time elapsed parallel: {time_for_parallel} ns')

        # np.savetxt('extended_array_data_x_parallel.txt', np.rot90(extended_array_data_x), fmt='%f')
        # np.savetxt('extended_array_data_y_parallel.txt', np.rot90(extended_array_data_y), fmt='%f')
        # np.savetxt('extended_array_data_z_parallel.txt', np.rot90(extended_array_data_z), fmt='%f')
        # np.savetxt('array_x_test_parallel.txt', np.rot90(array_x_test), fmt='%f')
        # np.savetxt('array_y_test_parallel.txt', np.rot90(array_y_test), fmt='%f')
        # np.savetxt('array_z_test_parallel.txt', np.rot90(array_z_test), fmt='%f')

        list_of_results_x = []
        list_of_results_y = []
        list_of_results_z = []

        for x, y, z in result_list:
            list_of_results_x.append(x)
            list_of_results_y.append(y)
            list_of_results_z.append(z)

        return list_of_results_x, list_of_results_y, list_of_results_z, time_for_parallel

    def solve_problem(self):
        example_number = int(self.example_chooser.get())
        index_i_testing = int(self.i_input.get())
        index_j_testing = int(self.j_input.get())
        index_k_testing = index_j_testing
        number_of_iterations = 0

        array_x_test = np.zeros((index_i_testing, index_j_testing))
        array_y_test = np.zeros((index_i_testing, index_j_testing))
        array_z_test = np.zeros((index_i_testing, index_j_testing))
        global fill_matrix_with_random
        global value_for_matrix
        if fill_matrix_with_random:
            if example_number == 1:
                extended_array_data_x = pm.fill_random(index_i_testing, index_j_testing)
            else:
                extended_array_data_x = pm.fill_random_second(index_i_testing, index_j_testing)
        else:
            if example_number == 1:
                extended_array_data_x = np.zeros((index_i_testing + 3, index_j_testing + 4))
                extended_array_data_x.fill(value_for_matrix)
            else:
                extended_array_data_x = np.zeros((index_i_testing + 3, index_j_testing + 5))
                extended_array_data_x.fill(value_for_matrix)

        extended_array_for_parallel = np.copy(extended_array_data_x)
        extended_array_data_y = np.copy(extended_array_data_x)
        extended_array_data_z = np.copy(extended_array_data_x)

        starting_index_for_input = math.ceil((index_i_testing / 2))
        iteration_indices_for_data_input_testing = np.arange(starting_index_for_input + 1, number_of_iterations + 1)

        start_time = time.perf_counter_ns()

        if example_number == 1:
            pm.solve_sequential(index_i_testing, index_j_testing, extended_array_data_x, extended_array_data_y,
                                extended_array_data_z, array_x_test, array_y_test, array_z_test)
        else:
            pm.solve_sequential_second(index_i_testing, index_j_testing, extended_array_data_x, extended_array_data_y,
                                       extended_array_data_z, array_x_test, array_y_test, array_z_test)

        finish_time = time.perf_counter_ns()

        time_for_default = finish_time - start_time
        if time_for_default >= 100_000_000:
            time_for_default_sec = time_for_default / 1_000_000_000
            self.label_time_for_default.config(text=f'Time elapsed: {time_for_default_sec} sec')
        else:
            self.label_time_for_default.config(text=f'Time elapsed: {time_for_default} ns')

        np.savetxt('extended_array_data_x.txt', np.rot90(extended_array_data_x), fmt='%f')
        np.savetxt('extended_array_data_y.txt', np.rot90(extended_array_data_y), fmt='%f')
        np.savetxt('extended_array_data_z.txt', np.rot90(extended_array_data_z), fmt='%f')
        np.savetxt('array_x_test.txt', np.rot90(array_x_test), fmt='%f')
        np.savetxt('array_y_test.txt', np.rot90(array_y_test), fmt='%f')
        np.savetxt('array_z_test.txt', np.rot90(array_z_test), fmt='%f')

        list_of_results_x = []
        list_of_results_y = []
        list_of_results_z = []

        for i in range(index_k_testing):
            list_of_results_x.append(array_x_test[-1][i])
            list_of_results_y.append(array_y_test[-1][i])
            list_of_results_z.append(array_z_test[-1][i])

        list_of_results_x_parallel, list_of_results_y_parallel, list_of_results_z_parallel, time_for_parallel = self.solve_problem_parallel(
            extended_array_for_parallel, example_number)

        if time_for_default > time_for_parallel:
            self.label_faster_method.config(text="Parallel method was faster")
        else:
            self.label_faster_method.config(text="Default method was faster")

        self.label_acceleration.config(text=f'Acceleration: {time_for_default / time_for_parallel}')

        result_df = pd.DataFrame({'default_x': list_of_results_x,
                                  'default_y': list_of_results_y,
                                  'default_z': list_of_results_z,
                                  'parallel_x': list_of_results_x_parallel,
                                  'parallel_y': list_of_results_y_parallel,
                                  'parallel_z': list_of_results_z_parallel
                                  })

        frame = tk.Toplevel()
        table = Table(frame, dataframe=result_df, showtoolbar=True, showstatusbar=True)
        table.show()

    def open_and_read_text_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        f = fd.askopenfile(filetypes=filetypes)
        # frame = tk.Toplevel()
        # frame.geometry("200x200")
        # file_text.insert('1.0', f.readlines())

    def show_grid(self):
        example_number = int(self.example_chooser.get())
        i_bound = int(self.i_input.get())
        j_bound = int(self.j_input.get())
        x = np.linspace(1, i_bound, i_bound)
        y = np.linspace(1, j_bound, j_bound)
        if example_number == 1:
            for i in range(1, i_bound + 1):
                for j in range(1, j_bound + 1):
                    plt.arrow(i - 2, j + 1, 2, -1, width=0.03, overhang=0, length_includes_head=True, color='red')
                    plt.arrow(i - 1, j, 1, 0, width=0.03, overhang=0, length_includes_head=True, color='green')
                    plt.arrow(i - 1, j - 2, 1, 2, width=0.03, overhang=0, length_includes_head=True,color='blue')
        else:
            for i in range(1, i_bound + 1):
                for j in range(1, j_bound + 1):
                    plt.arrow(i - 2, j + 1, 2, -1, width=0.03, overhang=0, length_includes_head=True, color='red')
                    plt.arrow(i - 1, j, 1, 0, width=0.03, overhang=0, length_includes_head=True, color='green')
                    plt.arrow(i - 1, j - 3, 1, 3, width=0.03, overhang=0, length_includes_head=True,color='blue')
        pts = itertools.product(x, y)
        plt.scatter(*zip(*pts), marker='o', s=50, color='black')
        plt.xticks(x)
        plt.yticks(y)
        plt.show()


def example_task(index_i_testing, index_j_testing, k, extended_array_data_x, extended_array_data_y, extended_array_data_z,
                 fifo_dictionary_testing, iteration_indices_for_data_output_testing,
                 iteration_indices_for_data_input_testing, array_x_test, array_y_test, array_z_test):
     res = pm.solve_parallel(index_i_testing, index_j_testing, k, extended_array_data_x, extended_array_data_y, extended_array_data_z,
                             fifo_dictionary_testing, iteration_indices_for_data_output_testing,
                             iteration_indices_for_data_input_testing, array_x_test, array_y_test, array_z_test)
     return res


def example_task_second(index_i_testing, index_j_testing, k, extended_array_data_x, extended_array_data_y,
                        extended_array_data_z,
                        fifo_dictionary_testing, iteration_indices_for_data_output_testing,
                        iteration_indices_for_data_input_testing, array_x_test, array_y_test, array_z_test):
    res = pm.solve_parallel_second(index_i_testing, index_j_testing, k, extended_array_data_x, extended_array_data_y,
                                   extended_array_data_z,
                                   fifo_dictionary_testing, iteration_indices_for_data_output_testing,
                                   iteration_indices_for_data_input_testing, array_x_test, array_y_test, array_z_test)
    return res


if __name__ == '__main__':
    root = MainWindow()
    root.mainloop()
