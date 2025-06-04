# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2023-2025 Wesley Gimenes <wehagy@proton.me>
# SPDX-Comment: See LICENSE for the full license text

##### Variable macros
%global tag                 v0.4.32
# BuildRequires dependencies
%global meson_version       1.0.0
%global libadwaita_version  1.5
# Recommends dependencies
%global yad_version         7.2

##### Constant macros
%global app_id              com.vysp3r.ProtonPlus
%global forgeurl            https://github.com/vysp3r/ProtonPlus
# forgemeta macro need to be after forgeurl and tag macros
%forgemeta
# unset weird prefix set by forgemeta (.gitvX.X.X)
%undefine distprefix


Name:           protonplus
Version:        %{fileref}
Release:        %autorelease
Summary:        A modern compatibility tools manager for Linux
ExclusiveArch:  x86_64

License:        GPL-3.0-or-later
URL:            https://protonplus.vysp3r.com
Source0:        %{forgesource}
# license of the spec file
Source1:        LICENSE
Source2:        README.md
Source3:        %{name}.rpmlintrc

##### Build dependencies
BuildRequires:  gettext
BuildRequires:  meson >= %{meson_version}
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsoup-3.0)

##### Check dependencies
# desktop-file-validate command
BuildRequires:  desktop-file-utils
# appstream-util command
BuildRequires:  libappstream-glib

##### Runtime dependencies
# fix: Directories without known owners: /usr/share/icons/hicolor/*
Requires:       hicolor-icon-theme

##### SteamTinkerLaunch dependencies
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
Recommends:     yad >= %{yad_version}


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
%forgeautosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{app_id}

%check
%meson_test

%files -f %{app_id}.lang
%license LICENSE.md
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}.png
%{_metainfodir}/%{app_id}.metainfo.xml

%changelog
%autochangelog
