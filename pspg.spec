Summary:	A unix pager optimized for psql
Name:		pspg
Version:	3.1.4
Release:	1
License:	BSD
Group:		Applications/Databases
Source0:	https://github.com/okbob/pspg/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	46430135d29f16a40511d56f4071af07
URL:		https://github.com/okbob/pspg
BuildRequires:	ncurses-devel
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
