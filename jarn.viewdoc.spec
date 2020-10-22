#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jarn.viewdoc
Version  : 2.3
Release  : 12
URL      : https://files.pythonhosted.org/packages/33/cd/e6e9ab725904adf3118d1b0be1552d298c855cf9980b733c5267c02d6fb1/jarn.viewdoc-2.3.zip
Source0  : https://files.pythonhosted.org/packages/33/cd/e6e9ab725904adf3118d1b0be1552d298c855cf9980b733c5267c02d6fb1/jarn.viewdoc-2.3.zip
Summary  : Python documentation viewer
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jarn.viewdoc-bin = %{version}-%{release}
Requires: jarn.viewdoc-license = %{version}-%{release}
Requires: jarn.viewdoc-python = %{version}-%{release}
Requires: jarn.viewdoc-python3 = %{version}-%{release}
Requires: Pygments
Requires: docutils
Requires: setuptools
BuildRequires : Pygments
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
jarn.viewdoc
        ============
        ------------------------------------
        Python documentation viewer
        ------------------------------------
        
        **viewdoc** is a Python package documentation viewer. It converts
        reST-formatted text to HTML and displays it in a browser window.
        
        viewdoc is typically used to check a package's long description before
        uploading it to PyPI.
        
        Installation
        ============
        
        viewdoc works with Python 2.7 - 3.7 and all released versions of setuptools
        and distribute.
        
        Use ``pip install jarn.viewdoc`` to install the ``viewdoc`` script.
        
        Usage
        =====
        
        ``viewdoc [options] [rst-file | egg-dir]``
        
        Options
        =======
        
        ``-s style, --style=style, or --style``
            Select the custom style added to the HTML output.
        
        ``-b browser, --browser=browser``
            Select the browser used for display. For a list of names see the
            `webbrowser`_ module.
        
        ``-c config-file, --config-file=config-file``
            Use config-file instead of the default ``~/.viewdoc``.
        
        ``-l, --list-styles``
            List available styles and exit.
        
        ``-h, --help``
            Print the help message and exit.
        
        ``-v, --version``
            Print the version string and exit.
        
        ``rst-file``
            The reST file to view.
        
        ``egg-dir``
            The Python package whose long description to view.
            Defaults to the current working directory.

%package bin
Summary: bin components for the jarn.viewdoc package.
Group: Binaries
Requires: jarn.viewdoc-license = %{version}-%{release}

%description bin
bin components for the jarn.viewdoc package.


%package license
Summary: license components for the jarn.viewdoc package.
Group: Default

%description license
license components for the jarn.viewdoc package.


%package python
Summary: python components for the jarn.viewdoc package.
Group: Default
Requires: jarn.viewdoc-python3 = %{version}-%{release}

%description python
python components for the jarn.viewdoc package.


%package python3
Summary: python3 components for the jarn.viewdoc package.
Group: Default
Requires: python3-core
Provides: pypi(jarn.viewdoc)
Requires: pypi(docutils)
Requires: pypi(pygments)
Requires: pypi(setuptools)

%description python3
python3 components for the jarn.viewdoc package.


%prep
%setup -q -n jarn.viewdoc-2.3
cd %{_builddir}/jarn.viewdoc-2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603393893
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jarn.viewdoc
cp %{_builddir}/jarn.viewdoc-2.3/LICENSE %{buildroot}/usr/share/package-licenses/jarn.viewdoc/1bec4c0d078ae3e99b06139c66f82fae86896000
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/viewdoc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jarn.viewdoc/1bec4c0d078ae3e99b06139c66f82fae86896000

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
