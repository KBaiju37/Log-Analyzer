import argparse
parser = argparse.ArgumentParser(
    description="Analyze log files"
)
parser.add_argument("file")
args = parser.parse_args()
print(args.file)