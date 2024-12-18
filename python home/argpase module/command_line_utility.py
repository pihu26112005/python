
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser() # defining object 
# add argument se new argument add hota hai , jisko hum fir terminal pe value input de skte hai 
  # --x , -xinput naam hai input ke jo hum denge , dono hi same chij ke do naam hai 
  # terminal pe koi sa bhi likh skta hi - python command_line_utility.py --x 4 --y 7 --o add
                                      # - python command_line_utility.py -xinput 4 -yinput 7 --o add
                                      # - python command_line_utility.py  4 7 add
    # default se vo value hoti hai agar input me kuch bhi nhi diya toh vo default vaue input me jati hai 
    # type hai data type jo input value ka hai

    parser.add_argument('--x','-xinput', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--y','-yinput', type=float, default=3.0,
                        help="Enter second number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation. Please contact harry bhai for more")


def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

# praser.parse_args se input de gyi chijo ka ek object bnta hai , jisme sare input hotr hai , 
#         unhe unke name se access kar skte hai  - jaise - args.o or args.x
#          but single dash vale nhi likh skte hai - jaise - args.xinput ya args.yinput not valid
args = parser.parse_args()
# sys.stdout.write(str(calc(args)))
print(calc(args))