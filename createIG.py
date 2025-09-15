import json
import xml.etree.ElementTree as ET

from pathlib import Path

FHIR_NS = "http://hl7.org/fhir"
NS = {"f": FHIR_NS}

INPUT_DIR = Path("input/resources")

BASE_IG = {
    "resourceType": "ImplementationGuide",
    "id": "PlugathonValidationIG",
    "url": "http://example.org/fhir/PlugathonValidationIG",
    "version": "0.1.",
    "name": "PlugathonValidationIG",
    "status": "draft",
    "experimental": True,
    "packageId": "example.org.fhir.plugathon.validation",
    "fhirVersion": ["4.0.1"],
    # At the time of writing, no package has been uploaded to the package repositories
    # "dependsOn": [
    #     {
    #         "packageId": "hl7.fhir.eu.eps",
    #         "version": "0.0.1-ci"
    #     }
    # ],
    "definition": {
        "resource": None,
        "parameter": [
            {
                "code": "path-pages",
                "value": "input/pages",
            }
        ]
    }
}

def getResourceType(resource):
    if isinstance(resource, ET.Element):
        return resource.tag.replace("{" + FHIR_NS + "}", "")
    elif isinstance(resource, dict):
        if "resourceType" in resource:
            return resource["resourceType"]
        else:
            raise Error("JSON resource misses the 'resourceType' key")

def getResourceId(resource):
    if isinstance(resource, ET.Element):
        try:
            id = resource.find("f:id", NS).attrib["value"]
        except KeyError:
            pass
            # TODO: Insert back id
    elif isinstance(resource, dict):
        try:
            id = resource["id"]
        except KeyError:
            pass
            # TODO: Insert back id

    return id

def mapToProfile(resource):
    resource_type = getResourceType(resource)

    if resource_type == "Patient":
        return "http://hl7.eu/fhir/eps/StructureDefinition/patient-eu-eps"
    elif resource_type == "Procedure":
        return "http://hl7.eu/fhir/eps/StructureDefinition/procedure-eu-eps"

    return None

if __name__ == "__main__":
    resources = []

    resource_type = None
    profile = None
    resource_id = None

    for file_path in INPUT_DIR.glob("*"):
        resource = None
        if len(file_path.suffixes) and file_path.suffixes[-1].lower() == ".xml":
            tree = ET.parse(file_path)
            resource = tree.getroot()
        elif len(file_path.suffixes) and file_path.suffixes[-1].lower() == ".json":
            with open(file_path) as f:
                resource = json.load(f)
        else:
            print(f"Not a FHIR resource: {file_path}. Skipping")

        if resource:
            resource_type = None
            try:
                resource_type = getResourceType(resource)
            except Error as e:
                print(f"Problem parsing resource: {file_path} ({e}). Skipping")
            profile = mapToProfile(resource)
            if not profile:
                print(f"No profile could be matched to resource: {file_path}. Skipping")
            resource_id = getResourceId(resource)

            if resource_type and profile and resource_id:
                resources.append({
                    "reference": {
                        "reference": f"{resource_type}/{resource_id}"
                    },
                    "exampleCanonical": profile
                })

    with open(Path("input/IG.json"), "w") as f:
        BASE_IG["definition"]["resource"] = resources
        f.write(json.dumps(BASE_IG, sort_keys=False, indent=4))