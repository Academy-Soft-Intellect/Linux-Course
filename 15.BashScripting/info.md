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

Expanding variable values
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
