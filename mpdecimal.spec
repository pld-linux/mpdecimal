Summary:	Fast arbitrary precision correctly-rounded decimal floating point arithmetic
Summary(pl.UTF-8):	Szybka arytmetyka zmiennoprzecinkowa dowolnej precyzji z właściwym zaokrąglaniem
Name:		mpdecimal
Version:	2.5.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: http://www.bytereef.org/mpdecimal/download.html
Source0:	http://www.bytereef.org/software/mpdecimal/releases/%{name}-%{version}.tar.gz
# Source0-md5:	3cacb882f59f795f4ed6822d80bd2f7d
Patch0:		build.patch
URL:		http://www.bytereef.org/mpdecimal/
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmpdec is a fast C/C++ library for correctly-rounded arbitrary
precision decimal floating point arithmetic. It is a complete
implementation of Mike Cowlishaw/IBM's General Decimal Arithmetic
Specification.

%description -l pl.UTF-8
libmpdec to szybka biblioteka C/C++ do arytmetyki zmiennoprzecinkowej
dowolnej precyzji z poprawnym zaokrąglaniem. Jest to pełna
implementacja specyfikacji Mike'a Cowlishawa/IBM General Decimal
Arithmetic.

%package devel
Summary:	Header files for libmpdec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmpdec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmpdec library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmpdec.

%package static
Summary:	Static libmpdec library
Summary(pl.UTF-8):	Statyczna biblioteka libmpdec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmpdec library.

%description static -l pl.UTF-8
Statyczna biblioteka libmpdec.

%package c++
Summary:	C++ interface to mpdec library
Summary(pl.UTF-8):	Intefejs C++ do biblioteki C++
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ interface to mpcdec fast arbitrary precision correctly-rounded
decimal floating point arithmetic library.

%description c++ -l pl.UTF-8
Interfejs C++ do biblioteki mpcdec - szybkiej arytmetyki
zmiennoprzecinkowej dowolnej precyzji z właściwym zaokrąglaniem.

%package c++-devel
Summary:	Header file for libmpdec++ library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libmpdec++
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header file for libmpdec++ library.

%description c++-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libmpdec++.

%package c++-static
Summary:	Static libmpdec++ library
Summary(pl.UTF-8):	Statyczna biblioteka libmpdec++
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static libmpdec++ library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka libmpdec++.

%package apidocs
Summary:	libmpdec API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmpdec
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libmpdec library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmpdec.

%prep
%setup -q
%patch -P0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mpdecimal

#ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libmpdec.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libmpdec.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt LICENSE.txt README.txt
%attr(755,root,root) %{_libdir}/libmpdec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpdec.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpdec.so
%{_includedir}/mpdecimal.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpdec.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpdec++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpdec++.so.2

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpdec++.so
%{_includedir}/decimal.hh

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libmpdec++.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/*
