Name:           perftest
Version:        4.5
Release:        4
License:        GPLv2 or BSD
Summary:        RDMA Performance Testing Tools
Url:            https://github.com/linux-rdma/perftest
Source:         https://github.com/linux-rdma/perftest/releases/download/v4.5-0.12/perftest-4.5-0.12.ge93c538.tar.gz

Patch1: 0001-perftest_parameters-Add-inline-feature-support-of-ER.patch
Patch2: 0002-Perftest-replace-rand-with-getrandom-during-MR-buffe.patch
Patch3: 0003-Perftest-Fix-verification-of-max_inline_data-for-_cr.patch
Patch4: 0004-Perftest-Increase-max-inline-size-to-support-larger-.patch
Patch5: 0005-Perftest-Add-support-for-HNS.patch
Patch6: 0006-Perftest-Add-new-HNS-roce-device-ROH-to-support-new_.patch
Patch7: 0007-add-loongarch-support-for-perftest.patch

BuildRequires:  automake gcc libibverbs-devel >= 1.2.0 librdmacm-devel >= 1.0.21 libibumad-devel >= 1.3.10.2
BuildRequires:  pciutils-devel
BuildRequires:  guile
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
* Fri Jan 6 2023 Wenlong Zhang<zhangwenlong@loongson.cn> - 4.5-4
- Type: bugfix
- ID: NA
- SUG: NA
- DESC: fix build error for loongarch64

* Tue Nov 22 2022 tangchengchang <tangchengchang@huawei.com> - 4.5-3
- Type: bugfix
- ID: NA
- SUG: NA
- DESC: Replace patches with the perftest community version.

* Mon Nov 07 2022 tangchengchang <tangchengchang@huawei.com> - 4.5-2
- Type: requirement
- ID: NA
- SUG: NA
- DESC: Add hns support and fixes some bug in perftest

* Tue Jan 18 2022 SimpleUpdate Robot <tc@openeuler.org> - 4.5-1
- Upgrade to version 4.5

* Tue Aug 03 2021 Shenmei Tu <tushenmei@huawei.com> - 4.2-7
- bugfix-of-gcc-10.patch

* Fri Jul 30 2021 Shenmei Tu <tushenmei@huawei.com> - 4.2-6
- bug fix of multiple definition

* Wed Jun 02 2021 zhaoyao<zhaoyao32@huawei.com> - 4.2-5
- fixs faileds: /bin/sh: gcc: command not found.

* Wed Nov 13 2019 Shuaishuai Song <songshuaishuai2@huawei.com> - 4.2-4
- Package init
