Name:		texlive-thucoursework
Version:	56435
Release:	2
Summary:	Coursework template for Tsinghua University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thucoursework
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thucoursework.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thucoursework.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thucoursework.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package for students of Tsinghua University to write
coursework more efficiently. It can also be used by students
from other universities. Note that the package itself does not
import the ctex package; to use it with Chinese writing, see
example file ithw.tex for details.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/thucoursework
%{_texmfdistdir}/tex/latex/thucoursework
%doc %{_texmfdistdir}/doc/latex/thucoursework

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
