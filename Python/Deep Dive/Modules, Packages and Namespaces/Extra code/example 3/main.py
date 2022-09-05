import sys
import importer

module3 = importer.import_('module3', 'module3_source.py', '.')

print(f"sys says {sys.modules.get('module3', 'module3 not found')}")

import module2
module2.hello()