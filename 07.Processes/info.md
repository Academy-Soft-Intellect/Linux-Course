- A process is a runing instace of a launched, executable program. You list your processes with 'ps' or 'top'. You typically care about the following process properties:  
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
  
## Load average
  * a cumulative CPU count of active system resource requests. 
  * Perceived system load over a time period. Representation of expected service wait times, not only for CPU but also for disk and network I/O.
  * uptime

## Putty 
 * make sure you are using Putty to log in to your server from now on, pay attention to the NAT vs Bridged Ip as well as the permit root login feature in /etc/ssh/sshd_config
 
