# Commands

## Client Configurations

The playbook for creating configurations on client updates is available with the
command

```bash
ansible-playbook client_config.yml
```

No tags are necessary.

The playbook will check if ARouteServer has been initialised on the host machine
under `~/arouteserver`. It will then copy the necessary configurations to that
directory. These configurations have been created partially by hydrating jinja2
templates from the `ix_client.yml` file.

Afterwards, a virtual pip environment is initialised and requirements are
installed. This environment is used to create `ixf.json` and `bird.conf`. The
last part copies these back to the ansible directory. Note: this could be
changed to instead copy the files back to the `route_server` role so they are
instantly ready for deployment.

A `members.md` file is also hydrated. Nothing is done with it. This should be
used to deploy an update to the website, `ix.labitat.dk`.

As a final note: `ansible.cfg` no longer asks for the sudo password and will
thus fail. This can be fixed by either supplying the `-k` flag when running that
playbook or by un-commenting the lines.

## Route Server Deployment

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
