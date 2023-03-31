Name:		texlive-shadethm
Version:	53350
Release:	2
Summary:	Theorem environments that are shaded
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shadethm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shadethm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shadethm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Extends the \newtheorem command. If you say
\newshadetheorem{theorem}{Theorem} in the preamble then your
regular \begin{theorem} .. \end{theorem} will produce a theorem
statement in a shaded box. It supports all the options of
\newtheorem, including forms \newshadetheorem{..}[..]{..} and
\newshadetheorem{..}{..}[..].

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/shadethm
%doc %{_texmfdistdir}/doc/latex/shadethm

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
