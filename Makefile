# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2025 Wesley Gimenes <wehagy@proton.me>

TOPDIR := $(CURDIR)
export TOPDIR

all:
	$(MAKE) -f $(TOPDIR)/.copr/Makefile all

%:
	$(MAKE) -f $(TOPDIR)/.copr/Makefile $@
