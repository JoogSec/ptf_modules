#!/usr/bin/env python
#####################################
# Installation module for proxmark3
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="bitbrute"

# DESCRIPTION OF THE MODULE
DESCRIPTION="A tool to limit the bandwidth (upload/download) of devices connected to your network without physical or administrative access."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/bitbrute/evillimiter"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="evillimiter"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python3"

# DEPENDS FOR FEDORA INSTALLS
ARCH="git,python3base-devel"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python3 setup.py install"

LAUNCHER="evillimiter"
