%global _empty_manifest_terminate_build 0
Name:		python-aiosnmp
Version:	0.2.3
Release:	1
Summary:	asyncio SNMP client
License:	MIT
URL:		https://github.com/hh-h/aiosnmp
Source0:	https://files.pythonhosted.org/packages/70/d4/1a9ce562053461102de168f561127d145b3cb1fb4f4071aeb4966c7238e4/aiosnmp-0.2.3.tar.gz
BuildArch:	noarch


%description
aiosnmp is an asynchronous SNMP client for use with asyncio.

%package -n python3-aiosnmp
Summary:	asyncio SNMP client
Provides:	python-aiosnmp
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-aiosnmp
aiosnmp is an asynchronous SNMP client for use with asyncio.

%package help
Summary:	Development documents and examples for aiosnmp
Provides:	python3-aiosnmp-doc
%description help
aiosnmp is an asynchronous SNMP client for use with asyncio.

%prep
%autosetup -n aiosnmp-0.2.3

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-aiosnmp -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Mon Jul 06 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
