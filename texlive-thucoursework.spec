%global tl_name thucoursework
%global tl_revision 56435

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6
Release:	%{tl_revision}.1
Summary:	Coursework template for Tsinghua University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thucoursework
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thucoursework.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thucoursework.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thucoursework.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package for students of Tsinghua University to write coursework
more efficiently. It can also be used by students from other
universities. Note that the package itself does not import the ctex
package; to use it with Chinese writing, see example file ithw.tex for
details.

