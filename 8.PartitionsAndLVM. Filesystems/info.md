- Partition is just a slide of the disk. It is easier to distinguish between different types of data. A sector is a unit in which partitions are measured.

- In Linux for the most part (the ones with which you would be working around 99%), you have 2 types of devices:
*  block devices => can be cached in memory and read back from cache, writes can be buffered.
*  character devices => writing/reading is an immediate action.

- An interface is just a pipe that transfers data to a hard disk with its own rules. Most common interfaces:
*  SCSI
*  SATA

- Master Boot Records(MBR, used with BIOS) defines a hard disk layout. Stored on the first sector on the disk and represents partition table + boot loader. 
*  MBR supports only 4 partitions, a workaround is to make an extended partition.

- GUID Partiton table (GPT, usually used with UEFI fimrware), used on the new Unified Extensible Firmware(UEFI)
*  Up to 128 partitions can be created.
*  A backup copy of the GUID partition table is created by default at the end of the disk, which eliminates the single point of failuer that exists in MBR.
*  2TB limit no longer exists. 

* states => running, sleeping.
* ids => each process has an id.
* parent => each process has a parent process, the ultimate parent process is 'systemd'.

- Running jobs in the foreground and background. Any executed program by default is ran as foreground job.
* & (ampersand) in the end of the process will start the command immediately in the background.
* Ctrl + Z => Stops the job temporarily so that it can be managed.
* Ctrl + C => Cancel the current interactive job.
* bg => Continues the job that has just been frozen using Ctrl + Z in the background.
* fg => Brings the last job that was moved to background execution back to the foreground.
* jobs => Shows which jobs are currently running from this shell. Display job numbers that can be used as an argument to the commands 'bg' and 'fg'.

- Sending a signal to a process.
* 1 = Hangup = Report termination of the controlling process of a terminall
* 9 = Kill = Causes program termination. Cannot be ignored, always fatal.
* 15 = Terminate = The defauilt kill signal, it asks politely the program to terminate.

- Process priority => by default is 20. The more negavite you go, the bigger the priority becomes. 

- Showing processes:
* top
* ps -ef | ps aux

