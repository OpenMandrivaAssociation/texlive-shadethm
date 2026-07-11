%global tl_name shadethm
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Theorem environments that are shaded
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/shadethm
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shadethm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shadethm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Extends the \newtheorem command. If you say
\newshadetheorem{theorem}{Theorem} in the preamble then your regular
\begin{theorem} .. \end{theorem} will produce a theorem statement in a
shaded box. It supports all the options of \newtheorem, including forms
\newshadetheorem{..}[..]{..} and \newshadetheorem{..}{..}[..].
Environments declared using the package require their body to remain on
one page; the mdframed package can frame and shade theorems, and its
environments break at the end of a page; users are generally
recommended, therefore, to use mdframed. In the same spirit, the author
told us in January 2020: "These materials are obsolete. There are a
number of more recent, more powerful packages that have capabilities
that greatly extend the simple ones here. A new project should use one
of those. These files only continue to be available to help people who
are working with an old project."

