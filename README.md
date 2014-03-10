Dette er en eksperiementell plugin til QGIS for å hente vektordata fra Nasjonal vegdatabank (NVDB).

## Installasjonsveiledning

1. Opprett en ny mappe i plugin-katalogen til QGIS. Eksempel: C:\Users\<brukernavn>\.qgis2\python\plugins\<Nvdb>
2. Kopier filene fra dette repoet til den nyopprettete mappen
3. Start QGIS, og aktiver pluginen gjennom Programtillegg-menyen


NB: Pluginen er avhengig av at Python-modulen [requests](http://docs.python-requests.org/en/latest/) er installert. 

## Brukerveiledning (under utarbeidelse)

1. Start ved å velge NVDB Plugin fra Programtillegg-menyen
2. Velg vegnett eller en objekttype fra [NVDB Datakatalog](http://labs.vegdata.no/nvdb-datakatalog/)
3. Velg et område. Enten hele Norge, et bestemt fylke eller en kommune.
4. Velg vegkategorier
5. Opprett lag. Dette vil ta noe tid for store datasett.


## Tekniske detaljer (under utarbeidelse)

Pluginen er laget på bakgrunn av maler produsert av [Plugin Builder](http://plugins.qgis.org/plugins/pluginbuilder/)

For å videreutvikle pluginen, må det tas utgangspunkt i følgende filer: 

* nvdb.py - Inneholder logikk
* ui_nvdb.ui - UI-fil laget i QT Designer
* compile.bat - Denne må kjøres om .ui-filen endres, for å generere en ny ui_nvdb.py. 

    
    
