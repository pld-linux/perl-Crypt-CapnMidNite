#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	CapnMidNite
Summary:	Crypt::CapnMidNite - Perl interface to MD5, RC4 encrypt/decrypt
Summary(pl):	Crypt::CapnMidNite - interfejs perlowy do szyfrowania/odszyfrowywania MD5, RC4
Name:		perl-Crypt-CapnMidNite
Version:	1.00
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.cpan.org/modules/by-authors/id/M/MI/MIKER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1931454ee2b6e28cf5f750ad283dd282
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Crypt::CapnMidNite module allows you to use the RSA Data Security
Inc. MD5 Message Digest algorithm, RC4 stream crypt function and a
modified, not readily reversible RC4 based stream crypt from within
Perl programs.

%description -l pl
Modu³ Crypt::CapnMidNite pozwala na u¿ywanie algorytmów RSA Data
Security Inc. takich jak algorytmu skrótu MD5, strumieniowej funkcji
szyfruj±cej RC4 oraz zmodyfikowanej, nie od razu odwracalnej wersji
strumieniowej funkcji szyfruj±cej opartej na RC4.

%package -n perl-Crypt-C_LockTite
Summary:	Crypt::C_LockTite - Perl interface to MD5, RC4 encrypt/decrypt
Summary(pl):	Crypt::C_LockTite - perlowy interfesj do szyfrowania/odszyfrowywania MD5, RC4
Group:		Development/Languages/Perl

%description -n perl-Crypt-C_LockTite
The Crypt::C_LockTite module allows you to use the RSA Data Security
Inc. MD5 Message Digest algorithm, RC4 stream crypt function and a
modified, not readily reversible RC4 based stream crypt from within
Perl programs.

This module contains proprietary version of "encode" function,
modified from one that comes in Crypt::CapnMidNite module.

%description -n perl-Crypt-C_LockTite -l pl
Modu³ Crypt::C_LockTite pozwala na u¿ywanie algorytmów RSA Data
Security Inc. takich jak algorytmu skrótu MD5, strumieniowej funkcji
szyfruj±cej RC4 oraz zmodyfikowanej, nie od razu odwracalnej wersji
strumieniowej funkcji szyfruj±cej opartej na RC4.

Ten modu³ zawiera w³asn± wersjê funkcji "encode", zmodyfikowan± w
stosunku do zawartej w module Crypt::CapnMidNite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

cp -f name name.CapnMidNite
mv -f Makefile Makefile.CapnMidNite
%{__perl} -pi -e 's/NAME = \(1\)/NAME = (0)/' Makefile.PL

%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

mv -f name name.C_LockTite
mv -f name.CapnMidNite name

%{__make} -f Makefile.CapnMidNite \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test -f Makefile.CapnMidNite}

mv -f blib blib.CapnMidNite
rm -f pm_to_blib
mv -f name.C_LockTite name

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf blib
mv -f blib.CapnMidNite blib

%{__make} install -f Makefile.CapnMidNite \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/CapnMidNite.pm
%dir %{perl_vendorarch}/auto/Crypt/CapnMidNite
%{perl_vendorarch}/auto/Crypt/CapnMidNite/CapnMidNite.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/CapnMidNite/CapnMidNite.so
%{_mandir}/man3/Crypt::CapnMidNite*

%files -n perl-Crypt-C_LockTite
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/C_LockTite.pm
%dir %{perl_vendorarch}/auto/Crypt/C_LockTite
%{perl_vendorarch}/auto/Crypt/C_LockTite/C_LockTite.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/C_LockTite/C_LockTite.so
%{_mandir}/man3/Crypt::C_LockTite*
