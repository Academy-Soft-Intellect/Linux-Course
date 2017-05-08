[Ansible introduction](https://www.ansible.com/configuration-management)
[Ansible Getting Started guide, official documentation](http://docs.ansible.com/ansible/intro_getting_started.html)

# Ansible layout
* /etc/ansible => The main configuration folder which encompasses all Ansible config
* /etc/ansible/hosts => This file holds information for the hosts/and host groups you will configure
* /etc/ansible/ansible.cfg => The main configuration file for Ansible
* /etc/ansible/roles => This folder allows you to create folders for each server role, web/app/db, etc.# Conspect

# Playbook
* Ansible playbooks are a way to send commands to remote computers in scripted way. Instead of using Ansible commands individually to remotely configure computers from the command line, you can configure entire complex environments by passing a script to one or more systems.

* Ansible playbooks are written in the YAML data serialization format.
* Some important properties:
1. Run your playbooks with --ask-become-pass, instead of storing the password somewhere.
2. If you need to use sudo, use 'become', the sudo user is expressed with 'become_user'.
```{r, engine='bash', count_lines}
 cat apache.yml
---
- hosts: all
  become: yes
  become_user: some_sudo_user
  vars:
    http_port: 80
    max_clients: 200
  tasks:
  - name: ensure apache is at the latest version
    yum: name=httpd state=latest
  - name: ensure apache is running
    service: name=httpd state=started  
```

```{r, engine='bash', count_lines}
ansible-playbook apache.yml --ask-become-pass
```

