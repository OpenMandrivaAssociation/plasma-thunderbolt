%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-thunderbolt
Version: 5.27.7
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: Thunderbolt support for Plasma Desktop
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5QmlModels)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(KF5Notifications)
Requires: bolt

%description
Thunderbolt support for Plasma Desktop

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_libdir}/libkbolt.so
%{_libdir}/qt5/plugins/kf5/kded/kded_bolt.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_bolt.so
%{_datadir}/applications/kcm_bolt.desktop
%{_datadir}/knotifications5/kded_bolt.notifyrc
%{_datadir}/kpackage/kcms/kcm_bolt
