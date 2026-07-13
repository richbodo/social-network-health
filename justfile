# Admin/devops recipes for socialnetwork.health. Run `just` to list them.
# Server layout, provisioning details, and SSH notes: ops/README.md

# list available recipes
default:
    @just --list

# rsync the two public/ files to the droplet (override host with SNH_HOST=rsb@<ip>)
deploy:
    ./ops/deploy.sh

# check the live site responds and serves the expected title
verify-live:
    curl -sI https://socialnetwork.health/ | head -n1
    curl -s https://socialnetwork.health/ | grep -o '<title>[^<]*</title>'

# full droplet bootstrap via Ansible (needs ops/ansible/inventory/hosts.ini — see ops/README.md)
provision:
    cd ops/ansible && ansible-playbook site.yml

# re-render the Caddy config only
provision-caddy:
    cd ops/ansible && ansible-playbook site.yml --tags caddy

# install the Ansible collections the playbook needs (one-time setup)
ansible-deps:
    cd ops/ansible && ansible-galaxy collection install -r collections/requirements.yml -p collections

# run a Slidev deck from presentations/ locally (opens localhost:3030)
slides deck="dwebcamp-berlin-2026/deck":
    cd presentations/{{deck}} && bun install && bun run dev
