Name: vscode
Version: 1.54.0
Release: 1%{?dist}
Summary: Code editing. Redefined.
License: MIT
URL: https://code.visualstudio.com/
Source0: %{name}-%{version}.tar.gz
BuildRequires: libX11-devel libxkbfile-devel libsecret-devel libXScrnSaver-devel
Requires: libX11 libxkbfile libsecret libXScrnSaver

%description
Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages (such as C++, C#, Java, Python, PHP, Go) and runtimes (such as .NET and Unity).

%prep
%autosetup -p1

%build
cd vscode-1.54.0
./scripts/code.sh --verbose --electronVersion=11.3.0 --no-git-reset --no-clean

%install
cd vscode-1.54.0
mkdir -p %{buildroot}/usr/share/code/
cp -r * %{buildroot}/usr/share/code/

%files
%defattr(-,root,root)
/usr/share/code/


%changelog
* Mon Feb 27 2023 Kalvin McCallum <kalvin_mccallum@student.uml.edu> - 1.63.2-1
- Initial build
