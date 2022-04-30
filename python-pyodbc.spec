%global module pyodbc

Name:		python-%{module}
Version:	4.0.32
Release:	2
Summary:	Python DB API 2.0 Module for ODBC
License:	MIT
URL:		https://github.com/mkleehammer/pyodbc
Source0:	https://github.com/mkleehammer/pyodbc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# (upstream)
Patch0:			Upgrade_deprecated_unicode_encoding_calls.patch
BuildRequires:	pkgconfig(odbc)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)

%{?python_provide:%python_provide python3-%{module}}
Recommends: (mariadb-connector-odbc if mariadb-server)
Recommends: (postgresql-odbc if postgresql-server)

%description
A Python DB API 2 and 3 module for ODBC. This project provides an up-to-date,\
convenient interface to ODBC using native data types like datetime and\
decimal.

%files
%license LICENSE.txt
%doc README.md notes.txt
%{py_platsitedir}/%{module}.pyi
%{py_platsitedir}/%{module}*.so
%{py_platsitedir}/%{module}-*-py%{python_version}.egg-info

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

# fix path
mv %{buildroot}%{_prefix}/%{module}.pyi %{buildroot}%{py_platsitedir}

