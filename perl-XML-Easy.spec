%define upstream_name    XML-Easy
%define upstream_version 0.008

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Basic manipulation of XML data nodes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl(Exporter)
BuildRequires: perl(IO::File)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Params::Classify)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
the XML::Easy manpage is a collection of modules relating to the
processing, parsing, and serialisation of XML data. It is oriented towards
the use of XML to represent data for interchange purposes, rather than the
use of XML as markup of principally textual data. It does not perform any
schema processing, and does not interpret DTDs or any other kind of schema.
It adheres strictly to the XML specification, in all its awkward details,
except for the aforementioned DTDs.

the XML::Easy manpage strictly separates the in-program manipulation of XML
data from the processing of the textual form of XML. This shields the XML
user from the inconvenient and obscure aspects of XML syntax. XML data
nodes are mainly processed in a clean functional style, using the the
XML::Easy::NodeBasics manpage module. In the (very likely) event that an
application requires some more purpose-specific XML data processing
facilities, they are readily built on top of the XML::Easy::NodeBasics
manpage, retaining the abstraction from textual XML.

When XML must be handled in textual form, for input and output, the the
XML::Easy::Text manpage module supplies a parser and a serialiser. The
interfaces here, too, are functional in nature.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


