%define name	mgcomp
%define version 1.4.3
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	DyALog compiler for Linguistic Meta-Grammars
License:	GPL
Group:		Sciences/Computer science
Url:		http://alpage.inria.fr/catalogue.en.html#mgcomp
Source:		https://gforge.inria.fr/frs/download.php/4346/%{name}-%{version}.tar.gz
Patch0:     mgcomp-1.4.3-fix-dyalog-test.patch
Buildrequires:	dyalog
Buildroot:	%{_tmppath}/%{name}-%{version}
# (tv) depends on dyalog which is ia32 only:
ExclusiveArch:  %{ix86}

%description
mgcomp is a DyALog compiler for Linguistic Meta-Grammars, with some additional
files for a full processing chain.

%prep
%setup -q
%patch0 -p 1

%build
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL LICENSE README
%{_bindir}/*
%{_libdir}/pkgconfig/mgcomp.pc
