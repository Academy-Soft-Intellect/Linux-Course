- The Filesystem Hierarchy Standard (FHS): defines the directory structure and directory contents in Unix-like operating systems. [RedHat example](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/3/html/Reference_Guide/s1-filesystem-fhs.html)
- Working with files commands: cp, mv and rm.
- INode: a data structure used to represent a filesystem object (file, directory). File systems (ext family, xfs) cares about Inodes, humans care about names. 
- Soft link: softlink is just a pointer with dummy values, it resolves the name of the file each time you access it through the symlink.
- Hard link: directory entry (a file) pointing to the same inode.
- tar: software utility for collecting many files into one archive file.
- gzip: compression (a way of reducing the size of a file on disk using different algorithms and mathematical calculations ) utility.

Usually tar and gzip are runned together.
