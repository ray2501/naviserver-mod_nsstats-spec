#
# spec file for package naviserver nsstats module
#

Summary:        NaviServer nsstats module
Name:           naviserver-mod_nsstats
Version:        1.9
Release:        0
License:        MPL-1.1
Group:          Productivity/Networking/Web/Servers
Url:            http://bitbucket.org/naviserver/nsstats
BuildRequires:  naviserver
Requires:       naviserver
Requires:       tcl
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Nsstats is a small pure Tcl module for NaviServer to report several
statistics about the liveliness off you naviserver installation.

%prep
%setup -q %{name}-%{version}

%build

%install
mkdir -p %buildroot/var/lib/naviserver/pages/
cp nsstats.tcl %buildroot/var/lib/naviserver/pages/

%clean
rm -rf %buildroot

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/pages/nsstats.tcl

%changelog

