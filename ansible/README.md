# Commands

```bash
ansible-playbook route_server.yml --list-tags
ansible-playbook route_server.yml -t <tag> 
```

The following tags are available:

```bash
apt        # update & install required apt packages
bird       # update bird configuration
deploy     # run & deploy everything
interfaces # update network interfaces
never      # prevent tasks like rebooting except on deployment
nftables   # update nftables
reboot     # reboot target
ping       # test ping connectivity
```

Note: the bird configuration file is currently invalid. This makes the playbook
fail. All configuration files can be found in `./roles/route_server/files/`. 

# Architecture

In the main directory is a file, `inventory`, containing a list of all machines.
The host running Ansible is responsible for connecting to these via `ssh`, so
make sure this is possible (e.g. by changing `~/.ssh/config`). Authenticate as
the user `user`. Emil knows the `sudo` password.

The `ansible.cfg`-file contains default configuration options, such as running
all as root and asking for the sudo password.

The `route_server.yml` calls the `route_server` role. This in turn calls
`main.yml` in the `./roles/route_server/tasks/` directory. This imports all the
different plays for updating and deploying.
