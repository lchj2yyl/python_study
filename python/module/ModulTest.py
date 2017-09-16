import sys

import ModuleA
from module1 import *
import module4
print sys.path


for path in sys.path:
    print path

ModuleA.moduleAFunctionB()
ModuleA.moduleAFunctionC()

ModuleB.moduleBFunctionC()


module4.ModuleD.moduleBFunctionC()














