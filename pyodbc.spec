%define _empty_manifest_terminate_build 0

%global modulename pyodbc

Name:           pyodbc
Version:        4.0.30
Release:        1
Summary:        Python DB API 2.0 Module for ODBC
License:        MIT
URL:            https://github.com/mkleehammer/pyodbc
Source0:        https://github.com/mkleehammer/pyodbc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  unixODBC-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
A Python DB API 2 and 3 module for ODBC. This project provides an up-to-date,\
convenient interface to ODBC using native data types like datetime and\
decimal.

%description %_description

%package -n python-%{modulename}
Summary:        Python DB API 2.0 Module for ODBC
%{?python_provide:%python_provide python3-%{modulename}}
Recommends: (mariadb-connector-odbc if mariadb-server)
Recommends: (postgresql-odbc if postgresql-server)

%description -n python-%{modulename}
A Python DB API 2 and 3 module for ODBC. This project provides an up-to-date,
convenient interface to ODBC using native data types like datetime and
decimal.


%prep
%setup -q

%build
%py3_build

%install
%py3_install

%files -n python-%{name}
%license LICENSE.txt
%doc README.md notes.txt
%{python3_sitearch}/*
