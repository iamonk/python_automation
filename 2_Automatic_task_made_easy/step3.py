import argparse
import configparser

def main(number, other_number):
    result = number*other_number
    print(f"The Result is {result}")


if __name__ == '__main__':
    # Creating Parser
    parser = argparse.ArgumentParser()
    # Adding Argument
    parser.add_argument("-n1", type=int, help="A number")
    parser.add_argument("-n2",type=int,help="Another Number")
    parser.add_argument("--config", '-c', type=argparse.FileType('r'), help = "Config File")

    #Parsing Argument
    args = parser.parse_args()

    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)

        # Transforming Values into integers

        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])

    main(args.n1, args.n2)   