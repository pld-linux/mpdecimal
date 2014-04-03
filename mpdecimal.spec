Summary:	Fast arbitrary precision correctly-rounded decimal floating point arithmetic
Summary(pl.UTF-8):	Szybka arytmetyka zmiennoprzecinkowa dowolnej precyzji z właściwym zaokrąglaniem
Name:		mpdecimal
Version:	2.3
Release:	2
License:	BSD
Group:		Libraries
#Source0Download: http://www.bytereef.org/mpdecimal/download.html
Source0:	http://www.bytereef.org/software/mpdecimal/releases/%{name}-%{version}.tar.gz
# Source0-md5:	71702aa93eff9a5fae5b5422b8f2da02
URL:		http://www.bytereef.org/mpdecimal/
BuildRequires:	gmp-devel
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

%package apidocs
Summary:	libmpdec API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmpdec
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for libmpdec library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmpdec.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mpdecimal

ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libmpdec.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libmpdec.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt LICENSE.txt README.txt
%attr(755,root,root) %{_libdir}/libmpdec.so.2.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpdec.so
%{_includedir}/mpdecimal.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpdec.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/* literature
