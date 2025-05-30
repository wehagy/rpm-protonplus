# ProtonPlus

Unofficial [ProtonPlus](https://github.com/Vysp3r/ProtonPlus) `rpm` package.

Report any packaging bugs to [downstream](https://github.com/wehagy/rpm-protonplus/issues) github issue trackers.\
New features, bugs, translation, etc, report to [upstream](https://github.com/Vysp3r/ProtonPlus/issues).

## Status

Copr project [wehagy/protonplus](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus)

| Spec file | Copr build status |
|---|---|
| [protonplus.spec](https://github.com/wehagy/rpm-protonplus/blob/main/protonplus.spec) | [![Copr build status](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus/package/protonplus/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus/package/protonplus/) |
| [protonplus-next.spec](https://github.com/wehagy/rpm-protonplus/blob/protonplus-next/protonplus-next.spec) | [![Copr build status](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus/package/protonplus-next/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus/package/protonplus-next/) |

## Installation Instructions

Enable this repo:

```shell
# Fedora
sudo dnf -y copr enable wehagy/protonplus
```

Install package:

```shell
# Stable
sudo dnf install protonplus

# Testing, please use with caution
sudo dnf install protonplus-next
```

**NOTE:** The RHEL / CentOS Stream not supported.
