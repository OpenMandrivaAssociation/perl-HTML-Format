%define	real_name HTML-Format

Summary:	CPAN %{real_name} perl module
Name:		perl-%{real_name}
Version:	2.04
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/%{real_name}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/HTML-Format/
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Font-AFM >= 1.17
BuildRequires:	perl-HTML-Tree >= 3.15
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
%setup -q -n %{real_name}-%{version}

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


