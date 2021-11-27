#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Object oriented C++ interface to CFITSIO library
Summary(pl.UTF-8):	Zorientowany obiektowo interfejs C++ do biblioteki CFITSIO
Name:		CCfits
Version:	2.6
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	https://heasarc.gsfc.nasa.gov/fitsio/ccfits/%{name}-%{version}.tar.gz
# Source0-md5:	442a2e8ca022b35402b189d146ba8ddd
URL:		https://heasarc.gsfc.nasa.gov/fitsio/ccfits/
BuildRequires:	cfitsio-devel >= 3.080
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	rpm-build >= 4.6
Requires:	cfitsio >= 3.080
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CCfits is an object oriented interface to the CFITSIO library. It is
designed to make the capabilities of CFITSIO available to programmers
working in C++. It is written in ANSI C++ and implemented using the
C++ Standard Library with namespaces, exception handling, and member
template functions.

%description -l pl.UTF-8
CCfits to zorientowany obiektowo interfejs do biblioteki CFITSIO. Jest
zaprojektowany, aby udostępnić możliwości biblioteki CFITSIO
programistom pracującym w C++. Jest napisany w ANSI C++,
zaimplementowany przy użyciu biblioteki standardowej C++ z
przestrzeniami nazw, obsługą wyjątków i szablonami metod.

%package devel
Summary:	Header files and documentation for CCfits
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do CCfits
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cfitsio-devel >= 3.080
Requires:	libstdc++-devel >= 6:5

%description devel
Header files and development documentation for CCfits.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty do CCfits.

%package static
Summary:	Static CCfits library
Summary(pl.UTF-8):	Statyczna biblioteka CCfits
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of CCfits library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki CCfits.

%package apidocs
Summary:	API documentation for CCfits library
Summary(pl.UTF-8):	Dokumentacja API biblioteki CCfits
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for CCfits library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki CCfits.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libCCfits.la
# demo
%{__rm} $RPM_BUILD_ROOT%{_bindir}/cookbook

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES License.txt
%attr(755,root,root) %{_libdir}/libCCfits.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCCfits.so.0

%files devel
%defattr(644,root,root,755)
%doc CCfits-2.6.pdf
%attr(755,root,root) %{_libdir}/libCCfits.so
%{_includedir}/CCfits
%{_pkgconfigdir}/CCfits.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libCCfits.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc html/*.{css,html,js,png}
