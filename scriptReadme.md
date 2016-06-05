#SCRIPT INSTRUCTIONS
##File: generator.py

##Dependencies:
python >= 3.0

##Description:
This script creates problem files for the domain files of the extension3 and extension4 of the gym planification
program. There are to options in order to generate those files:

* Generate random files: With this option you can generate problems for each extension randomizing all problem elements. You
can generate multiple files. They will be saved on the JocsDeProva/Ext3 (or Ext4) folder that will be created. They will be named
file_i.pddl being i the version number. If files exists the number version will be increased so no files are overwritten.

* Generate files interactively: With this option you will generate files controlling all elements of the problem, that they will be
asked to you. The file name and location will also be asked to you, saved upon the root folder of the project.

##Instructions:
-Give the file permission to be executed. For example:
```bash
 $ chmod +x generator.py
```
on unix-based systems.
-execute and follow the indications of the program.
