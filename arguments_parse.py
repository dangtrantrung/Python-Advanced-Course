import argparse

# create parser
parser=argparse.ArgumentParser()
""" Positional arguments """
# parse args
parser.add_argument("x",type=int)
parser.add_argument("y",type=int)

''' Optional arguments '''
# parse args
parser.add_argument("--x1",type=int,default=100)
parser.add_argument("--y1",type=int,required=True)
# get_info
args=parser.parse_args()
print("x= ",args.x)
print("y= ",args.y)
print("Sum= ", args.x+args.y)
print("x1= ",args.x1)
print("y1= ",args.y1)
print("Sum_opt= ", args.x1+args.y1)