- **Systemd** is the first process in Linux, responsbile for staring all kinds of different units. Units could be services, sockets, mounts. The most important unit is the **service** unit.
 
  [SystemD in Fedora Documentation.](https://fedoraproject.org/wiki/Systemd)
 
- In Systemd, the OS is controlled in **targets**. Each target consists of a set of units. 
  1. poweroff.target
  2. rescue.target
  3. **multi-user.target**
  4. **graphical.target**
  5. reboot.target
  
- The **default configuration** is located in **/usr/lib/systemd/system**. You could override the defaults in **/etc/systemd/system**.

- **systemctl** is the command that rules the units.
  * E.g **systemctl status sshd**
  * E.g **systemctl is-enabled sshd**
  
 - Targets could be isolated if they have the **isolate** option. You always have a default target. **systemctl get-default**
 
 - GRUB2 boot loader is installed on the boot sector of your hard driver and configured to load a Linux kernel and initramfs.
   
  [GNU GRUB](https://en.wikipedia.org/wiki/GNU_GRUB)
  
  [GRUB2 RedHat](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/ch-Working_with_the_GRUB_2_Boot_Loader.html)
 - **initramfs** a mini file system with drivers needed to continue the booting process ( LVM, SCSI modules for accessing disks)

  [Why the hell do we need it ?](http://unix.stackexchange.com/questions/122100/why-do-i-need-initramfs)
 - **grub2-mkconfig** the right tool to change something inside your GRUB2 coniguration.
