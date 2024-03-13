Name:		hello
Version:	0.0.1
Release:	1%{?dist}
Summary:	A trivial bash script.
BuildArch:	noarch        

License:	GPL
Source0:	%{name}-%{version}.tar.gz

Requires:	bash

%description
A demo RPM build.

%prep
%setup -q

%build

%install
#rm -rf $RPM_BUILD_ROOT
#mkdir -p $RPM_BUILD_ROOT/%{_bindir}
#cp %{name}.sh $RPM_BUILD_ROOT/%{_bindir}
#chmod 4755 $RPM_BUILD_ROOT/%{_bindir}/%{name}.sh
install -D -p -m 4755 %{name}.sh $RPM_BUILD_ROOT/%{_bindir}/%{name}.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}.sh

%changelog
* Thu Mar 07 2024 Matthew Yee <myee@redhat.com> - 0.0.1
- First version.
