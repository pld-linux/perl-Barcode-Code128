#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Barcode
%define		pnam	Code128
Summary:	Barcode::Code128 - Perl module for generating CODE 128 bar codes
Summary(pl):	Barcode::Code128 - modu³ Perla do generowania kodów paskowych CODE 128
Name:		perl-Barcode-Code128
Version:	2.00
Release:	1
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9838b2c070d90f781013a538c5ada15a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Barcode::Code128 generates bar codes using the CODE 128 symbology. It
can generate images in PNG or GIF format using the GD package, or it
can generate a text string representing the barcode that you can
render using some other technology if desired.

%description -l pl
Barcode::Code128 generuje kody paskowe przy u¿yciu symboli CODE 128.
Mo¿e generowaæ obrazki w formacie PNG lub GIF przy u¿yciu pakietu GD
albo tekst reprezentuj±cy kod paskowy, który mo¿na zrenderowaæ w inny
sposób.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Barcode/Code128.pm
%{_mandir}/man3/*
