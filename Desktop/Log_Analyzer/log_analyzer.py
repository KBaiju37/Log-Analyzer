import argparse


class LogAnalyzer:
    def __init__(self, file):
        self.file = file
        self.log_counts = {}

    def read_log(self):
        with open(self.file, "r") as f:
            for line in f:
                self.parse_log(line)

    def parse_log(self, line):
        parts = line.split()

        if len(parts) >= 4:
            level = parts[3].strip("[]")

            if level in self.log_counts:
                self.log_counts[level] += 1
            else:
                self.log_counts[level] = 1

    def display_summary(self):
        print("Log Summary")
        print("-" * 20)

        for level, count in self.log_counts.items():
            print(f"{level}: {count}")


# CLI
parser = argparse.ArgumentParser(
    description="Analyze log files"
)

parser.add_argument("file", help="Path to the log file")
parser.add_argument(
    "-s",
    "--summary",
    action="store_true",
    help="Display log summary"
)

args = parser.parse_args()

analyzer = LogAnalyzer(args.file)
analyzer.read_log()

if args.summary:
    analyzer.display_summary()