'''edit_police.py
Author: Bill Jameson
diff backups of cnc programs to sniff out manual editing
v0.2: prototype
'''
import difflib
import re

def line_check(line):
    '''Return True if the line is not common to both inputs, False otherwise
    (or if the line should be ignored regardless)'''
    # ignore commands beginning with E variables
    match_pattern = '^[+-?].*'
    ignore_pattern = '^...E.+'
    match = re.match(match_pattern, line)
    ignore = re.match(ignore_pattern, line)

    if match and not ignore:
        return True
    else:
        return False

def diff_files(prev_filename, new_filename):
    prev_backup = open(prev_filename)
    prev_backup_contents = prev_backup.read().splitlines()
    prev_backup.close()
    new_backup = open(new_filename)
    new_backup_contents = new_backup.read().splitlines()
    new_backup.close()

    d = difflib.Differ()
    return list(d.compare(prev_backup_contents, new_backup_contents))

testdata = ('108_2mockup.NC', '108_3modified.NC')
diff = diff_files(testdata[0], testdata[1])

report = [line for line in diff if line_check(line)]

for line in report:
    print(line)

