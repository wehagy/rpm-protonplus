# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2023-2025 Wesley Gimenes <wehagy@proton.me>
# SPDX-Comment: See LICENSE for the full license text

##### Variable macros
%global tag                 v0.6.4
# BuildRequires dependencies
%global meson_version       1.0.0
%global libadwaita_version  1.6

##### Constant macros
%global app_id              com.vysp3r.ProtonPlus
%global forgeurl            https://github.com/vysp3r/ProtonPlus
# forgemeta macro need to be after forgeurl and tag macros
%forgemeta
# unset weird prefix set by forgemeta (.gitvX.X.X)
%undefine distprefix


Name:           protonplus-next
Version:        %{fileref}
Release:        %autorelease
Summary:        Manage Proton, Wine, DXVK, and VKD3D tools for Linux game launchers
ExclusiveArch:  x86_64 aarch64

License:        GPL-3.0-or-later
URL:            https://protonplus.vysp3r.com
Source0:        %{forgesource}
# license of the spec file
Source1:        LICENSE
Source2:        protonplus.rpmlintrc

##### Build dependencies
BuildRequires:  gettext
BuildRequires:  meson >= %{meson_version}
BuildRequires:  vala

BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(sdl3)

##### Check dependencies
# desktop-file-validate command
BuildRequires:  desktop-file-utils
# appstream-util command
#BuildRequires:  libappstream-glib

##### Runtime dependencies
# fix: Directories without known owners: /usr/share/icons/hicolor/*
Requires:       hicolor-icon-theme


%description
ProtonPlus helps you install, update, remove, and organize compatibility tools
used by Steam and other Linux game launchers. It discovers supported
launcher installations, downloads releases from their upstream sources,
and installs them into the layouts expected by each launcher.

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
%{_bindir}/protonplus
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}.png
%{_metainfodir}/%{app_id}.metainfo.xml

%changelog
%autochangelog
