%define major 0
%define libname %mklibname natspec %{major}
%define develname %mklibname natspec -d

Name:		libnatspec
Version:	0.2.6
Release:	1
License:	LGPLv2
Group:		System/Libraries
Url:		http://sourceforge.net/projects/natspec/
Summary:	Library for national and language-specific issues
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRequires:	popt-devel

%description
Library for national and language-specific issues.
This library provides userful functions for
mount, submount, mkisofs, multimedia players.
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.

%package -n %{libname}
Summary:	Library for national and language-specific issues
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
Library for national and language-specific issues.
This library provides userful functions for
mount, submount, mkisofs, multimedia players.
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.

%package -n %{develname}
Summary:	Development package of library for national and language-specific issues
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains the necessary include files
for developing applications with %{name}
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.

%package devel-examples
Summary:	Examples of %{name} using
Group:		Books/Howtos

%description devel-examples
The %{name}-devel package contains examples of patches
for developing applications with %{name}

%prep
%setup -q

%build
sh aclocal
sh autoheader
sh libtoolize --copy --force
sh automake --add-missing --include-deps --copy --force-missing
sh autoconf
%configure2_5x
%make

pushd docs
doxygen ./libnatspecDox.cfg
popd

%install
%makeinstall_std

# FIXME: I don't know how to install in /lib
# move to /lib
mkdir -p %{buildroot}/%{_lib}
mv %{buildroot}%{_libdir}/%{name}.* %{buildroot}/%{_lib}

%files
%doc AUTHORS README ChangeLog NEWS TODO README-ru.html
%{_bindir}/*
%{_mandir}/man1/*.1*

%files -n %{libname}
/%{_lib}/*.so.*

%files -n %{develname}
%doc docs/html
%{_includedir}/*.h
/%{_lib}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*

%files devel-examples
%doc examples profile

%changelog
* Thu Jul 07 2011 Александр Казанцев <kazancas@mandriva.org> 0.2.4-2mdv2011.0
+ Revision: 689047
+ rebuild (emptylog)

* Wed Jul 06 2011 Александр Казанцев <kazancas@mandriva.org> 0.2.4-1
+ Revision: 688950
- imported package libnatspec
- Created package structure for libnatspec.

