#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansible module to manage digitalocean docker machines
# (c) 2016, Jonathan Rowlands <jonrowlands83@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: docker_machine_digitalocean
short_description: Create a digitalocean docker host machine using docker-machine
description:
     - Manage the life cycle of a DigitalOcean docker machine
version_added: "2.2"
options:
  name:
    description:
      - Name of the managed docker-machine
    required: true
  state:
    description:
      - 'I(absent) - A machine matching the specified name will be stopped and removed.'
      - 'I(present)" - Asserts the existence of a machine matching the name and any provided configuration parameters.
         If no machine matches the name, a container will be created. If a machine matches the name but the provided
         configuration does not match, the machine will be updated, if it can be. If it cannot be updated, it will be
         removed and re-created with the requested config. Use the recreate option to force the re-creation of the
         matching machine.'
      - 'I(started) - Asserts there is a running machine matching the name and any provided configuration. If no machine
         matches the name, a machine will be created and started. If a container matching the name is found but the
         configuration does not match, the container will be updated, if it can be. If it cannot be updated, it will be
         removed and a new container will be created with the requested configuration and started. Use recreate to
         always re-create a matching container, even if it is running. Use restart to force a matching machine to be
         stopped and restarted.'
      - 'I(stopped) - Asserts that the machine is first I(present), and then if the machine is running moves it to a
         stopped state.'
    required: false
    default: started
    choices:
      - absent
      - present
      - stopped
      - started
  access_token:
    description:
      - Your personal access token for the Digital Ocean API.
    default: null
    required: true
  image:
    description:
      - The name of the Digital Ocean image to use.
    default: null
    required: false
  region:
    description:
      - The region to create the droplet in, see Regions API for how to get a list.
    default: null
    required: false
  size:
    description:
      - The size of the Digital Ocean droplet (larger than default options are of the form 2gb).
    default: null
    required: false
  ipv6:
    description:
      - Enable IPv6 support for the droplet.
    default: null
    required: false
  private_networking:
    description:
      - Enable private networking support for the droplet.
    default: null
    required: false
  backups:
    description:
      - Enable Digital Oceans backups for the droplet.
    default: null
    required: false
  userdata:
    description:
      - Path to file containing User Data for the droplet.
    default: null
    required: false
  ssh_user:
    description:
      - SSH username.
    default: null
    required: false
  ssh_port:
    description:
      - SSH port.
    default: null
    required: false
  ssh_key_fingerprint:
    description:
      - Use an existing SSH key instead of creating a new one, see SSH keys.
    default: null
    required: false
'''

EXAMPLES = '''
# Create a docker-machine.
- docker_machine_digitalocean:
    name: machine01
    state: started

# Delete a docker-machine.
- docker_machine_digitalocean:
    name: machine01
    state: absent
'''

RETURN = '''
ansible_docker_machine:
    description: 'Facts representing the currently known configuration of the machine. Note that facts are not part of
                  registered vars but accessible directly.'
    returned: always
    type: dict
    sample: '{
            "config_version": 3,
            "driver": {
                "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "backups": false,
                "droplet_id": xxxxxxx,
                "droplet_name": "",
                "image": "ubuntu-15-10-x64",
                "ip_address": "xxx.xxx.xxx.xxx",
                "ipv6": false,
                "machine_name": "xxxxxxx",
                "private_networking": false,
                "region": "nyc3",
                "size": "512mb",
                "ssh_key_fingerprint": "",
                "ssh_key_id": xxxxxxx,
                "ssh_key_path": "/home/xxxxxx/.docker/machine/machines/xxxxxxxx/id_rsa",
                "ssh_port": 22,
                "ssh_user": "root",
                "store_path": "/home/xxxxxx/.docker/machine",
                "swarm_discovery": "",
                "swarm_host": "tcp://0.0.0.0:3376",
                "swarm_master": false,
                "user_data_file": ""
            },
            "driver_name": "digitalocean",
            "host_options": {
                "auth_options": {
                    "ca_cert_path": "/home/xxxxxx/.docker/machine/certs/ca.pem",
                    "ca_cert_remote_path": "",
                    "ca_private_key_path": "/home/xxxxxxx/.docker/machine/certs/ca-key.pem",
                    "cert_dir": "/home/xxxxxxx/.docker/machine/certs",
                    "client_cert_path": "/home/xxxxxxx/.docker/machine/certs/cert.pem",
                    "client_key_path": "/home/xxxxxxx/.docker/machine/certs/key.pem",
                    "server_cert_path": "/home/xxxxxxx/.docker/machine/machines/xxxxxxxx/server.pem",
                    "server_cert_remote_path": "",
                    "server_cert_sa_ns": [],
                    "server_key_path": "/home/xxxxxxx/.docker/machine/machines/xxxxxxxx/server-key.pem",
                    "server_key_remote_path": "",
                    "store_path": "/home/xxxxxx/.docker/machine/machines/xxxxxxxx"
                },
                "disk": 0,
                "driver": "",
                "engine_options": {
                    "arbitrary_flags": [],
                    "dns": null,
                    "env": [],
                    "graph_dir": "",
                    "insecure_registry": [],
                    "install_url": "https://get.docker.com",
                    "ipv6": false,
                    "labels": [],
                    "log_level": "",
                    "registry_mirror": [],
                    "selinux_enabled": false,
                    "storage_driver": "",
                    "tls_verify": true
                },
                "memory": 0,
                "swarm_options": {
                    "address": "",
                    "arbitrary_flags": [],
                    "discovery": "",
                    "env": null,
                    "heartbeat": 0,
                    "host": "tcp://0.0.0.0:3376",
                    "image": "swarm:latest",
                    "is_experimental": false,
                    "is_swarm": false,
                    "master": false,
                    "overcommit": 0,
                    "strategy": "spread"
                }
            },
            "name": "xxxxxxx"
        }
    }'
'''


from ansible.module_utils.docker_machine_common import *


def main():
    argument_spec = dict(
        access_token=dict(type='str', required=True),
        image=dict(type='str'),
        region=dict(type='str'),
        size=dict(type='str'),
        ipv6=dict(type='bool'),
        private_networking=dict(type='bool'),
        backups=dict(type='bool'),
        userdata=dict(type='str'),
        ssh_user=dict(type='str'),
        ssh_port=dict(type='str'),
        ssh_key_fingerprint=dict(type='str')
    )

    machine = AnsibleDockerMachine(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    results = dict(
        changed=False,
        actions=[],
        machine={}
    )

    MachineManager('digitalocean', machine, results)
    machine.module.exit_json(**results)


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
