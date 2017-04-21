=======
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
  
- A filesystem is the methods and data structures that an operating system uses to keep track of files on a disk or partition; that is, the way the files are organized on the disk. 
  * mounting a file system refers to a location under the root(/) file system. You create the file systems on the so called blocking device. A good practice is each file system to be mounted in /etc/fstab.
  * make sure your blocking device is unique and the same between each reboot, mount the partitions and disks with their UUID, blkid.
  * each file system has a journal, where each transaction is logged, that way a file system could be easily restored.
  * ext4 and xfs are the most common file systems nowadays.
  * superblock is a filesystem metadata and defines its size, status ... It is super important to each file system and therefore is stored in multiple redundant copies. If a superblock of a filesystem, becomes corrupt then the file system cannot be mounted. You could use 'fsck' to repair it from one of the already made back up copies.
     
- Logical Volume Manager(LVM) is a flexible way to manager your storage under 3 layers of abstraction.
   * The lowest layer is the physical volumes, where only storage devices are used(disks, parititons, logical units(LUNs) on a storage area network(SAN)). The storage devices needs to be labelled as physical voluems.
   * Physical volumes can be added to a volume group(a container) from where the storage could be distributed among logical volumes.
   * Logical volumes are simply virtual block devices => we could locate filesystems on the top of them.
  
  
