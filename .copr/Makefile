# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2023-2025 Wesley Gimenes <wehagy@proton.me>

outdir?=$(TOPDIR)/output
spec?=$(TOPDIR)

DNF_CMD:= \
	dnf install \
		--assumeyes \
		--nodocs \
		--setopt=install_weak_deps=False

ifeq ($(HOSTNAME),mock)
  SRCRPMDIR:=$(outdir)
else
  SRCRPMDIR:=$(outdir)/srpm
endif

prepare-srpm:
	$(DNF_CMD) \
		fedpkg \
		rpmautospec
	spectool -g $(spec)/*.spec
	sha256sum -c CHECKSUM

prepare-rpm:
	$(DNF_CMD) \
		mock \
		podman

srpm: prepare-srpm
	fedpkg \
		--release rawhide \
			srpm -- \
				--define "_srcrpmdir $(SRCRPMDIR)"

rpm: prepare-rpm
	mock \
		--rebuild $(outdir)/srpm/*.src.rpm \
		--resultdir "$(outdir)/rpm"

