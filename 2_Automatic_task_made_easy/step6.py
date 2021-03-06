import argparse
import sys
import configparser

def main(number, other_number, output):
    result = number * other_number
    print(f"The Result is {result}", file=output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n1", type=int, help="A number", default=1)
    parser.add_argument("-n2", type=int, default=1, help="Another Number")
    parser.add_argument("--config", "-c", type=argparse.FileType('r'), help="Config File" )
    parser.add_argument("-o", dest='output', type=argparse.FileType('w') ,default=sys.stdout, help='Output File')

    args= parser.parse_args()

    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)

        args.n1 = int(config["ARGUMENTS"]['n1'])
        args.n2 = int(config["ARGUMENTS"]["n2"])

    main(args.n1, args.n2, args.output)


