#!/usr/bin/python3
'''Log Parsing
'''
import sys
import re
from collections import defaultdict


def process_line(line, metrics):
    # Regular expression pattern for matching the input format
    pattern = re.compile(
        r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" '
        r'(\d+) (\d+)'
    )

    match = pattern.match(line)
    if match:
        ip_address, status_code, file_size = match.groups()
        metrics['total_size'] += int(file_size)
        metrics['status_codes'][status_code] += 1


def print_metrics(metrics):
    print(f"Total file size: {metrics['total_size']}")

    for code in sorted(metrics['status_codes']):
        count = metrics['status_codes'][code]
        print(f"{code}: {count}")


def main():
    metrics = {
        'total_size': 0,
        'status_codes': defaultdict(int)
    }

    try:
        for i, line in enumerate(sys.stdin, start=1):
            process_line(line.strip(), metrics)

            if i % 10 == 0:
                print_metrics(metrics)

    except KeyboardInterrupt:
        '''Handle KeyboardInterrupt (CTRL + C)
        '''
        print_metrics(metrics)
        sys.exit(0)


if __name__ == "__main__":
    main()
