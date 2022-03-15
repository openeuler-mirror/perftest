Name:           perftest
Version:        4.5
Release:        2
License:        GPLv2 or BSD
Summary:        RDMA Performance Testing Tools
Url:            https://github.com/linux-rdma/perftest
Source:         https://github.com/linux-rdma/perftest/releases/download/v4.5-0.12/perftest-4.5-0.12.ge93c538.tar.gz
Patch1:         support_get_cycles_for_riscv.patch

BuildRequires:  gcc libibverbs-devel >= 1.2.0 librdmacm-devel >= 1.0.21 libibumad-devel >= 1.3.10.2
BuildRequires:  pciutils-devel
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
* Tue Mar 15 2022 Xiaoqian Lv<xiaoqian@nj.iscas.ac.cn> - 4.5-2
- add patch to support get_cycles for riscv

* Tue Jan 18 2022 SimpleUpdate Robot <tc@openeuler.org> - 4.5-1
- Upgrade to version 4.5

* Tue 3 Aug 2021 Shenmei Tu <tushenmei@huawei.com> - 4.2-7
- bugfix-of-gcc-10.patch

* Fri 30 July 2021 Shenmei Tu <tushenmei@huawei.com> - 4.2-6
- bug fix of multiple definition

* Web 02 Jun 2021 zhaoyao<zhaoyao32@huawei.com> - 4.2-5
- fixs faileds: /bin/sh: gcc: command not found.

* Tue Nov 13 2019 Shuaishuai Song <songshuaishuai2@huawei.com> - 4.2-4
- Package init
