Summary:	Login program for SLIP
Summary(de):	Login-Programm f�r SLIP
Summary(fr):	Programme de login pour SLIP
Summary(pl):	Program do logowania z u�yciem SLIP
Summary(tr):	SLIP i�in sisteme giri� program�
Name:		sliplogin
Version:	2.1.1
Release:	4
Group:		Applications/System
License:	BSD
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/serial/%{name}-%{version}.tar.gz
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

%description -l de
F�gt Standardeingabe ein SLIP-Interface hinzu, was h�ufig dazu dient,
Einw�hl-SLIP-Verbindungen herzustellen.

%description -l fr
Attache une interface SLIP � l'entr�e standard. Ceci est souvent
utilis� pour permettre des connexions SLIP en dialin.

%description -l pl
Paket zawiera program pod��czaj�cy interfejsc SLIP do standardowego
wej�cia. Mo�e by� on wykorztystywany do udost�pniania po��czenia
opartego o SLIP na liniach modemowych.

%description -l tr
Bir SLIP aray�z�n� standart girdiye ba�lar. �evirmeli SLIP
ba�lant�lar�na izin verir.

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
