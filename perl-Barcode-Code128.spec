
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Barcode
%define pnam	Code128
Summary:	Barcode::Code128 - Perl module for generating CODE 128 bar codes
Name:		perl-Barcode-Code128
Version:	2.00
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9838b2c070d90f781013a538c5ada15a
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Similar functionality is available at shell prompts of *nix O/S.
This modules is attempting to provide the same to Perl programming,

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Barcode/Code128.pm
%{_mandir}/man3/*
