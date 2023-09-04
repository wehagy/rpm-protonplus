# ProtonPlus

Unofficial [ProtonPlus](https://github.com/Vysp3r/ProtonPlus) rpm package.\
Report any packaging bugs to [downstream](https://github.com/wehagy/rpm-protonplus/issues) github issue trackers. New features, bugs, translation, etc, report to [upstream](https://github.com/Vysp3r/ProtonPlus/issues).

Spec file for rpm are present as [protonplus.spec](https://github.com/wehagy/rpm-protonplus/blob/main/protonplus.spec) in the downstream repo.

# Status

COPR package link: [wehagy/protonplus](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus)

COPR build: [![Copr build status](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus/package/protonplus/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus/package/protonplus/)

## Installation Instructions

Enable this repo:

```bash
# Fedora
sudo dnf -y copr enable wehagy/protonplus
```

Install package:
```bash
# Stable
sudo dnf install protonplus

# Testing
sudo dnf install protonplus-next
```

**NOTE:** The RHEL / CentOS Stream not supported.
