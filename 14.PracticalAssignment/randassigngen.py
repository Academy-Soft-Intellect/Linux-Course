import os
from random import randint

potential_tasks = {

    "Essential": [
            "Redirect all your aliases into file /tmp/aliases",
            "Grep for users starting with 'r' and redirect it to /tmp/userswithr",
            "Find all files under /boot starting with 'vm'",
            "Find all man keywords for 'partition' and redirect it to /tmp/manpartinfo"
    ],

    "Filesystem": [
            "Create a compression archive of /home directory with name home.tar.gz, place it under /tmp",
            "Create an archive of 3 files, name it archive.tar"
    ],

    "UsersAndGroups": [
            "Add a sudo user 'genadi', use the 'wheel' group",
            "Add two users 'pesho' and 'gosho', make one of them member of 'wheel' group",
            "Create user 'vieri' and set his password to 'hello', make changable each 90 days",
            "Add a group 'skilledworkers', add 'linuxadmin' user as a member of it."
    ],

    "Permissions": [
            "Create a file  'script.sh' inside /tmp directory, make it executable",
            "Create a directory '/tmp/lol', make sure it has group collaboration set.",
            "Create a file 'weirdfile', create a user 'john', make sure john is added as being able to edit the file, add him using ACL."
    ],

    "Networking": [
            "Get all your listening TCP services and redirect the output in /tmp/services",
            "Change your hostname to 'linuxmaster'",
            "Add a host entry before any DNS lookup, 192.168.0.254 amilast?",
            "Change your DNS server to use Google's one 8.8.8.8"
    ],

    "Processes": [
            "Redirect all your current shell processes to /tmp/processes",
            "Redirect the load average to /tmp/loadaverage",
            "Find any ssh process and redirect it to /tmp/ssh"
    ],

    "PartitionsLVM": [
             "Two disks are added to your virtual machine, /dev/s*. Split the first one into two master partitions, create ext4 fs on both of them.\nMount the first fs under /first, mount the second under /second. Make sure they are pesistant. \nSecond disk must be used for LVM, fs schould be xfs, persistant again, mount it under /lvm"
    ],

    "SftMngAndCron": [
            "Add the Extra Packages for Enterprise Linux(EPEL) repository",
            "Create a simple bash script with the name 'cool.sh' that must run each day",
            "Search for the httpd package, if not found install it"
    ],

    "Systemd": [
            "Reset the root password to 'softintellect'",
            "Check the status of sshd and redirect to /tmp/statusshd",
            "Check whether httpd is enabled and redirect to /tmp/httpdenabled",
            "Get the default target and redirect to /tmp/defaulttarget"
    ],

    "Logging": [
            "Cat the generic log file and output it to /tmp/logcontent",
            "Log a message to rsyslog",
            "Get the logging for process 0 and redirect it to /tmp/loguid0",
            "Set the rotating logging policy to 3 weeks."
    ],

    "SSH": [
            "Permit the Root login",
            "Change the default SSH port",
            "Copy your ssh id to localhost"
    ],

    "NFSandSamba": [
            "Export /nfs/data to 192.168.0.253, read/write, root_squashed",
            "Export samba share with label [Data] under path=/samba/data"
    ],

    "Firewall": [
            "Open the firewall for both NFS and CIFS"
    ],

    "Bash-Scripting": [
            "Create a bash script that display the storage on all xfs and ext4 file systems in human readable format, make sure it runs as cron job every 4 hours",
            "Create a bash script that display the storage on all temprorary file systems, make sure it runs as cron job every day"
    ]
}

final_tasks = []


for task_cathegory, tasks in potential_tasks.items():
    l = len(tasks)
    random_task = tasks[randint(0, l - 1)]
    final_tasks.append(random_task)

counter = 1

with open( "/tmp/exam", "w" ) as f:
    for task in final_tasks:
        f.write(str(counter) + "." + task + "\n")
        counter += 1

os.system("cp /tmp/exam /tmp/exam.backup")

print("You assignment is located in /tmp/exam")
print("A back up of the assignment could be found in /tmp/exam.backp")
print("Do not run the script anymore, since it would produce a new exam")
