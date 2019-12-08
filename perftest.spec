%global fontname gnu-free

Name:          gnu-free-fonts
Version:       20120503
Release:       20
Summary:       GNU Unicode-encoded Fonts
License:       GPLv3+ with exceptions
URL:           http://www.gnu.org/software/freefont/
Source0:       http://ftp.gnu.org/gnu/freefont/freefont-src-%{version}.tar.gz
Source2:       69-gnu-free-mono.conf
Source3:       69-gnu-free-sans.conf
Source4:       69-gnu-free-serif.conf
Source5:       gnu-free.metainfo.xml
Source6:       gnu-free-mono.metainfo.xml
Source7:       gnu-free-sans.metainfo.xml
Source8:       gnu-free-serif.metainfo.xml

Patch0000:     gnu-free-fonts-devanagari-rendering.patch

BuildArch:     noarch
BuildRequires: fontpackages-devel fontforge /usr/bin/2to3


%description
Gnu FreeFont is a set of Unicode-encoded scalable outline fonts used on all modern operating systems.


%package common
Summary:  GNU FreeFont Common files
Requires: fontpackages-filesystem
Obsoletes: gnu-free-fonts-compat < 20120503
%description common
Some common files used by other %{name} font packages.

%package -n gnu-free-mono-fonts
Summary:  GNU Monospaced FreeFont
Requires: %{name}-common = %{version}-%{release}
%description -n gnu-free-mono-fonts
This package contains GNU Monospaced FreeFont files.


%package -n gnu-free-sans-fonts
Summary:  GNU Sans-Serif FreeFont
Requires: %{name}-common = %{version}-%{release}
%description -n gnu-free-sans-fonts
This package contains GNU Sans-Serif FreeFont files.


%package -n gnu-free-serif-fonts
Summary:  GNU Serif FreeFont
Requires: %{name}-common = %{version}-%{release}
%description -n gnu-free-serif-fonts
This package contains GNU Serif FreeFont files.


%prep
%autosetup -n freefont-%{version} -p1

cd tools/generate
rm *.pyc
for x in `ls`;do
   2to3 -w $x
done
cd -

%build
make

%install
cd sfd
install -m 755 -d %{buildroot}%{_fontdir}
install -p -m 644 *.ttf  %{buildroot}%{_fontdir}
install -m 755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/69-gnu-free-mono.conf
install -m 644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}/69-gnu-free-sans.conf
install -m 644 -p %{SOURCE4} %{buildroot}%{_fontconfig_templatedir}/69-gnu-free-serif.conf


for fconf in 69-gnu-free-mono.conf 69-gnu-free-sans.conf 69-gnu-free-serif.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done

install -Dm 644 -p %{SOURCE5} %{buildroot}%{_datadir}/appdata/gnu-free.metainfo.xml
install -Dm 644 -p %{SOURCE6} %{buildroot}%{_datadir}/appdata/gnu-free-mono.metainfo.xml
install -Dm 644 -p %{SOURCE7} %{buildroot}%{_datadir}/appdata/gnu-free-sans.metainfo.xml
install -Dm 644 -p %{SOURCE8} %{buildroot}%{_datadir}/appdata/gnu-free-serif.metainfo.xml

%_font_pkg -n mono -f 69-gnu-free-mono.conf FreeMono*.ttf
%{_datadir}/appdata/gnu-free-mono.metainfo.xml

%_font_pkg -n sans -f 69-gnu-free-sans.conf FreeSans*.ttf
%{_datadir}/appdata/gnu-free-sans.metainfo.xml

%_font_pkg -n serif -f 69-gnu-free-serif.conf FreeSerif*.ttf
%{_datadir}/appdata/gnu-free-serif.metainfo.xml

%files common
%doc AUTHORS ChangeLog CREDITS README
%license COPYING
%{_datadir}/appdata/gnu-free.metainfo.xml

%changelog
* Tue Nov 26 2019 Shuaishuai Song <songshuaishuai2@huawei.com> - 20120503-19
- package init
