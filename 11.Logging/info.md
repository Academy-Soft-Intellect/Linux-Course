 
**Logging in Linux**

  * Direct logging, services write to specific log files (Samba, Apache)
  
  * rsyslogd => service for managing centralized log files. Write the messages in different files in **/var/log/**
  
  * /var/log/messages => generic rsyslog folder. /var/log/secure => security and authentication-related messages. /var/log/cron => periodically executed tasks. /var/log/boot.log => system startup.
  
  
  * journald => with the introduction of systemd, the journald log service has been introduced as well. Tightly integrated with systemd. Log management service that collects messages from the kernel, the early stages of the boot process ... It writes these messages to a structured journal of events that by, default, does not persist between reboots.
  
 
  
 **Logger** => enables users to write messages to rsyslog from the command line.
   
 **Rsyslog configuration**
   * Facility = Catherogy
   * Severity = Priority
   
**Facilities** => kern, user, mail, auth, cron ...
**Severities** => debug, info, notice, warning, alert, emerg, crit.
   [Basic rsyslog configuration](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/s1-basic_configuration_of_rsyslog.html)    

    Configuration file => /etc/rsyslog.conf

  * kern.* => all messages from Facility kern with whatever priority. 
  * mail.crit => all messages from Facility mail with crit priority.
  * cron.!info,!.debug => all messages from Facility cron without info and debug.
  
**logrotate** => started periodically from crond to to make sure there is enough space in your /var/log directory.

    Configuration file => /etc/logrotate.conf 


[Rackspace logrorate knowledge article](https://support.rackspace.com/how-to/understanding-logrotate-utility/)    
