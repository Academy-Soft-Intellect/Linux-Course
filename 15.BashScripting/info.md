- Bash sciprt is simply an executable file, composed of a list of commands. 
- #! => indicates that the file is an executable shell script and the command interpreter.
- #!/bin/bash => the command interpreter is bash.

# A number of characters have special meaning to bash
 '#' beginning of a comment line.

```{r, engine='bash', count_lines}
echo # not a comment
echo \# not a comment
```

"\\" escape character only removes the special meaning of a single character.

' ' single quotes preserve the literal value of all characters.
```{r, engine='bash', count_lines}
echo '$USER'
```

 " " double quotes do not preserve the literal value of the dollar sign($), the back-ticks(\` \`) and the back-slash(\\)
```{r, engine='bash', count_lines}
echo "$USER"
```


Variables are just a cointaner that can store data.
```{r, engine='bash', count_lines}
COUNT=40
```
If you have string literals, quote them in some brackets, since the shell treats the space character as a word separator.

# Shell expansion/substitution

Expanding variables
```{r, engine='bash', count_lines}
FIRST=Mecho
SECOND=Puh
echo "$FIRST $SECOND"
```
Command substituion
```{r, engine='bash', count_lines}
echo "Current time: $(date)" 
```
Arithmetic expansion
```{r, engine='bash', count_lines}
echo $[1+1]
```

# Execution an action multiple times with the for loop
```{r, engine='bash', count_lines}
for <VARIABLE> in <LIST>; do
 <COMMAND>
 ...;
done
```

bash -x <SCRIPTNAME> to put the debug mode on a script.

# Referencing a script arguments.

$* vs $@

```{r, engine='bash', count_lines}
#!/bin/bash

for ARG in "$*"; do
 echo $ARG
done
```

```{r, engine='bash', count_lines}
#!/bin/bash

for ARG in "$@"; do
 echo $ARG
done
```

# Exit status.
Every command returns an exit status. A successfull command exits with an exit number of 0.
Upon completion, a command's exit status is passed to the parent process and stored in the '?' variable.
Therefore, the exit status can be retrieved with '$?'

# Integer comparison.
- eq => is equal to => [ "$a" -eq "$b" ]
- ne => is not equal to [ "$a" -ne "$b" ]
- gt => is greater than [ "$a" -gt "$b" ]
- ge => is greater than or equal to [ "$a" -ge "$b" ]
- lt => is less than [ "$a" -lt "$b" ]
- le => is less than or equal to [ "$a" -le "$b" ]

# String comparison.
- = is equal to => [ abc = abc ]
- == is equal to => [ abc == def ]
- != is not equal to => [ abc != def ]

# Testing files and directories.

- b => file exists and is special blokc => [ -b FILE ]
- c => file exists and is character special => [ -c FILE ]
- d => file exists and is directory => [ -d DIRECTORY ]
- e => file exists => [ -e FILE ]
- x => file exists and execute permission is granted => [ -x FILE ] 
 
