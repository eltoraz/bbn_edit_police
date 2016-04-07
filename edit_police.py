'''edit_police.py
Author: Bill Jameson
diff backups of cnc programs to sniff out manual editing
v0.2: prototype
'''
import difflib

def diff_files(prev_filename, new_filename):
    prev_backup = open(prev_filename)
    prev_backup_contents = prev_backup.read().splitlines()
    prev_backup.close()
    new_backup = open(new_filename)
    new_backup_contents = new_backup.read().splitlines()
    new_backup.close()
    diff = difflib.unified_diff(prev_backup_contents, new_backup_contents,
                                fromfile=prev_filename, tofile=new_filename)

    return [d for d in diff]

testdata = ('108_2mockup.NC', '108_3modified.NC')
deltas = diff_files(testdata[0], testdata[1])