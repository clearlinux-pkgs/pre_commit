#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pre_commit
Version  : 2.16.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/8e/e2/a5c93bd312072003117408cf87e2cb7dcf4992d28ce3cab9bc5eeabecf43/pre_commit-2.16.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8e/e2/a5c93bd312072003117408cf87e2cb7dcf4992d28ce3cab9bc5eeabecf43/pre_commit-2.16.0.tar.gz
Summary  : A framework for managing and maintaining multi-language pre-commit hooks.
Group    : Development/Tools
License  : MIT
Requires: pre_commit-bin = %{version}-%{release}
Requires: pre_commit-license = %{version}-%{release}
Requires: pre_commit-python = %{version}-%{release}
Requires: pre_commit-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : pypi(cfgv)
BuildRequires : pypi(identify)
BuildRequires : pypi(nodeenv)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(toml)
BuildRequires : pypi(virtualenv)

%description
[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/pre-commit.pre-commit?branchName=master)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=21&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/21/master.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=21&branchName=master)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pre-commit/master.svg)](https://results.pre-commit.ci/latest/github/pre-commit/pre-commit/master)

%package bin
Summary: bin components for the pre_commit package.
Group: Binaries
Requires: pre_commit-license = %{version}-%{release}

%description bin
bin components for the pre_commit package.


%package license
Summary: license components for the pre_commit package.
Group: Default

%description license
license components for the pre_commit package.


%package python
Summary: python components for the pre_commit package.
Group: Default
Requires: pre_commit-python3 = %{version}-%{release}

%description python
python components for the pre_commit package.


%package python3
Summary: python3 components for the pre_commit package.
Group: Default
Requires: python3-core
Provides: pypi(pre_commit)
Requires: pypi(cfgv)
Requires: pypi(identify)
Requires: pypi(nodeenv)
Requires: pypi(pyyaml)
Requires: pypi(toml)
Requires: pypi(virtualenv)

%description python3
python3 components for the pre_commit package.


%prep
%setup -q -n pre_commit-2.16.0
cd %{_builddir}/pre_commit-2.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638366558
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pre_commit
cp %{_builddir}/pre_commit-2.16.0/LICENSE %{buildroot}/usr/share/package-licenses/pre_commit/0a1b7c6ad0735b8a94231652bab67240e4b834f6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pre-commit
/usr/bin/pre-commit-validate-config
/usr/bin/pre-commit-validate-manifest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pre_commit/0a1b7c6ad0735b8a94231652bab67240e4b834f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
