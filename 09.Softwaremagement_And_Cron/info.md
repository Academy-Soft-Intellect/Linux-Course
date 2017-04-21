=======
- Yum is package manager for .rpm packages. RPM is also a package manager for .rpm pacakges.
  *  yum would resolve all dependencies. With RPM you would have to resolve the dependencies manually. Use yum by default.
     
- Software on Red Hat Enterprise Linux distributions is provided in the RPM format.
  *  RPM package files are named 'name-version-release.architecture' httpd-tools-2.4.6-7.el7.x86_64.rpm
  *  Processors run in two modes: 32 bit and 64. In 32 bit, they can access up to 4GB memory.
  *  x86_64 => runs on x86 architectuture(32 bits) and on 64 bits.


- Repository is usually a http container full with .rpm packages. 
  * To create a new repo, you would need a file ending in .repo located in /etc/yum.repos.d/:
  * The file must contain [label] section, [name] and [baseurl]. 
  * Use you-config-manager to automate the process.
  * RPM package can be signed by GNU Privacy Guard(GPG) key to verify that your package is trustworthy. Usually the key is available trhough the repository.
 

- The cron service is used as a generic one to run processes automatically at specific times.

  * Preconfigured time runner files in /etc/cron.hourly, cron.daily, cron.weekly and cron.monthly. Cron uses anacron to make sure they are always starting.
  
  * crontab -e => add a crontab entry. 
  [Crontab generator](http://crontab-generator.org/)



