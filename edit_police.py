'''edit_police.py
Author: Bill Jameson
diff backups of cnc programs to sniff out manual editing
v0.3: start generating report
TODO:
  - filter out hunks with only changes to E variables
    (will only occur as assignments at beginning of line)
  - get timestamps for files, save report with date in filename
  - generalize for all files in a directory/set of directories
  - append results from other files to end of report
'''
import difflib
import re

def match_diff(diff):
    '''Input: unified diff
    Output: list containing the diff separated into its constituent
    hunks (with the header leading)
    Note: the result will have an odd length: the header, plus two
    items per hunk (the control line, and the hunk itself)'''
    return re.split('(@@.*@@\n)', diff)

def diff_files(prev_filename, new_filename):
    with open(prev_filename, 'r') as prev_backup:
        prev_backup_contents = prev_backup.read().splitlines()
    with open(new_filename, 'r') as new_backup:
        new_backup_contents = new_backup.read().splitlines()

    diff = difflib.unified_diff(prev_backup_contents, new_backup_contents,
                                prev_filename, new_filename)

    return [d for d in diff]

report_filename = 'report.txt'
testdata = ('108_2mockup.NC', '108_3modified.NC')
diff = diff_files(testdata[0], testdata[1])
diff_text = '\n'.join(diff)

print(diff_text)

hunks = match_diff(diff_text)

with open(report_filename, 'w') as report_file:
    report_file.write(hunks[0])

    for h in hunks[1:]:
        report_file.write(h)
