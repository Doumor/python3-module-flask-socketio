%define pypi_name flask-socketio

%def_without check
%def_with docs

Name:    python3-module-%pypi_name
Version: 5.3.6
Release: alt1

Summary: Socket.IO integration for Flask applications.
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/Flask-SocketIO/
VCS:     https://github.com/miguelgrinberg/flask-socketio

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-flask
BuildRequires: python3-module-pytest
BuildRequires: python3-module-socketio
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: latexmk
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build
PYTHONPATH="${PWD}/src" %make_build -C docs latex SPHINXBUILD=sphinx-build-3
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'

%install
%pyproject_install

%check
%pyproject_run_pytest --ignore-glob='*/test_client.py'

%files
%doc CHANGES.md README.md SECURITY.md LICENSE docs/_build/latex/flask-socketio.pdf example/
%python3_sitelibdir/flask_socketio/
%python3_sitelibdir/Flask_SocketIO-%version.dist-info

%changelog
* Wed Oct 04 2023 Danilkin Danila <danild@altlinux.org> 5.3.6-alt1
- Initial build for Sisyphus
