import os.path
import types
import sys


module_name = 'module2'
module_file = 'module2.py'
module_path = '.'

# Build up the path
module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

# read source code from file
with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()

# Create a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# Set a ref in sys.modules
sys.modules[module_name] = mod

# compile source code
code = compile(source_code, filename=module_abs_file_path, mode='exec') # exec means there are multiple lines of code.

# execute compiled source code / this runs the module
#print(mod.__dict__)
exec(code, mod.__dict__) # mod.__dict__ tells which namespace to use and store what gets created in the module.
#print(mod.__dict__)

# Done!!!!.
mod.hello()

# or we can do
import module2 as m1 # it was plug into sys.modules

m1.hello()

