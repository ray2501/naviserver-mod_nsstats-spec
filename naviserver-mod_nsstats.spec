%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}
%define packagename nsstats

Name:          naviserver-mod_nsstats
Summary:       NaviServer nsstats module
Version:       1.13
Release:       1
License:       MPL-1.1
Group:         Productivity/Networking/Web/Servers
Source:        %{packagename}.tar.gz
Patch0:        Makefile.patch
URL:           https://sourceforge.net/projects/naviserver/
BuildRequires: make
BuildRequires: naviserver
BuildRequires: naviserver-devel
Requires:      tcl >= 8.6
Requires:      naviserver
BuildRoot:     %{buildroot}

%description
Nsstats is a pure Tcl module that delivers comprehensive insights into the
performance and activity of your NaviServer installation.

%prep
%setup -q -n %{packagename}
%patch 0

%build

%install
mkdir -p %{buildroot}/var/lib/naviserver/pages
make DESTDIR=%{buildroot} NAVISERVER=/var/lib/naviserver install

%clean
rm -rf %buildroot

%files
%dir %attr(-,nsadmin,nsadmin) /var/lib/naviserver
%defattr(-,nsadmin,nsadmin)
/var/lib/naviserver/pages/nsstats.tcl
/var/lib/naviserver/pages/nsstats.adp
/var/lib/naviserver/pages/nsstats-4.99.adp
