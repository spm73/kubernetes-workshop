#!/bin/bash

NETWORK=$(ip route | grep 'proto kernel scope link' | awk '{print $1}' | head -n 1)

echo "/var/nfs/kubernetes-workshop $NETWORK(rw,sync,no_subtree_check,no_root_squash)" | sudo tee -a /etc/exports

sudo systemctl restart nfs-server
