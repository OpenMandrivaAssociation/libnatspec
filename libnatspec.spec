%define name libnatspec
%define version 0.2.4
%define release %mkrel 1

%define major 0
%define libname %mklibname natspec %{major}
%define develname %mklibname natspec -d

Name: %{name}
Version: %{version}
Release: %{release}
License: LGPLv2
Group: System/Libraries
Url: http://sourceforge.net/projects/natspec/
Summary: Library for national and language-specific issues
BuildRoot: %{_tmppath}/%{name}-buildroot
Source0: %{name}-%{version}.tar.bz2
BuildRequires: doxygen popt-devel 

%description
Library for national and language-specific issues.
This library provides userful functions for
mount, submount, mkisofs, multimedia players.
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.

%package -n %{libname}
Summary: Library for national and language-specific issues
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
Library for national and language-specific issues.
This library provides userful functions for
mount, submount, mkisofs, multimedia players.
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.

%package -n %{develname}
Summary: Development package of library for national and language-specific issues
Group: Development/Other
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains the necessary include files
for developing applications with %{name}
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.

%package devel-examples
Summary: Examples of %{name} using
Group: Books/Howtos

%description devel-examples
The %{name}-devel package contains examples of patches
for developing applications with %{name}

#%package -n python-module-natspec
#Summary: Python binding (buggy therefore not used now)
#Group: Development/Python
#Requires: %name = %version-%release

#%description -n python-module-natspec
#Python binding for natspec

%prep
%setup -q

%build
sh aclocal
sh autoheader
sh libtoolize --copy --force
sh automake --add-missing --include-deps --copy --force-missing
sh autoconf
%configure
%make

%install
%makeinstall
rm -rf %buildroot%_docdir/%name-%version/html

# FIXME: I don't know how to install in /lib
# move to /lib
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/%{name}.* %buildroot/%_lib

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS TODO README-ru.html
/%_lib/*.so.*
%_bindir/*
#/etc/profile.d/*

%files -n %{develname}
%defattr(-,root,root)
%doc docs/html
%_includedir/*.h
/%_lib/*.la
/%_lib/*.so
%_libdir/pkgconfig/*
%_datadir/aclocal/*

%files devel-examples
%defattr(-,root,root)
%doc examples profile

#%files -n python-module-natspec
#%python_sitelibdir/natspec.py
#%python_sitelibdir/_natspec.so
