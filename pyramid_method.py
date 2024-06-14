import random
import numpy as np


def f(x):
    return np.sin(pow(x, 4) - np.exp(x))


def g(x):
    return np.cos(pow(x, 4) - np.exp(x))


def h(x):
    return np.cos(pow(x, 3) - np.exp(x))


def make_queues(index_k_testing, manager):
    fifo_dictionary_testing = manager.dict()
    for k in range(-1, index_k_testing + 1):
        threads = f'{k},{k + 2}'
        q = manager.Queue()
        fifo_dictionary_testing[threads] = q
    return fifo_dictionary_testing


#другий приклад
def make_queues_second(index_k_testing, manager):
    fifo_dictionary_testing = manager.dict()
    for k in range(-2, index_k_testing + 1):
        threads = f'{k},{k + 3}'
        q = manager.Queue()
        fifo_dictionary_testing[threads] = q
    return fifo_dictionary_testing


def is_odd(number):
    return number % 2 == 1


def is_even(number):
    return number % 2 == 0


def fill_random(index_i, index_j):
    array = np.zeros((index_i + 3, index_j + 4))
    for j in range(2):
        for i in range(index_i + 2):
            array[i][j] = random.randrange(1, 20)
    for i in range(2):
        for j in range(2, index_j + 2):
            array[i][j] = random.randrange(1, 20)
    for i in range(index_i + 2):
        array[i][index_j + 2] = random.randrange(1, 20)

    return array


def fill_random_second(index_i, index_j):
    array = np.zeros((index_i + 3, index_j + 5))
    for j in range(3):
        for i in range(index_i + 2):
            array[i][j] = random.randrange(1, 20)
    for i in range(2):
        for j in range(3, index_j + 4):
            array[i][j] = random.randrange(1, 20)
    for i in range(2, index_i + 2):
        array[i][index_j + 3] = random.randrange(1, 20)

    return array


