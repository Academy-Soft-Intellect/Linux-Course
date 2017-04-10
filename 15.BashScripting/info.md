- Bash sciprt is simply an executable file, composed of a list of commands. 
- #! => indicates that the file is an executable shell script and the command interpreter.
- #!/bin/bash => the command interpreter is bash.
- Good styling practices: use comments to clarify to readers the purpose and logic of the script. The top of every script should include comments providing an overview of the script's purpose, intendend actions ...
- Indent lines with multiline statements to represent the hierarchy of code logic and the flow of control structures.
- Use consistent formatting through the entirety of a script.

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


```{r, engine='bash', count_lines}
for EVEN in $(seq 2 2 8);
 do echo "$EVEN";
 done;
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

- b => file exists and is special block => [ -b FILE ]
- c => file exists and is character special => [ -c FILE ]
- d => file exists and is directory => [ -d DIRECTORY ]
- e => file exists => [ -e FILE ]
- x => file exists and execute permission is granted => [ -x FILE ] 
 
# If/then/else statement

```{r, engine='bash', count_lines}
#!/bin/bash

systemctl is-active mariadb > /dev/null 2>$1
MARIADB_ACTIVE=$?

if [ "$MARIADB_ACTIVE" -eq 0 ]; then
 echo "We have database"
else
 echo "No db for us"
fi
```


# AWK and SED

In 99 % of the time, AWK is used to print a column from an ouput.
Example below, printing all the block devices from 'df -h', excluding the temporary file systems.

```{r, engine='bash', count_lines}
df -h | grep -v tmpfs | awk '{print $1}'
Filesystem
/dev/mapper/cl-root
/dev/sda1
```

In 99 % of the time, SED is used to replace a string inside a file with another one.

```{r, engine='bash', count_lines}
$ sed 's/vermin/pony/g' metamorphosis.txt
```

AWK and SED are huge topics, the idea is just to be aware about them and know their most often use case.
