# this is to check that it looks in the cache.

print(f'Running {__name__}')

import module3 # When ran from main.py, we do not get a rerun of module3 but it actually goes
# and fetchs the cached version from sys.globals

def hello():
    print('module2 says Hello')
    module3.hello()