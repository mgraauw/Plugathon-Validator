# The European Patient Summary

## Background

The European PS has a long history. Development of various Patient Summaries started in the 00's of this century, with specifications such as CCD and C-CDA. The EU-funded European epSOS Patient Summary was an early European development, which was one of the inspirations of the International Patient Summary, as well as the EU cross-border specs in eHDSI (eHealth Digital Service Infrastructure) which are part of the MyHealth@EU project. The EHDS legislation was the starting point for the development of the FHIR Implementation Guide for the European PS, as well as the underlying logical models in the XtEHR. Relevant and useful material from these specifications is listed below.

## HL7 Europe specifications

HL7 Europe (also having non-EU members) publishes the European PS FHIR IG, as well as some others. The expectation is that the EU will adopt the HL7 Europe specifications for the EHDS, though it is still an open question to what extent they will be strictly required.

* [Europe Patient Summary](https://build.fhir.org/ig/hl7-eu/eps/)
* [Europe Medication Prescription and Dispense](https://hl7.eu/fhir/mpd/)
* [Europe Base and Core FHIR](https://hl7.eu/fhir/base/)
* [Europe Laboratory Report](https://hl7.eu/fhir/laboratory/)
* [Europe Hospital Discharge Report](https://hl7.eu/fhir/hdr/)
* [Europe Base and Core FHIR IG](https://hl7.eu/fhir/base/)

The latter 5 are "in ballot" which means these are frozen specifications for community feedback, which will normally lead to newer versions which may be balloted again until a final publication. The European PS is not in ballot yet but a "continous build" is available (see the first link above).

[HL7 Europe ballots and publications](https://hl7.eu/fhir/): these are the official and frozen specs.
[HL7 Europe development](https://build.fhir.org/ig/hl7-eu/): these are the latest developments which may change overnight.

The European specifications are developed in Github:

* [European PS](https://github.com/hl7-eu/eps)
* [all](https://github.com/hl7-eu/)

No one implementing the European PS will need those, but for those developing their own derived specification, the material may be useful as a starting point.

There are synthetic examples for the European PS in the [Synderai project](https://synderai.net/index.php?menu=examples/EPS) which may be useful as a reference.

## EU specifications

The EHDS consists broadly of 2 parts:

1. The cross-border **MyHealth@EU** exchanges. Those run over National Contact Points (NCP, one per member state) which exchange messages such a patient summaries. The interface between the NCP and the national infrastructure is up to the member state and not specified in the EHDS.
1. The **XtEHR** requirements for EHR to be allowed on the EU common market (they will need an CE certification). The XtEHR specifications therefore will be mandatory *within* each member state.

### eHealth Network guidelines

The EU eHealth Network guidelines are the basis for the EU developments, and they have been finalized for the European PS and other exchanges.

[eHN Guideline on Patient Summary](https://health.ec.europa.eu/publications/ehn-guideline-patient-summary_en)

This is a high-level document, not very useful for developers except as background. It is the basis for both MyHealth@EU and XtEHR specifications.

At [X-Bundle Registry](https://x-bundles.ehr-exchange-format.eu/index.html) there's a useful entry point to the other specifications.

### XtEHR specifications

The Extended EHR (XtEHR) specifications are of more use to developers. They contain the logical models for the FHIR Implementation Guides and can be used as a starting point for implementations.

[XtEHR Patient Summary](https://www.xt-ehr.eu/fhir/models/useCasePatientSummary.html)

Other XtEHR models can be found in the same repository. Mappings between the XtEHR models and the FHIR IG are under development.

### EEHRxF

One may also encounter the European Electronic Health Record Exchange Format (EEHRxF). This is more or less an umbrella term for the above specifications, grounded in EC regulation, and commonly called "The Format" due to its inpronouncability.

### MyHealth@EU

The EHDS specifications for cross-border exchange are not directly relevant to national European PS exchanges, but are listed here for completeness. The various versions of the specifications are at [https://art-decor.ehdsi.eu/publication/](https://art-decor.ehdsi.eu/publication/).

The main differences between MyHealth@EU and XtEHR are:

* MyHealth@EU is currently CDA (this is expected to change sometime in the future) and XtEHR is FHIR R4/5.
* MyHealth@EU has a very constrained vocabulary and terminology. This is because the content must be translated between member countries, which is more difficult with open vocabularies. The XtEHR is much more open with regard to terminology. However, the more constrained MyHealth@EU vocabularies could be a useful resource for implementers.

## The International Patient Summary (IPS)

The IPS is the basis for the European PS. The European PS FHIR profiles contain an ImposeProfile statement to the IPS which means that every valid European PS is also a valid IPS (but not necessarily the other way round). The European PS derives from the eHN guidelines and the XtEHR specifications; the IPS does not (although everything more or less derives from the same ancestors such as epSOS and the ISO IPS standard).

The IPS does contain some useful resources for eps developers:

* The [IPS specification](https://build.fhir.org/ig/HL7/fhir-ips/en/) has recently been updated to version 2.0.0 - this version will be the basis of the final European PS.
* The [IPS viewer](https://www.ipsviewer.com/) is a rendering tool,
* which also contains a lot of [IPS examples](https://www.ipsviewer.com/)
* I (Marc de Graauw) did a BgZ to IPS conversion 2 years ago, the [blog](https://www.marcdegraauw.com/2023/10/20/from-national-to-international-patient-summary/) may contain useful hints.