import task_setting
import book
import library
import math
import collections

from calculate_evaluation_params import *


def parse(input_file_path):
    with open(input_file_path, "r") as input_file:
        books_count, libraries_count, days = (int(x) for x in input_file.readline().split(' '))
        # print books_count, libraries_count, days
        books = [book.Book(book_id, score) for (book_id, score) in enumerate(input_file.readline().split(' '))]
        # for b in books:
        #    print b.id, b.score
        libraries_data_lines = input_file.readlines()
        # print libraries_data_lines
        libraries = []
        for lib_id in range(libraries_count):
            number_of_books, signup_time, scanning_throughput = (int(x) for x in
                                                                 libraries_data_lines[2 * lib_id].split(' '))
            # print number_of_books, signup_time, scanning_throughput
            books_ids = [int(x) for x in libraries_data_lines[2 * lib_id + 1].split(' ')]
            libraries.append(library.Library(lib_id, signup_time, scanning_throughput, books_ids))
        # for lib in libraries:
        #     print lib.id, lib.signup_time, lib.scanning_throughput, lib.books_ids
        return task_setting.TaskSetting(books_count, libraries_count, days, libraries, books)


def calculate_maximal_route(start_id, task_database):
    total_time = task_database.days
    total_result_tuple_array = []
    start_library = task_database.libraries[start_id]
    book_scoring_array = [int(task_database.books[i].score) for i in start_library.books_ids]
    total_score = sum( book_scoring_array )
    total_scanned_book_ids = start_library.books_ids
    total_time -= ( start_library.signup_time + math.ceil(len(book_scoring_array) / start_library.scanning_throughput)  )

    total_result_tuple_array.append( (start_id, total_scanned_book_ids) )
    while total_time > 0:
        timing_measure = calculate_timing_tradeoff(task_database, total_scanned_book_ids)
        libraries_ids = reversed(sorted((e, i) for i, e in enumerate(timing_measure)))
        start_library = task_database.libraries[start_id]
        current_scanned_book_ids = [start_library.books_ids[i] for i in range(len(start_library.books_ids))
                                    if start_library.books_ids[i] not in total_scanned_book_ids]

        total_scanned_book_ids += current_scanned_book_ids
        book_scoring_array = [int(task_database.books[i].score) for i in current_scanned_book_ids]
        total_score += sum(book_scoring_array)
        total_time -= (start_library.signup_time + math.ceil(len(book_scoring_array) / start_library.scanning_throughput))

        total_result_tuple_array.append((start_id, current_scanned_book_ids))

        print(start_id)
        print(total_score)
        print(total_time)
    return total_score, total_result_tuple_array


def day_after_day(task_database):
    total_days = task_database.days
    current_running_libraries = []
    running_libraries_count = 0
    scannable_books_ids = []
    about_to_register_lib = None
    time_until_next_lib_registeration = 0
    output_libs = collections.OrderedDict()
    for day_number in xrange(total_days):
        #print "day #{}".format(day_number)
        if time_until_next_lib_registeration is 0:
            if about_to_register_lib is not None:
                #print "lib #{} finished registeration".format(about_to_register_lib)
                running_libraries_count += 1
                output_libs[about_to_register_lib] = []
                current_running_libraries.append(about_to_register_lib)
                scannable_books_ids.extend([i for i in task_database.libraries[about_to_register_lib].books_ids if i not in scannable_books_ids])
                scannable_books_ids = sorted(scannable_books_ids, key=lambda i: task_database.books[i].score, reverse=True)
            about_to_register_lib = find_current_most_valuable_lib(task_database, total_days-day_number, current_running_libraries)
            if about_to_register_lib == -1:
                time_until_next_lib_registeration = -1
                #print "finish registeration of all libs"
            else:
                #print "lib #{} started registeration".format(about_to_register_lib)
                time_until_next_lib_registeration = task_database.libraries[about_to_register_lib].signup_time
        should_remove_libs = []
        for lib in current_running_libraries:
            scanned_books_by_current_lib = []
            for book_id in scannable_books_ids:
                if book_id in task_database.libraries[lib].books_ids:
                    scanned_books_by_current_lib.append(book_id)
                    task_database.books[book_id].is_scanned = True
                    if len(scanned_books_by_current_lib) == task_database.libraries[lib].scanning_throughput:
                        break
            for book_id in scanned_books_by_current_lib:
                scannable_books_ids.remove(book_id)
            if len(scanned_books_by_current_lib):
                #print "lib {} scanned book id:".format(lib), scanned_books_by_current_lib
                output_libs[lib].extend(scanned_books_by_current_lib)
            else:
                should_remove_libs.append(lib)
        for i in should_remove_libs:
            current_running_libraries.remove(i)
        # next day preparation:
        time_until_next_lib_registeration -= 1
    return running_libraries_count, output_libs








# for testing:
if __name__ == '__main__':
    input = "InputFiles/c_incunabula.txt"
    task = parse(input)
    count, output = day_after_day(task)
    with open(input + "_out.txt", "w") as f:
        print count
        f.writelines([str(count)])
        for k, v in output.items():
            f.writelines(["{} {}".format(k, len(v))])
            print k, len(v)
            f.writelines([' '.join([str(i) for i in v])])
            print ' '.join([str(i) for i in v])