Summary:	VTX file format player based on AY/YM emulation library
Summary(pl.UTF-8):	Odtwarzacz plików VTX oparty na bibliotece emulacji AY/YM
Name:		playvtx
Version:	0.9.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/libayemu/%{name}-%{version}.tar.gz
# Source0-md5:	644f28c8d371a6bdad0622c2c94671ee
URL:		http://sashnov.nm.ru/libayemu.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libayemu-devel >= 0.9
Requires:	libayemu >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is player for AY/YM sound chip music packed to VTX format.

%description -l pl.UTF-8
Odtwarzacz muzyki dla układów AY/YM spakowanej do plików w formacie
VTX.

%prep
%setup -q

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/playvtx
