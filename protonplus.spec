%define SHA256SUM0      ed22513e39107a88a088304d16eb6ae17fb477b84b555781def578aa5ccbb07e

%global provider        github
%global provider_tld    com
%global project         vysp3r
%global repo            ProtonPlus
%global built_tag       v0.4.6
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version     %(b=%{built_tag_strip}; echo ${b/-/"~"})

# https://github.com/vysp3r/ProtonPlus
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global git_repo        https://%{import_path}



Name:           protonplus
Version:        %{gen_version}
Release:        1%{?dist}
Summary:        Simple and powerful manager for Wine, Proton, DXVK and VKD3D

ExclusiveArch:  x86_64
License:        GPLv3+
URL:            %{git_repo}
Source0:        %{url}/archive/%{built_tag}/%{repo}-%{version}.tar.gz
Source1:        %{name}.rpmlintrc



BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsoup-3.0)



# Need for TLS support
Requires:       glib-networking



%description
%{repo} is a simple and powerful manager for:
 - Wine
 - Proton
 - DXVK
 - VKD3D
 - Several other runners

Supports Steam, Lutris, Heroic and Bottles.

%prep
echo "%SHA256SUM0 %{SOURCE0}" | sha256sum -c -
%autosetup -n %{repo}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/*.appdata.xml

%files
%license LICENSE.md
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md
%{_bindir}/*
%{_datadir}/*

%post
case "$1" in
  1) # Post install RPM, create symlink prontonplus -> com.vysp3r.ProtonPlus
    %{__ln_s} -f %{_bindir}/com.%{project}.%{repo} %{_bindir}/%{name}
  ;;
esac

%postun
case "$1" in
  0) # Post remove RPM, remove symlink protonplus -> com.vysp3r.ProtonPlus
    %{__rm} %{_bindir}/%{name}
  ;;
esac

%changelog
* Mon Sep 04 2023 Wesley H. Gimenes <wehagy+github@gmail.com> - 0.4.6-1
- First Release
