%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240223
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plasma-thunderbolt
Version: 6.4.2
Release: 1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/plasma-thunderbolt/-/archive/%{gitbranch}/plasma-thunderbolt-%{gitbranchd}.tar.bz2#/plasma-thunderbolt-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/plasma-thunderbolt-%{version}.tar.xz
%endif
Summary: Thunderbolt support for Plasma Desktop
URL: https://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlModels)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(KF6Notifications)
Requires: bolt
# Renamed after 6.0 2025-05-03
%rename plasma6-thunderbolt

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Thunderbolt support for Plasma Desktop

%files -f %{name}.lang
%{_libdir}/libkbolt.so
%{_qtdir}/plugins/kf6/kded/kded_bolt.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_bolt.so
%{_datadir}/applications/kcm_bolt.desktop
%{_datadir}/knotifications6/kded_bolt.notifyrc
