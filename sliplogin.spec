Summary:	Login program for SLIP
Summary(de):	Login-Programm für SLIP
Summary(fr):	Programme de login pour SLIP
Summary(pl):	Program do logowania z u¿yciem SLIP
Summary(tr):	SLIP için sisteme giriþ programý
Name:		sliplogin
Version:	2.1.1
Release:	4
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Copyright:	BSD
Source:		ftp://sunsite.unc.edu/pub/Linux/system/network/serial/%{name}-%{version}.tar.gz
Patch0:		sliplogin-misc.patch
Patch1:		sliplogin-modes.patch
Patch2:		sliplogin-path.patch
Patch4:		sliplogin-glibc.patch
Patch5:		sliplogin-includes.patch
Patch6:		sliplogin-netdev.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Attaches a SLIP interface to standard input. This is often used to allow
dialin SLIP connections.

%description -l de
Fügt Standardeingabe ein SLIP-Interface hinzu, was häufig dazu dient, 
Einwähl-SLIP-Verbindungen herzustellen.

%description -l fr
Attache une interface SLIP à l'entrée standard. Ceci est souvent utilisé
pour permettre des connexions SLIP en dialin.

%description -l pl
Paket zawiera program pod³±czaj±cy interfejsc SLIP do standardowego wej¶cia.
Mo¿e byæ on wykorztystywany do udostêpniania po³±czenia opartego o SLIP na
liniach modemowych.

%description -l tr
Bir SLIP arayüzünü standart girdiye baðlar. Çevirmeli SLIP baðlantýlarýna
izin verir.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
make clean
rm -f sliplogin
make access
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/slip,%{_sbindir},%{_mandir}/man8}
make install \
	SLIP=$RPM_BUILD_ROOT/etc/slip \
	SBIN=$RPM_BUILD_ROOT%{_sbindir} \
	MAN=$RPM_BUILD_ROOT%{_mandir}
install slip.{tty,hosts,route,passwd} $RPM_BUILD_ROOT/etc/slip

gzip -9nf README* TODO TROUBLE_SHOOTING \
	$RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README*,TODO,TROUBLE_SHOOTING}.gz
%dir /etc/slip
%config %verify(not md5 mtime size) /etc/slip/*
%attr(755,root,root) %{_sbindir}/sliplogin
%{_mandir}/man8/*
