#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Guard
Version  : 1.023
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Guard-1.023.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Guard-1.023.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libguard-perl/libguard-perl_1.023-1.debian.tar.xz
Summary  : safe cleanup blocks
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Guard-lib = %{version}-%{release}
Requires: perl-Guard-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Guard - safe cleanup blocks
SYNOPSIS
use Guard;

# temporarily chdir to "/etc" directory, but make sure
# to go back to "/" no matter how myfun exits:
sub myfun {
scope_guard { chdir "/" };
chdir "/etc";

code_that_might_die_or_does_other_fun_stuff;
}

%package dev
Summary: dev components for the perl-Guard package.
Group: Development
Requires: perl-Guard-lib = %{version}-%{release}
Provides: perl-Guard-devel = %{version}-%{release}
Requires: perl-Guard = %{version}-%{release}

%description dev
dev components for the perl-Guard package.


%package lib
Summary: lib components for the perl-Guard package.
Group: Libraries
Requires: perl-Guard-license = %{version}-%{release}

%description lib
lib components for the perl-Guard package.


%package license
Summary: license components for the perl-Guard package.
Group: Default

%description license
license components for the perl-Guard package.


%prep
%setup -q -n Guard-1.023
cd ..
%setup -q -T -D -n Guard-1.023 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Guard-1.023/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Guard
cp COPYING %{buildroot}/usr/share/package-licenses/perl-Guard/COPYING
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Guard.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Guard.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Guard/Guard.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Guard/COPYING
