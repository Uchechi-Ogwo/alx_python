import sys

def print_arguments():
    num_args = len(sys.argv) - 1
    args_word = "argument" if num_args == 1 else "arguments"
    ending = ":" if num_args > 0 else "."
    
    print(f"Number of argument(s): {num_args}, followed by {args_word}{ending}\n")
    
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments()
