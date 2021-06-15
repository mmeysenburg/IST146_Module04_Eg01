'''
Python program to create the README.md file
for IST 146 online materials.
'''

suffix = input('Enter header suffix: IST146_Module0')
headerStr = 'IST146_Module0' + suffix

import glob

# list of all files in the current directory
files = [x.replace('.\\', '') for x in glob.glob('./*')]
# sort by type, then by name within type
files = sorted(files, key = lambda x : (x[x.find('.'):], x))

defaults = {'README.md' : 'This README file.',
    'LICENSE' : 'GNU General Public License v3.0 for these materials.',
    'Main.java' : 'Main program to run the code from a user\'s perspective. This file\'s `main()` method is invoked when you click the "Run" button.',
    'test.sh' : 'Bash script to execute the JUnit4 unit tests in '}

for i, name in enumerate(files):
    print(i, name)

mainFileIdx = int(input('Choose file with TODOs in it: '))
mainFile = files[mainFileIdx]
testFileIdx = int(input('Choose JUnit test file (-1 for none): '))
if testFileIdx < 0:
    testFile = ''
else:
    testFile = files[testFileIdx]

with open('README.md', 'w') as outFile:
    outFile.write('# ' + headerStr + '\n\n')

    outFile.write('<TODO: add README introduction>\n\n')

    outFile.write('## Instructions\n\n')

    outFile.write('1. Log on to your replit account. \n')
    outFile.write('2. Click the "+ New repl" button to create a new repl. \n')
    outFile.write('3. Click on the "Import from GitHub" tab. \n')
    outFile.write('4. Type or paste the following URL into the "Paste any repository URL" text field: `github.com/mmeysenburg/' +
        headerStr + '`\n')
    outFile.write('5. Click on the "Import from github" button.\n')
    outFile.write('6. Click the "Done" button in the ".replit" dialog that appears.\n')
    outFile.write('7. From the "Console" tab, enter the following command: `rm .replit` *If you omit this step, the "Run" '+
        'button will not work as it should!*\n')
    outFile.write('8. Select the `' + mainFile + '` file. Search for the keyword "TODO", and write the specified code.\n')
    outFile.write('9. At any time you can run the code from the user\'s perspective, or, from a developer\'s point of view,' +
        ' execute the unit tests that have been provided.\n')
    outFile.write('  * To run the code, click the "Run" button.\n')
    outFile.write('  * To execute the unit tests (if any), enter the following command in the "Console" tab: `bash test.sh`\n')
    outFile.write('10. Once you have completed the code correctly, the unit tests (if any) should pass, and running the code' +
        ' should produce results that make sense.\n')
    outFile.write('11. When you are finished, submit your `' + mainFile + '` file via the Canvas assignment.\n\n')

    outFile.write('## Files in the repository\n\n')

    for f in files:
        outFile.write('* ')
        if f in defaults:
            outFile.write('`' + f + '`: ' + defaults[f])
            if f == 'test.sh':
                outFile.write(testFile + '\n')
            else:
                outFile.write('\n')
        else:
            txt = input('Enter file description for ' + f + ': ')
            outFile.write('`' + f + '`: ' + txt + '\n')