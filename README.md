# 📦 ProtonPlus

Unofficial [ProtonPlus](https://github.com/Vysp3r/ProtonPlus) `rpm` package.\
Although it is unofficial, the upstream is always willing to help, and we strive to collaborate whenever possible.

To report packaging bugs, please use the [downstream issue tracker](https://github.com/wehagy/rpm-protonplus/issues).\
For requests related to new features, bug reports, translations, and more, please refer to the [upstream issue tracker](https://github.com/Vysp3r/ProtonPlus/issues).\
If you're not sure where to report your issue, you can submit it anywhere, and you will be directed to the correct tracker.

---

## 📊 Status

Copr project: [wehagy/protonplus](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus)

| **Spec File** | **Copr Build Status** |
|---|---|
| [protonplus.spec](https://github.com/wehagy/rpm-protonplus/blob/main/protonplus.spec) | [![Copr build status](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus/package/protonplus/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus/package/protonplus/) |
| [protonplus-next.spec](https://github.com/wehagy/rpm-protonplus/blob/protonplus-next/protonplus-next.spec) | [![Copr build status](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus/package/protonplus-next/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/wehagy/protonplus/package/protonplus-next/) |

---

## 📥 Installation Instructions

1. **Enable this repository:**

   **Fedora**
   ```shell
   sudo dnf copr enable wehagy/protonplus
   ```

2. **Install the package:**

   **Stable**
   ```shell
   sudo dnf install protonplus
   ```

   **🚧 Testing: Use with Caution!**
   ```shell
   sudo dnf install protonplus-next
   ```

---

**⚠️  NOTE:** RHEL / CentOS Stream is not supported.
