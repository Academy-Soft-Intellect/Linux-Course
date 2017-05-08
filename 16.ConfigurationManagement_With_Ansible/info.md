1. [Ansible introduction](https://www.ansible.com/configuration-management)
2. [Ansible Getting Started guide, official documentation](http://docs.ansible.com/ansible/intro_getting_started.html)

# Ansible layout
* /etc/ansible => The main configuration folder which encompasses all Ansible config
* /etc/ansible/hosts => This file holds information for the hosts/and host groups you will configure
* /etc/ansible/ansible.cfg => The main configuration file for Ansible

# Good practice
* Ansible depends on SSH access to the servers you are managing. Ansible works best when you have SSH public key authentication configured so that you don’t have to use passwords to access your hosts.

# Inventory file
* Ansible uses an inventory file to determine what hosts to work against. In its simplest form, an inventory file is just a text file containing a list of host names or IP addresses - one on each line. The default location is /etc/ansible/hosts

# Modules
*  Ansible ships with a number of modules (called the ‘module library’) that can be executed directly on remote hosts or through Playbooks. 
* [Modules](http://docs.ansible.com/ansible/modules.html)

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
* Handlers are just like tasks, but they only run when they have been told by a task that changes have occurred on the client system. For instance, we have a handler here that starts the Nginx service after the package is installed. 
```{r, engine='bash', count_lines}
---
- hosts: droplets
  tasks:
    - name: Installs nginx web server
      apt: pkg=nginx state=installed update_cache=true
      notify:
        - start nginx

  handlers:
    - name: start nginx
      service: name=nginx state=started
```

