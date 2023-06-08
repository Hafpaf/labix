# Commands

```bash
ansible-playbook route_server.yml -t <tag> 
```

The following tags are available:

```bash
ping   # testing ping connectivity
deploy # deploy everything
bird   # update bird configuration
```

Note: the bird configuration file is currently empty. All configuration files
can be found in `./roles/route_server/files/`. This makes the playbook fail.

# Architecture

In the main directory is a file, `inventory`, containing a list of all machines.
The host running Ansible is responsible for connecting to these via `ssh`, so
make sure this is possible (e.g. by changing `~/.ssh/config`). Authenticate as
the user `user`. Emil knows the `sudo` password.

The `ansible.cfg`-file contains default configuration options, such as running
all as root and asking for the sudo password.

The `route_server.yml` calls the `route_server` role. This in turn calls
`main.yml` in the `./roles/route_server/tasks/` directory. This imports the
deployment and bird configuration scripts.
