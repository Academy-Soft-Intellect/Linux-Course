- Every file/directory has permissions.
- For Directory objects.
  * r => list the content.
  * w => create files.
  * x => go inside directory.
  
- For File objects.
  * r => read  the file :+1:
  * w => edit the file.
  * x => execute the file as a script.
- Special permissions
  * Set user id => a program is executed with the file owner's permissions.
  * Set group id => files created in the directory inherit its group id.
  * Sticky bit => any user can create files, but only the owner of the file can delete it.
- ACL => a way to extend the normal permissions. 