def fill_lists_of_iterations(index_i_testing, index_j_testing, index_k_testing,
                             iteration_indices_for_data_output_testing, is_index_i_odd, number_of_iterations):
    list_of_iterations_testing = [[]] * index_k_testing
    list_of_iterations_for_queue_testing = [[]] * index_k_testing
    for k in range(1, index_k_testing + 1):
        counter = 0
        list_of_kth_iterations = []
        list_of_kth_iterations_for_queue = []
        for i in range(1, index_i_testing + 1):
            for j in range(k, k + ((index_i_testing - i) // 2) + 1):
                list_of_kth_iterations.append([i, j])
                list_of_kth_iterations_for_queue.append([i - 1, j - 2])
                counter = counter + 1
        number_of_iterations = counter
        list_of_iterations_testing[k - 1] = list_of_kth_iterations
        list_of_iterations_for_queue_testing[k - 1] = list_of_kth_iterations_for_queue

    counter_for_indices = 1
    for i in range(len(list_of_iterations_testing[0])):
        if counter_for_indices == len(list_of_iterations_testing[0]):
            if is_index_i_odd:
                if is_odd(list_of_iterations_testing[0][i][0]):
                    pass
                else:
                    iteration_indices_for_data_output_testing.append(counter_for_indices)
            if not is_index_i_odd:
                if is_even(list_of_iterations_testing[0][i][0]):
                    pass
                else:
                    iteration_indices_for_data_output_testing.append(counter_for_indices)
        else:
            if is_index_i_odd:
                if is_odd(list_of_iterations_testing[0][i][0]) and not is_odd(
                        list_of_iterations_testing[0][i + 1][0]):
                    pass
                else:
                    iteration_indices_for_data_output_testing.append(counter_for_indices)
            if not is_index_i_odd:
                if is_even(list_of_iterations_testing[0][i][0]) and not is_even(
                        list_of_iterations_testing[0][i + 1][0]):
                    pass
                else:
                    iteration_indices_for_data_output_testing.append(counter_for_indices)
        counter_for_indices = counter_for_indices + 1

    return list_of_iterations_for_queue_testing, number_of_iterations


#другий приклад
def fill_lists_of_iterations_second(index_i_testing, index_j_testing, index_k_testing,
                             iteration_indices_for_data_output_testing, is_index_i_odd, number_of_iterations):
    list_of_iterations_testing = [[]] * index_k_testing
    list_of_iterations_for_queue_testing = [[]] * index_k_testing
    for k in range(1, index_k_testing + 1):
        counter = 0
        list_of_kth_iterations = []
        list_of_kth_iterations_for_queue = []
        for i in range(1, index_i_testing + 1):
            for j in range(k, k + ((index_i_testing - i) // 2) + 1):
                list_of_kth_iterations.append([i, j])
                list_of_kth_iterations_for_queue.append([i - 1, j - 3]) #поміняв на j-3
                counter = counter + 1
        number_of_iterations = counter
        list_of_iterations_testing[k - 1] = list_of_kth_iterations
        list_of_iterations_for_queue_testing[k - 1] = list_of_kth_iterations_for_queue

    counter_for_indices = 1
    for i in range(len(list_of_iterations_testing[0])):
        if counter_for_indices == len(list_of_iterations_testing[0]):
            if is_index_i_odd:
                if is_odd(list_of_iterations_testing[0][i][0]):
                    pass
                else:
                    iteration_indices_for_data_output_testing.append(counter_for_indices)
            if not is_index_i_odd:
                if is_even(list_of_iterations_testing[0][i][0]):
                    pass
                else:
                    iteration_indices_for_data_output_testing.append(counter_for_indices)
        else:
            if is_index_i_odd:
                if is_odd(list_of_iterations_testing[0][i][0]) and not is_odd(
                        list_of_iterations_testing[0][i + 1][0]):
                    pass
                else:
                    iteration_indices_for_data_output_testing.append(counter_for_indices)
            if not is_index_i_odd:
                if is_even(list_of_iterations_testing[0][i][0]) and not is_even(
                        list_of_iterations_testing[0][i + 1][0]):
                    pass
                else:
                    iteration_indices_for_data_output_testing.append(counter_for_indices)
        counter_for_indices = counter_for_indices + 1

    return list_of_iterations_for_queue_testing, number_of_iterations


def fill_first_two_fifo_channels(index_i_testing, index_j_testing, list_of_iterations_for_queue_testing,
                                 iteration_indices_for_data_output_testing,
                                 fifo_dictionary_testing, extended_array_data_z, number_of_iterations):
    counter = 1
    for i in range(number_of_iterations):
        index_i_for_element_for_queue = list_of_iterations_for_queue_testing[0][i][0]
        index_j_for_element_for_queue = list_of_iterations_for_queue_testing[0][i][1]
        if counter in iteration_indices_for_data_output_testing:
            if index_i_for_element_for_queue >= index_i_testing + 1 or index_j_for_element_for_queue >= index_j_testing + 1:
                fifo_dictionary_testing[f'{-1},{1}'].put(extended_array_data_z[0][0])
            else:
                fifo_dictionary_testing[f'{-1},{1}'].put(
                    extended_array_data_z[index_i_for_element_for_queue + 2][index_j_for_element_for_queue + 1])
        counter = counter + 1
    counter = 1
    for i in range(number_of_iterations):
        index_i_for_element_for_queue = list_of_iterations_for_queue_testing[1][i][0]
        index_j_for_element_for_queue = list_of_iterations_for_queue_testing[1][i][1]
        if counter in iteration_indices_for_data_output_testing:
            if index_i_for_element_for_queue >= index_i_testing + 1 or index_j_for_element_for_queue >= index_j_testing + 1:
                fifo_dictionary_testing[f'{0},{2}'].put(extended_array_data_z[0][0])
            else:
                fifo_dictionary_testing[f'{0},{2}'].put(
                    extended_array_data_z[index_i_for_element_for_queue + 2][index_j_for_element_for_queue + 1]) #+2 для i-1 дуже важливо!
        counter = counter + 1


#другий приклад
# поміняв -2 1 всюди, тобто номери каналів
def fill_first_three_fifo_channels(index_i_testing, index_j_testing, list_of_iterations_for_queue_testing,
                                   iteration_indices_for_data_output_testing,
                                   fifo_dictionary_testing, extended_array_data_z, number_of_iterations):
    counter = 1
    for i in range(number_of_iterations):
        index_i_for_element_for_queue = list_of_iterations_for_queue_testing[0][i][0]
        index_j_for_element_for_queue = list_of_iterations_for_queue_testing[0][i][1]
        if counter in iteration_indices_for_data_output_testing:
            if index_i_for_element_for_queue >= index_i_testing + 1 or index_j_for_element_for_queue >= index_j_testing + 1:
                fifo_dictionary_testing[f'{-2},{1}'].put(extended_array_data_z[0][0])
            else:
                fifo_dictionary_testing[f'{-2},{1}'].put(
                    extended_array_data_z[index_i_for_element_for_queue + 2][index_j_for_element_for_queue + 2])
        counter = counter + 1
    counter = 1
    for i in range(number_of_iterations):
        index_i_for_element_for_queue = list_of_iterations_for_queue_testing[1][i][0]
        index_j_for_element_for_queue = list_of_iterations_for_queue_testing[1][i][1]
        if counter in iteration_indices_for_data_output_testing:
            if index_i_for_element_for_queue >= index_i_testing + 1 or index_j_for_element_for_queue >= index_j_testing + 1:
                fifo_dictionary_testing[f'{-1},{2}'].put(extended_array_data_z[0][0])
            else:
                fifo_dictionary_testing[f'{-1},{2}'].put(
                    extended_array_data_z[index_i_for_element_for_queue + 2][index_j_for_element_for_queue + 2])
        counter = counter + 1
    counter = 1
    for i in range(number_of_iterations):
        index_i_for_element_for_queue = list_of_iterations_for_queue_testing[2][i][0] #поміняв тут на 2
        index_j_for_element_for_queue = list_of_iterations_for_queue_testing[2][i][1] #поміняв тут на 2
        if counter in iteration_indices_for_data_output_testing:
            if index_i_for_element_for_queue >= index_i_testing + 1 or index_j_for_element_for_queue >= index_j_testing + 1:
                fifo_dictionary_testing[f'{0},{3}'].put(extended_array_data_z[0][0])
            else:
                fifo_dictionary_testing[f'{0},{3}'].put(
                    extended_array_data_z[index_i_for_element_for_queue + 2][index_j_for_element_for_queue + 2])
        counter = counter + 1


# def solve_default(index_i_testing, index_j_testing, index_k_testing, extended_array_data_x, extended_array_data_y,
#                   extended_array_data_z, fifo_dictionary_testing,
#                   iteration_indices_for_data_output_testing, iteration_indices_for_data_input_testing, array_x_test,
#                   array_y_test, array_z_test):
#     for k in range(1, index_k_testing + 1):
#         counter = 1
#         for i in range(1, index_i_testing + 1):
#             for j_index in range(k, k + ((index_i_testing - i) // 2) + 1):
#                 if i >= index_i_testing + 1 or j_index >= index_j_testing + 1:
#                     if counter in iteration_indices_for_data_output_testing:
#                         fifo_dictionary_testing[f'{k},{k + 2}'].put(extended_array_data_z[0][0])
#                     if counter in iteration_indices_for_data_input_testing:
#                         el = fifo_dictionary_testing[f'{k - 2},{k}'].get()
#                     counter = counter + 1
#                     continue
#                 else:
#                     if counter in iteration_indices_for_data_input_testing:
#                         element_from_queue = fifo_dictionary_testing[f'{k - 2},{k}'].get()
#                     else:
#                         element_from_queue = extended_array_data_z[i][j_index - 1]
#
#                     for _ in range(1, 100):
#                         extended_array_data_x[i + 1][j_index + 1] = f(extended_array_data_x[i - 1][j_index + 2])
#                         extended_array_data_y[i + 1][j_index + 1] = g(extended_array_data_y[i][j_index + 1])
#                         extended_array_data_z[i + 1][j_index + 1] = h(element_from_queue)
#                     el_for_debug = extended_array_data_z[i + 1][j_index + 1]
#                     array_x_test[i - 1][j_index - 1] = f(extended_array_data_x[i - 1][j_index + 2])
#                     array_y_test[i - 1][j_index - 1] = g(extended_array_data_y[i][j_index + 1])
#                     if counter in iteration_indices_for_data_output_testing:
#                         fifo_dictionary_testing[f'{k},{k + 2}'].put(extended_array_data_z[i + 1][j_index + 1])
#                     array_z_test[i - 1][j_index - 1] = h(element_from_queue)
#                     el_for_debug2 = array_z_test[i - 1][j_index - 1]
#                     #print(f'Paral: z({i, j_index}) = {array_z_test[i - 1][j_index - 1]}')
#                 counter = counter + 1

#другий приклад
# def solve_default(index_i_testing, index_j_testing, index_k_testing, extended_array_data_x, extended_array_data_y,
#                   extended_array_data_z, fifo_dictionary_testing,
#                   iteration_indices_for_data_output_testing, iteration_indices_for_data_input_testing, array_x_test,
#                   array_y_test, array_z_test):
#     for k in range(1, index_k_testing + 1):
#         counter = 1
#         for i in range(1, index_i_testing + 1):
#             for j_index in range(k, k + ((index_i_testing - i) // 2) + 1):
#                 if i >= index_i_testing + 1 or j_index >= index_j_testing + 1:
#                     if counter in iteration_indices_for_data_output_testing:
#                         fifo_dictionary_testing[f'{k},{k + 3}'].put(extended_array_data_z[0][0])
#                     if counter in iteration_indices_for_data_input_testing:
#                         el = fifo_dictionary_testing[f'{k - 3},{k}'].get()
#                     counter = counter + 1
#                     continue
#                 else:
#                     if counter in iteration_indices_for_data_input_testing:
#                         element_from_queue = fifo_dictionary_testing[f'{k - 3},{k}'].get()
#                     else:
#                         element_from_queue = extended_array_data_z[i][j_index - 2] #поміняв з -1 на -2
#
#                     #фіктивні масиви
#                     extended_array_data_x[i + 1][j_index + 1] = f(extended_array_data_x[i - 1][j_index + 2])
#                     extended_array_data_y[i + 1][j_index + 1] = g(extended_array_data_y[i][j_index + 1])
#                     #фіктивні масиви
#
#                     #extended_array_data_z[i + 1][j_index + 1] = h(element_from_queue)
#
#                     extended_array_data_z[i + 1][j_index + 1] = f(extended_array_data_z[i - 1][j_index + 2]) +\
#                                                             g(extended_array_data_z[i][j_index + 1]) +\
#                                                             h(element_from_queue)
#
#                     el_for_debug = extended_array_data_z[i + 1][j_index + 1]
#                     array_x_test[i - 1][j_index - 1] = f(extended_array_data_x[i - 1][j_index + 2])
#                     array_y_test[i - 1][j_index - 1] = g(extended_array_data_y[i][j_index + 1])
#                     if counter in iteration_indices_for_data_output_testing:
#                         fifo_dictionary_testing[f'{k},{k + 3}'].put(extended_array_data_z[i + 1][j_index + 1])
#                     array_z_test[i - 1][j_index - 1] = f(extended_array_data_z[i - 1][j_index + 2]) +\
#                                                                 g(extended_array_data_z[i][j_index + 1]) +\
#                                                                 h(element_from_queue)
#                     el_for_debug2 = array_z_test[i - 1][j_index - 1]
#                 counter = counter + 1


def solve_parallel(index_i_testing, index_j_testing, k, extended_array_data_x_threads, extended_array_data_y_threads,
                   extended_array_data_z_threads, fifo_dictionary_threads,
                   iteration_indices_for_data_output_testing, iteration_indices_for_data_input_testing, array_x,
                   array_y, array_z):

    extended_array_data_x_threads = np.copy(extended_array_data_x_threads)
    extended_array_data_y_threads = np.copy(extended_array_data_y_threads)
    extended_array_data_z_threads = np.copy(extended_array_data_z_threads)
    array_x = np.copy(array_x)
    array_y = np.copy(array_y)
    array_z = np.copy(array_z)
    counter = 1
    for i in range(1, index_i_testing + 1):
        for j_index in range(k, k + ((index_i_testing - i) // 2) + 1):
            if i >= index_i_testing + 1 or j_index >= index_j_testing + 1:
                if counter in iteration_indices_for_data_output_testing:
                    fifo_dictionary_threads[f'{k},{k + 2}'].put(extended_array_data_z_threads[0][0])
                if counter in iteration_indices_for_data_input_testing:
                    succeeded = False
                    while not succeeded:
                        if not fifo_dictionary_threads[f'{k - 2},{k}'].empty():
                            el = fifo_dictionary_threads[f'{k - 2},{k}'].get()
                            succeeded = True
                        else:
                            pass
                counter = counter + 1
                continue
            else:
                if counter in iteration_indices_for_data_input_testing:
                    succeeded = False
                    while not succeeded:
                        if not fifo_dictionary_threads[f'{k - 2},{k}'].empty():
                            element_from_queue = fifo_dictionary_threads[f'{k - 2},{k}'].get()
                            succeeded = True
                        else:
                            pass
                else:
                    element_from_queue = extended_array_data_z_threads[i][j_index - 1]

                for _ in range(1, 1000):
                    extended_array_data_x_threads[i + 1][j_index + 1] = f(extended_array_data_x_threads[i - 1][j_index + 2])
                    extended_array_data_y_threads[i + 1][j_index + 1] = g(extended_array_data_y_threads[i][j_index + 1])
                    extended_array_data_z_threads[i + 1][j_index + 1] = h(element_from_queue)

                    array_x[i - 1][j_index - 1] = f(extended_array_data_x_threads[i - 1][j_index + 2])
                    array_y[i - 1][j_index - 1] = g(extended_array_data_y_threads[i][j_index + 1])
                    array_z[i - 1][j_index - 1] = h(element_from_queue)

                if counter in iteration_indices_for_data_output_testing:
                    fifo_dictionary_threads[f'{k},{k + 2}'].put(extended_array_data_z_threads[i + 1][j_index + 1])
                last_x = array_x[i - 1][j_index - 1]
                last_y = array_y[i - 1][j_index - 1]
                last_z = array_z[i - 1][j_index - 1]
            counter = counter + 1

    return last_x, last_y, last_z


#другий приклад
def solve_parallel_second(index_i_testing, index_j_testing, k, extended_array_data_x_threads, extended_array_data_y_threads,
                          extended_array_data_z_threads, fifo_dictionary_threads,
                          iteration_indices_for_data_output_testing, iteration_indices_for_data_input_testing, array_x,
                         array_y, array_z):
    extended_array_data_x_threads = np.copy(extended_array_data_x_threads)
    extended_array_data_y_threads = np.copy(extended_array_data_y_threads)
    extended_array_data_z_threads = np.copy(extended_array_data_z_threads)
    array_x = np.copy(array_x)
    array_y = np.copy(array_y)
    array_z = np.copy(array_z)
    counter = 1
    for i in range(1, index_i_testing + 1):
        for j_index in range(k, k + ((index_i_testing - i) // 2) + 1):
            if i >= index_i_testing + 1 or j_index >= index_j_testing + 1:
                if counter in iteration_indices_for_data_output_testing:
                    fifo_dictionary_threads[f'{k},{k + 3}'].put(extended_array_data_z_threads[0][0])
                if counter in iteration_indices_for_data_input_testing:
                    succeeded = False
                    while not succeeded:
                        if not fifo_dictionary_threads[f'{k - 3},{k}'].empty():
                            el = fifo_dictionary_threads[f'{k - 3},{k}'].get()
                            succeeded = True
                        else:
                            pass
                counter = counter + 1
                continue
            else:
                if counter in iteration_indices_for_data_input_testing:
                    succeeded = False
                    while not succeeded:
                        if not fifo_dictionary_threads[f'{k - 3},{k}'].empty():
                            element_from_queue = fifo_dictionary_threads[f'{k - 3},{k}'].get()
                            succeeded = True
                        else:
                            pass
                else:
                    element_from_queue = extended_array_data_z_threads[i][j_index - 1]

                for _ in range(1, 1000):
                    extended_array_data_x_threads[i + 1][j_index + 2] = f(extended_array_data_x_threads[i - 1][j_index + 3] + \
                                                                          extended_array_data_x_threads[i][j_index + 2])

                    #фікт
                    extended_array_data_y_threads[i + 1][j_index + 2] = extended_array_data_y_threads[i][j_index + 2]
                    #фікт

                    extended_array_data_z_threads[i + 1][j_index + 2] = h(element_from_queue)

                    # extended_array_data_z_threads[i + 1][j_index + 2] = f(extended_array_data_z_threads[i - 1][j_index + 3]) + \
                    #                                         g(extended_array_data_z_threads[i][j_index + 2]) + \
                    #                                         h(element_from_queue)

                    array_x[i - 1][j_index - 1] = f(extended_array_data_x_threads[i - 1][j_index + 3] + \
                                                    extended_array_data_x_threads[i][j_index + 2])
                    #фікт
                    array_y[i - 1][j_index - 1] = extended_array_data_y_threads[i][j_index + 2]
                    #фікт

                    array_z[i - 1][j_index - 1] = h(element_from_queue)

                    # array_z[i - 1][j_index - 1] = f(extended_array_data_z_threads[i - 1][j_index + 3]) + \
                    #                               g(extended_array_data_z_threads[i][j_index + 2]) + \
                    #                               h(element_from_queue)

                if counter in iteration_indices_for_data_output_testing:
                    fifo_dictionary_threads[f'{k},{k + 3}'].put(array_z[i - 1][j_index - 1])
                last_x = array_x[i - 1][j_index - 1]
                last_y = array_y[i - 1][j_index - 1]
                last_z = array_z[i - 1][j_index - 1]

            counter = counter + 1

    return last_x, last_y, last_z


#перший приклад
def solve_sequential(index_i_testing, index_j_testing, extended_array_data_x, extended_array_data_y,
                     extended_array_data_z, array_x_test, array_y_test, array_z_test):
    for i in range(1, index_i_testing + 1):
        for j_index in range(1, index_j_testing + 1):

            for _ in range(1, 1000):
                extended_array_data_x[i + 1][j_index + 1] = f(extended_array_data_x[i - 1][j_index + 2])
                extended_array_data_y[i + 1][j_index + 1] = g(extended_array_data_y[i][j_index + 1])
                extended_array_data_z[i + 1][j_index + 1] = h(extended_array_data_z[i][j_index - 1])

                array_x_test[i - 1][j_index - 1] = f(extended_array_data_x[i - 1][j_index + 2])
                array_y_test[i - 1][j_index - 1] = g(extended_array_data_y[i][j_index + 1])
                array_z_test[i - 1][j_index - 1] = h(extended_array_data_z[i][j_index - 1])


#другий приклад
def solve_sequential_second(index_i_testing, index_j_testing, extended_array_data_x_threads, extended_array_data_y_threads,
                            extended_array_data_z_threads, array_x, array_y, array_z):
    for i in range(1, index_i_testing + 1):
        for j_index in range(1, index_j_testing + 1):

            for _ in range(1, 1000):
                extended_array_data_x_threads[i + 1][j_index + 2] = f(extended_array_data_x_threads[i - 1][j_index + 3] + \
                                                                      extended_array_data_x_threads[i][j_index + 2])

                #фікт
                extended_array_data_y_threads[i + 1][j_index + 2] = extended_array_data_y_threads[i][j_index + 2]
                #фікт

                extended_array_data_z_threads[i + 1][j_index + 2] = h(extended_array_data_z_threads[i][j_index - 1])

                # extended_array_data_z_threads[i + 1][j_index + 2] = f(extended_array_data_z_threads[i - 1][j_index + 3]) + \
                #                                                     g(extended_array_data_z_threads[i][j_index + 2]) + \
                #                                                     h(extended_array_data_z_threads[i][j_index - 1])

                array_x[i - 1][j_index - 1] = f(extended_array_data_x_threads[i - 1][j_index + 3] + \
                                                extended_array_data_x_threads[i][j_index + 2])

                #фікт
                array_y[i - 1][j_index - 1] = extended_array_data_y_threads[i][j_index + 2]
                #фікт

                array_z[i - 1][j_index - 1] = h(extended_array_data_z_threads[i][j_index - 1])

                # array_z[i - 1][j_index - 1] = f(extended_array_data_z_threads[i - 1][j_index + 3]) + \
                #                               g(extended_array_data_z_threads[i][j_index + 2]) + \
                #                               h(extended_array_data_z_threads[i][j_index - 1])