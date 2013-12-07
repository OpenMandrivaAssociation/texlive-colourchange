# revision 21741
# category Package
# catalog-ctan /macros/latex/contrib/colourchange
# catalog-date 2011-03-16 12:04:55 +0100
# catalog-license gpl3
# catalog-version 1.22
Name:		texlive-colourchange
Version:	1.22
Release:	3
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

%description
The package allows you to change the colour of the structural
elements (inner theme and outer theme) of your beamer
presentation during the presentation. There is a manual option
but there is also the option to have your structure colour
change from one colour to another as a function of how far
through the presentation you are.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/colourchange/colourchange.sty
%doc %{_texmfdistdir}/doc/latex/colourchange/README
%doc %{_texmfdistdir}/doc/latex/colourchange/colourchangedoc.pdf
%doc %{_texmfdistdir}/doc/latex/colourchange/colourchangedoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.22-2
+ Revision: 750379
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.22-1
+ Revision: 718102
- texlive-colourchange
- texlive-colourchange
- texlive-colourchange
- texlive-colourchange

