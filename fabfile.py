#!/usr/bin/env python

from fabric.api import env, run, sudo


env.hosts = [ '10.0.2.158' ]

def upgrade_packages():
    sudo('apt-get update')
    sudo('apt-get upgrade -y')

def bootstrap_user():
    sudo('apt-get install vim git-core htop -y')
    run('git clone https://github.com/chuckbutler/dotfilesv2.git .dotfiles')
    run('ln -s .dotfiles/dotvim .vim')
    run('ln -s .dotfiles/dotvimrc .vimrc')
    run('ln -s .dotfiles/gitconfig .gitconfig')
    run('ln -s .dotfiles/githelpers .githelpers')

    
