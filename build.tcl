#!/usr/bin/tclsh

set arch "noarch"
set base "nsstats"

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force Makefile.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb naviserver-mod_nsstats.spec]
exec >@stdout 2>@stderr {*}$buildit

