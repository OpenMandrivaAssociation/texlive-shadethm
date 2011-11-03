# revision 20319
# category Package
# catalog-ctan /macros/latex/contrib/shadethm
# catalog-date 2010-11-04 00:16:31 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-shadethm
Version:	20101104
Release:	1
Summary:	Theorem environments that are shaded
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shadethm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shadethm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shadethm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Extends the \newtheorem command. If you say
\newshadetheorem{theorem}{Theorem} in the preamble then your
regular \begin{theorem} .. \end{theorem} will produce a theorem
statement in a shaded box. It supports all the options of
\newtheorem, including forms \newshadetheorem{..}[..]{..} and
\newshadetheorem{..}{..}[..].

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/shadethm/colored.sth
%{_texmfdistdir}/tex/latex/shadethm/shadein.sth
%{_texmfdistdir}/tex/latex/shadethm/shadethm.sty
%doc %{_texmfdistdir}/doc/latex/shadethm/1st_read.me
%doc %{_texmfdistdir}/doc/latex/shadethm/shadetest.pdf
%doc %{_texmfdistdir}/doc/latex/shadethm/shadetest.tex
%doc %{_texmfdistdir}/doc/latex/shadethm/shadethm-doc.pdf
%doc %{_texmfdistdir}/doc/latex/shadethm/shadethm-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
