- Privilleged vs Unprivilleged users. Root user has unlimited access.
- id => show information about the current logged in user.
- /etc/passwd => information about each user.  /etc/groups => information about groups. 
- useradd, usermod, userdel, userdel -r, passwd, chage, chage -l
- su => allow a user to switch to a different user account.
- In RH7, all members of group 'wheel' can use sudo to run commands as any user.
- Sudo is a program that allows users to run programs with the security privilleges of another user, by default the superuser.
[Sudo Info](https://en.wikipedia.org/wiki/Sudo)
- usermod, userdel, useradd, passwd.
- Regular expresions, match a string based on a pattern.
  * ^anna => lines that start with anna.
  * $py => files that end with py.
  * r[aou]t => rat, rot, rut.
- LDAP => a protocol for managing related information(most often users) from a centralized location.
[LDAP summary](https://www.electricmonk.nl/log/2013/03/10/quick-introduction-to-ldap-basics/)
