%define devname %mklibname -d KRdp

Name:		krdp
Version:	6.4.5
Release:	1
Source0:	https://download.kde.org/stable/plasma/%{version}/krdp-%{version}.tar.xz
Summary:	Remote Desktop Protocol (RDP) integration for Plasma
URL:		https://invent.kde.org/plasma/krdp
License:	GPL
Group:		Graphical desktop/KDE
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KPipeWire)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(freerdp3)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(winpr3)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Remote Desktop Protocol (RDP) integration for Plasma

%package -n %{devname}
Summary:	Development files for KDE RDP integration
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Development files for KDE RDP integration

%files -f %{name}.lang
%{_bindir}/krdpserver
%{_prefix}/lib/systemd/user/app-org.kde.krdpserver.service
%{_libdir}/libKRdp.so*
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_krdpserver.so
%{_datadir}/applications/kcm_krdpserver.desktop
%{_datadir}/applications/org.kde.krdpserver.desktop
%{_datadir}/qlogging-categories6/kcm_krdpserver.categories
%{_datadir}/qlogging-categories6/krdp.categories

%files -n %{devname}
%{_libdir}/cmake/KRdp
