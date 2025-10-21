import random
import argparse
import sys

"""
Parses input arguments and returns a list containing every line to parse as a string.

If multiple input arguments are given, return -1.
If none are given, return -2.
If another error message exists, return -3.
"""
def get_input_lines(echo, input_range, file):
    lines = []
    inputs_found = 0
    #parse input-range argument (expected: a-b, where type(a,b) = int)
    if input_range is not None:
        inputs_found += 1
        try:
            a,b = input_range.split("-")
            a = int(a)
            b = int(b)
            if a > b:
                raise Exception;
        except:
            print("Error: Invalid argument for --input-range. See --help for more information.")
            exit(1)
        for i in range(a, b+1): #b is inclusive
            lines.append(i)
    #parse echo argument (expected: multiple arguments to be interpreted as lines)
    if echo is not None:
        inputs_found += 1
        lines = echo
    #parse input file given
    if file != "-":
        inputs_found += 1
        try:
            with open(file, "r") as f:
                lines = [x.strip() for x in f.readlines()] #strips the "\n" from the end of every line
        except:
            print("Error: Unable to open input file. See --help for more information.")
            exit(1)

    #safe error handler
    if inputs_found > 1:
        print("Error: multiple input arguments given. See --help for more information.")
        exit(1)
    elif inputs_found == 0:
        print("Error: no input arguments given. See --help for more information.")
        exit(1)

    return lines

"""
Processes command line arguments and performs shuffling.
"""
def shuf(echo, input_range, head_count, repeat, file):
    #if no arguments are given (file == "-" basically means nothing), read from stdin
    if echo is None and input_range is None and file == "-":
        lines = [x.strip() for x in sys.stdin.readlines()] #may also have trailing "\n", ie .txt file
    #otherwise find the input in the arguments
    else:
        lines = get_input_lines(echo, input_range, file)
    
    if head_count is None and repeat == False: #if head_count is not set then every line should be printed once
        random.shuffle(lines)
        for line in lines:
            print(line)
    else: #otherwise we keep printing (and maybe repeating) values until head_count runs out
        if head_count is None:
            head_count = -1 #trigger an infinite loop if repeat is set but not head_count
        elif head_count <= 0:#now we expect a positive integer from head_count or -1 for an infinite loop
            print("Error: Invalid argument for --head-count. See --help for more information.")
            exit(1)
        else:
            repeat = True #set repeat to true so that head_count lines are printed

        should_remove = head_count < len(lines)
        
        while True:
            choice = random.choice(lines) #choose a random line
            print(choice)
            if should_remove:
                lines.remove(choice) #we want permutation not combination

            head_count -= 1
            if head_count == 0 or not repeat or len(lines) == 0: break

"""
Main function to parse arguments and call shuf function.
"""
def main():
    parser = argparse.ArgumentParser(
        description="Implementation of GNU shuf command. Read more https://www.gnu.org/software/coreutils/manual/html_node/shuf-invocation.html"
    )

    #define arguments
    #argparse has --help built-in, so defining help parameter will add to help message
    parser.add_argument(
        "--echo", "-e",
        nargs="+",
        help="Treat each command-line operand as an input line"
    )
    parser.add_argument(
        "--input-range", "-i",
        help="Act as if input came from a file containing the range of unsigned decimal integers lo...hi, one per line."
    )
    parser.add_argument(
        "--head-count", "-n",
        type=int, #this will help catch errors for us
        default=None,
        help="Output at most n lines. By default, all input lines are output."
    )
    parser.add_argument(
        "--repeat", "-r",
        action="store_true", #this is just a flag (not an argument) so we just want to set a True value if this is set
        default=False,
        help="Repeat output values, that is, select with replacement. With this option the output is not a permutation of the input; instead, each output line is randomly chosen from all the inputs. This option is typically combined with --head-count; if --head-count is not given, shuf repeats indefinitely."
    )
    parser.add_argument(
        "file",
        nargs="?", #zero or one arguments
        default="-", #"python3 shuf.py" is the same as "python3 shuf.py -"
        help="Input file name"
    )

    #parse arguments
    args = parser.parse_args() #returns a struct-like object

    #perform the shuffle
    shuf(args.echo, args.input_range, args.head_count, args.repeat, args.file)

main() #excute main function