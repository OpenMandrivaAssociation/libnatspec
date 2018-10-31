%define major 0
%define libname %mklibname natspec %{major}
%define devname %mklibname natspec -d
%bcond_with crosscompile

Summary:	Library for national and language-specific issues
Name:		libnatspec
Version:	0.3.0
Release:	5
License:	LGPLv2
Group:		System/Libraries
Url:		http://sourceforge.net/projects/natspec/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRequires:	pkgconfig(popt)

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

%package -n %{devname}
Summary:	Development package of library for national and language-specific issues
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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
%if %{with crosscompile}
export ac_cv_func_malloc_0_nonnull=yes
export ac_cv_func_realloc_0_nonnull=yes
%endif
%configure
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
%doc AUTHORS README NEWS TODO README-ru.html
%{_bindir}/*
%{_mandir}/man1/*.1*

%files -n %{libname}
/%{_lib}/libnatspec.so.%{major}*

%files -n %{devname}
%doc docs/html
%{_includedir}/*.h
/%{_lib}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*

%files devel-examples
%doc examples profile

