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

- Partprobe is a program that informs the operating system kernel of partition table changes, by requesting that the operating system re-read the partition table.
 
- Logical Volume Manager, flexible way to manager your storage. 3 layers of abstraction:
  * Physical Volume => your local hard disk, or disk presented using SAN.
  * Volume Group => container that unites the physical volumes storage. You could distribute its storage the way you want it.
  * Logical Volume => a block device where the File System resides. Gets its size from the volume group, you could change its size on demand.
  * Advantages of LVM => not limited by the size of one single disk, rather by the total size. Snapshots of LV.
[LVM advantages](http://askubuntu.com/questions/3596/what-is-lvm-and-what-is-it-used-for)
