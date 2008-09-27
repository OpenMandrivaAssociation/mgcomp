%define name	mgcomp
%define version 1.4.1
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	DyALog compiler for Linguistic Meta-Grammars
License:	GPL
Group:		Sciences/Computer science
Source:		ftp://ftp.inria.fr/INRIA/Projects/Atoll/Eric.Clergerie/TAG/%{name}-%{version}.tar.bz2
Url:		http://atoll.inria.fr/packages/packages.html#mgcomp
Buildrequires:	dyalog
Buildroot:	%{_tmppath}/%{name}-%{version}
# (tv) depends on dyalog which is ia32 only:
ExclusiveArch:  %{ix86}

%description
mgcomp is a DyALog compiler for Linguistic Meta-Grammars, with some additional
files for a full processing chain.

%prep
%setup -q

%build
export LDFLAGS=-L%{_libdir}/DyAlog
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL LICENSE NEWS README
%{_bindir}/*

