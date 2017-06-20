Name:	        cdk-minishift	
Version:	3.0.0
Release:	2%{?dist}
Summary:	Red Hat CDK Minishift binary 

License:        ASL 2.0	
URL:		https://developers.redhat.com
Source0:	 %{name}-%{version}.tar.gz

#BuildRequires:	
Requires:       libvirt

%description
RPM for installing minishift binary which is part of Red Hat Container Development Kit

%prep
%setup -n %{name}-%{version} -c


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}-%{version}
cp %{_builddir}/%{name}-%{version}/minishift %{buildroot}/%{_sharedstatedir}/%{name}-%{version}
chmod +x %{buildroot}/%{_sharedstatedir}/%{name}-%{version}/minishift

%postun
if [ $1 -eq 0 ] ; then
        rm -rf %{buildroot}/%{_sharedstatedir}/%{name}-%{version}
fi

#%post

%files
%{_sharedstatedir}/%{name}-%{version}/minishift

#%doc 



%changelog
* Tue Jun 20 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Bumping the release for cdk-minishift

* Wed May 17 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Removing dependancy on qemu (i.e. qemu-kvm)

* Wed May 17 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- adding dependancy on qemu (i.e. qemu-kvm)

* Wed May 17 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Adding excutable access to minishift binary

* Wed Apr 26 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Initial commit
