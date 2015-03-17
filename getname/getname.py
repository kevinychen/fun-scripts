# kerberos -> name

import subprocess

while True:
    s = raw_input()
    p = subprocess.Popen(['finger', s + '@mitdir.mit.edu'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()

    # name: 'name'
    if 'name: ' not in stdout:
        print '?'
        continue
    i = stdout.index('name: ')
    stdout = stdout[i + len('name: '):]

    # cut off rest of line
    i = stdout.index('\n')
    stdout = stdout[:i]

    # last name, first name to first name last name
    i = stdout.index(', ')
    stdout = stdout[i + len(', '):] + ' ' + stdout[:i]
    print stdout

