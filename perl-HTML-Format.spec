%define	modname	HTML-Format
%define	modver	2.09

Summary:	CPAN %{modname} perl module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/HTML-Format/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Font::AFM) >= 1.17
BuildRequires:	perl(HTML::Tree) >= 3.15
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More) >= 0.960.0

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
%setup -qn %{modname}-%{modver}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{perl_vendorlib}/HTML/*
%{_mandir}/man3/*

