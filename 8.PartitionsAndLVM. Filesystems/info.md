[Devices/Interfaces](http://www.tldp.org/HOWTO/Partition-Mass-Storage-Definitions-Naming-HOWTO/)

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

 
