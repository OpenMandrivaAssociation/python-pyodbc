Name:		python-pyodbc
Version:	4.0.35
Release:	1
Summary:	Python DB API 2.0 Module for ODBC
License:	MIT
URL:		https://github.com/mkleehammer/pyodbc
#Source0:	https://github.com/mkleehammer/pyodbc/archive/%{version}.tar.gz/pyodbc-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/p/pyodbc/pyodbc-%{version}.tar.gz
BuildRequires:	pkgconfig(odbc)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

Recommends: (mariadb-connector-odbc if mariadb-server)
Recommends: (postgresql-odbc if postgresql-server)

%description
A Python DB API 2 and 3 module for ODBC. This project provides an up-to-date,\
convenient interface to ODBC using native data types like datetime and\
decimal.

%files
%license LICENSE.txt
%doc README.md
%{py_platsitedir}/pyodbc.pyi
%{py_platsitedir}/pyodbc*.so
%{py_platsitedir}/pyodbc-*.*-info

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n pyodbc-%{version}

%build
%py_build

%install
%py_install

# fix path
mv %{buildroot}%{_prefix}/pyodbc.pyi %{buildroot}%{py_platsitedir}

