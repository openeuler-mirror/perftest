Name:           perftest
Version:        4.2
Release:        4
License:        GPLv2 or BSD
Summary:        RDMA Performance Testing Tools
Url:            https://github.com/linux-rdma/perftest
Source:         https://github.com/linux-rdma/%{name}/releases/download/V4.2-0.8/perftest-4.2-0.8.g0e24e67.tar.gz


BuildRequires:  libibverbs-devel >= 1.2.0 librdmacm-devel >= 1.0.21 libibumad-devel >= 1.3.10.2
Obsoletes:      openib-perftest < 1.3

%description
Perftest is a collection of simple tools for testing bandwidth and latency over RDMA connections.

%prep
%autosetup -p1

%build
%configure
%make_build CFLAGS+="-fPIC -g -Wall -D_GNU_SOURCE -O3"

%install
for file in ib_{atomic,read,send,write}_{lat,bw} raw_ethernet_{lat,bw}; do
     install -D -m 0755 $file %{buildroot}%{_bindir}/$file
done

%files
%doc README COPYING
%_bindir/*

%changelog
* Tue Nov 13 2019 Shuaishuai Song <songshuaishuai2@huawei.com> - 4.2-4
- Package init
