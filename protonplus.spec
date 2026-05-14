# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2023-2025 Wesley Gimenes <wehagy@proton.me>
# SPDX-Comment: See LICENSE for the full license text

##### Variable macros
# BuildRequires dependencies
%global meson_version       1.0.0
%global libadwaita_version  1.6

##### Constant macros
%global app_id              com.vysp3r.ProtonPlus
%global forgeurl0           https://github.com/vysp3r/ProtonPlus


Name:           protonplus
Version:        0.5.20
Release:        %autorelease
Summary:        A modern compatibility tools manager
ExclusiveArch:  x86_64

%forgemeta

License:        GPL-3.0-or-later
URL:            https://protonplus.vysp3r.com
Source0:        %{forgesource0}
# license of the spec file
Source1:        LICENSE
Source2:        %{name}.rpmlintrc

##### Build dependencies
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


BuildSystem: meson

%description
ProtonPlus allows you to easily manage and update various compatibility tools
like Proton, Wine, DXVK, and VKD3D across different launchers.

%install -a
%find_lang %{app_id}

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
