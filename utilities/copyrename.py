#copy_rename
#copies file and renames it

import shutil

source = 'a/b/sample.txt'
target = 'c/d/new_sample.txt'

shutil.copy(source, target)