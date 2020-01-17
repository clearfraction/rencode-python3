Name: rencode-python3
Version: 1.0.6
Release: 1
Summary: A Module similar to bencode from the BitTorrent project

License: GPLv3
URL: https://github.com/aresch/rencode
Source0: https://github.com/aresch/rencode/archive/v1.0.6.tar.gz

BuildRequires: python3-dev
BuildRequires: pip
BuildRequires: Cython

%description
pyparsing is a module that can be used to easily and directly configure syntax
The rencode module is similar to bencode from the BitTorrent project. For 
complex, heterogeneous data structures with many small elements

%prep
%setup -n rencode-1.0.6

%build

unset http_proxy
unset no_proxy 
unset https_proxy

python3 setup.py build

%install
unset http_proxy
unset no_proxy 
unset https_proxy

python3 -tt setup.py build  install --root=%{buildroot}

%files 
/usr/lib/python3.8/site-packages/rencode-1.0.6-py3.8.egg-info/*
/usr/lib/python3.8/site-packages/rencode/

%changelog

* Thu Jan 16 2020 David Va <davidva AT tuta DOT io> - 1.0.6-1
* Initial build
