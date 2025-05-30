# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2023-2025 Wesley Gimenes <wehagy@proton.me>
# SPDX-Comment: See LICENSE for the full license text

%global SHA256SUM0      1abbf8053f37b2cc765c18cb2d5b355e687d25b32bbb1bd0426749295328b357

%global provider        github
%global provider_tld    com
%global owner           vysp3r
%global repo            ProtonPlus
%global built_tag       v0.4.31
%global built_tag_strip %{sub %{built_tag} 2}
%global gen_version     %{gsub %{built_tag_strip} - .}

# com.vysp3r.ProtonPlus
%global flatpak_name    %{provider_tld}.%{owner}.%{repo}

# https://github.com/vysp3r/ProtonPlus
%global provider_prefix %{provider}.%{provider_tld}/%{owner}/%{repo}
%global import_path     %{provider_prefix}
%global git_repo        https://%{import_path}



Name:           %{lower %{repo}}
Version:        %{gen_version}
Release:        1%{?dist}
Summary:        A modern compatibility tools manager for Linux

ExclusiveArch:  x86_64
License:        GPL-3.0-or-later
URL:            %{git_repo}
Source0:        %{url}/archive/%{built_tag}/%{repo}-%{version}.tar.gz
Source1:        README.md
# license of the spec file
Source2:        LICENSE
Source3:        %{name}.rpmlintrc


Patch0:         rename-executable-to-protonplus.patch


BuildRequires:  gettext
BuildRequires:  meson >= 0.62.0
BuildRequires:  vala

# desktop-file-validate command
BuildRequires:  desktop-file-utils
# appstream-util command
BuildRequires:  libappstream-glib

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsoup-3.0)


# TLS support
Requires:       glib-networking
# fix: Package must own all directories that it creates.
# Directories without known owners: /usr/share/icons/hicolor/*
Requires:       hicolor-icon-theme


# SteamTinkerLaunch
Recommends:     bash
Recommends:     gawk
Recommends:     git
Recommends:     procps-ng
Recommends:     unzip
Recommends:     wget
Recommends:     xdotool
Recommends:     xprop
Recommends:     xrandr
Recommends:     xwininfo
Recommends:     xxd
Recommends:     yad >= 7.2



%description
Install and manage Wine/Proton based compatibility tools
with a graphical user interface.

Supported launchers:
 - Steam
 - Lutris
 - Heroic Games Launcher
 - Bottles

Supported compatibility tools:
 - Steam Tinker Launch
 - Proton-GE
 - Luxtorpeda
 - Boxtron
 - Roberta
 - NorthstarProton
 - DXVK
 - And much more


%prep
sha256sum -c <(echo "%{SHA256SUM0} %{SOURCE0}")
%autosetup -p1 -n %{repo}-%{built_tag_strip}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{flatpak_name}


%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{flatpak_name}.desktop

appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{flatpak_name}.metainfo.xml


%files -f %{flatpak_name}.lang
%license LICENSE.md
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md
%{_bindir}/%{name}
%{_datadir}/applications/%{flatpak_name}.desktop
%{_datadir}/glib-2.0/schemas/%{flatpak_name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{flatpak_name}.png
%{_metainfodir}/%{flatpak_name}.metainfo.xml



%changelog
* Fri May 30 2025 Wesley Gimenes <wehagy@proton.me> - 0.4.31-1
- add patch rename executable to protonplus

* Thu May 29 2025 Wesley Gimenes <wehagy@proton.me> - 0.4.31-1
- new upstream version v0.4.31
- update README.md
- update SPDX copyright
- rename *.appdata.xml to *.metainfo.xml
- rename *.svg to *.png
- modernize macros
- add SteamTinkerLaunch dependencies
- remove fdupes
- fix Package must own all directories that it creates.
- sync description with upstream
- rework BuildRequires
- revise comments and fix indentation
- add README.md and LICENSE to rpm package
- change Name to macro lowercase

* Sun Aug 04 2024 Wesley Gimenes <wehagy@proton.me> - 0.4.11-1
- new upstream version v0.4.11

* Mon May 27 2024 Wesley Gimenes <wehagy@proton.me> - 0.4.10-1
- new upstream version v0.4.10

* Wed Apr 10 2024 Wesley Gimenes <wehagy@proton.me> - 0.4.9-2
- build: rebuild for fedora 40 release

* Sun Dec 17 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.9-1
- new upstream version v0.4.9

* Sun Dec 17 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.8-1
- new upstream version v0.4.8

* Sun Dec 17 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.7.2-1
- style: fixed indentation
- new upstream version v0.4.7-2

* Sun Dec 17 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.7.1-1
- fix: change upstream version dash to dot
- fix: %%autosetup use upstream versioning
- new upstream version v0.4.7-1

* Sat Dec 16 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.7-1
- tighten dependencies
- removed unused files to accomodate new version
- new upstream version v0.4.7

* Sat Dec 16 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.6-3
- fix: incorrect day of week in changelog

* Thu Nov 09 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.6-3
- rebuild for fedora 39 release
- rename global variable project to owner
- add license to source of the specfile
- add SPDX license header

* Tue Sep 05 2023 Wesley H. Gimenes <wehagy+github@gmail.com> - 0.4.6-2
- rebuild v0.4.6-2 because of the file below
- fix: rename prontonplus-next.rpmlintrc to protonplus.rpmlintrc
- fix: change %%define to %%global
- fix: macros in changelog
- changed legacy license format to SPDX
- fix: W: dangerous-command-in-%%postun rm
- fix: W: dangerous-command-in-%%post ln
- fix: general improvements
- fix: E: standard-dir-owned-by-package
- fix: W: file-not-in-%%lang
- fix: W: no-manual-page-for-binary 
- fix: W: files-duplicate

* Mon Sep 04 2023 Wesley H. Gimenes <wehagy+github@gmail.com> - 0.4.6-2
- fix: use-of-RPM_SOURCE_DIR 

* Mon Sep 04 2023 Wesley H. Gimenes <wehagy+github@gmail.com> - 0.4.6-1
- First Release
