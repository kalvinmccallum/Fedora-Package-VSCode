Name: vscode
Version: 1.63.2
Release: 1%{?dist}
Summary: Code editing redefined
License: MIT
URL: https://code.visualstudio.com/
Source0: https://update.code.visualstudio.com/latest/linux-x64/stable
BuildArch: x86_64

BuildRequires: nodejs
Requires: nodejs

%description
Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/share/vscode/
tar xzf stable -C %{buildroot}/usr/share/vscode/

%files
/usr/share/vscode/

%changelog
* Tue Feb 16 2023 Kalvin McCallum <kalvin_mccallum@student.uml.edu> - 1.63.2-1
- Initial build
