Name:           bubblejail
Version:        0.8.3
Release:        1%{?dist}
Summary:        Bubblewrap based sandboxing for desktop applications

License:        GPLv3+
URL:            https://github.com/igo95862/bubblejail
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  python3-jinja2
BuildRequires:  scdoc
Requires:       python3 >= 3.10
Requires:       python3-pyxdg
Requires:       python3-tomli
Requires:       python3-tomli-w
Requires:       bubblewrap >= 0.5.0
Requires:       xdg-dbus-proxy
Requires:       python3-pyqt6-base
Requires:       libseccomp
Recommends:     desktop-file-utils
Recommends:     libnotify
Suggests:       bash-completion
Suggests:       fish
Suggests:       slirp4netns

%global debug_package %{nil}

%description
Bubblejail is a bubblewrap-based alternative to Firejail.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README.md docs/breaking_changes.md
%_bindir/bubblejail
%_bindir/bubblejail-config
%_libdir/bubblejail
%_datadir/applications/bubblejail-config.desktop
%_datadir/bash-completion/completions/bubblejail
%_datadir/bubblejail
%_datadir/fish/vendor_completions.d/bubblejail.fish
%_datadir/icons/hicolor/48x48/apps/bubblejail-config.png
%_datadir/icons/hicolor/scalable/apps/bubblejail-config.svg
%_mandir/man1/bubblejail.1.gz
%_mandir/man5/bubblejail.services.5.gz


%changelog
* Mo Mar 04 2024 trytomakeyouprivate - 0.8.3-1
- Update to 0.8.3

* Wed Oct 25 2023 rusty-snake - 0.8.2-1
- Update to 0.8.2

* Sun Aug 06 2023 rusty-snake - 0.8.1-1
- Update to 0.8.1

* Sun Aug 06 2023 rusty-snake - 0.8.0-4
- Cherry-pick more patches

* Sat Aug 05 2023 rusty-snake - 0.8.0-3
- Fix from igo95862/bubblejail#68

* Sun Jul 09 2023 rusty-snake - 0.8.0-2
- Fix igo95862/bubblejail#63

* Sun Jul 02 2023 rusty-snake - 0.8.0-1
- Update to 0.8.0

* Sun Feb 12 2023 rusty-snake - 0.7.0-1
- Update to 0.7.0

* Sat Jul 09 2022 rusty-snake - 0.6.2-1
- Update to 0.6.2

* Wed Jun 08 2022 rusty-snake - 0.6.1-1
- Update to 0.6.1

* Mon May 23 2022 rusty-snake - 0.6.0-1
- Update to 0.6.0

* Tue Apr 19 2022 rusty-snake - 0.5.3-1
- Update to 0.5.3

* Wed Apr 06 2022 rusty-snake - 0.5.2-1
- Update to 0.5.2

* Sun Feb 13 2022 rusty-snake - 0.5.1-1
- Update to 0.5.1

* Mon Jan 31 2022 rusty-snake - 0.5.0-1
- Update to 0.5.0

* Mon Oct 11 2021 rusty-snake - 0.4.2-1
- Initial bubblejail spec
