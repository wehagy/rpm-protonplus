# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2025 Wesley Gimenes <wehagy@proton.me>

TOPDIR := $(or $(TOPDIR),$(CURDIR))
OUTDIR := $(or $(outdir),$(TOPDIR)/output)
SPEC_FILE := $(wildcard $(TOPDIR)/*.spec)

DNF_CMD := dnf install --assumeyes --nodocs --setopt=install_weak_deps=False

REPO := $(shell grep -oP '^%global\s+forgeurl\s+https://github.com/\K.*' $(SPEC_FILE))
REPO_NAME := $(notdir $(REPO))

LOCAL_TAG := $(shell grep -oP '^%global\s+tag\s+\K.*' $(SPEC_FILE))
LOCAL_TAG_STRIP := $(subst v,,$(LOCAL_TAG))

REMOTE_TAG := $(notdir $(word 2,$(shell git ls-remote --refs --tags --sort='-version:refname' https://github.com/$(REPO).git)))
REMOTE_TAG_STRIP := $(subst v,,$(REMOTE_TAG))

ARCHIVE_FILE := $(REPO_NAME)-$(REMOTE_TAG_STRIP).tar.gz
HASH_FILE :=  $(TOPDIR)/CHECKSUM

define compare_release
$(shell \
  printf '%s\n%s' "$(1)" "$(2)" | sort -VC || printf "outdated"
)
endef

ifeq ($(HOSTNAME),mock)
  SRCRPMDIR := $(OUTDIR)
else
  SRCRPMDIR := $(OUTDIR)/srpm
endif

update-release:
ifeq ($(call compare_release,$(REMOTE_TAG),$(LOCAL_TAG)),outdated)
	echo "[INFO] Updating from $(LOCAL_TAG) to $(REMOTE_TAG)"
	curl -fsSL https://github.com/$(REPO)/archive/$(REMOTE_TAG)/$(ARCHIVE_FILE) \
		| sha256sum \
		| sed 's/-/$(ARCHIVE_FILE)/' > $(HASH_FILE)
	sed -Ei 's/^(%global\s+tag\s+).*/\1$(REMOTE_TAG)/' $(SPEC_FILE)
	git add $(SPEC_FILE) $(HASH_FILE)
	git commit -s \
		-m "update to $(REMOTE_TAG_STRIP)" \
		-m "- upstream changelog: https://github.com/$(REPO)/releases/tag/$(REMOTE_TAG)"
else
	echo "[INFO]: No update needed"
endif

prepare-srpm:
	$(DNF_CMD) fedpkg rpmautospec
	spectool -g $(SPEC_FILE)
	sha256sum -c $(HASH_FILE)

prepare-rpm:
	$(DNF_CMD) mock podman

srpm: prepare-srpm
	fedpkg --release rawhide srpm -- --define "_srcrpmdir $(SRCRPMDIR)"

rpm: prepare-rpm
	mock --rebuild $(wildcard $(SRCRPMDIR)/*.src.rpm) --resultdir $(OUTDIR)/rpm
