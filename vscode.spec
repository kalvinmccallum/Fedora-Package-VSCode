Name:           vscode
Version:        1.63.2
Release:        1%{?dist}
Summary:        Visual Studio Code

Group:          Applications/Editors
License:        MIT
URL:            https://code.visualstudio.com/

Source0:        https://update.code.visualstudio.com/latest/linux-x64/stable
BuildRequires:  libX11-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  glibc-devel
BuildRequires:  libstdc++-devel
BuildRequires:  expat-devel
BuildRequires:  desktop-file-utils
Requires:       libX11
Requires:       libxkbfile
Requires:       glibc
Requires:       libstdc++
Requires:       expat

%description
Visual Studio Code is a code editor.

%prep
%setup -q

%build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 "code" %{buildroot}%{_bindir}/code

install -d -m 755 %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    --mode=644 \
    --add-category=X-Red-Hat-Base \
    --add-category=X-Red-Hat-Dev \
    --add-category=X-Red-Hat-Tools \
    --add-category=Development \
    --add-category=IDE \
    --add-category=TextEditor \
    --add-category=Utility \
    --add-category=GTK \
    --add-category=GNOME \
    --add-category=Qt \
    "resources/linux/code.desktop"

%files
%{_bindir}/code
%{_datadir}/applications/code.desktop

%changelog
* Mon Feb 27 2023 Kalvin McCallum <kalvin_mccallum@student.uml.edu> - 1.63.2-1
- Initial build
