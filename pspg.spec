Summary:	A unix pager optimized for psql
Name:		pspg
Version:	4.3.0
Release:	1
License:	BSD
Group:		Applications/Databases
Source0:	https://github.com/okbob/pspg/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	94ca75be8065c408b09cde6391317c1c
URL:		https://github.com/okbob/pspg
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-ext-devel
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pspg is a unix pager optimized for psql. It can freeze rows, freeze
columns, and lot of color themes are included.

%prep
%setup -q

%build
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
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/pspg
