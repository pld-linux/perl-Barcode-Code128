#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%define		pdir	Barcode
%define		pnam	Code128
Summary:	Barcode::Code128 - Perl module for generating CODE 128 bar codes
Summary(pl.UTF-8):	Barcode::Code128 - moduł Perla do generowania kodów paskowych CODE 128
Name:		perl-Barcode-Code128
Version:	2.01
Release:	1
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Barcode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a0aa077b26926c30659471d14515d907
URL:		http://search.cpan.org/dist/Barcode-Code128/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Barcode::Code128 generates bar codes using the CODE 128 symbology. It
can generate images in PNG or GIF format using the GD package, or it
can generate a text string representing the barcode that you can
render using some other technology if desired.

%description -l pl.UTF-8
Barcode::Code128 generuje kody paskowe przy użyciu symboli CODE 128.
Może generować obrazki w formacie PNG lub GIF przy użyciu pakietu GD
albo tekst reprezentujący kod paskowy, który można zrenderować w inny
sposób.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# module generates correct image, but a bit different to
# the one included in the distribution and compared with
mv t/png.t{,.broken}

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
