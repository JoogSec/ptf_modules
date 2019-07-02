#!/usr/bin/env python
#####################################
# Installation module for proxmark3
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="RfidResearchGroup"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This repo is based on iceman fork for Proxmark3. It is dedicated to bringing the most out of the new features for Proxmark3 RDV4.0 new hardware and design."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/RfidResearchGroup/proxmark3.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="proxmark3"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python2.7,python3,p7zip,ca-certificates,build-essential,libreadline5,libreadline-dev,libusb-0.1-4,libusb-dev,libqt4-dev,perl,pkg-config,wget,libncurses5-dev,gcc-arm-none-eabi,libstdc++-arm-none-eabi-newlib"

# DEPENDS FOR FEDORA INSTALLS
ARCH="git,python3base-devel,p7zip,libusb,readline,ncurses,arm-none-eabi-gcc,arm-none-eabi-newlib"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make clean && make all"

LAUNCHER="proxmark3"
