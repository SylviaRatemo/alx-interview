#!/usr/bin/python3
'''Log Parsing
'''
import sys

STATUS_CODES = {"200", "301", "400", "401", "403", "404", "405", "500"}
stats = {code: 0 for code in STATUS_CODES}
total_size = 0


def print_stats():
    """
    Function that prints stats about log
    """
    print(f'File size: {total_size}')
    for code, count in sorted(stats.items()):
        if count > 0:
            print(f'{code}: {count}')


if __name__ == "__main__":
    line_count = 0

    try:
        """ Iterate over standard input """
        for line in sys.stdin:
            try:
                fields = line.split()
                status_code = fields[-2]

                """ If there is a status code """
                if status_code in STATUS_CODES:
                    stats[status_code] += 1

                """ If there is a length """
                total_size += int(fields[-1])

            except (ValueError, IndexError):
                pass

            """ Printing control """
            line_count += 1
            if line_count == 10:
                print_stats()
                line_count = 0

    except KeyboardInterrupt:
        print_stats()
        raise
    else:
        print_stats()
