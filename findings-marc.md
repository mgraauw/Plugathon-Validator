# findings plugathon bgz bestand

* G-standaard waardelijsten bestaan niet
  * leidt telkens tot een drietal fouten als hieronder:
  * *Unable to check whether the code is in the value set '' because the code system urn:oid:2.16.840.1.113883.2.4.4.10 was not found (from https://terminologieserver.nl/fhir)*
  * *A definition for CodeSystem 'urn:oid:2.16.840.1.113883.2.4.4.10' could not be found, so the code cannot be validated (from https://terminologieserver.nl/fhir)*
  * *Geen van de gevonden codings bestaan in waardelijst 'ProductCodeCodelijsten' (http://decor.nictiz.nl/fhir/ValueSet/2.16.840.1.113883.2.4.3.11.60.121.11.12--20200901000000|2020-09-01T00:00:00) en een coding uit deze waardelijst is verplicht (codes = urn:oid:2.16.840.1.113883.2.4.4.10#104280)*
* veel codelijsten zijn niet in het Nederlands
  * geldt voor HL7 en ISO waardelijsten (en wellicht meer)
  * leidt tot fouten als:
  * *'Nederland' is the default display; the code system urn:iso:std:iso:3166 has no Display Names for the language nl (from https://terminologieserver.nl/fhir)*
  * *'Divorced' is de standaardweergavenaam; het codesysteem http://terminology.hl7.org/CodeSystem/v3-MaritalStatus heeft geen weergavenamen voor de taal nl
* ePS gaat uit van document
  * dus ook section narrative
* geen LOINC namen voor documenten in NL op NTS
  * *'Probleemlijst [bevinding] d.m.v. rapportage' is the default display; the code system http://loinc.org has no Display Names for the language nl*
* ICD 10 NL is afgeschermd
  * fouten als:
  * *Error from https://terminologieserver.nl/fhir: Error: The user does not have sufficient permissions to perform this action.*
  * voor: 
  ```
                  "code": {
                    "coding": [
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-nl",
                            "code": "G35",
                            "display": "Multiple sclerose"
                        }
                    ]
                },
    ```
    * 