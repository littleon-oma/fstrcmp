%define         major 0
%define         libname %mklibname %{name} %{major}
%define         devel %mklibname -d %{name}
%define         static %mklibname -d -s %{name}

Name:           fstrcmp
Version:        0.7.D001
Release:        %mkrel 1
Summary:        Library that is used to make fuzzy comparisons of strings and byte arrays
Group:          System/Libraries
License:        GPLv2
URL:            http://fstrcmp.sourceforge.net/
Source0:        http://fstrcmp.sourceforge.net/%{name}-%{version}.tar.gz

BuildRequires:  groff
BuildRequires:  libtool
BuildRequires:  ghostscript

%description
The fstrcmp project provides a library that is used to make fuzzy comparisons
of strings and byte arrays, including multi-byte character strings.

This can be useful in error messages, enabling the suggestion of likely valid
alternatives. In compilers, this can reduce the cascade of secondary errors. 

%package -n %{libname}
Summary:        Library that is used to make fuzzy comparisons of strings and byte arrays
Group:          System/Libraries

%description -n %{libname}
The fstrcmp project provides a library that is used to make fuzzy comparisons
of strings and byte arrays, including multi-byte character strings.

This can be useful in error messages, enabling the suggestion of likely valid
alternatives. In compilers, this can reduce the cascade of secondary errors. 

%package -n %{devel}
Summary:        Library that is used to make fuzzy comparisons of strings and byte arrays
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}

%description -n %{devel}
The fstrcmp project provides a library that is used to make fuzzy comparisons
of strings and byte arrays, including multi-byte character strings.

This can be useful in error messages, enabling the suggestion of likely valid
alternatives. In compilers, this can reduce the cascade of secondary errors. 

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup

%build
%configure --enable-shared --disable-static
%make_build

%install
%make_install

# Remove static libraries
find %{buildroot} \( -name "*.la" -o -name "*.a" \) -delete

# Fix permissions
chmod 0755 %{buildroot}%{_libdir}/*.so.*
rm %{buildroot}%{_defaultdocdir}/%{name}/*.pdf

%check
# make t0001a ... t0010a
%__make $(seq -f "t%04ga" 1 10)

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1*

%files -n %{devel}
%doc etc/reference.pdf
%{_includedir}/fstrcmp.h
%{_libdir}/libfstrcmp.so
%{_libdir}/pkgconfig/fstrcmp.pc
%{_mandir}/man3/fmemcmp.3*
%{_mandir}/man3/fmemcmpi.3*
%{_mandir}/man3/fstrcasecmp.3*
%{_mandir}/man3/fstrcasecmpi.3*
%{_mandir}/man3/fstrcmp.3*
%{_mandir}/man3/fstrcmpi.3*
%{_mandir}/man3/fstrcoll.3*
%{_mandir}/man3/fstrcolli.3*
%{_mandir}/man3/fwcscmp.3*
%{_mandir}/man3/fwcscmpi.3*

%files -n %{libname}
%{_libdir}/libfstrcmp.so.%{major}*




