- Every file/directory has permissions.
- For Directory objects.
  * r => list the content.
  * w => create files.
  * x => go inside directory.
  
- For File objects.
  * r => read  the file :+1:
  * w => edit the file.
  * x => execute the file as a script.
  
- Each permission has a decimal value:
  * read = 4
  * write = 2
  * exec = 1

- Change file/directory permissions.
  * Symbolic method => chmod who?(u,g,o,a)what?(+,-,=)which?(r,w,x)
  * Numerical method => chmod 750 simplefile
  ## Very important
  * The chmod command suports the -R option for recursively setting permissions on an entire directory tree. When using this option, be sure to use the X permissions instead of the x to indicate that execute permissions should only be set on directories, not regular files.
  
- Special permissions
  * Set user id => a program is executed with the file owner's permissions. A good exmaple is /bin/passwd, which needs to modify /etc/passwd, file which only root can edit.
  * Set group id => files created in the directory inherit its group id. A good way to allow a group to share its permission :)
  * Sticky bit => any user can create files, but only the owner of the file can delete it. By default the /tmp directory is set that way.
  
- chown, umask.

- ACL => a way to extend the normal permissions. 

