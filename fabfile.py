#!/usr/bin/env python

from fabric.api import env, run, sudo, local


env.hosts = [ '10.0.2.158' ]

def upgrade_packages():
    sudo('apt-get update')
    sudo('apt-get upgrade -y')

def bootstrap_server():
    sudo('apt-get install vim git-core htop -y')
    run('git clone https://github.com/chuckbutler/dotfilesv2.git .dotfiles')
    run('ln -s .dotfiles/dotvim .vim')
    run('ln -s .dotfiles/dotvimrc .vimrc')
    run('ln -s .dotfiles/gitconfig .gitconfig')
    run('ln -s .dotfiles/githelpers .githelpers')

def bootstrap_workstation():
    local('sudo apt-get install vim git-core htop -y')
    local('git clone https://github.com/chuckbutler/dotfilesv2.git $HOME/.dotfiles')
    local('ln -s $HOME/.dotfiles/dotvim .vim')
    local('ln -s $HOME/.dotfiles/dotvimrc .vimrc')
    local('ln -s $HOME/.dotfiles/gitconfig .gitconfig')
    local('ln -s $HOME/.dotfiles/githelpers .githelpers')


def setup_qemu(user="charles"):
    sudo('apt-get install qemu-kvm libvirt-bin bridge-utils -y')
    sudo('adduser' + user + 'libvirtd')
        
