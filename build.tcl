#!/usr/bin/tclsh

set arch "noarch"
set base "naviserver-mod_nsstats-1.6"

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb naviserver-mod_nsstats.spec]
exec >@stdout 2>@stderr {*}$buildit

