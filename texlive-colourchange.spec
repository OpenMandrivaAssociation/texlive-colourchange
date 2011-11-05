# revision 21741
# category Package
# catalog-ctan /macros/latex/contrib/colourchange
# catalog-date 2011-03-16 12:04:55 +0100
# catalog-license gpl3
# catalog-version 1.22
Name:		texlive-colourchange
Version:	1.22
Release:	1
Summary:	colourchange
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colourchange
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colourchange.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colourchange.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows you to change the colour of the structural
elements (inner theme and outer theme) of your beamer
presentation during the presentation. There is a manual option
but there is also the option to have your structure colour
change from one colour to another as a function of how far
through the presentation you are.

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
%{_texmfdistdir}/tex/latex/colourchange/colourchange.sty
%doc %{_texmfdistdir}/doc/latex/colourchange/README
%doc %{_texmfdistdir}/doc/latex/colourchange/colourchangedoc.pdf
%doc %{_texmfdistdir}/doc/latex/colourchange/colourchangedoc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
