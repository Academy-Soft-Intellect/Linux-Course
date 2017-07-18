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

```{r, engine='bash', count_lines}
# check your hosts
ansible all --list-hosts

# ad hoc command 
ansible all -a "df -hT"

# using the 'setup' module for ansible, list all of the known facts for all systems configured in the 'hosts' file on the #system.
ansible all -m setup 

# filter the result 
ansible all -m setup -a 'filter=ans*ipv4*'

# a little bit more complicated commands, require a module
ansible all -m shell -a 'yum list installed | grep python'
```

# Modules
*  Ansible ships with a number of modules (called the ‘module library’) that can be executed directly on remote hosts or through Playbooks. 
* [Modules](http://docs.ansible.com/ansible/modules.html)
* Install 'ansible-doc'
* List all available modules or search for a desired one. View the module information and make sure you are aware about the
mandatory options with the '=' sign. Examples:

```{r, engine='bash', count_lines}
#list all the modules coming with the standart installation.
ansible -l 

#search for some file system modules
ansible -l | grep fs
ansible zfs

#when zfs module is used, name and state are mandatory fields.
Options (= is mandatory):
= name
        File system, snapshot or volume name e.g. `rpool/myfs'
= state
        Whether to create (`present'), or remove (`absent') a file system, snapshot or volume.
        
# Create a new volume called myvol in pool rpool.
- zfs:
    name: rpool/myvol
    state: present
    volsize: 10M

```

# Playbook
* Ansible playbooks are a way to send commands to remote computers in scripted way. Instead of using Ansible commands individually to remotely configure computers from the command line, you can configure entire complex environments by passing a script to one or more systems.

* Ansible playbooks are written in the YAML data serialization format.
* Some important properties:
1. Run your playbooks with --ask-become-pass, instead of storing the password somewhere.
2. If you need to use sudo, use 'become', the sudo user is expressed with 'become_user'.
[Become Privileges](http://docs.ansible.com/ansible/become.html)
```{r, engine='bash', count_lines}
 cat apache.yml
---
- hosts: all
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

* When ansible-playbook is executed with --check it will not make any changes on remote systems. Instead, any module instrumented to support ‘check mode’ (which contains most of the primary core modules, but it is not required that all modules do this) will report what changes they would have made rather than making them.

* A task is simply the use of one of Ansible modules. For exampple, installing package would be a task since it will require you to use the ‘yum’ module.



