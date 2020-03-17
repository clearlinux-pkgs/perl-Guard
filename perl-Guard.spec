#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Guard
Version  : 1.023
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Guard-1.023.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Guard-1.023.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libguard-perl/libguard-perl_1.023-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Guard-license = %{version}-%{release}
Requires: perl-Guard-perl = %{version}-%{release}
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
Provides: perl-Guard-devel = %{version}-%{release}
Requires: perl-Guard = %{version}-%{release}

%description dev
dev components for the perl-Guard package.


%package license
Summary: license components for the perl-Guard package.
Group: Default

%description license
license components for the perl-Guard package.


%package perl
Summary: perl components for the perl-Guard package.
Group: Default
Requires: perl-Guard = %{version}-%{release}

%description perl
perl components for the perl-Guard package.


%prep
%setup -q -n Guard-1.023
cd %{_builddir}
tar xf %{_sourcedir}/libguard-perl_1.023-1.debian.tar.xz
cd %{_builddir}/Guard-1.023
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Guard-1.023/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Guard
cp %{_builddir}/Guard-1.023/COPYING %{buildroot}/usr/share/package-licenses/perl-Guard/9a56f3b919dfc8fced3803e165a2e38de62646e5
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Guard/9b58a31518909aa40c7625c6632ea065158e4db1
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Guard.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Guard/9a56f3b919dfc8fced3803e165a2e38de62646e5
/usr/share/package-licenses/perl-Guard/9b58a31518909aa40c7625c6632ea065158e4db1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/Guard.pm
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/auto/Guard/Guard.so
