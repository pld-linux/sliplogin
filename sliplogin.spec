Summary:	Login program for SLIP
Summary(de.UTF-8):	Login-Programm für SLIP
Summary(fr.UTF-8):	Programme de login pour SLIP
Summary(pl.UTF-8):	Program do logowania z użyciem SLIP
Summary(tr.UTF-8):	SLIP için sisteme giriş programı
Name:		sliplogin
Version:	2.1.1
Release:	4
Group:		Applications/System
License:	BSD
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/serial/%{name}-%{version}.tar.gz
# Source0-md5:	82996108ddb21c2fd9b7db23369af40e
Patch0:		%{name}-misc.patch
Patch1:		%{name}-modes.patch
Patch2:		%{name}-path.patch
Patch4:		%{name}-glibc.patch
Patch5:		%{name}-includes.patch
Patch6:		%{name}-netdev.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Attaches a SLIP interface to standard input. This is often used to
allow dialin SLIP connections.

%description -l de.UTF-8
Fügt Standardeingabe ein SLIP-Interface hinzu, was häufig dazu dient,
Einwähl-SLIP-Verbindungen herzustellen.

%description -l fr.UTF-8
Attache une interface SLIP à l'entrée standard. Ceci est souvent
utilisé pour permettre des connexions SLIP en dialin.

%description -l pl.UTF-8
Pakiet zawiera program podłączający interfejs SLIP do standardowego
wejścia. Może być on wykorzystywany do udostępniania połączenia
opartego o SLIP na liniach modemowych.

%description -l tr.UTF-8
Bir SLIP arayüzünü standart girdiye bağlar. Çevirmeli SLIP
bağlantılarına izin verir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__make} clean
rm -f sliplogin
%{__make} access
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/slip,%{_sbindir},%{_mandir}/man8}
%{__make} install \
SLIP=$RPM_BUILD_ROOT%{_sysconfdir}/slip \
	SBIN=$RPM_BUILD_ROOT%{_sbindir} \
	MAN=$RPM_BUILD_ROOT%{_mandir}
install slip.{tty,hosts,route,passwd} $RPM_BUILD_ROOT%{_sysconfdir}/slip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README*,TODO,TROUBLE_SHOOTING}
%dir %{_sysconfdir}/slip
%config %verify(not md5 mtime size) %{_sysconfdir}/slip/*
%attr(755,root,root) %{_sbindir}/sliplogin
%{_mandir}/man8/*
