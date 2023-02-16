# Fedora-Package-VSCode

Set up a build environment: Before packaging Visual Studio Code for Fedora, you will need to set up a build environment on your Fedora machine. You can do this by installing the necessary development tools and build dependencies, which can be done using the following python command: sudo dnf groupinstall "Development Tools" "C Development Tools and Libraries"

Download Visual Studio Code: Download the latest version of Visual Studio Code for Linux from the official Visual Studio Code website. The file will have a .tar.gz extension.

Create a spec file: Create a spec file for the Visual Studio Code RPM package. The spec file should include information about the package, such as its name, version, and dependencies. You can create the spec file using a text editor, such as nano or vim.

The spec file has been provided as: vscode.spec

Build the RPM package: Once the spec file has been created, you can use the rpmbuild command to build the RPM package: rpmbuild -bb vscode.spec

Install the RPM package: Once the RPM package has been created, you can install it using the dnf command:sudo dnf install RPMS/x86_64/vscode-1.63.2-1.fc34.x86_64.rpm

Note that you should replace 1.63.2-1 with the version and release number of the package that you built, and fc34 with the version of Fedora that you are using.

Launch Visual Studio Code: After the installation is complete, you can launch Visual Studio Code by searching for it in the Activities menu or by typing code in the terminal window.
