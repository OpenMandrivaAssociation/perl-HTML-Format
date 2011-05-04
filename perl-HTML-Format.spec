%define	upstream_name    HTML-Format
%define	upstream_version 2.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	CPAN %{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/HTML-Format/
Source:     http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Font::AFM) >= 1.17
BuildRequires:	perl(HTML::Tree) >= 3.15
BuildRequires:	perl(Test::More) >= 0.960.0
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a collection of modules that formats HTML as plaintext,
PostScript or RTF.

The modules present in this package are:

  HTML::FormatText - Formatter that converts a syntax tree to plain
        readable text.

  HTML::FormatPS - Formatter that outputs PostScript code.

  HTML::FormatRTF - Formatter that outputs RTF code.

  HTML::Formatter - Base class for various formatters.  Formatters
        traverse a syntax tree and produce some textual output.  None
        of the current formatters handle tables or forms yet.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/HTML/*
