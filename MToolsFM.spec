%define	vend_ver	1.9
%define	vend_release	3

Summary:	Graphical frontend to mtools - easy access to floppies
Summary(pl):	Graficzny interfejs do mtools - ³atwy dostêp do dyskietek
Name:		MToolsFM
Version:	%{vend_ver}.%{vend_release}
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.core-coutainville.org/%{name}/archive/SOURCES/%{name}-%{vend_ver}-%{vend_release}.tar.gz
# Source0-md5:	5ce76261ad969209c86b28e49924fc43
URL:		http://www.core-coutainville.org/MToolsFM/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
Requires:	mtools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is a little file-manager and allows easy access to
(dos-)floppies under Linux / UNIX. It uses mtools and has a nice GUI.

%description -l pl
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_bindir}/MToolsFM
%{_mandir}/man1/MToolsFM.1*
