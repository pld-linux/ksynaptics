Summary:	Touchpad configuration module for KDE Control Center
Summary(pl):	Modu³ konfiguracyjny dla touchpadów do centrum sterowania KDE
Name:		ksynaptics
Version:	0.2.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://qsynaptics.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	227c3eaa7dde7e5abd0a984a11c70e29
URL:		http://qsynaptics.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040805
Requires:	X11-synaptics >= 0.14.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSynaptics is a control center module that enables users to take full
advantage of their mobiles' Synaptics touch pad. It depends on the
XFree86's synaptics driver and offers the following features:
 - adjustable pressure sensitivity
 - tapping configuration / smart tapping
 - mouse button emulation
 - circular scrolling
 - smart mode

%description -l pl
KSynaptics to modu³ centrum sterowania KDE pozwalaj±cy u¿ytkownikom
korzystaæ z pe³ni mo¿liwo¶ci touchpadów Synaptics. Polega na
sterowniku synapics z XFree86 i oferuje nastêpuj±ce mo¿liwo¶ci:
 - regulowanie czu³o¶ci nacisku
 - konfiguracja stukania
 - emulacja przycisków myszy
 - przewijanie w kó³ko
 - tryb inteligentny

%prep
%setup -q
#cd po
#SUBDIRS=`find ./ -name \*.po -printf "%h\n"|cut -c 3-|tr "\n" " "`;
#%{__sed} -i -e "s,SUBDIRS.*,SUBDIRS=$SUBDIRS,g" Makefile.am
#cd ..

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name}  --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_desktopdir}/kde/ksynaptics.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_iconsdir}/*/*/apps/syndock*.png
%{_datadir}/autostart/*
%{_datadir}/config.kcfg/*
