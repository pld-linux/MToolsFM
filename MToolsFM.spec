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
BuildRequires:	gtk+-devel
BuildRequires:	autoconf
BuildRequires:  automake
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is a little file-manager and allows easy access to
(dos-)floppies under Linux / UNIX. It uses mtools and has a nice GUI.

%description
Program ten jest niewielkim zarz±dc± plików umo¿liwiaj±cym ³atwy
dostêp spod Linuksa / UNIX-a do DOS-owych dyskietek. Korzysta z mtools
i posiada fajny interfejs graficzny.

%prep
%setup -q -n %{name}-%{vend_ver}-%{vend_release}

%build
%{__aclocal} 
%{__autoconf} 
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog AUTHORS NEWS README THANKS
%doc %{_mandir}/man1/MToolsFM.1.gz
%attr(755,root,root) %{_bindir}/MToolsFM
%{_datadir}/locale/de/LC_MESSAGES/MToolsFM.mo
%{_datadir}/locale/fr/LC_MESSAGES/MToolsFM.mo

%clean
rm -rf $RPM_BUILD_ROOT
