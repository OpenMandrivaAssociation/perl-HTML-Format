%define	upstream_name    HTML-Format
%define	upstream_version 2.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:	CPAN %{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/HTML-Format/
Source:     http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Font::AFM) >= 1.17
BuildRequires:	perl(HTML::Tree) >= 3.15
BuildRequires:	perl(Module::Build)
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
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/HTML/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.90.0-3mdv2012.0
+ Revision: 765303
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.90.0-1
+ Revision: 690263
- update to new version 2.09

* Tue May 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.70.0-1
+ Revision: 675504
- new version

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.50.0-2
+ Revision: 667193
- mass rebuild

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.50.0-1
+ Revision: 646418
- new version

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.40.0-1mdv2010.1
+ Revision: 403254
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.04-5mdv2009.0
+ Revision: 223786
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.04-4mdv2008.1
+ Revision: 180406
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 2.04-3mdv2007.0
+ Revision: 85636
- Import perl-HTML-Format

* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 2.04-3
- use the %%mkrel macro

* Mon Jul 11 2005 Oden Eriksson <oeriksson@mandriva.com> 2.04-2mdk
- fix deps

* Sat Jul 09 2005 Andreas Hasenack <andreas@mandriva.com> 2.04-1mdk
- packaged for Mandriva

