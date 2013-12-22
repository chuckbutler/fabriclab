#!/usr/bin/env python

from fabric.api import env, run, sudo, local


#env.hosts = [ '10.0.2.158' ]
env.hosts = [ '10.0.2.170' ]

def upgrade_packages():
    sudo('apt-get update')
    sudo('apt-get upgrade -y')

def bootstrap_server():
    sudo('apt-get install vim git-core htop python-software-properties byobu -y')
    run('git clone https://github.com/chuckbutler/dotfilesv2.git .dotfiles')
    run('ln -s .dotfiles/dotvim .vim')
    run('ln -s .dotfiles/dotvimrc .vimrc')
    run('ln -s .dotfiles/gitconfig .gitconfig')
    run('ln -s .dotfiles/githelpers .githelpers')

def bootstrap_workstation():
    local('sudo apt-get install vim git-core htop byobu -y')
    local('git clone https://github.com/chuckbutler/dotfilesv2.git $HOME/.dotfiles')
    local('ln -s $HOME/.dotfiles/dotvim .vim')
    local('ln -s $HOME/.dotfiles/dotvimrc .vimrc')
    local('ln -s $HOME/.dotfiles/gitconfig .gitconfig')
    local('ln -s $HOME/.dotfiles/githelpers .githelpers')


def bootstrap_starbound(username="",password=""):
	sudo('apt-get install lib32gcc1')
	run('wget http://media.steampowered.com/installer/steamcmd_linux.tar.gz')
	run('tar xvfz steamcmd_linux.tar.gz')
	run('$HOME/steamcmd.sh +login ' + username + ' ' + password + ' +force_install_dir ./starbound/ +app_update 211820 validate +quit')

def setup_qemu(user="charles"):
    sudo('apt-get install qemu-kvm libvirt-bin bridge-utils -y')
    sudo('adduser' + user + 'libvirtd')
    
def install_juju():
    sudo('add-apt-repository ppa:juju/stable')
    upgrade_packages() 
    sudo('apt-get install juju-core juju-local charm-tools -y')
    run('juju init')

def juju_local(): 
    run('juju switch local')
    sudo('juju bootstrap')
    run('juju deploy juju-gui')

