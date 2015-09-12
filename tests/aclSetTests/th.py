import os
import glob

class Suite:
    def __init__(self, th):
	aclSet = os.path.abspath(th.path + '/aclSet')

        for test in glob.glob(th.path + '/*Test'):
            cmd = [aclSet]

            args = test + '/data/args'
            if os.path.exists(args):
                cmd += open(args).read().split()

            th.Test(os.path.basename(test), command = cmd)

