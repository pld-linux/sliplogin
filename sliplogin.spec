Summary:     Login program for SLIP
Summary(de): Login-Programm für SLIP
Summary(fr): Programme de login pour SLIP
Summary(pl): Program do logowania z u¿yciem SLIP
Summary(tr): SLIP için sisteme giriþ programý
Name:        sliplogin
Version:     2.1.1
Release:     4
Group:       Utilities/System
Copyright:   BSD
Source:      ftp://sunsite.unc.edu/pub/Linux/system/network/serial/%{name}-%{version}.tar.gz
Patch0:      sliplogin-2.1.0-misc.patch
Patch1:      sliplogin-2.1.1-modes.patch
Patch2:      sliplogin-2.1.0-path.patch
Patch4:      sliplogin-2.1.0-glibc.patch
Patch5:      sliplogin-2.1.1-includes.patch
Buildroot:   /tmp/%{name}-%{version}-root

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
%patch1 -p1 -b .modes
%patch2 -p1 -b .path
%patch4 -p1 -b .glibc
%patch5 -p1 -b .includes

%build
make clean
rm -f sliplogin
make access
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/slip,usr/{sbin,man/man8}}
make install \
	SLIP=$RPM_BUILD_ROOT/etc/slip \
	SBIN=$RPM_BUILD_ROOT/usr/sbin \
	MAN=$RPM_BUILD_ROOT%{_mandir}
install slip.{tty,hosts,route,passwd} $RPM_BUILD_ROOT/etc/slip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README* TODO TROUBLE_SHOOTING
%dir /etc/slip
%config %verify(not md5 mtime size) /etc/slip/*
%attr(755, root, root) /usr/sbin/sliplogin
%attr(644, root,  man) %{_mandir}/man8/*

%changelog
* Thu Aug 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.1.1-3]
- added -q %setup parameter,
- added using %%{name} and %%{version} in Source,
- spec rewrited for using Buildroot,
- added %clean section,
- some simplification in %install and %build,
- added pl translation,
- added "%dir /etc/slip" to %files,
- added %verify rules to %config files,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- upgraded to 2.1.1
- struct password needs <pwd.h>

* Thu Oct 09 1997 Erik Troan <ewt@redhat.com>
- removed excludearch for alpha

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
