%define vend_ver 1.9
%define vend_release 3

Summary:	Graphical frontend to mtools - easy access to floppies
Summary(pl):	Graficzny interfejs do mtools - ³atwy dostêp do dyskietek
Name:		MToolsFM
Version:	%{vend_ver}.%{vend_release}
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.core-coutainville.org/%{name}/archive/SOURCES/%{name}-%{vend_ver}-%{vend_release}.tar.gz
#Source0-MD5: 5ce76261ad969209c86b28e49924fc43

%description
This program is a little file-manager and allows easy access to
(dos-)floppies under linux / UNIX. It uses mtools and has a nice GUI.

%prep
%setup -q -n %{name}-%{vend_ver}-%{vend_release}

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

##./configure --prefix=/usr --bindir=/usr/X11R6/bin --mandir=/usr/share/man
##make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install
gzip %{_mandir}/man1/MToolsFM.1

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog AUTHORS NEWS README THANKS
%doc %{_mandir}/man1/MToolsFM.1.gz
%attr(755,root,root) %{_bindir}/MToolsFM
%{_datadir}/locale/de/LC_MESSAGES/MToolsFM.mo
%{_datadir}/locale/fr/LC_MESSAGES/MToolsFM.mo

%clean
rm -rf $RPM_BUILD_ROOT
