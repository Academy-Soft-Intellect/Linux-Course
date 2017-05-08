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
--ask-become-pass instead, while also swapping out the use of sudo throughout your playbooks with become.

