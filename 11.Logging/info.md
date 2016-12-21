**Logging in Linux**
  * Direct logging, services write to specific log files (Samba, Apache)
  * rsyslogd => service for managing centralized log files. Write the messages in different files in **/var/log/messages**
  * journald => with the introduction of systemd, the journald log service has been introduced sa well. Tightly integrated with systemd.
  
 **Logger**
   * enables users to write messages to rsyslog from the command line.
   
 **Rsyslog configuration**
   * Facility = Catherogy
   * Severity = Priority
   
   [Basic rsyslog configuration](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/s1-basic_configuration_of_rsyslog.html)    
    
**Facilities** => kern, user, mail, auth, cron ...
**Severities** => debug, info, notice, warning, alert, emerg, crit.

    Configuration file => /etc/rsyslog.conf

  * kern.* => all messages from Facility kern with whatever priority. 
  * mail.crit => all messages from Facility mail with crit priority.
  * cron.!info,!.debug => all messages from Facility cron without info and debug.
  
**logrotate** => started periodically from crond to to make sure there is enough space in your /var/log directory.

    Configuration file => /etc/logrotate.conf 


[Rackspace logrorate knowledge article](https://support.rackspace.com/how-to/understanding-logrotate-utility/)    